use std::cmp;
use std::fs::File;
use std::io::{Seek, Write};
use std::path::{Path, PathBuf};
use std::sync::Arc;
use std::thread;
use std::time::Instant;

use anyhow::{Context, Result};
use futures::TryStreamExt;
use reqwest::{Client, Response};
use tokio::sync::{Mutex, Semaphore};

use crate::helpers::config::{DEFAULT_CHUNK_SIZE, DEFAULT_TTL_TIME};
use crate::helpers::file;
use crate::helpers::interface::{start_detailed_progress, start_download_progress, update_download_progress};
use crate::helpers::logs::debug;
use crate::helpers::network;

struct BandwidthTest {
    bandwidth: u64,
    timestamp: Instant,
}

#[derive(Clone)]
pub struct DownloadManager {
    client: Client,
    chunk_size: u64,

    download: Arc<Mutex<usize>>,
    downloaded: Arc<Mutex<usize>>,

    total_bytes: Arc<Mutex<u64>>,
    downloaded_bytes: Arc<Mutex<u64>>,

    last_speed: Arc<Mutex<(Instant, u64)>>,
    current_speed: Arc<Mutex<u64>>,

    bandwidth_cache: Arc<Mutex<Option<BandwidthTest>>>,
    bandwidth_cache_ttl: u64,
}

impl DownloadManager {
    pub fn new(client: Client, chunk_size: u64) -> Self {
        Self {
            client,
            chunk_size: DEFAULT_CHUNK_SIZE,
            download: Arc::new(Mutex::new(0)),
            downloaded: Arc::new(Mutex::new(0)),
            total_bytes: Arc::new(Mutex::new(0)),
            downloaded_bytes: Arc::new(Mutex::new(0)),
            last_speed: Arc::new(Mutex::new((Instant::now(), 0))),
            current_speed: Arc::new(Mutex::new(0)),
            bandwidth_cache: Arc::new(Mutex::new(None)),
            bandwidth_cache_ttl: DEFAULT_TTL_TIME,
        }
    }

    pub fn with_bandwidth_cache_ttl(mut self, ttl_seconds: u64) -> Self {
        self.bandwidth_cache_ttl = ttl_seconds;
        self
    }

