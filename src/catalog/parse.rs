use crate::helpers::api::{
    ApiData, AssetBundle, BundleDownloadInfo, GameFiles, GlobalCatalog, HashValue, MediaResources,
    Resource, TableResources
};
use crate::helpers::config::{ServerConfig, ServerRegion};
use crate::utils::file::FileManager;
use crate::utils::json::{load_json, save_json};

use anyhow::Result;
use bacy::{MediaCatalog, TableCatalog};
use reqwest::Client;

struct Resources<'a> {
    asset_bundles: Vec<&'a Resource>,
    media_resources: Vec<&'a Resource>,
    table_bundles: Vec<&'a Resource>,
}

pub struct CatalogParser {
    client: Client,
    file_manager: FileManager,
    config: ServerConfig,
}

impl CatalogParser {
    pub fn new(file_manager: &FileManager, config: &ServerConfig) -> Result<Self> {
        let client = Client::new();

        Ok(Self {
            client,
            config: config.clone(),
            file_manager: file_manager.clone(),
        })
    }

    async fn japan_data(&self, catalog_url: &String) -> Result<()> {
        let asset_data = self
            .client
            .get(format!("{}/Android/bundleDownloadInfo.json", catalog_url))
            .send()
            .await?
            .json::<BundleDownloadInfo>()
            .await?;

        save_json(
            &self.file_manager,
            "catalog/japan/bundleDownloadInfo.json",
            &asset_data,
        )
        .await?;

        let media_bytes = self
            .client
            .get(format!(
                "{}/MediaResources/Catalog/MediaCatalog.bytes",
                catalog_url
            ))
            .send()
            .await?
            .bytes()
            .await?;
        let media_data = MediaCatalog::deserialize(&media_bytes, &catalog_url)?;

        save_json(
            &self.file_manager,
            "catalog/japan/MediaCatalog.json",
            &media_data,
        )
        .await?;

        let table_bytes = self
            .client
            .get(format!("{}/TableBundles/TableCatalog.bytes", catalog_url))
            .send()
            .await?
            .bytes()
            .await?;
        let table_data = TableCatalog::deserialize(&table_bytes, &catalog_url)?;

        save_json(
            &self.file_manager,
            "catalog/japan/TableCatalog.json",
            &table_data,
        )
        .await?;

        Ok(())
    }

    async fn japan_gamefiles(&self, catalog_url: &String) -> Result<()> {
        let bundle_info: BundleDownloadInfo =
            load_json(&self.file_manager, "catalog/japan/bundleDownloadInfo.json").await?;
        let table_catalog: TableCatalog =
            load_json(&self.file_manager, "catalog/japan/TableCatalog.json").await?;
        let media_catalog: MediaCatalog =
            load_json(&self.file_manager, "catalog/japan/MediaCatalog.json").await?;

        let mut asset = Vec::new();
        let mut table = Vec::new();
        let mut media = Vec::new();

        for bundle in bundle_info.bundle_files {
            asset.push(GameFiles {
                url: format!("{}/Android/{}", catalog_url, bundle.name),
                path: format!("Android/{}", bundle.name),
                hash: HashValue::Crc(bundle.crc),
                size: bundle.size,
            });
        }

        for (_, table_entry) in table_catalog.table {
            table.push(GameFiles {
                url: format!("{}/TableBundles/{}", catalog_url, table_entry.name),
                path: format!("TableBundles/{}", table_entry.name),
                hash: HashValue::Crc(table_entry.crc),
                size: table_entry.size,
            });
        }

        for (_, media_entry) in media_catalog.table {
            let media_path = media_entry.path.replace('\\', "/");
            
            media.push(GameFiles {
                url: format!("{}/MediaResources/{}", catalog_url, media_path),
                path: media_path.clone(),
                hash: HashValue::Crc(media_entry.crc),
                size: media_entry.bytes,
            });
        }

        self.combine_catalogs(
            "catalog/japan/GameFiles.json",
            asset,
            table,
            media,
        )
        .await?;

        Ok(())
    }


