use std::cmp;
use std::io;
use std::path::{Path, PathBuf};
use std::sync;
use std::sync::Arc;
use std::thread;
use std::time::{Duration, Instant};

use anyhow::{Context, Result, anyhow};
use futures::stream::{self, StreamExt};
use reqwest::{self, Client};
use sysinfo::System;
use tokio::fs::{self, File};
use tokio::io::{AsyncSeekExt, AsyncWriteExt};
use tokio::spawn;
use tokio::time;

use crate::helpers::config::USE_CHUNKED_DOWNLOAD;
use crate::helpers::file;
use crate::helpers::interface::{DOWNLOAD_START_TIME, PROGRESS_DATA};
use crate::helpers::network;
use crate::{debug, info};

pub struct DownloadManager {
    client: Client,
    limit: usize,
    threads: usize,
}

impl DownloadManager {
    pub fn new(client: Client, threads: usize, limit: usize) -> Self {
        let threads = if threads == 0 {
            thread::available_parallelism().map(|p| p.get()).unwrap_or(1)
        } else {
            threads
        };

        let limit = if limit == 0 { 1 } else { limit };

        debug!("Creating DownloadManager with threads={}, limit={}", threads, limit);

        DownloadManager { client, limit, threads }
    }

    fn calculate_chunk_size(&self, file_size: u64) -> usize {
        let mut sys = System::new_all();
        sys.refresh_all();

        let available_ram = sys.total_memory() as u64;
        let usable_ram = (available_ram as f64 * 0.85) as u64;
        let target_chunks = self.threads * 4;
        let chunk_size = if available_ram > 0 && target_chunks > 0 {
            cmp::min(file_size / target_chunks as u64, (available_ram / target_chunks as u64) / 2)
        } else {
            1024 * 1024
        };

        debug!("Available RAM: {}", network::format_size(available_ram));
        debug!("Usable RAM: {}", network::format_size(usable_ram));
        debug!("Target Chunks: {}", target_chunks);
        debug!("Chunk Size: {}", network::format_size(chunk_size));

        cmp::min(cmp::max(chunk_size, 1024 * 1024) as usize, 20 * 1024 * 1024)
    }

    pub async fn download_large_file<P: AsRef<Path>>(&self, url: &str, path: P) -> Result<()> {
        self.download_large_file_with_progress(url, path).await
    }

    async fn download_chunk(&self, client: &Client, url: &str, path: &PathBuf, start: u64, end: u64) -> Result<()> {
        let response = client
            .get(url)
            .header("Range", format!("bytes={}-{}", start, end - 1))
            .send()
            .await
            .context("Failed to send request for chunk")?;

        if !response.status().is_success() {
            return Err(anyhow!("Failed to download chunk: HTTP {}", response.status()));
        }

        let bytes = response.bytes().await.context("Failed to read chunk bytes")?;

        let mut file = fs::OpenOptions::new()
            .write(true)
            .open(path)
            .await
            .context("Failed to open file for chunk write")?;

        file.seek(io::SeekFrom::Start(start)).await.context("Failed to seek to chunk position")?;
        file.write_all(&bytes).await.context("Failed to write chunk data")?;

        Ok(())
    }

