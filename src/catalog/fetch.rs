use crate::apk::ApkFetcher;
use crate::helpers::{
    ErrorContext, ErrorExt, GlobalAddressable,
    GlobalCatalog, JapanAddressable, ServerConfig, ServerRegion,
    GAME_CONFIG_PATTERN, GLOBAL_API_URL
};
use crate::utils::json::{load_json, save_json, update_api_data};
use crate::utils::FileManager;

use anyhow::Result;
use bacy::table_encryption_service::{convert_string, create_key, new_encrypt_string};
use base64::{engine::general_purpose, Engine};
use reqwest::Client;
use serde_json::{to_string_pretty, Value};
use std::fs;
use walkdir::WalkDir;

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

    pub fn find_game_config(&self) -> Result<Vec<u8>> {
        let data = self.file_manager.get_data_path("data");

        for entry in WalkDir::new(data) {
            let entry = entry.handle_errors()?;
            if !entry.file_type().is_file() {
                continue;
            }

            let buffer = fs::read(entry.path()).handle_errors()?;

            if let Some(pos) = buffer
                .windows(GAME_CONFIG_PATTERN.len())
                .position(|window| window == GAME_CONFIG_PATTERN)
            {
                let data_start = pos + GAME_CONFIG_PATTERN.len();
                let data = &buffer[data_start..];

                if data.len() >= 2 {
                    return Ok(data[..data.len() - 2].to_vec());
                }
            }
        }

        None.error_context("Game config not found")
    }

    pub fn decrypt_game_config(&self, data: &[u8]) -> Result<String> {
        let encoded_data = general_purpose::STANDARD.encode(data);

        let game_config = create_key(b"GameMainConfig");
        let server_data = create_key(b"ServerInfoDataUrl");

        let decrypted_data = convert_string(&encoded_data, &game_config).handle_errors()?;
        let loaded_data: Value = serde_json::from_str(&decrypted_data).handle_errors()?;

        let decrypted_key = new_encrypt_string("ServerInfoDataUrl", &server_data).handle_errors()?;
        let decrypted_value = loaded_data
            .get(&decrypted_key)
            .and_then(|v| v.as_str())
            .error_context(&format!("Key '{}' not found in JSON", decrypted_key))?;

        convert_string(decrypted_value, &server_data).handle_errors()
    }

    async fn japan_addressable(&self) -> Result<String> {
        let api_url = self.decrypt_game_config(self.find_game_config()?.as_slice())?;

        let catalog = self
            .client
            .get(&api_url)
            .send()
            .await
            .handle_errors()?
            .json::<JapanAddressable>()
            .await
            .handle_errors()?;

        save_json(
            &self.file_manager,
            "catalog/JapanAddressables.json",
            &catalog,
        )
        .await?;

        update_api_data(&self.file_manager, |data| {
            data.japan.addressable_url = api_url;
        })
        .await?;

        Ok(to_string_pretty(&catalog).handle_errors()?)
    }

    async fn japan_catalog(&self) -> Result<String> {
        self.japan_addressable().await?;

        let addressable: JapanAddressable =
            load_json(&self.file_manager, "catalog/JapanAddressables.json").await?;

        let catalog_url = addressable
            .connection_groups
            .first()
            .and_then(|group| group.override_connection_groups.get(1))
            .map(|override_group| &override_group.addressables_catalog_url_root)
            .error_context("Second override connection group not found")?;

        update_api_data(&self.file_manager, |data| {
            data.japan.catalog_url = catalog_url.to_string();
        })
        .await?;

        Ok(catalog_url.to_string())
    }

    async fn global_addressable(&self) -> Result<String> {
        let version = self.apk_fetcher.check_version().await?
            .error_context("Failed to get version")?;
        let build_number = version.split('.').last()
            .error_context("Invalid version format - missing build number")?;

        let api = self
            .client
            .post(GLOBAL_API_URL)
            .json(&serde_json::json!({
                "market_game_id": "com.nexon.bluearchive",
                "market_code": "playstore",
                "curr_build_version": version,
                "curr_build_number": build_number
            }))
            .send()
            .await
            .handle_errors()?
            .json::<GlobalAddressable>()
            .await
            .handle_errors()?;


        save_json(&self.file_manager, "catalog/GlobalAddressables.json", &api).await?;

        Ok(to_string_pretty(&api).handle_errors()?)
    }

    async fn global_resources(&self) -> Result<String> {
        self.global_addressable().await?;

        let addressable: GlobalAddressable =
            load_json(&self.file_manager, "catalog/GlobalAddressables.json").await?;

        let catalog = self
            .client
            .get(&addressable.patch.resource_path)
            .send()
            .await
            .handle_errors()?
            .json::<GlobalCatalog>()
            .await
            .handle_errors()?;


        save_json(&self.file_manager, "catalog/global/Resources.json", &catalog).await?;

        update_api_data(&self.file_manager, |data| {
            data.global.catalog_url = addressable.patch.resource_path;
        })
        .await?;

        Ok(to_string_pretty(&catalog).handle_errors()?)
    }
    
    pub async fn get_catalogs(&self) -> Result<String> {
        match &self.config.region {
            ServerRegion::Japan => {
                Ok(self.japan_catalog().await?)
            },
            ServerRegion::Global => {
                Ok(self.global_resources().await?)
            },
        }
    }
    
    pub async fn get_addressable(&self) -> Result<String> {
        match &self.config.region {
            ServerRegion::Japan => {
                Ok(self.japan_addressable().await?)
            },
            ServerRegion::Global => {
                Ok(self.global_addressable().await?)
            }
        }
    }
}
