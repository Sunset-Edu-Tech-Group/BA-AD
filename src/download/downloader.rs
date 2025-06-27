use crate::download::ResourceFilter;
use crate::helpers::{
    ErrorContext, GameFiles, GameResources, HashValue, ServerConfig, ServerRegion,
};
use crate::utils::json::load_json;
use crate::utils::FileManager;
use crate::{debug, error, info, success, warn};

use anyhow::Result;
use std::path::{Path, PathBuf};
use std::rc::Rc;
use trauma::download::{Download, Status};
use trauma::downloader::{Downloader, DownloaderBuilder, ProgressBarOpts, StyleOptions};

#[derive(Debug, Clone)]
pub enum ResourceCategory {
    Assets,
    Tables,
    Media,
    All,
    Multiple(Vec<ResourceCategory>),
}

impl ResourceCategory {
    pub fn multiple(categories: Vec<ResourceCategory>) -> Self {
        ResourceCategory::Multiple(categories)
    }
}

pub struct ResourceDownloader {
    downloader: Downloader,
    config: Rc<ServerConfig>,
    file_manager: Rc<FileManager>,
}

pub struct ResourceDownloadBuilder {
    output: Option<PathBuf>,
    retries: u32,
    limit: u64,
    file_manager: Rc<FileManager>,
    config: Rc<ServerConfig>,
}

impl ResourceDownloader {
    pub fn new(output: Option<PathBuf>, file_manager: Rc<FileManager>, config: Rc<ServerConfig>) -> Result<Self> {
        ResourceDownloadBuilder::new(file_manager, config)?
            .output(output)
            .build()
    }

    pub async fn download(&self, category: ResourceCategory, filter: Option<ResourceFilter>) -> Result<()> {
        let game_files_path = match &self.config.region {
            ServerRegion::Global => "catalog/global/GameFiles.json",
            ServerRegion::Japan => "catalog/japan/GameFiles.json",
        };

        let game_resources: GameResources = load_json(&self.file_manager, game_files_path)
            .await
            .error_context("Failed to load game resources - run CatalogParser first")?;

        let collections = Self::get_collections(&category, &game_resources);
        
        info!("Downloading Assets...");
        debug!("Using catalog: <b><u><blue>{}</>", collections.len());

        let downloads: Vec<Download> = collections
            .into_iter()
            .flat_map(|v| v.iter())
            .filter_map(|files| {
                if let Some(ref filter) = filter {
                    let filename = Path::new(&files.path)
                        .file_name()
                        .and_then(|name| name.to_str())
                        .unwrap_or(&files.path);

                    if !filter.matches(filename) {
                        return None;
                    }
                }

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

        if downloads.is_empty() {
            warn!("No files matched the filter criteria for catalog: <b><u><yellow>{:?}</>", category);
            return Ok(());
        }

        info!("Found <b><u><bright-blue>{}</> files for download (catalog: <b><u><blue>{:?}</>)", downloads.len(), category);
        self.downloader.download(&downloads).await;

        Ok(())
    }

    fn get_collections<'a>(category: &ResourceCategory, game_resources: &'a GameResources, ) -> Vec<&'a Vec<GameFiles>> {
        match category {
            ResourceCategory::Assets => vec![&game_resources.asset_bundles],
            ResourceCategory::Tables => vec![&game_resources.table_bundles],
            ResourceCategory::Media => vec![&game_resources.media_resources],
            ResourceCategory::All => vec![
                &game_resources.asset_bundles,
                &game_resources.table_bundles,
                &game_resources.media_resources,
            ],

            ResourceCategory::Multiple(categories) => {
                let mut collections = Vec::new();

                for cat in categories {
                    let nested_collections = Self::get_collections(cat, game_resources);
                    collections.extend(nested_collections);
                }

                collections.sort_by_key(|c| c.as_ptr());
                collections.dedup_by_key(|c| c.as_ptr());
                collections
            }
        }
    }
}

impl ResourceDownloadBuilder {
    pub fn new(file_manager: Rc<FileManager>, config: Rc<ServerConfig>) -> Result<Self> {
        Ok(Self {
            output: None,
            retries: 10,
            limit: 10,
            file_manager,
            config,
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

    pub fn limit(mut self, limit: u64) -> Self {
        self.limit = limit;
        self
    }

    pub fn build(self) -> Result<ResourceDownloader> {
        if self.retries == 0 {
            return None.error_context("Retry count cannot be zero");
        }

        if self.limit == 0 {
            return None.error_context("Download limit cannot be zero");
        }

        let style = StyleOptions::new(ProgressBarOpts::hidden(), ProgressBarOpts::hidden());

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
                        error!(
                            "Failed to download <u><red>{}</> Error: {}",
                            filename, error
                        );
                    }
                    Status::Skipped(_reason) => {
                        warn!("Skipped <u><yellow>{}</> - {}", filename, _reason);
                    }
                    Status::NotStarted => {
                        info!("Downloading <u><blue>{}</>", filename);
                    }
                    Status::HashMismatch(_reason) => {
                        warn!("Outdated <u><yellow>{}</> - {}", filename, _reason);
                    }
                }
            })
            .build();

        Ok(ResourceDownloader {
            downloader,
            config: self.config,
            file_manager: self.file_manager,
        })
    }
}