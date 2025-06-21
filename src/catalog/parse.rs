use crate::helpers::api::{
    ApiData, AssetBundle, GlobalCatalog, MediaResources, Resource, TableResources,
};
use crate::helpers::config::ServerConfig;
use crate::utils::file::FileManager;
use crate::utils::json::{load_json, save_json};

use anyhow::Result;
use bacy::{Asset, MediaCatalog, TableCatalog};
use reqwest::Client;

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

    pub async fn japan_catalogs(self) -> Result<()> {
        let api_data: ApiData = load_json(&self.file_manager, "api_data.json").await?;
        let catalog_url = api_data.japan.catalog_url;

        self.japan_data(catalog_url).await?;
        Ok(())
    }

    async fn japan_data(&self, catalog_url: String) -> Result<()> {
        let asset_data = self
            .client
            .get(format!("{}/Android/bundleDownloadInfo.json", catalog_url))
            .send()
            .await?
            .json::<Asset>()
            .await?;

        save_json(
            &self.file_manager,
            "catalog/japan/MediaCatalog.json",
            &asset_data,
        )
        .await?;

        let media = self
            .client
            .get(format!(
                "{}/MediaResources/Catalog/MediaCatalog.bytes",
                catalog_url
            ))
            .send()
            .await?;
        let media_bytes = media.bytes().await?;
        let media_data = MediaCatalog::deserialize(&media_bytes, &catalog_url)?;

        save_json(
            &self.file_manager,
            "catalog/japan/MediaCatalog.json",
            &media_data,
        )
        .await?;

        let table = self
            .client
            .get(format!("{}/TableBundles/TableCatalog.bytes", catalog_url))
            .send()
            .await?;
        let table_bytes = table.bytes().await?;
        let table_data = TableCatalog::deserialize(&table_bytes, &catalog_url)?;

        save_json(
            &self.file_manager,
            "catalog/japan/TableCatalog.json",
            &table_data,
        )
        .await?;

        Ok(())
    }

    pub async fn global_catalogs(self) -> Result<()> {
        let resources: GlobalCatalog =
            load_json(&self.file_manager, "catalog/global/Resources.json").await?;

        self.global_data(resources.resources).await?;

        Ok(())
    }

    async fn global_data(&self, resources: Vec<Resource>) -> Result<()> {
        let mut asset_bundles = Vec::new();
        let mut media_resources = Vec::new();
        let mut table_bundles = Vec::new();

        for resource in resources {
            if resource.resource_path.contains("/Android/") {
                asset_bundles.push(resource);
            } else if resource.resource_path.contains("/MediaResources/") {
                media_resources.push(resource);
            } else if resource.resource_path.contains("/TableBundles/") {
                table_bundles.push(resource);
            }
        }

        if !asset_bundles.is_empty() {
            let asset_data = AssetBundle { asset_bundles };
            save_json(
                &self.file_manager,
                "catalog/global/bundleDownloadInfo.json",
                &asset_data,
            )
            .await?;
        }

        if !media_resources.is_empty() {
            let media_data = MediaResources { media_resources };
            save_json(
                &self.file_manager,
                "catalog/global/MediaCatalog.json",
                &media_data,
            )
            .await?;
        }

        if !table_bundles.is_empty() {
            let table_data = TableResources { table_bundles };
            save_json(
                &self.file_manager,
                "catalog/global/TableCatalog.json",
                &table_data,
            )
            .await?;
        }

        Ok(())
    }
}