    pub async fn download_files_with_progress<P: AsRef<Path> + Clone>(&self, urls_and_paths: Vec<(String, P)>) -> Vec<Result<()>> {
        debug!("Threads: {}", self.threads);
        debug!("Limit: {}", self.limit);

        let total_files = urls_and_paths.len();

        // Initialize progress data
        {
            let mut progress_data = PROGRESS_DATA.lock().unwrap();
            progress_data.set_simple();
            progress_data.update_progress(0, total_files, 0, 0, 0, None);

            let mut start_time = DOWNLOAD_START_TIME.lock().unwrap();
            if start_time.is_none() {
                *start_time = Some(Instant::now());
                progress_data.start_timer();
            }
        }

        let completed = Arc::new(sync::atomic::AtomicUsize::new(0));
        let total_bytes = Arc::new(sync::atomic::AtomicU64::new(0));

        let completed_for_ui = completed.clone();
        let total_bytes_for_ui = total_bytes.clone();
        let progress_task = spawn(async move {
            let update_interval = Duration::from_millis(100);
            let mut last_update = Instant::now();
            let mut last_bytes = 0;
            let mut speed_samples = Vec::with_capacity(10);

            loop {
                time::sleep(update_interval).await;

                let now = Instant::now();
                let current_completed = completed_for_ui.load(sync::atomic::Ordering::Relaxed);
                let current_bytes = total_bytes_for_ui.load(sync::atomic::Ordering::Relaxed);

                if current_completed >= total_files {
                    break;
                }

                let bytes_diff = current_bytes.saturating_sub(last_bytes);
                let time_diff = now.duration_since(last_update).as_secs_f64();

                if time_diff > 0.0 {
                    let current_speed = (bytes_diff as f64 / time_diff) as u64;

                    speed_samples.push(current_speed);
                    if speed_samples.len() > 10 {
                        speed_samples.remove(0);
                    }

                    let avg_speed = if !speed_samples.is_empty() {
                        speed_samples.iter().sum::<u64>() / speed_samples.len() as u64
                    } else {
                        0
                    };

                    let mut progress_data = PROGRESS_DATA.lock().unwrap();
                    progress_data.update_progress(current_completed, total_files, 0, 0, avg_speed, None);
                }

                last_update = now;
                last_bytes = current_bytes;
            }
        });

        let results = stream::iter(urls_and_paths)
            .map(|(url, path)| {
                let completed_clone = completed.clone();
                let total_bytes_clone = total_bytes.clone();

                async move {
                    let result = Self::stream_download_file(&self.client, &url, path.as_ref(), total_bytes_clone.clone()).await;
                    let new_completed = completed_clone.fetch_add(1, sync::atomic::Ordering::Relaxed) + 1;
                    let mut progress_data = PROGRESS_DATA.lock().unwrap();

                    progress_data.update_progress(new_completed, total_files, 0, 0, 0, None);

                    result
                }
            })
            .buffer_unordered(self.limit)
            .collect::<Vec<_>>()
            .await;

        progress_task.abort();

        {
            let mut progress_data = PROGRESS_DATA.lock().unwrap();
            progress_data.update_progress(total_files, total_files, 0, 0, 0, None);
        }

        results
    }

    async fn stream_download_file(client: &Client, url: &str, path: &Path, total_bytes: Arc<sync::atomic::AtomicU64>) -> Result<()> {
        let filename = file::get_filename(path);

        let response = client.get(url).send().await.context("Failed to send request")?;
        let status = response.status();

        info!("Downloading file: {}", filename);

        if !status.is_success() {
            return Err(anyhow!("Failed to download: HTTP {}", status));
        }

        if let Some(parent) = path.parent() {
            fs::create_dir_all(parent).await.context("Failed to create parent directories")?;
        }

        let mut file = File::create(path).await.context("Failed to create file")?;
        let mut stream = response.bytes_stream();

        while let Some(chunk_result) = stream.next().await {
            let chunk = chunk_result.context("Failed to download chunk")?;
            file.write_all(&chunk).await.context("Failed to write chunk to file")?;

            total_bytes.fetch_add(chunk.len() as u64, sync::atomic::Ordering::Relaxed);
        }

        info!("Downloaded file: {}", filename);
        Ok(())
    }

    pub async fn download_large_file_with_progress<P: AsRef<Path>>(&self, url: &str, path: P) -> Result<()> {
        let filename = file::get_filename(path.as_ref());
        let file_size = network::get_content_length(&self.client, url).await?;

        info!("Downloading file: {}", filename);
        debug!("File Size: {}", network::format_size(file_size));

        self.initialize_progress(&filename, file_size).await?;
        let file_path = self.prepare_file_path(path.as_ref()).await?;

        if USE_CHUNKED_DOWNLOAD {
            debug!("Using chunked download");
            self.download_with_chunks(url, &file_path, file_size, &filename).await?;
        } else {
            debug!("Using streaming download");
            self.download_with_streaming(url, &file_path, file_size, &filename).await?;
        }

        info!("Downloaded file: {}", filename);
        Ok(())
    }

    async fn initialize_progress(&self, filename: &str, file_size: u64) -> Result<()> {
        let mut progress_data = PROGRESS_DATA.lock().unwrap();
        progress_data.set_detailed();
        progress_data.update_progress(0, 1, 0, file_size, 0, Some(filename.to_string()));

        let mut start_time = DOWNLOAD_START_TIME.lock().unwrap();
        if start_time.is_none() {
            *start_time = Some(Instant::now());
            progress_data.start_timer();
        }

        Ok(())
    }

    async fn prepare_file_path(&self, path: &Path) -> Result<PathBuf> {
        if let Some(parent) = path.parent() {
            fs::create_dir_all(parent).await.context("Failed to create parent directories")?;
        }

        Ok(path.to_path_buf())
    }

