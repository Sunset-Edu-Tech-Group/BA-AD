use crate::crypto::hash;
use crate::helpers::download_manager::{DownloadManager, DownloadStrategy};
use crate::helpers::file::FileManager;
use crate::utils::catalog_parser::{CatalogParser, GlobalGameFiles, JPGameFiles};

use anyhow::{Error, Result};
use reqwest::Client;
use tokio::task::JoinHandle;
use std::collections::HashMap;
use std::fs;
use std::path::{Path, PathBuf};


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

impl Region {
    pub fn as_str(&self) -> &'static str {
        match self {
            Region::Japan => "japan",
            Region::Global => "global",
        }
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
    pub fn new(
        file_manager: &'a FileManager,
        region: Region,
        catalog_url: Option<String>,
        output_path: Option<&Path>,
    ) -> Result<Self> {
        let client: Client = Client::new();
        let max_concurrent_downloads = 5; // Default value
        let download_manager: DownloadManager = DownloadManager::with_full_config(
            client.clone(), 
            1024 * 1024, // 1MB chunk size
            8,           // Max connections per download
            max_concurrent_downloads
        );

        let output: PathBuf = match output_path {
            Some(path) => path.to_path_buf(),
            None => file_manager.data_path("downloads"),
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
            thread_count: 0,
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

    fn get_file_path(&self, file_info: &HashMap<String, serde_json::Value>) -> PathBuf {
        if let Some(path) = file_info.get("path").and_then(|v| v.as_str()).filter(|s| !s.is_empty()) {
            return PathBuf::from(path);
        }

        if let Some(url_str) = file_info.get("url").and_then(|v| v.as_str()) {
            return PathBuf::from(url_str.split('/').last().unwrap_or("unknown_file"));
        }

        PathBuf::from("unknown_file")
    }

    async fn check_existing_file(&self, file_path: &Path, crc: Option<i64>, md5: Option<&str>) -> Result<bool> {
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
                    println!("CRC mismatch for {}, will re-download", file_path.display());
                    return Ok(false);
                }
            }
            (None, Some(md5_value)) => {
                let file_md5: String = hash::calculate_md5(file_path.to_path_buf())?;
                if file_md5 != md5_value {
                    println!("MD5 mismatch for {}, will re-download", file_path.display());
                    return Ok(false);
                }
            }
            (None, None) => {
                return Err(anyhow::anyhow!("Please provide either a CRC or MD5 for file verification"));
            }
        }

