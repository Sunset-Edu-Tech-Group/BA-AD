use crate::apk::fetch::ApkFetcher;
use crate::helpers::api::{GlobalApi, GlobalCatalog, JapanCatalog};
use crate::helpers::config::{GAME_CONFIG_PATTERN, GLOBAL_API_URL, ServerConfig};
use crate::utils::file::FileManager;
use crate::utils::json::{load_json, save_json};

use anyhow::{Result, anyhow};
use base64::{Engine, engine::general_purpose};
use bacy::table_encryption_service::{create_key, convert_string, new_encrypt_string};
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
            let entry = entry?;
            if !entry.file_type().is_file() {
                continue;
            }

            let buffer = fs::read(entry.path())?;

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

        Err(anyhow!("Game config not found"))
    }

    pub fn decrypt_game_config(&self, data: &[u8]) -> Result<String> {
        let encoded_data = general_purpose::STANDARD.encode(data);
        
        let game_config = create_key(b"GameMainConfig");
        let server_data = create_key(b"ServerInfoDataUrl");
        
        let decrypted_data = convert_string(&encoded_data, &game_config)?;
        let loaded_data: Value = serde_json::from_str(&decrypted_data)?;
        
        let decrypted_key = new_encrypt_string("ServerInfoDataUrl", &server_data)?;
        let decrypted_value = loaded_data
            .get(&decrypted_key)
            .and_then(|v| v.as_str())
            .ok_or_else(|| anyhow!("Key '{}' not found in JSON", decrypted_key))?;
        
        convert_string(decrypted_value, &server_data)
    }
    
    pub async fn japan_addressable(&self) -> Result<String> {
        let api_url = self.decrypt_game_config(self.find_game_config()?.as_slice())?;
        
        let japan_catalog = self
            .client
            .get(&api_url)
            .send()
            .await?
            .json::<JapanCatalog>()
            .await?;
        
        save_json(
            &self.file_manager,
            "catalog/JapanAddressables.json",
            &japan_catalog,
        )
        .await?;
        
        Ok(to_string_pretty(&japan_catalog)?)
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
        )
        .await?;

        Ok(to_string_pretty(&api_response)?)
    }

    pub async fn global_resources(&self) -> Result<String> {
        self.global_addressable().await?;

        let api_response: GlobalApi =
            load_json(&self.file_manager, "catalog/GlobalAddressables.json").await?;

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
        )
        .await?;

        Ok(to_string_pretty(&catalog_response)?)
    }
}