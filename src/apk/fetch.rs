use crate::helpers::{
    apk_headers, ErrorContext, ErrorExt, ServerConfig, ServerRegion,
    GLOBAL_REGEX_VERSION, GLOBAL_URL, JAPAN_REGEX_URL, JAPAN_REGEX_VERSION
};
use crate::utils::file::FileManager;
use crate::utils::json;
use crate::utils::network::get_content_length;
use crate::{debug, info, warn};

use anyhow::Result;
use reqwest::{Client, Url};
use std::path::PathBuf;
use std::rc::Rc;
use tokio::fs;
use trauma::download::Download;
use trauma::downloader::{Downloader, DownloaderBuilder};

#[derive(Clone)]
pub struct ApkFetcher {
    client: Client,
    config: Rc<ServerConfig>,
    file_manager: Rc<FileManager>,
    downloader: Downloader,
}

impl ApkFetcher {
    pub fn new(file_manager: Rc<FileManager>, config: Rc<ServerConfig>) -> Result<Self> {
        let client = Client::builder().default_headers(apk_headers()).build().handle_errors()?;

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
            downloader,
        })
    }

    pub async fn get_current_version(&self) -> Result<String> {
        let response = self.client.get(&self.config.version_url).send().await.handle_errors()?;
        let body: String = response.text().await.handle_errors()?;
        self.extract_version(&body)
    }

    fn extract_version(&self, body: &str) -> Result<String> {
        JAPAN_REGEX_VERSION
            .find(body)
            .map(|m| m.as_str().to_string())
            .error_context("Failed to extract version from server response")
    }

    fn extract_url(&self, body: &str) -> Result<String> {
        match JAPAN_REGEX_URL.captures(body) {
            Some(caps) if caps.len() >= 3 => Ok(caps.get(2).unwrap().as_str().to_string()),
            _ => None.error_context("Failed to get download url"),
        }
    }

    pub async fn check_version(&self) -> Result<Option<String>> {
        match &self.config.region {
            ServerRegion::Global => {
                let re_url = self.client.get(GLOBAL_URL).send().await.handle_errors()?.text().await.handle_errors()?;
                let new_version = GLOBAL_REGEX_VERSION
                    .find(&re_url)
                    .error_context("Failed to get version")?
                    .as_str()
                    .to_string();

                json::update_api_data(&self.file_manager, |data| {
                    data.global.version = new_version.to_string();
                })
                .await?;

                Ok(Some(new_version))
            }
            ServerRegion::Japan => {
                let response = self.client.get(&self.config.version_url).send().await.handle_errors()?;
                let body = response.text().await.handle_errors()?;
                let new_version = self.extract_version(&body)?;

                json::update_api_data(&self.file_manager, |data| {
                    data.japan.version = new_version.to_string();
                })
                .await?;

                Ok(Some(new_version))
            }
        }
    }

    async fn check_apk(&self, download_url: &str, apk_path: &PathBuf) -> Result<bool> {
        if !apk_path.exists() {
            return Ok(true);
        }

        let local_size = match fs::metadata(apk_path).await {
            Ok(metadata) => metadata.len(),
            Err(_) => return Ok(true),
        };

        let response = self
            .client
            .get(download_url)
            .header("Range", "bytes=0-0")
            .send()
            .await
            .handle_errors()?;

        if !response.status().is_success()
            && response.status() != reqwest::StatusCode::PARTIAL_CONTENT
        {
            return None.error_context("Failed to get APK info");
        }

        let remote_size = get_content_length(&response);
        if remote_size == 0 || local_size != remote_size {
            warn!("APK is outdated or incomplete");
            return Ok(true);
        }

        Ok(false)
    }

    pub async fn download_apk(&self) -> Result<(String, PathBuf)> {
        if self.config.region == ServerRegion::Global {
            return None.error_context("Global server APK download is not supported");
        }

        let new_version = self.get_current_version().await?;
        debug!("Using version <b><u><yellow>{}</>", new_version);

        let apk_path = self.file_manager.get_data_path(&self.config.apk_path);
        
        let response = self.client.get(&self.config.version_url).send().await.handle_errors()?;
        let body = response.text().await.handle_errors()?;
        let download_url = self.extract_url(&body)?;

        let needs_download = self.check_apk(&download_url, &apk_path).await?;
        if needs_download {
            if !apk_path.exists() {
                info!("APK doesn't exist, downloading...");
            } else {
                warn!("APK is outdated, downloading...");
            }

            debug!("Download URL: <b><u><bright-blue>{}</>", download_url);

            info!("Downloading APK...");
            let apk = vec![Download {
                url: Url::parse(download_url.as_str())?,
                filename: self.config.apk_path.clone(),
                hash: None
            }];
            self.downloader.download(&apk).await;
        } else {
            info!("APK is up to date, skipping download");
        }

        Ok((
            new_version,
            self.file_manager.get_data_path(&self.config.apk_path),
        ))
    }
}