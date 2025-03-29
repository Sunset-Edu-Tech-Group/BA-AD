use crate::crypto::catalog::{Catalog, Media, MediaCatalog, TableCatalog};
use crate::helpers::config::{API_DATA_FILENAME, RegionConfig};
use crate::helpers::download_manager::{DownloadManager, DownloadStrategy};
use crate::helpers::file::FileManager;
use crate::helpers::json;
use crate::utils::catalog_fetcher::CatalogFetcher;

use anyhow::{Context, Result};
use rand;
use reqwest::Client;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::path::PathBuf;

#[derive(Debug, Serialize, Deserialize)]
pub struct ConnectionGroup {
    #[serde(rename = "OverrideConnectionGroups")]
    pub override_connection_groups: Vec<OverrideConnectionGroup>,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct OverrideConnectionGroup {
    #[serde(rename = "AddressablesCatalogUrlRoot")]
    pub addressables_catalog_url_root: String,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct ServerData {
    #[serde(rename = "ConnectionGroups")]
    pub connection_groups: Vec<ConnectionGroup>,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct BundleFile {
    #[serde(rename = "Name")]
    pub name: String,
    #[serde(rename = "Crc")]
    pub crc: Option<i64>,
    #[serde(rename = "Size")]
    pub size: Option<i64>,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct BundleDownloadInfo {
    #[serde(rename = "BundleFiles")]
    pub bundle_files: Vec<BundleFile>,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct JPGameFile {
    pub url: String,
    pub crc: i64,
    pub path: Option<String>,
    pub size: Option<i64>,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct GlobalGameFile {
    pub url: String,
    pub hash: String,
    pub path: String,
    pub size: i64,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct JPGameFiles {
    #[serde(rename = "AssetBundles")]
    pub asset_bundles: Vec<JPGameFile>,
    #[serde(rename = "TableBundles")]
    pub table_bundles: Vec<JPGameFile>,
    #[serde(rename = "MediaResources")]
    pub media_resources: Vec<JPGameFile>,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct GlobalGameFiles {
    #[serde(rename = "AssetBundles")]
    pub asset_bundles: Vec<GlobalGameFile>,
    #[serde(rename = "TableBundles")]
    pub table_bundles: Vec<GlobalGameFile>,
    #[serde(rename = "MediaResources")]
    pub media_resources: Vec<GlobalGameFile>,
}

pub struct CatalogParser<'a> {
    client: Client,
    file_manager: &'a FileManager,
    catalog_url: Option<String>,
    region_config: RegionConfig,
    addressable_url_cache: Option<String>,
    download_manager: DownloadManager,
}

impl<'a> CatalogParser<'a> {
    pub fn new(file_manager: &'a FileManager, catalog_url: Option<String>, config: &RegionConfig) -> Self {
        let client: Client = Client::new();
        let download_manager = DownloadManager::with_config(
            client.clone(),
            512 * 1024, // 512KB chunks for catalog files (usually smaller)
            4,          // Fewer connections to avoid server throttling
        );

        Self {
            client,
            file_manager,
            catalog_url,
            region_config: config.clone(),
            addressable_url_cache: None,
            download_manager,
        }
    }

    fn get_file_path(&self, filename: &str) -> String {
        self.region_config.catalog_file_path(filename)
    }

    async fn fetch_data<T: for<'de> serde::Deserialize<'de>>(&self, url: &str) -> Result<T> {
        self.client.get(url).send().await?.json::<T>().await.map_err(Into::into)
    }

    async fn fetch_bytes(&self, url: &str) -> Result<Vec<u8>> {
        let temp_path: PathBuf = self.file_manager.create_temp_file("download", "bytes")?;

        self.download_manager
            .download_file_with_strategy(url, &temp_path, DownloadStrategy::SingleThread)
            .await?;

        let bytes: Vec<u8> =
            std::fs::read(&temp_path).with_context(|| format!("Failed to read temporary file: {}", temp_path.display()))?;
        let _ = std::fs::remove_file(temp_path);

        if rand::random::<f32>() < 0.01 {
            let _ = self.file_manager.cleanup_temp_files();
        }

        Ok(bytes)
    }

    fn get_cached_addressable_url(&self, region: &str) -> Result<String> {
        let api_data: HashMap<String, serde_json::Value> = json::load_json(self.file_manager, API_DATA_FILENAME)?;

        let url: &str = api_data
            .get(region)
            .and_then(|v| v.get("addressable_url"))
            .and_then(|v| v.as_str())
            .ok_or_else(|| anyhow::anyhow!("Addressable URL not found for {}", region))?;

        Ok(url.to_string())
    }

    pub async fn save_addressable_url(&self, addressable_url: &str) -> Result<()> {
        json::update_region_data(self.file_manager, &self.region_config.id, None, Some(addressable_url), None)
    }

    pub async fn fetch_addressable_url(&mut self) -> Result<String> {
        if let Some(url) = &self.addressable_url_cache {
            return Ok(url.clone());
        }

        let catalog_fetcher: CatalogFetcher<'_> = CatalogFetcher::new(self.file_manager);
        let server_api: String = match &self.catalog_url {
            Some(url) => url.clone(),
            None => catalog_fetcher.get_catalog_url(&self.region_config.id).await?,
        };

        let server_data: ServerData = self.fetch_data(&server_api).await?;
        let addressable_url: String = server_data.connection_groups[0]
            .override_connection_groups
            .last()
            .context("No override connection groups found")?
            .addressables_catalog_url_root
            .clone();

        self.save_addressable_url(&addressable_url).await?;

        self.addressable_url_cache = Some(addressable_url.clone());

        Ok(addressable_url)
    }

    pub async fn fetch_catalogs(&mut self) -> Result<()> {
        self.file_manager.create_dir(&format!("catalogs/{}", self.region_config.id))?;

        match self.region_config.id.as_str() {
            "global" => {
                let catalog_fetcher: CatalogFetcher<'_> = CatalogFetcher::new(self.file_manager);
                let global_url: String = catalog_fetcher.get_catalog_url("global").await?;
                let resources_data: serde_json::Value = self.fetch_data(&global_url).await?;
                json::save_json(self.file_manager, &self.get_file_path("resources_path.json"), &resources_data)?;
            }
            _ => {
                let addressable_url: String = self.fetch_addressable_url().await?;

                let bundle_data: BundleDownloadInfo = self
                    .fetch_data(&format!("{}/Android/bundleDownloadInfo.json", addressable_url))
                    .await?;
                json::save_json(
                    self.file_manager,
                    &self.get_file_path("bundleDownloadInfo.json"),
                    &bundle_data,
                )?;

                let table_data: Vec<u8> = self
                    .fetch_bytes(&format!("{}/TableBundles/TableCatalog.bytes", addressable_url))
                    .await?;
                let table_catalog = TableCatalog::deserialize(&table_data, &addressable_url)?;
                table_catalog.to_json(self.file_manager, &self.get_file_path("TableCatalog.json"))?;

                let media_data: Vec<u8> = self
                    .fetch_bytes(&format!("{}/MediaResources/Catalog/MediaCatalog.bytes", addressable_url))
                    .await?;
                let media_catalog: Catalog<Media> = MediaCatalog::deserialize(&media_data, &addressable_url)?;
                media_catalog.to_json(self.file_manager, &self.get_file_path("MediaCatalog.json"))?;
            }
        }

        Ok(())
    }

    pub async fn get_game_jp_files(&mut self) -> Result<JPGameFiles> {
        let addressable_url: String = match &self.addressable_url_cache {
            Some(url) => url.clone(),
            None => match self.get_cached_addressable_url("japan") {
                Ok(url) => url,
                Err(_) => self.fetch_addressable_url().await?,
            },
        };

        let bundle_data: BundleDownloadInfo = json::load_json(self.file_manager, &self.get_file_path("bundleDownloadInfo.json"))?;

        let table_catalog: HashMap<String, serde_json::Value> =
            json::load_json(self.file_manager, &self.get_file_path("TableCatalog.json"))?;
        let table_data: &serde_json::Map<String, serde_json::Value> = table_catalog
            .get("Table")
            .and_then(|v| v.as_object())
            .context("Failed to find Table field in TableCatalog")?;

        let media_catalog: HashMap<String, serde_json::Value> =
            json::load_json(self.file_manager, &self.get_file_path("MediaCatalog.json"))?;
        let media_data: &serde_json::Map<String, serde_json::Value> = media_catalog
            .get("Table")
            .and_then(|v| v.as_object())
            .context("Failed to find Table field in MediaCatalog")?;

        let capacity: usize = bundle_data.bundle_files.len().max(table_data.len().max(media_data.len()));

        let mut asset_bundles: Vec<JPGameFile> = Vec::with_capacity(capacity);
        let mut table_bundles: Vec<JPGameFile> = Vec::with_capacity(capacity);
        let mut media_resources: Vec<JPGameFile> = Vec::with_capacity(capacity);

        for asset in &bundle_data.bundle_files {
            asset_bundles.push(JPGameFile {
                url: format!("{}/Android/{}", addressable_url, asset.name),
                crc: asset.crc.unwrap_or(0),
                path: None,
                size: asset.size,
            });
        }

        for (key, asset) in table_data {
            let crc: i64 = asset.get("Crc").and_then(|c| c.as_i64()).unwrap_or(0);
            let size: Option<i64> = asset.get("Size").and_then(|s| s.as_i64());

            table_bundles.push(JPGameFile {
                url: format!("{}/TableBundles/{}", addressable_url, key),
                crc,
                path: None,
                size,
            });
        }

        for (_, value) in media_data {
            let path: String = value
                .get("Path")
                .and_then(|p: &serde_json::Value| p.as_str())
                .unwrap_or("")
                .replace("\\", "/");

            let crc: i64 = value.get("Crc").and_then(|c: &serde_json::Value| c.as_i64()).unwrap_or(0);
            let bytes: Option<i64> = value.get("Bytes").and_then(|b: &serde_json::Value| b.as_i64());

            media_resources.push(JPGameFile {
                url: format!("{}/MediaResources/{}", addressable_url, path),
                crc,
                path: Some(path),
                size: bytes,
            });
        }

        Ok(JPGameFiles {
            asset_bundles,
            table_bundles,
            media_resources,
        })
    }

    pub async fn get_game_global_files(&self) -> Result<GlobalGameFiles> {
        let resources_data: serde_json::Value = json::load_json(self.file_manager, &self.get_file_path("resources_path.json"))?;

        let addressable_url: String = match self.get_cached_addressable_url("global") {
            Ok(url) => url.replace("/resource-data.json", ""),
            Err(_) => return Err(anyhow::anyhow!("Global addressable URL not found")),
        };

        let resources: &Vec<serde_json::Value> = resources_data["resources"]
            .as_array()
            .context("Failed to find resources array in resources_path.json")?;

        let capacity: usize = resources.len() / 3;
        let mut asset_bundles: Vec<GlobalGameFile> = Vec::with_capacity(capacity);
        let mut table_bundles: Vec<GlobalGameFile> = Vec::with_capacity(capacity);
        let mut media_resources: Vec<GlobalGameFile> = Vec::with_capacity(capacity);

        for resource in resources {
            let path: &str = resource["resource_path"]
                .as_str()
                .context("Failed to find resource_path in resource")?;
            let size: i64 = resource["resource_size"]
                .as_i64()
                .context("Failed to find resource_size in resource")?;
            let hash: &str = resource["resource_hash"]
                .as_str()
                .context("Failed to find resource_hash in resource")?;

            let game_file: GlobalGameFile = GlobalGameFile {
                url: format!("{}/{}", addressable_url, path),
                hash: hash.to_string(),
                path: path.to_string(),
                size,
            };

            if path.contains("Android") || path.contains("/assets-") {
                asset_bundles.push(game_file);
            } else if path.contains("TableBundles") {
                table_bundles.push(game_file);
            } else if path.contains("MediaResources") {
                media_resources.push(game_file);
            }
        }

        Ok(GlobalGameFiles {
            asset_bundles,
            table_bundles,
            media_resources,
        })
    }

    pub async fn save_game_files(&mut self) -> Result<()> {
        match self.region_config.id.as_str() {
            "global" => {
                let global_files: GlobalGameFiles = self.get_game_global_files().await?;
                json::save_json(self.file_manager, &self.get_file_path("GameFiles.json"), &global_files)?;
            }
            _ => {
                let jp_files: JPGameFiles = self.get_game_jp_files().await?;
                json::save_json(self.file_manager, &self.get_file_path("GameFiles.json"), &jp_files)?;
            }
        }

        Ok(())
    }
}
