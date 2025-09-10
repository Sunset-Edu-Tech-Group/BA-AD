use crate::apk::ApkFetcher;
use crate::helpers::{
    GlobalAddressable, GlobalCatalog, JapanAddressable, ServerConfig, ServerRegion,
    GAME_CONFIG_PATTERN, GLOBAL_API_URL,
};
use crate::utils::json;

use baad_core::{debug, file, info, AnyhowToEyre};
use bacy::table_encryption_service::{convert_string, create_key, new_encrypt_string};
use base64::{engine::general_purpose, Engine};
use eyre::{eyre, ContextCompat, Result};
use reqwest::Client;
use serde_json::{to_string_pretty, Value};
use std::fs;
use std::path::Path;
use std::rc::Rc;
use walkdir::WalkDir;

struct Paths {
    addressable_path: Box<Path>,
    resources_path: Box<Path>,
}

pub struct CatalogFetcher {
    client: Client,
    apk_fetcher: Rc<ApkFetcher>,
    config: Rc<ServerConfig>,
    paths: Paths,
}

impl CatalogFetcher {
    pub fn new(config: Rc<ServerConfig>, apk_fetcher: ApkFetcher) -> Result<Self> {
        let addressable_path = match config.region {
            ServerRegion::Global => file::get_data_path("catalog/GlobalAddressables.json")?,
            ServerRegion::Japan => file::get_data_path("catalog/JapanAddressables.json")?,
        };
        let resources_path = file::get_data_path("catalog/global/Resources.json")?;

        let client = Client::new();

        Ok(Self {
            client,
            apk_fetcher: Rc::new(apk_fetcher),
            config,
            paths: Paths {
                addressable_path: addressable_path.into_boxed_path(),
                resources_path: resources_path.into_boxed_path(),
            },
        })
    }

    pub fn find_game_config(&self) -> Result<Vec<u8>> {
        info!("Searching for game config...");

        let data_path = file::get_data_path("data")?;
        for entry in WalkDir::new(&data_path) {
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

        Err(eyre!("Game config not found"))
    }

    pub fn decrypt_game_config(&self, data: &[u8]) -> Result<String> {
        info!("Decrypting game config...");

        let encoded_data = general_purpose::STANDARD.encode(data);
        debug!(encoded_data, "Encoded data");

        let game_config = create_key(b"GameMainConfig");
        debug!(?game_config, "Game config");

        let server_data = create_key(b"ServerInfoDataUrl");
        debug!(?server_data, "Server data");

        let decrypted_data = convert_string(&encoded_data, &game_config).to_eyre()?;
        debug!(decrypted_data, "Decrypted data");

        let loaded_data: Value = serde_json::from_str(&decrypted_data)?;
        debug!(?loaded_data, "Loaded data");

        let decrypted_key = new_encrypt_string("ServerInfoDataUrl", &server_data).to_eyre()?;
        debug!(decrypted_key, "Decrypted key");

        let decrypted_value = loaded_data
            .get(&decrypted_key)
            .and_then(|v| v.as_str())
            .wrap_err_with(|| format!("Key '{}' not found in JSON", decrypted_key))?;
        debug!(decrypted_value, "Decrypted value");

        let converted = convert_string(decrypted_value, &server_data).to_eyre()?;
        Ok(converted)
    }

    async fn japan_addressable(&self) -> Result<String> {
        let api_url = self.decrypt_game_config(self.find_game_config()?.as_slice())?;
        debug!(api_url, "API URL");

        let catalog = self
            .client
            .get(&api_url)
            .send()
            .await?
            .json::<JapanAddressable>()
            .await?;

        json::save_json(&self.paths.addressable_path, &catalog).await?;

        json::update_api_data(|data| {
            data.japan.addressable_url = api_url;
            data.japan.platform = format!("{:?}", self.config.platform);
        })
        .await?;

        info!(success = true, "Saved addressables info");

        Ok(to_string_pretty(&catalog)?)
    }

    async fn japan_catalog(&self) -> Result<String> {
        self.japan_addressable().await?;

        let addressable: JapanAddressable = json::load_json(&self.paths.addressable_path).await?;

        let catalog_url = addressable
            .connection_groups
            .first()
            .and_then(|group| group.override_connection_groups.get(1))
            .map(|override_group| &override_group.addressables_catalog_url_root)
            .wrap_err_with(|| "Second override connection group not found")?;

        json::update_api_data(|data| {
            data.japan.catalog_url = catalog_url.to_string();
            data.japan.platform = format!("{:?}", self.config.platform);
        })
        .await?;

        info!(success = true, "Saved catalog info");

        Ok(catalog_url.to_string())
    }

    async fn global_addressable(&self) -> Result<String> {
        let version = self
            .apk_fetcher
            .check_version()
            .await?
            .wrap_err_with(|| "Failed to get version")?;
        debug!(version, "Version");

        let build_number = version
            .split('.')
            .next_back()
            .wrap_err_with(|| "Invalid version format - missing build number")?;
        debug!(build_number, "Build number");

        let market_config = self
            .config
            .get_market_config()
            .wrap_err_with(|| "Market config should be available for Global server")?;

        let api = self
            .client
            .post(GLOBAL_API_URL)
            .json(&serde_json::json!({
                "market_game_id": market_config.market_game_id,
                "market_code": market_config.market_code,
                "curr_build_version": version,
                "curr_build_number": build_number
            }))
            .send()
            .await?
            .json::<GlobalAddressable>()
            .await?;

        json::save_json(&self.paths.addressable_path, &api).await?;

        info!(success = true, "Saved addressables info");

        Ok(to_string_pretty(&api)?)
    }

    async fn global_resources(&self) -> Result<String> {
        self.global_addressable().await?;

        let addressable: GlobalAddressable = json::load_json(&self.paths.addressable_path).await?;

        let catalog = self
            .client
            .get(&addressable.patch.resource_path)
            .send()
            .await?
            .json::<GlobalCatalog>()
            .await?;

        json::save_json(&self.paths.resources_path, &catalog).await?;

        json::update_api_data(|data| {
            data.global.catalog_url = addressable.patch.resource_path;
            data.global.platform = format!("{:?}", self.config.platform);
            data.global.build_type = format!("{:?}", self.config.build_type);
        })
        .await?;

        info!(success = true, "Saved catalogs info");

        Ok(to_string_pretty(&catalog)?)
    }

    pub async fn get_catalogs(&self) -> Result<String> {
        info!("Fetching catalogs...");

        match &self.config.region {
            ServerRegion::Japan => Ok(self.japan_catalog().await?),
            ServerRegion::Global => Ok(self.global_resources().await?),
        }
    }

    pub async fn get_addressable(&self) -> Result<String> {
        info!("Fetching addressables...");

        match &self.config.region {
            ServerRegion::Japan => Ok(self.japan_addressable().await?),
            ServerRegion::Global => Ok(self.global_addressable().await?),
        }
    }
}