        println!("Skipping {}, already downloaded", file_path.display());
        Ok(true)
    }

    async fn download_file(&self, url: String, output_path: PathBuf, crc: Option<i64>, md5: Option<String>) -> Result<()> {
        let parent: Option<&Path> = output_path.parent();
        if parent.is_some() && !parent.unwrap().exists() {
            fs::create_dir_all(parent.unwrap())?;
        }

        let crc_match: bool = match crc {
            Some(crc_val) => self.check_existing_file(&output_path, Some(crc_val), None).await?,
            None => false,
        };
        if crc_match {
            return Ok(());
        }

        let md5_match: bool = match md5 {
            Some(ref md5_val) => self.check_existing_file(&output_path, None, Some(md5_val)).await?,
            None => false,
        };
        if md5_match {
            return Ok(());
        }

        println!("Downloading: {}", output_path.display());

        self.download_manager
            .download_file_with_strategy(&url, &output_path, DownloadStrategy::Auto)
            .await?;

        Ok(())
    }

    async fn download_jp_category(&self, files: &[crate::utils::catalog_parser::JPGameFile], base_path: &Path) -> Result<()> {
        fs::create_dir_all(base_path)?;

        let mut download_tasks: Vec<JoinHandle<Result<(), Error>>> = Vec::with_capacity(files.len());

        for file in files {
            let url = file.url.clone();
            let path = match &file.path {
                Some(p) => p.clone(),
                None => file.url.split('/').last().unwrap_or("unknown").to_string(),
            };
            let output_path = base_path.join(&path);
            let crc = file.crc;
            let size = file.size;
            let dm = self.download_manager.clone();

            if let Some(parent) = output_path.parent() {
                if !parent.exists() {
                    fs::create_dir_all(parent)?;
                }
            }

            if output_path.exists() && crc != 0 {
                if let Ok(existing_crc) = hash::calculate_crc32(output_path.clone()) {
                    if existing_crc == crc as u32 {
                        println!("Skipping {}, already downloaded", output_path.display());
                        continue;
                    }
                }
            }

            let thread_count = self.thread_count;
            download_tasks.push(tokio::spawn(async move {
                let strategy = if thread_count > 0 {
                    DownloadStrategy::MultiThread { thread_count }
                } else if size.unwrap_or(0) > 5 * 1024 * 1024 {
                    DownloadStrategy::MultiThread { thread_count: 4 }
                } else {
                    DownloadStrategy::SingleThread
                };

                println!("Downloading: {}", output_path.display());
                dm.download_file_with_strategy(&url, &output_path, strategy).await?;

                if crc != 0 {
                    let downloaded_crc = hash::calculate_crc32(output_path.clone())?;
                    if downloaded_crc != crc as u32 {
                        println!("CRC mismatch for {}", output_path.display());
                    } else {
                        println!("Successfully verified: {}", output_path.display());
                    }
                }

                Ok::<_, anyhow::Error>(())
            }));
        }

        for task in download_tasks {
            let result = task.await?;
            if let Err(e) = result {
                eprintln!("Download error: {}", e);
            }
        }

        Ok(())
    }

    async fn download_global_category(
        &self,
        files: &[crate::utils::catalog_parser::GlobalGameFile],
        base_path: &Path,
    ) -> Result<()> {
        fs::create_dir_all(base_path)?;

        let mut download_tasks: Vec<JoinHandle<Result<(), Error>>> = Vec::with_capacity(files.len());

        for file in files {
            let url = file.url.clone();
            let path = file.path.clone();
            let output_path = base_path.join(&path);
            let hash = file.hash.clone();
            let size = file.size;
            let dm = self.download_manager.clone();

            if let Some(parent) = output_path.parent() {
                if !parent.exists() {
                    fs::create_dir_all(parent)?;
                }
            }

            if output_path.exists() {
                if let Ok(existing_hash) = hash::calculate_md5(output_path.clone()) {
                    if existing_hash == hash {
                        println!("Skipping {}, already downloaded", output_path.display());
                        continue;
                    }
                }
            }

            let thread_count = self.thread_count;
            download_tasks.push(tokio::spawn(async move {
                let strategy = if thread_count > 0 {
                    DownloadStrategy::MultiThread { thread_count }
                } else if size > 5 * 1024 * 1024 {
                    DownloadStrategy::MultiThread { thread_count: 4 }
                } else {
                    DownloadStrategy::SingleThread
                };

                println!("Downloading: {}", output_path.display());
                dm.download_file_with_strategy(&url, &output_path, strategy).await?;

                let downloaded_hash = hash::calculate_md5(output_path.clone())?;
                if downloaded_hash != hash {
                    println!("MD5 mismatch for {}", output_path.display());
                } else {
                    println!("Successfully verified: {}", output_path.display());
                }

                Ok::<_, anyhow::Error>(())
            }));
        }

        for task in download_tasks {
            let result = task.await?;
            if let Err(e) = result {
                eprintln!("Download error: {}", e);
            }
        }

        Ok(())
    }

    async fn download_jp_categories(&self, game_files: &JPGameFiles, categories: &[ResourceCategory]) -> Result<()> {
        let base_path = &self.output_path;

        for category in categories {
            match category {
                ResourceCategory::AssetBundles => {
                    println!("Downloading Asset Bundles...");
                    let asset_path = base_path.join("AssetBundles");
                    self.download_jp_category(&game_files.asset_bundles, &asset_path).await?;
                }
                ResourceCategory::TableBundles => {
                    println!("Downloading Table Bundles...");
                    let table_path = base_path.join("TableBundles");
                    self.download_jp_category(&game_files.table_bundles, &table_path).await?;
                }
                ResourceCategory::MediaResources => {
                    println!("Downloading Media Resources...");
                    let media_path = base_path.join("MediaResources");
                    self.download_jp_category(&game_files.media_resources, &media_path).await?;
                }
                ResourceCategory::All => {
                    continue;
                }
            }
        }

        Ok(())
    }

    async fn download_global_categories(&self, game_files: &GlobalGameFiles, categories: &[ResourceCategory]) -> Result<()> {
        let base_path = &self.output_path;

        for category in categories {
            match category {
                ResourceCategory::AssetBundles => {
                    println!("Downloading Global Asset Bundles...");
                    let asset_path = base_path.join("AssetBundles");
                    self.download_global_category(&game_files.asset_bundles, &asset_path).await?;
                }
                ResourceCategory::TableBundles => {
                    println!("Downloading Global Table Bundles...");
                    let table_path = base_path.join("TableBundles");
                    self.download_global_category(&game_files.table_bundles, &table_path).await?;
                }
                ResourceCategory::MediaResources => {
                    println!("Downloading Global Media Resources...");
                    let media_path = base_path.join("MediaResources");
                    self.download_global_category(&game_files.media_resources, &media_path)
                        .await?;
                }
                ResourceCategory::All => {
                    continue;
                }
            }
        }

        Ok(())
    }

    pub async fn download(&self, categories: &[ResourceCategory]) -> Result<()> {
        fs::create_dir_all(&self.output_path)?;

        let region_config = crate::helpers::config::RegionConfig::new(self.region.as_str());
        let mut catalog_parser: CatalogParser<'_> = CatalogParser::new(self.file_manager, self.catalog_url.clone(), &region_config);

        println!("Fetching catalogs...");
        catalog_parser.fetch_catalogs().await?;

        let download_all = categories.contains(&ResourceCategory::All);
        let effective_categories = if download_all {
            vec![
                ResourceCategory::AssetBundles,
                ResourceCategory::TableBundles,
                ResourceCategory::MediaResources,
            ]
        } else {
            categories.to_vec()
        };

        println!("Saving game files information...");
        catalog_parser.save_game_files().await?;

        match self.region {
            Region::Japan => {
                let game_files: JPGameFiles = catalog_parser.get_game_jp_files().await?;
                self.download_jp_categories(&game_files, &effective_categories).await?;
            }
            Region::Global => {
                let game_files: GlobalGameFiles = catalog_parser.get_game_global_files().await?;
                self.download_global_categories(&game_files, &effective_categories).await?;
            }
        }

        println!("Download complete!");
        Ok(())
    }
}
