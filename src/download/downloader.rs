use crate::download::ResourceFilter;
use crate::helpers::{
    GameFiles, GlobalGameResources, HashValue, JapanGameResources, ServerConfig, ServerRegion,
};
use crate::utils::{file, json};

use anyhow::Result;
use baad_core::{error, errors::ErrorContext, info, success, warn};
use std::mem::discriminant;
use std::path::{Path, PathBuf};
use std::rc::Rc;
use trauma::download::{Download, Status};
use trauma::downloader::{Downloader, DownloaderBuilder, ProgressBarOpts, StyleOptions};

#[derive(Debug, Clone, PartialEq)]
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
}

pub struct ResourceDownloadBuilder {
    output: Option<PathBuf>,
    retries: u32,
    limit: u64,
    config: Rc<ServerConfig>,
}

impl ResourceDownloader {
    pub async fn new(output: Option<PathBuf>, config: Rc<ServerConfig>) -> Result<Self> {
        ResourceDownloadBuilder::new(config)?
            .output(output)
            .build()
            .await
    }

    fn matches_filter(
        filter: &ResourceFilter,
        path: &str,
        bundle_files: Option<&[String]>,
    ) -> bool {
        let filename = Path::new(path)
            .file_name()
            .and_then(|name| name.to_str())
            .unwrap_or(path);

        if filter.matches(filename) {
            return true;
        }

        if let Some(bundles) = bundle_files {
            return bundles
                .iter()
                .any(|bundle_name| filter.matches(bundle_name));
        }

        false
    }

    fn get_collections<'a>(
        category: &ResourceCategory,
        game_resources: &'a GlobalGameResources,
    ) -> Vec<&'a Vec<GameFiles>> {
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

    pub async fn download(
        &self,
        category: ResourceCategory,
        filter: Option<ResourceFilter>,
    ) -> Result<()> {
        match &self.config.region {
            ServerRegion::Global => {
                let game_resources: GlobalGameResources = {
                    let path = file::get_data_path("catalog/global/GameFiles.json")?;
                    json::load_json(&path).await
                }
                .error_context("Failed to load global game resources - run CatalogParser first")?;

                let collections = Self::get_collections(&category, &game_resources);
                let downloads = self.process_global_files(collections, filter);
                self.execute_downloads(downloads, category).await
            }
            ServerRegion::Japan => {
                let game_resources: JapanGameResources = {
                    let path = file::get_data_path("catalog/japan/GameFiles.json")?;
                    json::load_json(&path).await
                }
                .error_context("Failed to load japan game resources - run CatalogParser first")?;

                let downloads = self.process_japan_files(&game_resources, &category, filter);
                self.execute_downloads(downloads, category).await
            }
        }
    }

    fn process_global_files(
        &self,
        collections: Vec<&Vec<GameFiles>>,
        filter: Option<ResourceFilter>,
    ) -> Vec<Download> {
        collections
            .into_iter()
            .flat_map(|v| {
                Self::process_files_with_bundles(
                    v,
                    filter.as_ref(),
                    |f| &f.url,
                    |f| &f.path,
                    |f| &f.hash,
                    |_| None,
                )
            })
            .collect()
    }

    fn process_files_with_bundles<T>(
        files: &[T],
        filter: Option<&ResourceFilter>,
        get_url: impl Fn(&T) -> &str,
        get_path: impl Fn(&T) -> &str,
        get_hash: impl Fn(&T) -> &HashValue,
        get_bundles: impl Fn(&T) -> Option<&[String]>,
    ) -> Vec<Download> {
        files
            .iter()
            .filter(|file| {
                filter.is_none_or(|f| {
                    Self::matches_filter(f, get_path(file), get_bundles(file))
                })
            })
            .filter_map(|file| Self::create_download(get_url(file), get_path(file), get_hash(file)))
            .collect()
    }

    fn process_japan_files(
        &self,
        game_resources: &JapanGameResources,
        _category: &ResourceCategory,
        _filter: Option<ResourceFilter>,
    ) -> Vec<Download> {
        macro_rules! process_category {
            ($downloads:expr, $cat:ident, $files:expr, $bundles:expr) => {
                if self.should_include_category(_category, ResourceCategory::$cat) {
                    $downloads.extend(Self::process_files_with_bundles(
                        $files,
                        _filter.as_ref(),
                        |f| &f.url,
                        |f| &f.path,
                        |f| &f.hash,
                        $bundles,
                    ));
                }
            };
        }

        let mut downloads = Vec::new();
        process_category!(downloads, Assets, &game_resources.asset_bundles, |f| Some(&f.bundle_files));
        process_category!(downloads, Tables, &game_resources.table_bundles, |_| None);
        process_category!(downloads, Media, &game_resources.media_resources, |_| None);
        downloads
    }

    fn should_include_category(
        &self,
        selected: &ResourceCategory,
        target: ResourceCategory,
    ) -> bool {
        match selected {
            ResourceCategory::All => true,
            cat if discriminant(cat) == discriminant(&target) => true,
            ResourceCategory::Multiple(cats) => cats.contains(&target),
            _ => false,
        }
    }

    fn create_download(url: &str, path: &str, hash: &HashValue) -> Option<Download> {
        Download::try_from(url)
            .map(|mut download| {
                download.filename = path.to_string();
                download.hash = Some(match hash {
                    HashValue::Crc(crc) => crc.to_string(),
                    HashValue::Md5(md5) => md5.clone(),
                });
                download
            })
            .ok()
    }

    async fn execute_downloads(
        &self,
        downloads: Vec<Download>,
        category: ResourceCategory,
    ) -> Result<()> {
        if downloads.is_empty() {
            warn!(
                "No files matched the filter criteria for catalog: <b><u><yellow>{:?}</>",
                category
            );
            return Ok(());
        }

        info!(
            "Found <b><u><bright-blue>{}</> files for download (catalog: <b><u><blue>{:?}</>)",
            downloads.len(),
            category
        );
        self.downloader.download(&downloads).await;
        Ok(())
    }
}

impl ResourceDownloadBuilder {
    pub fn new(config: Rc<ServerConfig>) -> Result<Self> {
        Ok(Self {
            output: None,
            retries: 10,
            limit: 10,
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

    pub async fn build(self) -> Result<ResourceDownloader> {
        if self.retries == 0 {
            return None.error_context("Retry count cannot be zero");
        }

        if self.limit == 0 {
            return None.error_context("Download limit cannot be zero");
        }

        let style = StyleOptions::new(ProgressBarOpts::hidden(), ProgressBarOpts::hidden());

        let downloader = DownloaderBuilder::new()
            .directory(file::get_output_dir(self.output).await?)
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
        })
    }
}
