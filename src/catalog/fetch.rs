use crate::apk::fetch::ApkFetcher;
use crate::helpers::api::{GlobalApi, GlobalCatalog};
use crate::helpers::config::{GLOBAL_API_URL, ServerConfig};
use crate::utils::file::FileManager;
use crate::utils::json::{load_json, save_json};

use anyhow::Result;
use reqwest::Client;
use serde_json::to_string_pretty;

pub struct CatalogFetcher {
    client: Client,
    apk_fetcher: ApkFetcher,
    config: ServerConfig,
    file_manager: FileManager,
}

impl CatalogFetcher {
    pub fn new(file_manager: &FileManager, config: &ServerConfig) -> Result<Self> {
        let client = Client::new();
        let apk_fetcher = ApkFetcher::new(&file_manager, &config);

        Ok(Self {
            client,
            apk_fetcher: apk_fetcher?,
            config: config.clone(),
            file_manager: file_manager.clone(),
        })
    }

    pub async fn global_addressable(&self) -> Result<String> {
        let version = self.apk_fetcher.check_version().await?.unwrap();
        let build_number = version.split('.').last().unwrap();

        let api_response = self
            .client
            .post(GLOBAL_API_URL)
            .json(&serde_json::json!({
                "market_game_id": "com.nexon.bluearchive",
                "market_code": "playstore",
                "curr_build_version": version,
                "curr_build_number": build_number
            }))
            .send()
            .await?
            .json::<GlobalApi>()
            .await?;

        save_json(
            &self.file_manager,
            "catalog/GlobalAddressables.json",
            &api_response,
        ).await?;

        Ok(to_string_pretty(&api_response)?)
    }
    
    pub async fn global_resources(&self) -> Result<String> {
        self.global_addressable().await?;
        
        let api_response: GlobalApi = load_json(
            &self.file_manager, 
            "catalog/GlobalAddressables.json"
        ).await?;

        let catalog_response = self
            .client
            .get(&api_response.patch.resource_path)
            .send()
            .await?
            .json::<GlobalCatalog>()
            .await?;

        save_json(
            &self.file_manager,
            "catalog/data/Resources.json",
            &catalog_response,
        ).await?;

        Ok(to_string_pretty(&catalog_response)?)
    }
}