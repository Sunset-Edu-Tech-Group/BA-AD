use crate::helpers::api::{GameResources, HashValue};
use crate::helpers::config::{ServerConfig, ServerRegion};
use crate::utils::file::FileManager;
use crate::utils::json::load_json;
use crate::{error, info, success, warn};

use anyhow::Result;
use reqwest::Client;
use std::path::{Path, PathBuf};
use std::time::Duration;
use trauma::download::{Download, Status};
use trauma::downloader::{Downloader, DownloaderBuilder, ProgressBarOpts, StyleOptions};

pub struct ResourceDownloader {
    client: Client,
    downloader: Downloader,
    config: ServerConfig,
    file_manager: FileManager,
}

pub struct ResourceDownloadBuilder {
    output: Option<PathBuf>,
    retries: u32,
    timeout: u64,
    limit: u64,
    file_manager: FileManager,
    config: ServerConfig,
}

impl ResourceDownloader {
    pub fn new(
        output: Option<PathBuf>,
        file_manager: &FileManager,
        config: &ServerConfig,
    ) -> Result<Self> {
        ResourceDownloadBuilder::new(file_manager, config)?
            .output(output)
            .build()
    }

    pub async fn download(&self) -> Result<()> {
        let game_files_path = match &self.config.region {
            ServerRegion::Global => "catalog/global/GameFiles.json",
            ServerRegion::Japan => "catalog/japan/GameFiles.json",
        };

        let game_resources: GameResources = load_json(&self.file_manager, game_files_path).await?;

        let downloads: Vec<Download> = [
            &game_resources.asset_bundles,
            &game_resources.table_bundles,
            &game_resources.media_resources,
        ]
        .into_iter()
        .flat_map(|v| v.iter())
        .filter_map(|files| {
            Download::try_from(files.url.as_str())
                .map(|mut download| {
                    download.filename = files.path.clone();
                    download.hash = Some(match &files.hash {
                        HashValue::Crc(crc) => crc.to_string(),
                        HashValue::Md5(md5) => md5.clone(),
                    });
                    download
                })
                .ok()
        })
        .collect();

        if !downloads.is_empty() {
            self.downloader.download(&downloads).await;
        }

        Ok(())
    }
}

impl ResourceDownloadBuilder {
    pub fn new(file_manager: &FileManager, config: &ServerConfig) -> Result<Self> {
        Ok(Self {
            output: None,
            retries: 10,
            timeout: 60,
            limit: 10,
            file_manager: file_manager.clone(),
            config: config.clone(),
        })
    }

    pub fn output(mut self, output: Option<PathBuf>) -> Self {
        self.output = output;
        self
    }

    pub fn retries(mut self, retries: u32) -> Self {
        self.retries = retries;
        self
    }

    pub fn timeout(mut self, timeout: u64) -> Self {
        self.timeout = timeout;
        self
    }

    pub fn limit(mut self, limit: u64) -> Self {
        self.limit = limit;
        self
    }

    pub fn build(self) -> Result<ResourceDownloader> {
        let client = Client::builder()
            .timeout(Duration::from_secs(self.timeout))
            .build()?;

        let style = StyleOptions::new(
            ProgressBarOpts::hidden(),
            ProgressBarOpts::hidden(),
        );

        let downloader = DownloaderBuilder::new()
            .directory(FileManager::get_output_dir(self.output)?)
            .concurrent_downloads(self.limit as usize)
            .retries(self.retries)
            .style_options(style)
            .on_complete(|summary| {
                let filename = Path::new(&summary.download().filename)
                    .file_name()
                    .and_then(|name| name.to_str())
                    .unwrap_or(&summary.download().filename);

                match summary.status() {
                    Status::Success => {
                        success!("Downloaded <u><green>{}</>", filename);
                    }
                    Status::Fail(error) => {
                        error!("Failed to download <u><red>{}</> Error: {}",filename, error);
                    }
                    Status::Skipped(reason) => {
                        warn!("Skipped <u><yellow>{}</> - {}", filename, reason);
                    }
                    Status::NotStarted => {
                        info!("Downloading <u><blue>{}</>", filename);
                    }
                    Status::HashMismatch(reason) => {
                        warn!("Outdated <u><yellow>{}</> - {}", filename, reason);
                    }
                }
            })
            .build();

        Ok(ResourceDownloader {
            client,
            downloader,
            config: self.config,
            file_manager: self.file_manager,
        })
    }
}
