use anyhow::{Context, Result};
use serde::{de::DeserializeOwned, Serialize};

use crate::helpers::api::{ApiData, GlobalData, JapanData};
use crate::helpers::config::API_FILENAME;
use crate::utils::file::FileManager;

pub async fn load_json<T: DeserializeOwned>(file_manager: &FileManager, filename: &str) -> Result<T> {
    let bytes = file_manager.load_file(filename)?;
    let json_data = String::from_utf8(bytes).context("Failed to convert file content to UTF-8")?;
    serde_json::from_str(&json_data).with_context(|| format!("Failed to parse JSON from file: {}", filename))
}

pub async fn save_json<T: Serialize>(file_manager: &FileManager, filename: &str, data: &T) -> Result<()> {
    let json_data = serde_json::to_string_pretty(data).context("Failed to serialize data to JSON")?;
    let file_path = file_manager.get_data_path(filename);
    FileManager::create_parent_dir(&file_path)?;
    file_manager.save_file(filename, json_data.as_bytes())
}

pub async fn get_api_data(file_manager: &FileManager) -> Result<ApiData> {
    if file_manager.get_data_path(API_FILENAME).exists() {
        load_json(file_manager, API_FILENAME).await
    } else {
        Ok(create_default_api_data())
    }
}

pub async fn save_api_data(file_manager: &FileManager, api_data: &ApiData) -> Result<()> {
    save_json(file_manager, API_FILENAME, api_data).await
}

pub async fn update_api_data<F>(file_manager: &FileManager, updater: F) -> Result<()>
where
    F: FnOnce(&mut ApiData),
{
    let mut api_data = get_api_data(file_manager).await?;
    updater(&mut api_data);
    save_api_data(file_manager, &api_data).await
}

pub fn create_default_api_data() -> ApiData {
    ApiData {
        japan: JapanData {
            version: String::new(),
            catalog_url: String::new(),
            addressable_url: String::new(),
        },
        global: GlobalData {
            version: String::new(),
            catalog_url: String::new(),
        },
    }
}

pub async fn update_server_data(
    file_manager: &FileManager,
    server: &str,
    catalog_url: Option<&str>,
    addressable_url: Option<&str>,
    version: Option<&str>,
) -> Result<()> {
    let mut api_data: ApiData = get_api_data(file_manager).await?;

    match server {
        "japan" => {
            if let Some(url) = catalog_url {
                api_data.japan.catalog_url = url.to_string();
            }
            if let Some(url) = addressable_url {
                api_data.japan.addressable_url = url.to_string();
            }
            if let Some(ver) = version {
                api_data.japan.version = ver.to_string();
            }
        }
        "global" => {
            if let Some(url) = catalog_url {
                api_data.global.catalog_url = url.to_string();
            }
            if let Some(ver) = version {
                api_data.global.version = ver.to_string();
            }
        }
        _ => return Err(anyhow::anyhow!("Invalid server: {}", server)),
    }

    save_api_data(file_manager, &api_data).await
}