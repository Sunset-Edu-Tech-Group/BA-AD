use std::cmp;
use std::fs::File;
use std::io::{Seek, Write};
use std::path::Path;
use std::path::PathBuf;
use std::sync::Arc;
use std::time::Instant;

use anyhow::{Context, Result};
use futures::TryStreamExt;
use reqwest::{Client, Response};
use tokio::sync::{Mutex, Semaphore};

use crate::helpers::interface::{start_download_progress, update_download_progress};
use crate::helpers::network;

#[derive(Debug, Clone, Copy, PartialEq)]
pub enum DownloadStrategy {
    SingleThread,
    MultiThread {
        thread_count: usize,
    },

    #[allow(dead_code)]
    Auto,
}

#[derive(Clone)]
pub struct DownloadManager {
    client: Client,
    chunk_size: u64,
    max_connections: usize,
    connection_semaphore: Arc<Semaphore>,
    max_single_thread_downloads: usize,
    single_thread_semaphore: Arc<Semaphore>,
    files_to_download: Arc<Mutex<usize>>,
    files_downloaded: Arc<Mutex<usize>>,
    total_bytes: Arc<Mutex<u64>>,
    downloaded_bytes: Arc<Mutex<u64>>,
    last_speed_update: Arc<Mutex<(Instant, u64)>>,
    current_speed: Arc<Mutex<u64>>,
}

impl DownloadManager {
    pub fn new(client: Client) -> Self {
        Self {
            client,
            chunk_size: 1024 * 1024,
            max_connections: 8,
            connection_semaphore: Arc::new(Semaphore::new(8)),
            max_single_thread_downloads: 0,
            single_thread_semaphore: Arc::new(Semaphore::new(1000)),
            files_to_download: Arc::new(Mutex::new(0)),
            files_downloaded: Arc::new(Mutex::new(0)),
            total_bytes: Arc::new(Mutex::new(0)),
            downloaded_bytes: Arc::new(Mutex::new(0)),
            last_speed_update: Arc::new(Mutex::new((Instant::now(), 0))),
            current_speed: Arc::new(Mutex::new(0)),
        }
    }

    pub fn with_config(client: Client, chunk_size: u64, max_connections: usize) -> Self {
        Self {
            client,
            chunk_size,
            max_connections,
            connection_semaphore: Arc::new(Semaphore::new(max_connections)),
            max_single_thread_downloads: 0,
            single_thread_semaphore: Arc::new(Semaphore::new(1000)),
            files_to_download: Arc::new(Mutex::new(0)),
            files_downloaded: Arc::new(Mutex::new(0)),
            total_bytes: Arc::new(Mutex::new(0)),
            downloaded_bytes: Arc::new(Mutex::new(0)),
            last_speed_update: Arc::new(Mutex::new((Instant::now(), 0))),
            current_speed: Arc::new(Mutex::new(0)),
        }
    }

    pub fn with_full_config(client: Client, chunk_size: u64, max_connections: usize, max_single_thread_downloads: usize) -> Self {
        let single_thread_limit = if max_single_thread_downloads == 0 {
            1000
        } else {
            max_single_thread_downloads
        };

        Self {
            client,
            chunk_size,
            max_connections,
            connection_semaphore: Arc::new(Semaphore::new(max_connections)),
            max_single_thread_downloads,
            single_thread_semaphore: Arc::new(Semaphore::new(single_thread_limit)),
            files_to_download: Arc::new(Mutex::new(0)),
            files_downloaded: Arc::new(Mutex::new(0)),
            total_bytes: Arc::new(Mutex::new(0)),
            downloaded_bytes: Arc::new(Mutex::new(0)),
            last_speed_update: Arc::new(Mutex::new((Instant::now(), 0))),
            current_speed: Arc::new(Mutex::new(0)),
        }
    }

    pub fn set_max_single_thread_downloads(&mut self, limit: usize) {
        self.max_single_thread_downloads = limit;
        let new_limit = if limit == 0 { 1000 } else { limit };
        self.single_thread_semaphore = Arc::new(Semaphore::new(new_limit));
    }

    pub async fn init_batch_download(&self, file_count: usize, total_size: u64) {
        {
            let mut files_to_download = self.files_to_download.lock().await;
            *files_to_download = file_count;
        }
        {
            let mut files_downloaded = self.files_downloaded.lock().await;
            *files_downloaded = 0;
        }
        {
            let mut total_bytes = self.total_bytes.lock().await;
            *total_bytes = total_size;
        }
        {
            let mut downloaded_bytes = self.downloaded_bytes.lock().await;
            *downloaded_bytes = 0;
        }
        {
            let mut last_speed_update = self.last_speed_update.lock().await;
            *last_speed_update = (Instant::now(), 0);
        }
        {
            let mut current_speed = self.current_speed.lock().await;
            *current_speed = 0;
        }

        start_download_progress(file_count, total_size);
    }

