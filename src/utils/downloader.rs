use std::collections::HashMap;
use std::fs;
use std::path::{Path, PathBuf};

use anyhow::Result;
use reqwest::Client;

use crate::crypto::hash;
use crate::helpers::config::RESOURCE_DOWNLOAD_CHUNK_SIZE;
use crate::helpers::download_manager::DownloadManager;
use crate::helpers::file;
use crate::helpers::file::FileManager;
use crate::helpers::interface::{reset_download_progress, start_simple_progress};
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
    download_manager: DownloadManager,
    connections: usize,
    cores: usize,
    limit: usize,
    update: bool,
    chunk_size: u64,
}

impl<'a> ResourceDownloader<'a> {
    pub fn new(file_manager: &'a FileManager, region: Region, catalog_url: Option<String>, output_path: Option<&Path>) -> Result<Self> {
        let client: Client = Client::new();

        let connections = 0;
        let cores = 0;
        let limit = 1;
        let chunk_size = RESOURCE_DOWNLOAD_CHUNK_SIZE;

        let download_manager = DownloadManager::new(client, chunk_size);

        let output: PathBuf = match output_path {
            Some(path) => path.to_path_buf(),
            None => file_manager.download_dir().to_path_buf(),
        };

        Ok(Self {
            file_manager,
            catalog_url,
            output_path: output,
            region,
            download_manager,
            connections,
            cores,
            limit,
            update: false,
            chunk_size,
        })
    }

    pub fn set_max_concurrent_downloads(&mut self, limit: usize) {
        self.limit = limit;
    }

    pub fn with_concurrent_downloads(mut self, limit: usize) -> Self {
        self.limit = limit;
        self
    }

    pub fn set_update(&mut self, update: bool) {
        self.update = update;
    }

    pub fn with_update(mut self, update: bool) -> Self {
        self.update = update;
        self
    }

    pub fn set_thread_count(&mut self, cores: usize) {
        self.cores = cores;
    }

    pub fn with_thread_count(mut self, cores: usize) -> Self {
        self.cores = cores;
        self
    }

    pub fn set_connections(&mut self, connections: usize) {
        self.connections = connections;
    }

    pub fn with_connections(mut self, connections: usize) -> Self {
        self.connections = connections;
        self
    }

    pub fn set_chunk_size(&mut self, chunk_size: u64) {
        self.chunk_size = chunk_size;
    }

    pub fn with_chunk_size(mut self, chunk_size: u64) -> Self {
        self.chunk_size = chunk_size;
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
                    let filename = file::get_filename(file_path);
                    warn(&format!("CRC mismatch for {}, will re-download", filename));
                    return Ok(false);
                }
            }
            (None, Some(md5_value)) => {
                let file_md5: String = hash::calculate_md5(file_path.to_path_buf())?;
                if file_md5 != md5_value {
                    let filename = file::get_filename(file_path);
                    warn(&format!("MD5 mismatch for {}, will re-download", filename));
                    return Ok(false);
                }
            }
            (None, None) => {
                return Err(anyhow::anyhow!("Please provide either a CRC or MD5 for file verification"));
            }
        }

        let filename = file::get_filename(file_path);
        warn(&format!("Skipping {}, already downloaded", filename));

        Ok(true)
    }

    async fn download_file(&self, url: String, output_path: PathBuf, crc: Option<i64>, md5: Option<&str>) -> Result<()> {
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

        self.download_manager
            .download(&url, &output_path, false, self.connections, self.cores, self.limit)
            .await?;

        let file_name = file::get_filename(&output_path);
        info(&format!("Downloaded {}", file_name));

        Ok(())
    }

    async fn download_category<T: GameFile>(&self, files: &[T], base_path: &PathBuf) -> Result<()> {
        fs::create_dir_all(base_path)?;

        let mut total_size: u64 = 0;
        for file in files {
            if let Some(size) = file.get_size() {
                total_size += size as u64;
            }
        }

        start_simple_progress(files.len());
        self.download_manager.init_batch_download(files.len(), total_size).await;

        let output_dir = match std::fs::canonicalize(base_path) {
            Ok(path) => path,
            Err(_) => base_path.clone(),
        };

        for file in files {
            let file_path = match file.get_path() {
                Some(p) => p.to_string(),
                None => file.get_url().split('/').last().unwrap_or("unknown").to_string(),
            };
            let output_path = output_dir.join(&file_path);

            self.download_file(file.get_url().to_string(), output_path, file.get_crc(), file.get_hash())
                .await?;
        }

        reset_download_progress();
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
                info("Downloading Everything...");
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
        // Reset any existing progress before starting new downloads
        reset_download_progress();

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

        // Reset progress display at the end of all downloads
        reset_download_progress();

        Ok(())
    }
}
