use crate::helpers::{
    apk_headers, ApiData, ServerConfig, ServerRegion, GLOBAL_REGEX_VERSION, GLOBAL_URL,
    JAPAN_REGEX_URL, JAPAN_REGEX_VERSION,
};
use crate::utils::{file, json, network};

use anyhow::Result;
use baad_core::{
    debug,
    errors::{ErrorContext, ErrorExt},
    info, success, warn,
};
use reqwest::{Client, Url};
use std::path::{Path, PathBuf};
use std::rc::Rc;
use tokio::fs;
use trauma::download::Download;
use trauma::downloader::{Downloader, DownloaderBuilder};

#[derive(Clone)]
pub struct ApkFetcher {
    client: Client,
    config: Rc<ServerConfig>,
    downloader: Downloader,
}

impl ApkFetcher {
    pub fn new(config: Rc<ServerConfig>) -> Result<Self> {
        let client = Client::builder()
            .default_headers(apk_headers())
            .build()
            .handle_errors()?;

        let downloader = DownloaderBuilder::new()
            .directory(file::data_dir()?)
            .headers(apk_headers())
            .use_range_for_content_length(true)
            .single_file_progress(true)
            .overwrite(true)
            .build();

        Ok(Self {
            client,
            config,
            downloader,
        })
    }

    pub async fn get_current_version(&self) -> Result<String> {
        let response = self
            .client
            .get(&self.config.version_url)
            .send()
            .await
            .handle_errors()?;
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

    pub async fn get_version(&self) -> Result<String> {
        match &self.config.region {
            ServerRegion::Global => {
                let re_url = self
                    .client
                    .get(GLOBAL_URL)
                    .send()
                    .await
                    .handle_errors()?
                    .text()
                    .await
                    .handle_errors()?;
                Ok(GLOBAL_REGEX_VERSION
                    .find(&re_url)
                    .error_context("Failed to get version")?
                    .as_str()
                    .to_string())
            }
            ServerRegion::Japan => {
                let response = self
                    .client
                    .get(&self.config.version_url)
                    .send()
                    .await
                    .handle_errors()?;
                let body = response.text().await.handle_errors()?;
                self.extract_version(&body)
            }
        }
    }

    pub async fn check_version(&self) -> Result<Option<String>> {
        let version = self.get_version().await?;

        json::update_api_data(|data| match &self.config.region {
            ServerRegion::Global => data.global.version = version.clone(),
            ServerRegion::Japan => data.japan.version = version.clone(),
        })
        .await?;

        Ok(Some(version))
    }

    async fn check_apk(&self, download_url: &str, apk_path: &Path) -> Result<bool> {
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

        let remote_size = network::get_content_length(&response);
        if remote_size == 0 || local_size != remote_size {
            debug!("APK is outdated or incomplete");
            return Ok(true);
        }

        Ok(false)
    }

    pub async fn needs_catalog_update(&self) -> Result<bool> {
        let api_data_path = file::get_data_path("api_data.json")?;
        if !api_data_path.exists() {
            return Ok(true);
        }

        let current_version = self.get_version().await?;
        let api_data: ApiData = json::load_json(&api_data_path).await?;

        let cached_version = match &self.config.region {
            ServerRegion::Global => &api_data.global.version,
            ServerRegion::Japan => &api_data.japan.version,
        };

        if current_version != *cached_version {
            info!("Version has changed, updating catalogs...");
            Ok(true)
        } else {
            info!("Version is up to date, skipping catalog processing..");
            Ok(false)
        }
    }

    pub async fn needs_update(&self, download_url: &str, apk_path: &Path) -> Result<bool> {
        let needs_download = self.check_apk(download_url, apk_path).await?;

        if !needs_download {
            info!("APK is up to date, skipping download");
            return Ok(false);
        }

        if !apk_path.exists() {
            warn!("APK doesn't exist, downloading...");
        } else {
            warn!("APK is outdated, downloading...");
        }

        Ok(true)
    }

    pub async fn download_apk(&self, force: bool) -> Result<(String, PathBuf, bool)> {
        let new_version = self.get_current_version().await?;
        debug!("Using version <b><u><yellow>{}</>", new_version);

        let apk_path = file::get_data_path(&self.config.apk_path)?;

        let response = self
            .client
            .get(&self.config.version_url)
            .send()
            .await
            .handle_errors()?;
        let body = response.text().await.handle_errors()?;
        let download_url = self.extract_url(&body)?;

        debug!("Download URL: <b><u><bright-blue>{}</>", download_url);

        if !force && !self.needs_update(&download_url, &apk_path).await? {
            return Ok((new_version, apk_path, false));
        }

        info!("Downloading APK...");
        let apk = vec![Download {
            url: Url::parse(download_url.as_str())?,
            filename: self.config.apk_path.clone(),
            hash: None,
        }];
        self.downloader.download(&apk).await;

        success!("APK downloaded");

        Ok((new_version, apk_path, true))
    }
}
