use crate::helpers::config::{apk_headers, ServerConfig, JAPAN_REGEX_URL, JAPAN_REGEX_VERSION};
use crate::helpers::network::get_content_length;
use crate::utils::file::FileManager;
use crate::utils::json;
use crate::{debug, info, warn};

use anyhow::{anyhow, Result};
use regex::Regex;
use reqwest::{Client, Response, Url};
use std::path::PathBuf;
use tokio::fs;
use trauma::download::Download;
use trauma::downloader::{Downloader, DownloaderBuilder};

#[derive(Clone)]
pub struct ApkFetcher {
    client: Client,
    config: ServerConfig,
    file_manager: FileManager,
    downloader: Downloader
}

impl ApkFetcher {
    pub fn new(file_manager: FileManager, config: ServerConfig) -> Result<Self> {
        let client: Client = Client::builder().default_headers(apk_headers()).build()?;
        
        let downloader = DownloaderBuilder::new()
            .directory(file_manager.get_data_dir().to_path_buf())
            .headers(apk_headers())
            .use_range_for_content_length(true)
            .single_file_progress(true)
            .build();

        Ok(Self {
            client,
            config,
            file_manager,
            downloader
        })
    }

    pub async fn get_current_version(&self) -> Result<String> {
        let response: Response = self.client.get(&self.config.version_url).send().await?;
        if !response.status().is_success() {
            return Err(anyhow!("Failed to get versions: {}", response.status()));
        }

        let body: String = response.text().await?;
        self.extract_version(&body)
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

        let remote_size: u64 = get_content_length(&response);
        if remote_size == 0 || local_size != remote_size {
            warn!("APK is outdated or incomplete");
            return Ok(true);
        }

        Ok(false)
    }

    pub async fn download_apk(&self) -> Result<(String, PathBuf)> {
        if self.config.version_url.is_empty() {
            return Err(anyhow!("Invalid configuration: missing version_url or you are using an unsupported server"));
        }
        
        let new_version = self.get_current_version().await?;
        debug!("Using version <b><u><yellow>{}</>", new_version);

        let response = self.client.get(&self.config.version_url).send().await?;
        let body = response.text().await?;
        let download_url = self.extract_url(&body)?;
        
        debug!("Download URL: <b><u><bright-blue>{}</>", download_url);

        info!("Downloading APK...");
        let apk = vec![Download {
            url: Url::parse(download_url.as_str())?,
            filename: self.config.apk_path.clone(),
        }];
        self.downloader.download(&apk).await;
        
        Ok((new_version, self.file_manager.get_data_path(&self.config.apk_path)))
    }
}