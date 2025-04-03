use std::cmp;
use std::io;
use std::path::{Path, PathBuf};
use std::thread;

use anyhow::{Context, Result, anyhow};
use futures::stream::{self, StreamExt};
use reqwest::Client;
use sysinfo::System;
use tokio::fs::{self, File};
use tokio::io::{AsyncSeekExt, AsyncWriteExt};

use crate::helpers::file;
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

        let available_ram = sys.total_memory() as u64 * 1024;
        let usable_ram = (available_ram as f64 * 0.85) as u64;
        let target_chunks = self.threads * 8;
        let chunk_size = cmp::min(file_size / target_chunks as u64, usable_ram / target_chunks as u64);

        debug!("Availble RAM: {}", available_ram);
        debug!("Usable RAM: {}", usable_ram);
        debug!("Target Chunks: {}", target_chunks);
        debug!("Chunk Size: {}", chunk_size);

        cmp::min(cmp::max(chunk_size, 1024 * 1024) as usize, 20 * 1024 * 1024)
    }

    pub async fn download_file<P: AsRef<Path>>(&self, url: &str, path: P) -> Result<()> {
        let filename = file::get_filename(path.as_ref());

        if let Ok(content_length) = network::get_content_length(&self.client, url).await {
            if content_length > 5 * 1024 * 1024 {
                return self.download_large_file(url, path).await;
            }
        }

        let response = self.client.get(url).send().await.context("Failed to send request")?;
        let status = response.status();

        info!("Downloading file: {}", filename);

        if !status.is_success() {
            return Err(anyhow!("Failed to download: HTTP {}", status));
        }

        debug!("Reponse Status: {}", status);

        let bytes = response.bytes().await.context("Failed to read response bytes")?;

        debug!("Bytes: {}", bytes.len());

        if let Some(parent) = path.as_ref().parent() {
            fs::create_dir_all(parent).await.context("Failed to create parent directories")?;
        }

        let mut file = File::create(&path).await.context("Failed to create file")?;
        file.write_all(&bytes).await.context("Failed to write to file")?;

        info!("Downloaded file: {}", filename);

        Ok(())
    }

    pub async fn download_large_file<P: AsRef<Path>>(&self, url: &str, path: P) -> Result<()> {
        let filename = file::get_filename(path.as_ref());
        let file_size = network::get_content_length(&self.client, url).await?;

        info!("Downloading file: {}", filename);

        debug!("File Size: {}", file_size);

        let chunk_size = self.calculate_chunk_size(file_size);

        debug!("Calculated Chunk Size: {}", chunk_size);

        if let Some(parent) = path.as_ref().parent() {
            fs::create_dir_all(parent).await.context("Failed to create parent directories")?;
        }

        let file = File::create(&path).await.context("Failed to create file")?;
        file.set_len(file_size).await.context("Failed to set file length")?;
        drop(file);

        let chunks = (0..file_size)
            .step_by(chunk_size)
            .map(|start| {
                let end = std::cmp::min(start + chunk_size as u64, file_size);
                (start, end)
            })
            .collect::<Vec<_>>();

        let path = path.as_ref().to_path_buf();
        let results = stream::iter(chunks)
            .map(|(start, end)| {
                let url = url.to_string();
                let path = path.clone();
                let client = self.client.clone();

                async move { self.download_chunk(&client, &url, &path, start, end).await }
            })
            .buffer_unordered(self.threads)
            .collect::<Vec<_>>()
            .await;

        for result in results {
            result?;
        }

        info!("Downloaded file: {}", filename);

        Ok(())
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

    pub async fn download_files<P: AsRef<Path> + Clone>(&self, urls_and_paths: Vec<(String, P)>) -> Vec<Result<()>> {
        debug!("Threads: {}", self.threads);
        debug!("Limit: {}", self.limit);

        stream::iter(urls_and_paths)
            .map(|(url, path)| async move { self.download_file(&url, path).await })
            .buffer_unordered(self.limit)
            .collect::<Vec<_>>()
            .await
    }
}
