use crate::helpers::api::{AssetBundle, GlobalCatalog, MediaResources, Resource, TableResources};
use crate::helpers::config::ServerConfig;
use crate::utils::file::FileManager;
use crate::utils::json::{load_json, save_json};

use anyhow::Result;

pub struct CatalogParser {
    file_manager: FileManager,
    config: ServerConfig
}

impl CatalogParser {
    pub fn new(file_manager: &FileManager, config: &ServerConfig) -> Result<Self> {
        Ok(Self {
            config: config.clone(),
            file_manager: file_manager.clone(),
        })
    }
    
    pub async fn global_catalogs(self) -> Result<()> {
        let resources: GlobalCatalog = load_json(
            &self.file_manager,
            "catalog/data/Resources.json",
        ).await?;
        
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
            let asset_data = AssetBundle {
                asset_bundles,
            };
            save_json(
                &self.file_manager,
                "catalog/data/bundleDownloadInfo.json",
                &asset_data,
            ).await?;
        }
        
        if !media_resources.is_empty() {
            let media_data = MediaResources {
                media_resources,
            };
            save_json(
                &self.file_manager,
                "catalog/data/MediaCatalog.json",
                &media_data,
            ).await?;
        }
        
        if !table_bundles.is_empty() {
            let table_data = TableResources {
                table_bundles,
            };
            save_json(
                &self.file_manager,
                "catalog/data/TableCatalog.json",
                &table_data,
            ).await?;
        }
        
        Ok(())
    }
}