use crate::helpers::progress::DownloadProgress;

use anyhow::{Context, Result};
use reqwest::{Client, Response};
use std::cmp;
use std::fs::File;
use std::io::{Seek, Write};
use std::path::PathBuf;
use std::sync::Arc;
use tokio::sync::Mutex;

#[derive(Debug, Clone, Copy, PartialEq)]
pub enum DownloadStrategy {
    SingleThread,
    MultiThread { chunk_count: usize },
    Auto,
}

pub struct DownloadManager {
    client: Client,
    chunk_size: u64,
    max_connections: usize,
}

impl DownloadManager {
    pub fn new(client: Client) -> Self {
        Self {
            client,
            chunk_size: 1024 * 1024,
            max_connections: 8,
        }
    }

    pub fn with_config(client: Client, chunk_size: u64, max_connections: usize) -> Self {
        Self {
            client,
            chunk_size,
            max_connections,
        }
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
                    let optimal_chunks = cmp::min((total_size / self.chunk_size) as usize, self.max_connections);
                    DownloadStrategy::MultiThread {
                        chunk_count: cmp::max(optimal_chunks, 1),
                    }
                }
            }
            _ => strategy,
        };

        match actual_strategy {
            DownloadStrategy::SingleThread => self.download_single_thread(url, total_size, output_path).await,
            DownloadStrategy::MultiThread { chunk_count } => {
                let chunks: usize = if chunk_count == 0 {
                    cmp::min((total_size / self.chunk_size) as usize, self.max_connections)
                } else {
                    chunk_count
                };
                self.download_multi_thread(url, total_size, chunks, output_path).await
            }
            _ => unreachable!(),
        }
    }

    pub async fn download_file(&self, url: &str, total_size: u64, output_path: &PathBuf) -> Result<()> {
        let chunk_count: usize = cmp::min((total_size / self.chunk_size) as usize, self.max_connections);
        self.download_multi_thread(url, total_size, chunk_count, output_path).await
    }

    async fn download_single_thread(&self, url: &str, total_size: u64, output_path: &PathBuf) -> Result<()> {
        let progress: Arc<DownloadProgress> = Arc::new(DownloadProgress::new(total_size));
        let mut file: File = File::create(output_path)?;

        let mut response: Response = self.client.get(url).send().await?;

        while let Some(chunk) = response.chunk().await? {
            file.write_all(&chunk)?;
            progress.inc(chunk.len() as u64);
        }

        progress.finish_with_message("Download complete!");
        Ok(())
    }

    async fn download_multi_thread(&self, url: &str, total_size: u64, chunk_count: usize, output_path: &PathBuf) -> Result<()> {
        let progress: Arc<DownloadProgress> = Arc::new(DownloadProgress::new(total_size));
        let file: Arc<Mutex<File>> = Arc::new(Mutex::new(File::create(output_path)?));
        let mut tasks: Vec<tokio::task::JoinHandle<std::result::Result<(), anyhow::Error>>> = Vec::with_capacity(chunk_count);

        let chunk_size: u64 = (total_size + chunk_count as u64 - 1) / chunk_count as u64;

        for i in 0..chunk_count {
            let start: u64 = i as u64 * chunk_size;
            let end: u64 = cmp::min(start + chunk_size, total_size);

            if start >= total_size || start >= end {
                continue;
            }

            let client = self.client.clone();
            let url = url.to_string();
            let progress = Arc::clone(&progress);
            let file = Arc::clone(&file);

            tasks.push(tokio::spawn(async move {
                Self::download_chunk(client, &url, start, end, progress, file).await
            }));
        }

        for task in tasks {
            task.await??;
        }

        progress.finish_with_message("Download complete!");
        Ok(())
    }

    async fn download_chunk(
        client: Client,
        url: &str,
        start: u64,
        end: u64,
        progress: Arc<DownloadProgress>,
        file: Arc<Mutex<File>>,
    ) -> Result<()> {
        let mut response = client
            .get(url)
            .header("Range", format!("bytes={}-{}", start, end - 1))
            .send()
            .await?;

        let estimated_size: u64 = end - start;
        let initial_capacity: usize = cmp::min(estimated_size, 1024 * 1024) as usize;
        let mut buffer: Vec<u8> = Vec::with_capacity(initial_capacity);

        while let Some(chunk) = response.chunk().await? {
            buffer.extend_from_slice(&chunk);
            progress.inc(chunk.len() as u64);
        }

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