    async fn global_data(&self, resources: &Resources<'_>) -> Result<()> {
        if !resources.asset_bundles.is_empty() {
            let asset_data = AssetBundle {
                asset_bundles: resources.asset_bundles.iter().map(|&r| r.clone()).collect(),
            };
            save_json(
                &self.file_manager,
                "catalog/global/bundleDownloadInfo.json",
                &asset_data,
            ).await?;
        }

        if !resources.media_resources.is_empty() {
            let media_data = MediaResources {
                media_resources: resources.media_resources.iter().map(|&r| r.clone()).collect(),
            };
            save_json(
                &self.file_manager,
                "catalog/global/MediaCatalog.json",
                &media_data,
            ).await?;
        }

        if !resources.table_bundles.is_empty() {
            let table_data = TableResources {
                table_bundles: resources.table_bundles.iter().map(|&r| r.clone()).collect(),
            };
            save_json(
                &self.file_manager,
                "catalog/global/TableCatalog.json",
                &table_data,
            ).await?;
        }

        Ok(())
    }


    async fn global_gamefiles(&self, catalog_url: &String, resources: &Resources<'_>) -> Result<()> {
        let asset_bundles: Result<Vec<GameFiles>, _> = resources
            .asset_bundles
            .iter()
            .map(|&resource| self.process_global_gamefiles(resource, catalog_url))
            .collect();

        let table_bundles: Result<Vec<GameFiles>, _> = resources
            .table_bundles
            .iter()
            .map(|&resource| self.process_global_gamefiles(resource, catalog_url))
            .collect();

        let media_resources: Result<Vec<GameFiles>, _> = resources
            .media_resources
            .iter()
            .map(|&resource| self.process_global_gamefiles(resource, catalog_url))
            .collect();

        self.combine_catalogs(
            "catalog/global/GameFiles.json",
            asset_bundles?,
            table_bundles?,
            media_resources?,
        )
        .await?;

        Ok(())
    }

    fn process_global_resources(resources: &[Resource]) -> Result<Resources> {
        let mut asset = Vec::new();
        let mut media = Vec::new();
        let mut table = Vec::new();

        for resource in resources {
            if resource.resource_path.contains("/Android/") {
                asset.push(resource);
            } else if resource.resource_path.contains("/MediaResources/") {
                media.push(resource);
            } else if resource.resource_path.contains("/TableBundles/") {
                table.push(resource);
            }
        }

        Ok(Resources {
            asset_bundles: asset,
            media_resources: media,
            table_bundles: table,
        })
    }

    fn process_global_gamefiles(
        &self,
        resource: &Resource,
        catalog_url: &str,
    ) -> Result<GameFiles> {
        Ok(GameFiles {
            url: format!("{}/{}", catalog_url, resource.resource_path),
            path: resource.resource_path.clone(),
            hash: HashValue::Md5(resource.resource_hash.clone()),
            size: resource.resource_size,
        })
    }

    async fn combine_catalogs(
        &self,
        output: &str,
        asset: Vec<GameFiles>,
        table: Vec<GameFiles>,
        media: Vec<GameFiles>,
    ) -> Result<()> {
        let combined_data = serde_json::json!({
            "AssetBundles": asset,
            "TableBundles": table,
            "MediaResources": media
        });

        save_json(&self.file_manager, output, &combined_data).await?;

        Ok(())
    }

    pub async fn process_catalogs(&self) -> Result<()> {
        let api_data: ApiData = load_json(&self.file_manager, "api_data.json").await?;

        match self.config.region {
            ServerRegion::Japan => {
                let catalog_url = &api_data.japan.catalog_url;

                self.japan_data(catalog_url).await?;
                self.japan_gamefiles(catalog_url).await?;
            }
            ServerRegion::Global => {
                let resources: GlobalCatalog =
                    load_json(&self.file_manager, "catalog/global/Resources.json").await?;
                let catalog_url = &api_data.global.catalog_url;

                let processed_resources = Self::process_global_resources(&resources.resources)?;
                self.global_data(&processed_resources).await?;
                self.global_gamefiles(&catalog_url, &processed_resources).await?;
            }
        }

        Ok(())
    }
}