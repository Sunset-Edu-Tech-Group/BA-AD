use std::path::{Path, PathBuf};

use anyhow::Result;
use reqwest::Client;
use tokio::fs;

use crate::crypto::hash;
use crate::helpers::download_manager::DownloadManager;
use crate::helpers::file;
use crate::helpers::file::FileManager;
use crate::helpers::interface::reset_download_progress;
use crate::utils::catalog_parser::{CatalogParser, GlobalGameFiles, JPGameFiles};
use crate::utils::catalog_parser::{GlobalGameFile, JPGameFile};
use crate::{debug, info, warn};

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

    #[allow(dead_code)]
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

    #[allow(dead_code)]
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

    #[allow(dead_code)]
    fn get_size(&self) -> Option<i64> {
        Some(self.size)
    }
}

pub struct ResourceDownloader<'a> {
    file_manager: &'a FileManager,
    catalog_url: Option<String>,
    output_path: PathBuf,
    region: Region,
    threads: usize,
    limit: usize,
    update: bool,
    download_manager: DownloadManager,
}

impl<'a> ResourceDownloader<'a> {
    pub fn new(file_manager: &'a FileManager, region: Region, catalog_url: Option<String>, output_path: Option<&Path>) -> Result<Self> {
        let client: Client = Client::new();
        let threads = 0;
        let limit = 1;

        let download_manager = DownloadManager::new(client, threads, limit);

        let output: PathBuf = match output_path {
            Some(path) => path.to_path_buf(),
            None => file_manager.download_dir().to_path_buf(),
        };

        Ok(Self {
            file_manager,
            catalog_url,
            output_path: output,
            region,
            threads,
            limit,
            update: false,
            download_manager,
        })
    }

    pub fn set_limit(&mut self, limit: usize) {
        self.limit = limit;
        self.download_manager = DownloadManager::new(reqwest::Client::new(), self.threads, limit);
    }

    #[allow(dead_code)]
    pub fn with_limit(mut self, limit: usize) -> Self {
        self.limit = limit;
        self
    }

    pub fn set_update(&mut self, update: bool) {
        self.update = update;
    }

    #[allow(dead_code)]
    pub fn with_update(mut self, update: bool) -> Self {
        self.update = update;
        self
    }

    pub fn set_threads(&mut self, threads: usize) {
        self.threads = threads;
        self.download_manager = DownloadManager::new(reqwest::Client::new(), threads, self.limit);
    }

    #[allow(dead_code)]
    pub fn with_threads(mut self, threads: usize) -> Self {
        self.threads = threads;
        self
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
                    warn!("CRC mismatch for {}, will re-download", filename);
                    return Ok(false);
                }
            }
            (None, Some(md5_value)) => {
                let file_md5: String = hash::calculate_md5(file_path.to_path_buf())?;
                if file_md5 != md5_value {
                    let filename = file::get_filename(file_path);
                    warn!("MD5 mismatch for {}, will re-download", filename);
                    return Ok(false);
                }
            }
            (None, None) => {
                return Err(anyhow::anyhow!("Please provide either a CRC or MD5 for file verification"));
            }
        }

        let filename = file::get_filename(file_path);
        warn!("Skipping {}, already downloaded", filename);

        Ok(true)
    }

    async fn download_category<T: GameFile>(&self, files: &[T], base_path: &PathBuf) -> Result<()> {
        fs::create_dir_all(base_path).await?;

        let output_dir = match fs::canonicalize(base_path).await {
            Ok(path) => path,
            Err(_) => base_path.clone(),
        };

        debug!("Using {} threads", self.threads);
        debug!("Using {} limit", self.limit);

        let mut url_path = Vec::new();
        for file in files {
            let file_path = match file.get_path() {
                Some(p) => p.to_string(),
                None => file.get_url().split('/').last().unwrap_or("unknown").to_string(),
            };
            let output_path = output_dir.join(&file_path);

            debug!("File Path: {}", file_path);

            let crc_match: bool = match file.get_crc() {
                Some(crc_val) => self.check_file(&output_path, Some(crc_val), None).await?,
                None => false,
            };

            let md5_match: bool = match file.get_hash() {
                Some(hash_val) => self.check_file(&output_path, None, Some(hash_val)).await?,
                None => false,
            };

            debug!("CRC {:?} Match: {}", file.get_crc(), crc_match);
            debug!("MD5 {:?} Match: {}", file.get_hash(), md5_match);

            if !crc_match && !md5_match {
                let url = file.get_url().to_string();

                debug!("URL: {}", url);
                debug!("Output Path {}", output_path.display());

                url_path.push((url, output_path));
            }
        }

        if !url_path.is_empty() {
            info!("Downloading {} files", url_path.len());
            let results = self.download_manager.download_files_with_progress(url_path).await;

            for result in results {
                if let Err(e) = result {
                    warn!("Error downloading file: {}", e);
                }
            }
        } else {
            info!("No files to download");
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
                info!("Downloading AssetBundles...");
                let category_path = base_path.join("AssetBundles");
                self.process_category(game_files, category, &category_path).await?;
            }
            ResourceCategory::TableBundles => {
                info!("Downloading TableBundles...");
                let category_path = base_path.join("TableBundles");
                self.process_category(game_files, category, &category_path).await?;
            }
            ResourceCategory::MediaResources => {
                info!("Downloading MediaResources...");
                let category_path = base_path.join("MediaResources");
                self.process_category(game_files, category, &category_path).await?;
            }
            ResourceCategory::All => {
                info!("Downloading Everything...");
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

        reset_download_progress();

        Ok(())
    }
}
