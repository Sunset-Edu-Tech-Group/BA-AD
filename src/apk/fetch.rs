use crate::helpers::config::{apk_headers, ServerConfig, JAPAN_REGEX_URL, JAPAN_REGEX_VERSION};
use crate::utils::file::FileManager;
use crate::utils::json;
use anyhow::{anyhow, Result};
use regex::Regex;
use reqwest::{Client, Response};
use std::path::PathBuf;
use tokio::fs;

pub struct ApkFetcher {
    client: Client,
    config: ServerConfig,
    file_manager: FileManager,
}

impl ApkFetcher {
    pub fn new(file_manager: &FileManager, config: &ServerConfig) -> Result<Self> {
        let client: Client = Client::builder().default_headers(apk_headers()).build()?;

        Ok(Self {
            client,
            config: config.clone(),
            file_manager: file_manager.clone(),
        })
    }

    fn extract_version(&self, body: &str) -> Result<String> {
        let version: Regex = Regex::new(JAPAN_REGEX_VERSION)?;
        version
            .find(body)
            .map(|m| m.as_str().to_string())
            .ok_or_else(|| anyhow!("Failed to find version in response"))
    }

    fn extract_url(&self, body: &str) -> Result<String> {
        let re_url: Regex = Regex::new(JAPAN_REGEX_URL)?;
        match re_url.captures(body) {
            Some(caps) if caps.len() >= 3 => Ok(caps.get(2).unwrap().as_str().to_string()),
            _ => Err(anyhow!("Failed to get download url")),
        }
    }

    async fn check_version(&self) -> Result<Option<String>> {
        let response: Response = self.client.get(&self.config.version_url).send().await?;
        if !response.status().is_success() {
            return Err(anyhow!("Failed to get versions: {}", response.status()));
        }

        let body: String = response.text().await?;
        let new_version: String = self.extract_version(&body)?;

        json::update_api_data(&self.file_manager, |data| {
            data.japan.version = new_version.to_string();
        })
        .await?;

        Ok(Some(new_version))
    }

    async fn check_apk(&self, download_url: &str, apk_path: &PathBuf) -> Result<bool> {
        if !self
            .file_manager
            .get_data_path(&apk_path.to_string_lossy())
            .exists()
        {
            return Ok(true);
        }

        let local_size: u64 = match fs::metadata(apk_path).await {
            Ok(metadata) => metadata.len(),
            Err(_) => return Ok(true),
        };

        let response: Response = self
            .client
            .get(download_url)
            .header("Range", "bytes=0-0")
            .send()
            .await?;

        if !response.status().is_success()
            && response.status() != reqwest::StatusCode::PARTIAL_CONTENT
        {
            return Err(anyhow!("Failed to get file info: {}", response.status()));
        }

        let remote_size: u64 = if let Some(content_range) = response.headers().get("Content-Range")
        {
            content_range
                .to_str()
                .ok()
                .and_then(|range| range.split('/').last())
                .and_then(|size| size.parse::<u64>().ok())
                .unwrap_or(0)
        } else {
            response.content_length().unwrap_or(0).saturating_add(1)
        };

        if remote_size == 0 || local_size != remote_size {
            // warn!("APK is outdated or incomplete");
            return Ok(true);
        }

        Ok(false)
    }

    pub async fn download_apk(&self) -> Result<()> {
        if self.config.apk_path.is_empty() || self.config.version_url.is_empty() {
            // warn!("The {} server doesn't support APK download", self.config.id);
            return Ok(());
        }

        let response = self.client.get(&self.config.version_url).send().await?;
        let body = response.text().await?;
        let download_url = self.extract_url(&body)?;

        Ok(())
    }
}
