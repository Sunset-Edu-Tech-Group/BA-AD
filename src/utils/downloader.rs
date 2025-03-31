use std::collections::HashMap;
use std::fs;
use std::path::{Path, PathBuf};

use anyhow::Result;
use reqwest::Client;

use crate::crypto::hash;
use crate::helpers::download_manager::{DownloadManager, DownloadStrategy};
use crate::helpers::file::FileManager;
use crate::helpers::logs::{info, warn};
use crate::utils::catalog_parser::{CatalogParser, GlobalGameFiles, JPGameFiles};
use crate::utils::catalog_parser::{GlobalGameFile, JPGameFile};

#[derive(Debug, Clone, Copy, PartialEq)]
pub enum ResourceCategory {
    AssetBundles,
    TableBundles,
    MediaResources,
    All,
}

#[derive(Debug, Clone, Copy, PartialEq)]
pub enum Region {
    Japan,
    Global,
}
pub enum GameFiles<'a> {
    JP(&'a JPGameFiles),
    Global(&'a GlobalGameFiles),
}

impl Region {
    pub fn as_str(&self) -> &'static str {
        match self {
            Region::Japan => "japan",
            Region::Global => "global",
        }
    }
}

trait GameFile {
    fn get_url(&self) -> &str;
    fn get_path(&self) -> Option<&str>;
    fn get_crc(&self) -> Option<i64>;
    fn get_hash(&self) -> Option<&str>;
    fn get_size(&self) -> Option<i64>;
}

impl GameFile for JPGameFile {
    fn get_url(&self) -> &str {
        &self.url
    }

    fn get_path(&self) -> Option<&str> {
        self.path.as_deref()
    }

    fn get_crc(&self) -> Option<i64> {
        Some(self.crc)
    }

    fn get_hash(&self) -> Option<&str> {
        None
    }

    fn get_size(&self) -> Option<i64> {
        self.size
    }
}

impl GameFile for GlobalGameFile {
    fn get_url(&self) -> &str {
        &self.url
    }

    fn get_path(&self) -> Option<&str> {
        Some(&self.path)
    }

    fn get_crc(&self) -> Option<i64> {
        None
    }

    fn get_hash(&self) -> Option<&str> {
        Some(&self.hash)
    }

    fn get_size(&self) -> Option<i64> {
        Some(self.size)
    }
}

pub struct ResourceDownloader<'a> {
    file_manager: &'a FileManager,
    catalog_url: Option<String>,
    output_path: PathBuf,
    region: Region,
    client: Client,
    download_manager: DownloadManager,
    max_concurrent_downloads: usize,
    update: bool,
    thread_count: usize,
}

impl<'a> ResourceDownloader<'a> {
    pub fn new(file_manager: &'a FileManager, region: Region, catalog_url: Option<String>, output_path: Option<&Path>) -> Result<Self> {
        let client: Client = Client::new();
        let thread_count = 0;
        let max_concurrent_downloads = 5;
        let download_manager: DownloadManager =
            DownloadManager::with_full_config(client.clone(), 1024 * 1024, thread_count, max_concurrent_downloads);
        let output: PathBuf = match output_path {
            Some(path) => path.to_path_buf(),
            None => file_manager.download_dir().to_path_buf(),
        };

        Ok(Self {
            file_manager,
            catalog_url,
            output_path: output,
            region,
            client,
            download_manager,
            max_concurrent_downloads,
            update: false,
            thread_count,
        })
    }

    pub fn set_max_concurrent_downloads(&mut self, limit: usize) {
        self.max_concurrent_downloads = limit;
        self.download_manager.set_max_single_thread_downloads(limit);
    }

    pub fn with_concurrent_downloads(mut self, limit: usize) -> Self {
        self.max_concurrent_downloads = limit;
        self.download_manager.set_max_single_thread_downloads(limit);
        self
    }

    pub fn set_update(&mut self, update: bool) {
        self.update = update;
    }

    pub fn with_update(mut self, update: bool) -> Self {
        self.update = update;
        self
    }

    pub fn set_thread_count(&mut self, thread_count: usize) {
        self.thread_count = thread_count;
    }

    pub fn with_thread_count(mut self, thread_count: usize) -> Self {
        self.thread_count = thread_count;
        self
    }

    pub fn get_file_path(&self, file_info: &HashMap<String, serde_json::Value>) -> PathBuf {
        if let Some(path) = file_info.get("path").and_then(|v| v.as_str()).filter(|s| !s.is_empty()) {
            return PathBuf::from(path);
        }

        if let Some(url_str) = file_info.get("url").and_then(|v| v.as_str()) {
            return PathBuf::from(url_str.split('/').last().unwrap_or("unknown_file"));
        }

        PathBuf::from("unknown_file")
    }

    pub fn get_base_path(&self) -> PathBuf {
        match self.region {
            Region::Japan => self.output_path.join("JP"),
            Region::Global => self.output_path.join("Global"),
        }
    }