    async fn update_progress(&self, bytes_added: u64, file_name: Option<&str>) {
        let downloaded_files;
        let total_files;
        let downloaded_size;
        let total_size;
        let speed;

        {
            let mut downloaded_bytes = self.downloaded_bytes.lock().await;
            *downloaded_bytes += bytes_added;
            downloaded_size = *downloaded_bytes;
        }

        {
            let total_bytes = self.total_bytes.lock().await;
            total_size = *total_bytes;
        }

        {
            let mut last_update = self.last_speed_update.lock().await;
            let now = Instant::now();
            let elapsed = now.duration_since(last_update.0).as_millis();

            if elapsed >= 500 {
                let bytes_since_last = downloaded_size - last_update.1;
                let speed_kbps = if elapsed > 0 {
                    (bytes_since_last * 1000 / elapsed as u64) / 1024
                } else {
                    0
                };

                {
                    let mut current_speed = self.current_speed.lock().await;
                    *current_speed = speed_kbps;
                }

                *last_update = (now, downloaded_size);
            }
        }

        {
            let current_speed = self.current_speed.lock().await;
            speed = *current_speed;
        }

        {
            let files_downloaded = self.files_downloaded.lock().await;
            downloaded_files = *files_downloaded;

            let files_to_download = self.files_to_download.lock().await;
            total_files = *files_to_download;
        }

        update_download_progress(
            downloaded_files,
            total_files,
            downloaded_size,
            total_size,
            speed,
            file_name.map(String::from),
        );
    }

    async fn complete_file(&self, file_path: &Path) {
        let mut files_downloaded = self.files_downloaded.lock().await;
        *files_downloaded += 1;

        let file_name = file_path.file_name().and_then(|n| n.to_str()).unwrap_or("unknown");
        drop(files_downloaded);
        self.update_progress(0, Some(file_name)).await;
    }

    pub async fn prepare_download(&self, url: &str) -> Result<(u64, Response)> {
        let total_size = network::get_content_length(&self.client, url).await?;
        let response = self.client.get(url).send().await?;
        Ok((total_size, response))
    }

    pub async fn download_file_with_strategy(&self, url: &str, output_path: &PathBuf, strategy: DownloadStrategy) -> Result<()> {
        let (total_size, _) = self.prepare_download(url).await?;

        if total_size == 0 {
            return self.download_without_progress(url, output_path).await;
        }

        let actual_strategy: DownloadStrategy = match strategy {
            DownloadStrategy::Auto => {
                if total_size < 5 * 1024 * 1024 {
                    DownloadStrategy::SingleThread
                } else {
                    let optimal_chunks: usize = cmp::min((total_size / self.chunk_size) as usize, self.max_connections);
                    DownloadStrategy::MultiThread {
                        thread_count: cmp::max(optimal_chunks, 1),
                    }
                }
            }
            _ => strategy,
        };

        match actual_strategy {
            DownloadStrategy::SingleThread => self.download_single_thread(url, total_size, output_path).await,
            DownloadStrategy::MultiThread { thread_count } => {
                let chunks: usize = if thread_count == 0 {
                    cmp::min((total_size / self.chunk_size) as usize, self.max_connections)
                } else {
                    thread_count
                };
                self.download_multi_thread(url, total_size, chunks, output_path).await
            }
            _ => unreachable!(),
        }
    }

    pub async fn download_file(&self, url: &str, total_size: u64, output_path: &PathBuf) -> Result<()> {
        let thread_count: usize = cmp::min((total_size / self.chunk_size) as usize, self.max_connections);
        let file_name = output_path.file_name().and_then(|n| n.to_str()).unwrap_or("unknown");
        if total_size > 5 * 1024 * 1024 {
            self.download_multi_thread(url, total_size, thread_count, output_path).await
        } else {
            self.download_single_thread(url, total_size, output_path).await
        }
    }

