use crate::crypto::table_encryption::table_encryption_service;
use crate::helpers::config::{API_URL, GAME_CONFIG_PATTERN, PLAYSTORE_URL};
use crate::helpers::file::FileManager;
use crate::helpers::json;

use anyhow::{Context, Result};
use base64::{Engine, engine::general_purpose};
use regex::Regex;
use reqwest::Client;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::path::PathBuf;

#[derive(Serialize, Deserialize, Debug)]
#[serde(rename_all = "PascalCase")]
pub struct GameMainConfig {
    pub server_info_data_url: String,
    pub default_connection_group: String,
    pub skip_tutorial: String,
    pub language: String,
}

#[derive(Deserialize, Serialize, Debug)]
pub struct ApiResponse {
    pub api_version: String,
    pub market_game_id: String,
    pub latest_build_version: String,
    pub latest_build_number: String,
    pub min_build_version: String,
    pub min_build_number: String,
    pub patch: Patch,
}

#[derive(Deserialize, Serialize, Debug)]
pub struct Patch {
    pub patch_version: i32,
    pub resource_path: String,
    pub bdiff_path: Vec<HashMap<String, String>>,
}

impl GameMainConfig {
    pub fn from_bytes(bytes: &[u8]) -> Result<Self> {
        let key: [u8; 8] = table_encryption_service::create_key(b"GameMainConfig");
        let b64: String = general_purpose::STANDARD.encode(bytes);
        let encrypted: String = table_encryption_service::convert_string(&b64, &key)?;
        let encrypted_map: HashMap<String, serde_json::Value> = serde_json::from_str(&encrypted)?;

        let keys: [&str; 4] = ["ServerInfoDataUrl", "DefaultConnectionGroup", "SkipTutorial", "Language"];
        let keys_map: HashMap<String, &str> = keys
            .iter()
            .map(|key| {
                let k: [u8; 8] = table_encryption_service::create_key(key.as_bytes());
                let value: String = table_encryption_service::new_encrypt_string(*key, &k).expect("Failed to encrypt config key");
                (value, *key)
            })
            .collect();

        let mut config_map: HashMap<&str, String> = HashMap::with_capacity(keys.len());
        for (encrypted_key, decrypted_key) in &keys_map {
            let encrypted_value = encrypted_map
                .get(encrypted_key)
                .with_context(|| format!("Missing key: {}", encrypted_key))?;

            let encrypted_str = encrypted_value
                .as_str()
                .with_context(|| format!("Invalid value type for key: {}", encrypted_key))?;

            let key: [u8; 8] = table_encryption_service::create_key(decrypted_key.as_bytes());
            let decrypted_value: String = table_encryption_service::convert_string(encrypted_str, &key)?;

            config_map.insert(decrypted_key, decrypted_value);
        }

        let json_s: String = serde_json::to_string_pretty(&config_map)?;
        serde_json::from_str(&json_s).map_err(Into::into)
    }
}

pub struct CatalogFetcher<'a> {
    file_manager: &'a FileManager,
    client: Client,
}

impl<'a> CatalogFetcher<'a> {
    pub fn new(file_manager: &'a FileManager) -> Self {
        Self {
            file_manager,
            client: Client::new(),
        }
    }

    fn find_game_config(&self) -> Result<Option<Vec<u8>>> {
        let game_path: PathBuf = self.file_manager.data_path("data");

        for entry in walkdir::WalkDir::new(game_path)
            .into_iter()
            .filter_map(Result::ok)
            .filter(|e| e.file_type().is_file())
        {
            let content: Vec<u8> =
                std::fs::read(entry.path()).with_context(|| format!("Failed to read file: {}", entry.path().display()))?;

            if let Some(start_index) = content
                .windows(GAME_CONFIG_PATTERN.len())
                .position(|window| window == GAME_CONFIG_PATTERN)
            {
                let data: Vec<u8> = content[start_index + GAME_CONFIG_PATTERN.len()..]
                    .iter()
                    .take_while(|&&b| b != 0)
                    .copied()
                    .collect();

                return Ok(Some(data));
            }
        }
        Ok(None)
    }

    pub fn save_catalog_url(&self, catalog_url: &str, region: &str, version: Option<&str>) -> Result<()> {
        match region {
            "japan" => json::update_japan_catalog_url(self.file_manager, catalog_url),
            "global" => {
                if let Some(ver) = version {
                    json::update_region_data(self.file_manager, region, None, Some(catalog_url), Some(ver))
                } else {
                    json::update_global_addressable_url(self.file_manager, catalog_url)
                }
            }
            _ => Err(anyhow::anyhow!("Invalid region: {}", region)),
        }
    }

    pub fn save_addressable_url(&self, addressable_url: &str, region: &str) -> Result<()> {
        match region {
            "japan" => json::update_japan_addressable_url(self.file_manager, addressable_url),
            "global" => json::update_global_addressable_url(self.file_manager, addressable_url),
            _ => Err(anyhow::anyhow!("Invalid region: {}", region)),
        }
    }

    pub async fn get_catalog_url(&self, region: &str) -> Result<String> {
        match region {
            "japan" => self.get_jp_catalog_url(),
            "global" => self.get_global_catalog_url().await,
            _ => Err(anyhow::anyhow!("Invalid region: {}", region)),
        }
    }

    fn get_jp_catalog_url(&self) -> Result<String> {
        let config_data: Vec<u8> = self
            .find_game_config()?
            .ok_or_else(|| anyhow::anyhow!("Game config not found"))?;

        let config: GameMainConfig = GameMainConfig::from_bytes(&config_data)?;
        self.save_catalog_url(&config.server_info_data_url, "japan", None)?;
        Ok(config.server_info_data_url)
    }

    async fn get_global_catalog_url(&self) -> Result<String> {
        let version: String = self.get_global_version().await?;
        let build_number: &str = version
            .split('.')
            .last()
            .ok_or_else(|| anyhow::anyhow!("Invalid version format"))?;

        let api_response: ApiResponse = self
            .client
            .post(API_URL)
            .json(&serde_json::json!({
                "market_game_id": "com.nexon.bluearchive",
                "market_code": "playstore",
                "curr_build_version": version,
                "curr_build_number": build_number
            }))
            .send()
            .await?
            .json::<ApiResponse>()
            .await?;

        self.save_catalog_url(&api_response.patch.resource_path, "global", Some(&version))?;
        Ok(api_response.patch.resource_path)
    }

    async fn get_global_version(&self) -> Result<String> {
        let regex_version: Regex = Regex::new(r"\d{1}\.\d{2}\.\d{6}")?;
        let res: String = self.client.get(PLAYSTORE_URL).send().await?.text().await?;

        let version: String = regex_version
            .find(&res)
            .ok_or_else(|| anyhow::anyhow!("Failed to find version in Play Store response"))?
            .as_str()
            .to_string();

        Ok(version)
    }
}