    async fn setup_progress_tracker(&self, file_size: u64, filename: &str) -> (Arc<sync::atomic::AtomicU64>, tokio::task::JoinHandle<()>) {
        let downloaded = Arc::new(std::sync::atomic::AtomicU64::new(0));
        let downloaded_for_ui = downloaded.clone();
        let filename_for_task = filename.to_string();

        let progress_update_task = spawn(async move {
            let update_interval = Duration::from_millis(100);
            let mut last_update = Instant::now();
            let mut last_bytes = 0;
            let mut speed_samples = Vec::with_capacity(10);

            loop {
                time::sleep(update_interval).await;

                let now = Instant::now();
                let current_bytes = downloaded_for_ui.load(sync::atomic::Ordering::Relaxed);

                if current_bytes >= file_size {
                    break;
                }

                let bytes_diff = current_bytes.saturating_sub(last_bytes);
                let time_diff = now.duration_since(last_update).as_secs_f64();

                if time_diff > 0.0 {
                    let current_speed = (bytes_diff as f64 / time_diff) as u64;

                    speed_samples.push(current_speed);
                    if speed_samples.len() > 10 {
                        speed_samples.remove(0);
                    }

                    let avg_speed = if !speed_samples.is_empty() {
                        speed_samples.iter().sum::<u64>() / speed_samples.len() as u64
                    } else {
                        0
                    };

                    let mut progress_data = PROGRESS_DATA.lock().unwrap();
                    progress_data.update_progress(0, 1, current_bytes, file_size, avg_speed, Some(filename_for_task.clone()));
                }

                last_update = now;
                last_bytes = current_bytes;
            }
        });

        (downloaded, progress_update_task)
    }

    async fn finalize_progress(&self, progress_task: tokio::task::JoinHandle<()>, file_size: u64, filename: &str) {
        progress_task.abort();

        let mut progress_data = PROGRESS_DATA.lock().unwrap();
        progress_data.update_progress(0, 1, file_size, file_size, 0, Some(filename.to_string()));
    }

    async fn download_with_chunks(&self, url: &str, path: &Path, file_size: u64, filename: &str) -> Result<()> {
        let chunk_size = self.calculate_chunk_size(file_size);
        debug!("Calculated Chunk Size: {}", network::format_size(chunk_size as u64));

        let file = File::create(path).await.context("Failed to create file")?;
        file.set_len(file_size).await.context("Failed to set file length")?;
        drop(file);

        let chunks = (0..file_size)
            .step_by(chunk_size)
            .map(|start| {
                let end = std::cmp::min(start + chunk_size as u64, file_size);
                (start, end)
            })
            .collect::<Vec<_>>();

        let path_buf = path.to_path_buf();

        let (downloaded, progress_task) = self.setup_progress_tracker(file_size, filename).await;

        let results = stream::iter(chunks)
            .map(|(start, end)| {
                let url = url.to_string();
                let path = path_buf.clone();
                let client = self.client.clone();
                let downloaded = downloaded.clone();
                let chunk_size = end - start;

                async move {
                    let result = self.download_chunk(&client, &url, &path, start, end).await;

                    if result.is_ok() {
                        downloaded.fetch_add(chunk_size, sync::atomic::Ordering::Relaxed);
                    }

                    result
                }
            })
            .buffer_unordered(self.threads)
            .collect::<Vec<_>>()
            .await;

        self.finalize_progress(progress_task, file_size, filename).await;

        for result in results {
            result?;
        }

        Ok(())
    }

    async fn download_with_streaming(&self, url: &str, path: &Path, file_size: u64, filename: &str) -> Result<()> {
        let res = self.client.get(url).send().await.context("Failed to send request")?;
        if !res.status().is_success() {
            return Err(anyhow!("Failed to download: HTTP {}", res.status()));
        }

        let mut file = File::create(path).await.context("Failed to create file")?;
        let mut stream = res.bytes_stream();

        let (downloaded, progress_task) = self.setup_progress_tracker(file_size, filename).await;

        while let Some(chunk_result) = stream.next().await {
            let chunk = chunk_result.context("Failed to download chunk")?;
            file.write_all(&chunk).await.context("Failed to write chunk to file")?;

            downloaded.fetch_add(chunk.len() as u64, sync::atomic::Ordering::Relaxed);
        }

        self.finalize_progress(progress_task, file_size, filename).await;

        Ok(())
    }
}