    pub async fn init_batch_download(&self, file_count: usize, total_size: u64) {
        {
            let mut files_to_download = self.download.lock().await;
            *files_to_download = file_count;
        }
        {
            let mut files_downloaded = self.downloaded.lock().await;
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
            let mut last_speed_update = self.last_speed.lock().await;
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
            let mut last_update = self.last_speed.lock().await;
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
            let files_downloaded = self.downloaded.lock().await;
            downloaded_files = *files_downloaded;

            let files_to_download = self.download.lock().await;
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
        let mut files_downloaded = self.downloaded.lock().await;
        *files_downloaded += 1;

        drop(files_downloaded);
        self.update_progress(0, Some(&file::get_filename(file_path))).await;
    }

    pub async fn prepare_download(&self, url: &str) -> Result<(u64, Response)> {
        let total_size = network::get_content_length(&self.client, url).await?;
        let response = self.client.get(url).send().await?;

        Ok((total_size, response))
    }

    async fn get_bandwidth(&self, url: &str) -> Result<u64> {
        {
            let bandwidth_cache = self.bandwidth_cache.lock().await;
            if let Some(test) = &*bandwidth_cache {
                let age = test.timestamp.elapsed().as_secs();
                if age < self.bandwidth_cache_ttl {
                    return Ok(test.bandwidth);
                }
            }
        }

        let start_time = Instant::now();

        let test_size: u64 = 256 * 1024;
        let response = self.client.get(url).header("Range", format!("bytes=0-{}", test_size - 1)).send().await?;

        if !response.status().is_success() {
            return Ok(1 * 1024 * 1024);
        }

        let data = response.bytes().await?;
        let download_size = data.len() as u64;

        let elapsed = start_time.elapsed().as_secs_f64();
        if elapsed <= 0.0 || download_size == 0 {
            return Ok(1 * 1024 * 1024);
        }

        let bandwidth = (download_size as f64 / elapsed) as u64;

        {
            let mut bandwidth_cache = self.bandwidth_cache.lock().await;
            *bandwidth_cache = Some(BandwidthTest {
                bandwidth,
                timestamp: Instant::now(),
            });
        }

        Ok(bandwidth)
    }

    async fn calculate_optimal_connections(&self, url: &str, total_size: u64, available_cores: usize) -> Result<usize> {
        if total_size < 1 * 1024 * 1024 {
            return Ok(1);
        }

        let bandwidth = self.get_bandwidth(url).await?;

        let chunks_by_size = ((total_size + self.chunk_size - 1) / self.chunk_size) as usize;

        let bandwidth_factor = (bandwidth / (1024 * 1024)) as usize;
        let connections_by_bandwidth = cmp::max(1, cmp::min(bandwidth_factor, 32));

        let size_scaling = if total_size < 10 * 1024 * 1024 {
            0.5
        } else if total_size < 100 * 1024 * 1024 {
            1.0
        } else {
            1.5
        };

        let calculated = ((connections_by_bandwidth as f64 * size_scaling) as usize)
            .min(chunks_by_size)
            .min(available_cores * 4)
            .max(1);

        Ok(calculated)
    }

    pub async fn download(&self, url: &str, output_path: &PathBuf, detailed: bool, connections: usize, cores: usize, limit: usize) -> Result<()> {
        let (total_size, _) = self.prepare_download(url).await?;

        if total_size == 0 {
            return self.download_without_progress(url, output_path).await;
        }

        {
            let mut files_to_download = self.download.lock().await;
            *files_to_download = 1;
        }
        {
            let mut files_downloaded = self.downloaded.lock().await;
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
            let mut last_speed_update = self.last_speed.lock().await;
            *last_speed_update = (Instant::now(), 0);
        }
        {
            let mut current_speed = self.current_speed.lock().await;
            *current_speed = 0;
        }

        if detailed {
            start_detailed_progress(total_size);
        } else {
            start_download_progress(1, total_size);
        }

        let available_cores = thread::available_parallelism().map(|p| p.get()).unwrap_or(1);
        let effective_cores = if cores == 0 { available_cores } else { cores };

        let effective_connections = if connections == 0 {
            self.calculate_optimal_connections(url, total_size, effective_cores).await?
        } else {
            connections
        };

        let parallel_semaphore = if limit > 0 { Some(Arc::new(Semaphore::new(limit))) } else { None };

        if let Some(semaphore) = &parallel_semaphore {
            let _permit = semaphore.acquire().await?;
            self.download_file(url, output_path, effective_connections, total_size).await?;
        } else {
            self.download_file(url, output_path, effective_connections, total_size).await?;
        }

        Ok(())
    }

    async fn download_file(&self, url: &str, output_path: &PathBuf, connections: usize, total_size: u64) -> Result<()> {
        if connections == 1 {
            return self.download_single_connection(url, output_path).await;
        }

        let file = Arc::new(Mutex::new(File::create(output_path)?));
        let mut tasks = Vec::with_capacity(connections);

        let adaptive_chunk_size = if total_size < self.chunk_size * connections as u64 {
            cmp::max(total_size / connections as u64, 64 * 1024)
        } else {
            self.chunk_size
        };

        let file_name = file::get_filename(output_path);

        let connection_semaphore = Arc::new(Semaphore::new(connections));

        for i in 0..connections {
            let start = i as u64 * adaptive_chunk_size;

            let end = if i == connections - 1 {
                total_size
            } else {
                (start + adaptive_chunk_size).min(total_size)
            };

            if start >= total_size || start >= end {
                continue;
            }

            let client = self.client.clone();
            let url = url.to_string();
            let file = Arc::clone(&file);
            let semaphore = Arc::clone(&connection_semaphore);
            let download_manager = self.clone();
            let file_name = file_name.to_string();

            let permit = semaphore.clone().acquire_owned().await?;

            tasks.push(tokio::spawn(async move {
                let result = Self::download_chunk(client, &url, start, end, file, &download_manager, &file_name).await;
                drop(permit); // Explicitly drop the permit
                result
            }));
        }

        for task in tasks {
            task.await??;
        }

        self.complete_file(output_path).await;

        Ok(())
    }

    async fn download_single_connection(&self, url: &str, output_path: &PathBuf) -> Result<()> {
        let file = Arc::new(Mutex::new(File::create(output_path)?));
        let response = self.client.get(url).send().await?;

        let file_name = file::get_filename(output_path);

        let mut progress_accumulator = 0u64;

        response
            .bytes_stream()
            .map_err(anyhow::Error::from)
            .try_for_each(|chunk| {
                let file_clone = Arc::clone(&file);
                let chunk_size = chunk.len() as u64;
                let file_name = file_name.to_string();
                let download_manager = self.clone();

                progress_accumulator += chunk_size;

                async move {
                    if progress_accumulator >= 102400 {
                        download_manager.update_progress(progress_accumulator, Some(&file_name)).await;
                        progress_accumulator = 0;
                    }

                    let mut file_guard = file_clone.lock().await;
                    file_guard.write_all(&chunk)?;
                    Ok(())
                }
            })
            .await?;

        if progress_accumulator > 0 {
            self.update_progress(progress_accumulator, Some(&file_name)).await;
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
