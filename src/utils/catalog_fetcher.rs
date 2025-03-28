use crate::crypto::table_encryption::table_encryption_service;
use crate::helpers::file::FileManager;
use crate::utils::apk::{ApiData, RegionData};

use anyhow::{Context, Result};
use base64::{Engine, engine::general_purpose};
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

const GAME_CONFIG_PATTERN: &[u8] = &[
    0x47, 0x61, 0x6D, 0x65, 0x4D, 0x61, 0x69, 0x6E, 0x43, 0x6F, 0x6E, 0x66, 0x69, 0x67, 0x00, 0x00,
    0x92, 0x03, 0x00, 0x00,
];

#[derive(Serialize, Deserialize, Debug)]
#[serde(rename_all = "PascalCase")]
pub struct GameMainConfig {
    pub server_info_data_url: String,
    pub default_connection_group: String,
    pub skip_tutorial: String,
    pub language: String,
}

impl GameMainConfig {
    pub fn from_bytes(bytes: &[u8]) -> Result<Self> {
        let key: [u8; 8] = table_encryption_service::create_key(b"GameMainConfig");
        let b64: String = general_purpose::STANDARD.encode(bytes);
        let encrypted: String = table_encryption_service::convert_string(&b64, &key)?;
        let encrypted_map: HashMap<String, serde_json::Value> = serde_json::from_str(&encrypted)?;

        let keys: [&str; 4] = [
            "ServerInfoDataUrl",
            "DefaultConnectionGroup",
            "SkipTutorial",
            "Language",
        ];
        let keys: HashMap<String, &str> = keys
            .iter()
            .map(|key| {
                let k: [u8; 8] = table_encryption_service::create_key(key.as_bytes());
                let value: String = table_encryption_service::new_encrypt_string(*key, &k).unwrap();
                (value, *key)
            })
            .collect();

        let map: HashMap<&str, String> = keys
            .iter()
            .map(|(encrypted_key, decrypted_key)| {
                let encrypted_value: &serde_json::Value = encrypted_map
                    .get(encrypted_key)
                    .ok_or_else(|| anyhow::anyhow!("Missing key: {}", encrypted_key))?;
                let key: [u8; 8] = table_encryption_service::create_key(decrypted_key.as_bytes());
                let decrypted_value: String = table_encryption_service::convert_string(
                    encrypted_value.as_str().ok_or_else(|| {
                        anyhow::anyhow!("Invalid value type for key: {}", encrypted_key)
                    })?,
                    &key,
                )?;
                Ok((*decrypted_key, decrypted_value))
            })
            .collect::<Result<HashMap<_, _>>>()?;

        let json_s: String = serde_json::to_string_pretty(&map)?;
        let config: GameMainConfig = serde_json::from_str(&json_s)?;
        Ok(config)
    }
}

pub struct CatalogFetcher<'a> {
    file_manager: &'a FileManager,
}

impl<'a> CatalogFetcher<'a> {
    pub fn new(file_manager: &'a FileManager) -> Self {
        Self { file_manager }
    }

    fn find_game_config(&self) -> Result<Option<Vec<u8>>> {
        let game_path: std::path::PathBuf = self.file_manager.data_path("data");

        for entry in walkdir::WalkDir::new(game_path)
            .into_iter()
            .filter_map(|e| e.ok())
            .filter(|e| e.file_type().is_file())
        {
            let content: Vec<u8> = std::fs::read(entry.path())
                .with_context(|| format!("Failed to read file: {}", entry.path().display()))?;

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

    pub fn get_catalog_url(&self) -> Result<String> {
        let config_data: Vec<u8> = self
            .find_game_config()?
            .ok_or_else(|| anyhow::anyhow!("Game config not found"))?;

        let config: GameMainConfig = GameMainConfig::from_bytes(&config_data)?;
        
        // Load existing API data or create new
        let mut api_data = if self.file_manager.file_exists("api_data.json") {
            self.file_manager.load_json::<ApiData>("api_data.json")?
        } else {
            ApiData {
                japan: RegionData {
                    version: String::new(),
                    catalog_url: String::new(),
                },
                global: RegionData {
                    version: String::new(),
                    catalog_url: String::new(),
                },
            }
        };

        // Update the catalog URL
        api_data.japan.catalog_url = config.server_info_data_url.clone();
        self.file_manager.save_json("api_data.json", &api_data)?;

        Ok(config.server_info_data_url)
    }
}