    async fn download_single_thread(&self, url: &str, total_size: u64, output_path: &PathBuf) -> Result<()> {
        let _permit = self.single_thread_semaphore.acquire().await?;

        let file: Arc<Mutex<File>> = Arc::new(Mutex::new(File::create(output_path)?));
        let response: Response = self.client.get(url).send().await?;

        let file_name = output_path.file_name().and_then(|n| n.to_str()).unwrap_or("unknown");

        let mut downloaded: u64 = 0;
        let mut progress_accumulator = 0u64;

        response
            .bytes_stream()
            .map_err(anyhow::Error::from)
            .try_for_each(|chunk| {
                let file_clone: Arc<Mutex<File>> = Arc::clone(&file);
                let chunk_size = chunk.len() as u64;
                downloaded += chunk_size;
                progress_accumulator += chunk_size;

                let file_name = file_name.to_string();
                let this = self.clone();

                async move {
                    // Update progress every 100KB
                    if progress_accumulator >= 102400 {
                        this.update_progress(progress_accumulator, Some(&file_name)).await;
                        progress_accumulator = 0;
                    }

                    let mut file_guard = file_clone.lock().await;
                    file_guard.write_all(&chunk)?;
                    Ok(())
                }
            })
            .await?;

        if progress_accumulator > 0 {
            self.update_progress(progress_accumulator, Some(file_name)).await;
        }

        self.complete_file(output_path).await;

        Ok(())
    }

    pub fn get_optimal_threads(&self, file_size: u64) -> usize {
        if file_size > 100 * 1024 * 1024 {
            self.max_connections
        } else {
            let thread_count = (file_size / (5 * 1024 * 1024)).max(1) as usize;
            thread_count.min(self.max_connections)
        }
    }

    async fn download_multi_thread(&self, url: &str, total_size: u64, thread_count: usize, output_path: &PathBuf) -> Result<()> {
        let file = Arc::new(Mutex::new(File::create(output_path)?));
        let mut tasks = Vec::with_capacity(thread_count);

        let chunk_size = ((total_size / thread_count as u64).max(1 * 1024 * 1024).min(10 * 1024 * 1024)) as u64;

        let file_name = output_path.file_name().and_then(|n| n.to_str()).unwrap_or("unknown");

        for i in 0..thread_count {
            let start = i as u64 * chunk_size;
            let end = if i == thread_count - 1 {
                total_size
            } else {
                (start + chunk_size).min(total_size)
            };

            if start >= total_size || start >= end {
                continue;
            }

            let client = self.client.clone();
            let url = url.to_string();
            let file = Arc::clone(&file);
            let semaphore = Arc::clone(&self.connection_semaphore);
            let download_manager = self.clone();
            let file_name = file_name.to_string();

            tasks.push(tokio::spawn(async move {
                let _permit = semaphore.acquire().await?;
                Self::download_chunk(client, &url, start, end, file, &download_manager, &file_name).await
            }));
        }

        for task in tasks {
            task.await??;
        }

        self.complete_file(output_path).await;
        Ok(())
    }

    async fn download_chunk(
        client: Client,
        url: &str,
        start: u64,
        end: u64,
        file: Arc<Mutex<File>>,
        download_manager: &DownloadManager,
        file_name: &str,
    ) -> Result<()> {
        let response = client.get(url).header("Range", format!("bytes={}-{}", start, end - 1)).send().await?;

        let mut progress_accumulator = 0u64;

        let buffer = response
            .bytes_stream()
            .map_err(anyhow::Error::from)
            .try_fold(Vec::with_capacity((end - start) as usize), |mut buffer, chunk| async move {
                let len = chunk.len() as u64;
                progress_accumulator += len;

                if progress_accumulator >= 32768 {
                    download_manager.update_progress(progress_accumulator, Some(file_name)).await;
                    progress_accumulator = 0;
                }

                buffer.extend_from_slice(&chunk);
                Ok(buffer)
            })
            .await?;

        if progress_accumulator > 0 {
            download_manager.update_progress(progress_accumulator, Some(file_name)).await;
        }

        let mut file_guard = file.lock().await;
        file_guard.seek(std::io::SeekFrom::Start(start))?;
        file_guard.write_all(&buffer)?;

        Ok(())
    }

    pub async fn download_without_progress(&self, url: &str, output_path: &PathBuf) -> Result<()> {
        let total_size = network::get_content_length(&self.client, url).await?;
        let response = self.client.get(url).send().await?;

        if !response.status().is_success() {
            return Err(anyhow::anyhow!("Failed to download: {}", response.status()));
        }

        let content = response.bytes().await?;
        std::fs::write(output_path, &content).with_context(|| format!("Failed to write to {}", output_path.display()))?;

        // Update progress with the downloaded content
        self.update_progress(content.len() as u64, output_path.file_name().and_then(|n| n.to_str()))
            .await;

        // Mark file as completed
        self.complete_file(output_path).await;
        Ok(())
    }
}
