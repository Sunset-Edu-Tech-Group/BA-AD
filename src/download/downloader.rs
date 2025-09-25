use crate::download::ResourceFilter;
use crate::helpers::{
    DownloadError, GameFiles, GameFilesBundles, GlobalGameResources, HashValue, JapanGameResources,
    ServerConfig, ServerRegion,
};
use crate::utils::{json, network};

use baad_core::{error, file, info, warn};
use reqwest::Url;
use std::mem::discriminant;
use std::path::{Path, PathBuf};
use std::rc::Rc;
use trauma::download::{Download, Status};
use trauma::downloader::{Downloader, DownloaderBuilder};
use trauma::progress::{ProgressBarOpts, StyleOptions};

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
    proxy: Option<String>,
}

pub struct ResourceDownloadBuilder {
    output: Option<PathBuf>,
    retries: u32,
    limit: u64,
    config: Rc<ServerConfig>,
    proxy: Option<String>,
}

impl ResourceDownloader {
    pub async fn new(
        output: Option<PathBuf>,
        config: Rc<ServerConfig>,
    ) -> Result<Self, DownloadError> {
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
    ) -> Result<(), DownloadError> {
        match &self.config.region {
            ServerRegion::Global => {
                let game_resources: GlobalGameResources = {
                    let path = file::get_data_path("catalog/global/GameFiles.json")?;
                    json::load_json(&path).await?
                };

                let collections = Self::get_collections(&category, &game_resources);
                let downloads = self.process_global_files(collections, filter);
                self.execute_downloads(downloads, category).await
            }
            ServerRegion::Japan => {
                let game_resources: JapanGameResources = {
                    let path = file::get_data_path("catalog/japan/GameFiles.json")?;
                    json::load_json(&path).await?
                };

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
                filter.is_none_or(|f| Self::matches_filter(f, get_path(file), get_bundles(file)))
            })
            .filter_map(|file| {
                Self::create_download(get_url(file), get_path(file), get_hash(file), None)
            })
            .collect()
    }

    fn process_japan_files(
        &self,
        game_resources: &JapanGameResources,
        _category: &ResourceCategory,
        _filter: Option<ResourceFilter>,
    ) -> Vec<Download> {
        let mut downloads = Vec::new();

        if self.should_include_category(_category, ResourceCategory::Assets) {
            downloads.extend(Self::process_japan_assets(
                &game_resources.asset_bundles,
                _filter.as_ref(),
            ));
        }

        if self.should_include_category(_category, ResourceCategory::Tables) {
            downloads.extend(Self::process_files_with_bundles(
                &game_resources.table_bundles,
                _filter.as_ref(),
                |f| &f.url,
                |f| &f.path,
                |f| &f.hash,
                |_| None,
            ));
        }

        if self.should_include_category(_category, ResourceCategory::Media) {
            downloads.extend(Self::process_files_with_bundles(
                &game_resources.media_resources,
                _filter.as_ref(),
                |f| &f.url,
                |f| &f.path,
                |f| &f.hash,
                |_| None,
            ));
        }

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

    fn convert_path_to_bundle(zip_path: &str, bundle_filename: &str) -> String {
        if let Some(last_slash) = zip_path.rfind('/') {
            format!("{}/{}", &zip_path[..last_slash], bundle_filename)
        } else {
            bundle_filename.to_string()
        }
    }

    fn process_japan_assets(
        files: &[GameFilesBundles],
        filter: Option<&ResourceFilter>,
    ) -> Vec<Download> {
        files
            .iter()
            .filter_map(|file| {
                if let Some(f) = filter {
                    let filename = Path::new(&file.path)
                        .file_name()
                        .and_then(|name| name.to_str())
                        .unwrap_or(&file.path);

                    if f.matches(filename) {
                        return Self::create_download(&file.url, &file.path, &file.hash, None);
                    }

                    if let Some(matched_bundle) = file
                        .bundle_files
                        .iter()
                        .find(|bundle_name| f.matches(bundle_name))
                    {
                        return Self::create_download(
                            &file.url,
                            &file.path,
                            &file.hash,
                            Some(matched_bundle),
                        );
                    }

                    None
                } else {
                    Self::create_download(&file.url, &file.path, &file.hash, None)
                }
            })
            .collect()
    }

    fn create_download(
        url: &str,
        path: &str,
        hash: &HashValue,
        target: Option<&str>,
    ) -> Option<Download> {
        let parsed_url = Url::parse(url).ok()?;
    
        let final_path = if let Some(bundle_filename) = target {
            Self::convert_path_to_bundle(path, bundle_filename)
        } else {
            path.to_string()
        };
    
        let target_filename = Path::new(&final_path)
            .file_name()?
            .to_str()?
            .to_string();

        Some(Download {
            url: parsed_url,
            filename: final_path,
            target_file: Some(target_filename),
            hash: Some(match hash {
                HashValue::Crc(crc) => crc.to_string(),
                HashValue::Md5(md5) => md5.clone(),
            }),
        })
    }

    async fn execute_downloads(
        &self,
        downloads: Vec<Download>,
        category: ResourceCategory,
    ) -> Result<(), DownloadError> {
        if downloads.is_empty() {
            warn!(
                ?category,
                "No files matched the filter criteria for catalog"
            );
            return Err(DownloadError::NoFilesMatched);
        }

        info!(?category, "Found {} files for download", downloads.len());
        info!("Downloading...");

        let proxy = network::create_proxy(self.proxy.as_deref()).map_err(DownloadError::Network)?;
        self.downloader.download(&downloads, proxy).await;

        Ok(())
    }
}

impl ResourceDownloadBuilder {
    pub fn new(config: Rc<ServerConfig>) -> Result<Self, DownloadError> {
        Ok(Self {
            output: None,
            retries: 10,
            limit: 10,
            config,
            proxy: None,
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

    pub fn proxy(mut self, proxy: Option<String>) -> Self {
        self.proxy = proxy;
        self
    }

    pub async fn build(self) -> Result<ResourceDownloader, DownloadError> {
        if self.retries == 0 {
            return Err(DownloadError::RetryCountZero);
        }

        if self.limit == 0 {
            return Err(DownloadError::DownloadLimitZero);
        }

        let style = StyleOptions::new(ProgressBarOpts::hidden(), ProgressBarOpts::hidden());

        let downloader = DownloaderBuilder::new()
            .directory(file::get_output_dir(self.output).await?)
            .concurrent_downloads(self.limit as usize)
            .retries(self.retries)
            .style_options(style)
            .on_complete({
                move |summary| {
                    let filename = Path::new(&summary.download().filename)
                        .file_name()
                        .and_then(|name| name.to_str())
                        .unwrap_or(&summary.download().filename);
                    match summary.status() {
                        Status::Success => {
                            info!(success = true, filename = filename, "Downloaded");
                        }
                        Status::Fail(error) => {
                            error!(cause = error, filename = filename, "Failed to download");
                        }
                        Status::Skipped(reason) => {
                            warn!(cause = reason, filename = filename, "Skipped");
                        }
                        Status::HashMismatch(reason) => {
                            warn!(cause = reason, filename = filename, "Outdated");
                        }
                        Status::NotStarted => {
                            // Ignore
                        }
                    }
                }
            })
            .build();

        Ok(ResourceDownloader {
            downloader,
            config: self.config,
            proxy: self.proxy,
        })
    }
}