    async fn check_file(&self, file_path: &Path, crc: Option<i64>, md5: Option<&str>) -> Result<bool> {
        if !file_path.exists() {
            return Ok(false);
        }

        match (crc, md5) {
            (Some(_), Some(_)) => {
                return Err(anyhow::anyhow!("Cannot specify both CRC and MD5 for file verification"));
            }
            (Some(crc_value), None) => {
                let file_crc: u32 = hash::calculate_crc32(file_path.to_path_buf())?;
                if file_crc != crc_value as u32 {
                    let filename = self.file_manager.get_filename(file_path);
                    warn(&format!("CRC mismatch for {}, will re-download", filename));
                    return Ok(false);
                }
            }
            (None, Some(md5_value)) => {
                let file_md5: String = hash::calculate_md5(file_path.to_path_buf())?;
                if file_md5 != md5_value {
                    let filename = self.file_manager.get_filename(file_path);
                    warn(&format!("MD5 mismatch for {}, will re-download", filename));
                    return Ok(false);
                }
            }
            (None, None) => {
                return Err(anyhow::anyhow!("Please provide either a CRC or MD5 for file verification"));
            }
        }

        let filename = self.file_manager.get_filename(file_path);
        warn(&format!("Skipping {}, already downloaded", filename));

        Ok(true)
    }

    async fn download_file(&self, url: String, output_path: PathBuf, crc: Option<i64>, md5: Option<&str>, mode: DownloadStrategy) -> Result<()> {
        let parent: Option<&Path> = output_path.parent();
        if parent.is_some() && !parent.unwrap().exists() {
            fs::create_dir_all(parent.unwrap())?;
        }

        let crc_match: bool = match crc {
            Some(crc_val) => self.check_file(&output_path, Some(crc_val), None).await?,
            None => false,
        };
        if crc_match {
            return Ok(());
        }

        let md5_match: bool = match md5 {
            Some(ref md5_val) => self.check_file(&output_path, None, Some(md5_val)).await?,
            None => false,
        };
        if md5_match {
            return Ok(());
        }

        self.download_manager.download_file_with_strategy(&url, &output_path, mode).await?;

        let file_name = self.file_manager.get_filename(&output_path);
        info(&format!("Downloaded {}", file_name));

        Ok(())
    }

    async fn download_category<T: GameFile>(&self, files: &[T], base_path: &PathBuf) -> Result<()> {
        fs::create_dir_all(base_path)?;

        let output_dir = self.file_manager.canonical_path(base_path)?;
        for file in files {
            let file_path = match file.get_path() {
                Some(p) => p.to_string(),
                None => file.get_url().split('/').last().unwrap_or("unknown").to_string(),
            };
            let output_path = output_dir.join(&file_path);

            self.download_file(
                file.get_url().to_string(),
                output_path,
                file.get_crc(),
                file.get_hash(),
                DownloadStrategy::Auto,
            )
            .await?;
        }
        Ok(())
    }

    async fn process_category(&self, game_files: &GameFiles<'_>, category: ResourceCategory, path: &PathBuf) -> Result<()> {
        match game_files {
            GameFiles::JP(jp_files) => match category {
                ResourceCategory::AssetBundles => self.download_category(&jp_files.asset_bundles, path).await?,
                ResourceCategory::TableBundles => self.download_category(&jp_files.table_bundles, path).await?,
                ResourceCategory::MediaResources => self.download_category(&jp_files.media_resources, path).await?,
                ResourceCategory::All => {}
            },
            GameFiles::Global(global_files) => match category {
                ResourceCategory::AssetBundles => self.download_category(&global_files.asset_bundles, path).await?,
                ResourceCategory::TableBundles => self.download_category(&global_files.table_bundles, path).await?,
                ResourceCategory::MediaResources => self.download_category(&global_files.media_resources, path).await?,
                ResourceCategory::All => {}
            },
        }

        Ok(())
    }

    async fn fetch_category(&self, game_files: &GameFiles<'_>, category: ResourceCategory, base_path: &Path) -> Result<()> {
        match category {
            ResourceCategory::AssetBundles => {
                info("Downloading AssetBundles...");
                let category_path = base_path.join("AssetBundles");
                self.process_category(game_files, category, &category_path).await?;
            }
            ResourceCategory::TableBundles => {
                info("Downloading TableBundles...");
                let category_path = base_path.join("TableBundles");
                self.process_category(game_files, category, &category_path).await?;
            }
            ResourceCategory::MediaResources => {
                info("Downloading MediaResources...");
                let category_path = base_path.join("MediaResources");
                self.process_category(game_files, category, &category_path).await?;
            }
            ResourceCategory::All => {
                // This case should be handled in the calling function
            }
        }

        Ok(())
    }

    async fn initialize_categories(&self, game_files: &GameFiles<'_>, categories: &[ResourceCategory]) -> Result<()> {
        let base_path = self.get_base_path();

        for category in categories {
            if *category == ResourceCategory::All {
                continue;
            }

            self.fetch_category(game_files, *category, &base_path).await?;
        }

        Ok(())
    }

    pub async fn download(&self, categories: &[ResourceCategory]) -> Result<()> {
        let region_config = crate::helpers::config::RegionConfig::new(self.region.as_str());
        let mut catalog_parser: CatalogParser<'_> = CatalogParser::new(self.file_manager, self.catalog_url.clone(), &region_config);

        let selected_categories = if categories.contains(&ResourceCategory::All) {
            vec![
                ResourceCategory::AssetBundles,
                ResourceCategory::TableBundles,
                ResourceCategory::MediaResources,
            ]
        } else {
            categories.to_vec()
        };

        match self.region {
            Region::Japan => {
                let game_files: JPGameFiles = catalog_parser.get_game_jp_files().await?;
                self.initialize_categories(&GameFiles::JP(&game_files), &selected_categories).await?;
            }
            Region::Global => {
                let game_files: GlobalGameFiles = catalog_parser.get_game_global_files().await?;
                self.initialize_categories(&GameFiles::Global(&game_files), &selected_categories).await?;
            }
        }

        Ok(())
    }
}
