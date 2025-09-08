use crate::apk::ApkFetcher;
use crate::helpers::{
    GlobalAddressable, GlobalCatalog, JapanAddressable, ServerConfig, ServerRegion,
    GAME_CONFIG_PATTERN, GLOBAL_API_URL,
};
use crate::utils::{file, json};

use anyhow::Result;
use baad_core::{
    debug,
    errors::{ErrorContext, ErrorExt},
    info, success,
};
use bacy::table_encryption_service::{convert_string, create_key, new_encrypt_string};
use base64::{engine::general_purpose, Engine};
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
            ServerRegion::Global => file::get_data_path("catalog/GlboalAddressables.json")?,
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
        info!("Decrypting game config...");

        let encoded_data = general_purpose::STANDARD.encode(data);
        debug!("Encoded data: <b><u><blue>{}</>", encoded_data);

        let game_config = create_key(b"GameMainConfig");
        debug!("Game config: <b><u><blue>{:?}</>", game_config);

        let server_data = create_key(b"ServerInfoDataUrl");
        debug!("Server data: <b><u><blue>{:?}</>", server_data);

        let decrypted_data = convert_string(&encoded_data, &game_config).handle_errors()?;
        debug!("Decrypted data: <b><u><blue>{}</>", decrypted_data);

        let loaded_data: Value = serde_json::from_str(&decrypted_data).handle_errors()?;
        debug!("Loaded data: <b><u><blue>{:?}</>", loaded_data);

        let decrypted_key =
            new_encrypt_string("ServerInfoDataUrl", &server_data).handle_errors()?;
        debug!("Decrypted key: <b><u><blue>{}</>", decrypted_key);

        let decrypted_value = loaded_data
            .get(&decrypted_key)
            .and_then(|v| v.as_str())
            .error_context(&format!("Key '{}' not found in JSON", decrypted_key))?;
        debug!("Decrypted value: <b><u><blue>{}</>", decrypted_value);

        convert_string(decrypted_value, &server_data).handle_errors()
    }

    async fn japan_addressable(&self) -> Result<String> {
        let api_url = self.decrypt_game_config(self.find_game_config()?.as_slice())?;
        debug!("API URL: <b><u><bright-blue>{}</>", api_url);

        let catalog = self
            .client
            .get(&api_url)
            .send()
            .await
            .handle_errors()?
            .json::<JapanAddressable>()
            .await
            .handle_errors()?;

        json::save_json(&self.paths.addressable_path, &catalog).await?;

        json::update_api_data(|data| {
            data.japan.addressable_url = api_url;
        })
        .await?;

        success!("Saved addressables info");

        to_string_pretty(&catalog).handle_errors()
    }

    async fn japan_catalog(&self) -> Result<String> {
        self.japan_addressable().await?;

        let addressable: JapanAddressable = json::load_json(&self.paths.addressable_path).await?;

        let catalog_url = addressable
            .connection_groups
            .first()
            .and_then(|group| group.override_connection_groups.get(1))
            .map(|override_group| &override_group.addressables_catalog_url_root)
            .error_context("Second override connection group not found")?;

        json::update_api_data(|data| {
            data.japan.catalog_url = catalog_url.to_string();
        })
        .await?;

        success!("Saved catalog info");

        Ok(catalog_url.to_string())
    }

    async fn global_addressable(&self) -> Result<String> {
        let version = self
            .apk_fetcher
            .check_version()
            .await?
            .error_context("Failed to get version")?;
        debug!("Version: <b><u><yellow>{}</>", version);

        let build_number = version
            .split('.')
            .next_back()
            .error_context("Invalid version format - missing build number")?;
        debug!("Build number: <b><u><yellow>{}</>", build_number);

        let market_config = self
            .config
            .get_market_config()
            .error_context("Market config should be available for Global server")?;

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
            .await
            .handle_errors()?
            .json::<GlobalAddressable>()
            .await
            .handle_errors()?;

        json::save_json(&self.paths.addressable_path, &api).await?;

        success!("Saved addressables info");

        to_string_pretty(&api).handle_errors()
    }

    async fn global_resources(&self) -> Result<String> {
        self.global_addressable().await?;

        let addressable: GlobalAddressable = json::load_json(&self.paths.addressable_path).await?;

        let catalog = self
            .client
            .get(&addressable.patch.resource_path)
            .send()
            .await
            .handle_errors()?
            .json::<GlobalCatalog>()
            .await
            .handle_errors()?;

        json::save_json(&self.paths.resources_path, &catalog).await?;

        json::update_api_data(|data| {
            data.global.catalog_url = addressable.patch.resource_path;
        })
        .await?;

        success!("Saved catalogs info");

        to_string_pretty(&catalog).handle_errors()
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
