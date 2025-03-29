use crate::helpers::progress::DownloadProgress;

use anyhow::{Context, Result};
use futures::TryStreamExt;
use reqwest::{Client, Response};
use std::cmp;
use std::fs::File;
use std::io::{Seek, Write};
use std::path::PathBuf;
use std::sync::Arc;
use tokio::sync::{Mutex, Semaphore};

#[derive(Debug, Clone, Copy, PartialEq)]
pub enum DownloadStrategy {
    SingleThread,
    MultiThread { thread_count: usize },
    
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
        }
    }
    
    pub fn with_full_config(client: Client, chunk_size: u64, max_connections: usize, max_single_thread_downloads: usize) -> Self {
        let single_thread_limit = if max_single_thread_downloads == 0 {
            1000 // Effectively unlimited but within tokio's MAX_PERMITS limit
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
        }
    }
    
    pub fn set_max_single_thread_downloads(&mut self, limit: usize) {
        self.max_single_thread_downloads = limit;
        let new_limit = if limit == 0 {
            1000 // Use a reasonable maximum instead of std::usize::MAX
        } else {
            limit
        };
        self.single_thread_semaphore = Arc::new(Semaphore::new(new_limit));
    }

    pub async fn prepare_download(&self, url: &str) -> Result<(u64, Response)> {
        let response: Response = self.client.get(url).send().await?;
        let total_size: u64 = response.content_length().unwrap_or(0);
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
        self.download_multi_thread(url, total_size, thread_count, output_path).await
    }

    async fn download_single_thread(&self, url: &str, total_size: u64, output_path: &PathBuf) -> Result<()> {
        let _permit = self.single_thread_semaphore.acquire().await?;
        
        let progress: Arc<DownloadProgress> = Arc::new(DownloadProgress::new(total_size));
        let file: Arc<Mutex<File>> = Arc::new(Mutex::new(File::create(output_path)?));
        let response: Response = self.client.get(url).send().await?;

        let p_clone: Arc<DownloadProgress> = Arc::clone(&progress);
        response
            .bytes_stream()
            .map_err(anyhow::Error::from)
            .try_for_each(|chunk| {
                let p: Arc<DownloadProgress> = Arc::clone(&p_clone);
                let file_clone: Arc<Mutex<File>> = Arc::clone(&file);
                async move {
                    let mut file_guard: tokio::sync::MutexGuard<'_, File> = file_clone.lock().await;
                    file_guard.write_all(&chunk)?;
                    p.inc(chunk.len() as u64);
                    Ok(())
                }
            })
            .await?;

        progress.finish_with_message("Download complete!");
        Ok(())
    }

    async fn download_multi_thread(&self, url: &str, total_size: u64, thread_count: usize, output_path: &PathBuf) -> Result<()> {
        let progress: Arc<DownloadProgress> = Arc::new(DownloadProgress::new(total_size));
        let file: Arc<Mutex<File>> = Arc::new(Mutex::new(File::create(output_path)?));
        let mut tasks: Vec<tokio::task::JoinHandle<std::result::Result<(), anyhow::Error>>> = Vec::with_capacity(thread_count);

        let chunk_size: u64 = (total_size + thread_count as u64 - 1) / thread_count as u64;

        for i in 0..thread_count {
            let start: u64 = i as u64 * chunk_size;
            let end: u64 = cmp::min(start + chunk_size, total_size);

            if start >= total_size || start >= end {
                continue;
            }

            let client: Client = self.client.clone();
            let url: String = url.to_string();
            let progress: Arc<DownloadProgress> = Arc::clone(&progress);
            let file: Arc<Mutex<File>> = Arc::clone(&file);
            let semaphore: Arc<Semaphore> = Arc::clone(&self.connection_semaphore);

            tasks.push(tokio::spawn(async move {
                let _permit = semaphore.acquire().await?;
                let result = Self::download_chunk(client, &url, start, end, progress, file).await;
                result
            }));
        }

        for task in tasks {
            task.await??;
        }

        progress.finish_with_message("Download complete!");
        Ok(())
    }

    async fn download_chunk(client: Client, url: &str, start: u64, end: u64, progress: Arc<DownloadProgress>, file: Arc<Mutex<File>>) -> Result<()> {
        let response: Response = client.get(url).header("Range", format!("bytes={}-{}", start, end - 1)).send().await?;

        let estimated_size: u64 = end - start;
        let initial_capacity: usize = cmp::min(estimated_size, 1024 * 1024) as usize;

        let buffer: Vec<u8> = response
            .bytes_stream()
            .map_err(anyhow::Error::from)
            .try_fold(Vec::with_capacity(initial_capacity), |mut buffer, chunk| {
                let len = chunk.len() as u64;
                buffer.extend_from_slice(&chunk);
                progress.inc(len);
                async move { Ok(buffer) }
            })
            .await?;

        let mut file_guard: tokio::sync::MutexGuard<'_, File> = file.lock().await;
        file_guard.seek(std::io::SeekFrom::Start(start))?;
        file_guard.write_all(&buffer)?;

        drop(file_guard);

        Ok(())
    }

    pub async fn download_without_progress(&self, url: &str, output_path: &PathBuf) -> Result<()> {
        let response: Response = self.client.get(url).send().await?;

        if !response.status().is_success() {
            return Err(anyhow::anyhow!("Failed to download: {}", response.status()));
        }

        let content = response.bytes().await?;
        std::fs::write(output_path, &content).with_context(|| format!("Failed to write to {}", output_path.display()))?;

        Ok(())
    }
}
