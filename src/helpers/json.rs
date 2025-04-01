use anyhow::{Context, Result};
use serde::{Serialize, de::DeserializeOwned};

use crate::helpers::config::API_DATA_FILENAME;
use crate::helpers::file::FileManager;
use crate::utils::apk::{ApiData, GlobalRegionData, RegionData};

pub fn load_json<T: DeserializeOwned>(file_manager: &FileManager, filename: &str) -> Result<T> {
    let json_data: String = file_manager.load_text(filename)?;
    serde_json::from_str(&json_data).with_context(|| format!("Failed to parse JSON from file: {}", filename))
}

pub fn save_json<T: Serialize>(file_manager: &FileManager, filename: &str, data: &T) -> Result<()> {
    let json_data: String = serde_json::to_string_pretty(data).context("Failed to serialize data to JSON")?;
    file_manager.save_text(filename, &json_data)
}

pub fn get_api_data(file_manager: &FileManager) -> Result<ApiData> {
    if file_manager.data_path(API_DATA_FILENAME).exists() {
        load_json(file_manager, API_DATA_FILENAME)
    } else {
        Ok(create_default_api_data())
    }
}

pub fn save_api_data(file_manager: &FileManager, api_data: &ApiData) -> Result<()> {
    save_json(file_manager, API_DATA_FILENAME, api_data)
}

pub fn create_default_api_data() -> ApiData {
    ApiData {
        japan: RegionData {
            version: String::new(),
            catalog_url: String::new(),
            addressable_url: String::new(),
        },
        global: GlobalRegionData {
            version: String::new(),
            addressable_url: String::new(),
        },
    }
}

pub fn update_japan_catalog_url(file_manager: &FileManager, catalog_url: &str) -> Result<()> {
    let mut api_data = get_api_data(file_manager)?;
    api_data.japan.catalog_url = catalog_url.to_string();
    save_api_data(file_manager, &api_data)
}

pub fn update_japan_addressable_url(file_manager: &FileManager, addressable_url: &str) -> Result<()> {
    let mut api_data = get_api_data(file_manager)?;
    api_data.japan.addressable_url = addressable_url.to_string();
    save_api_data(file_manager, &api_data)
}

pub fn update_japan_version(file_manager: &FileManager, version: &str) -> Result<()> {
    let mut api_data = get_api_data(file_manager)?;
    api_data.japan.version = version.to_string();
    save_api_data(file_manager, &api_data)
}

pub fn update_global_addressable_url(file_manager: &FileManager, addressable_url: &str) -> Result<()> {
    let mut api_data = get_api_data(file_manager)?;
    api_data.global.addressable_url = addressable_url.to_string();
    save_api_data(file_manager, &api_data)
}

pub fn update_global_version(file_manager: &FileManager, version: &str) -> Result<()> {
    let mut api_data = get_api_data(file_manager)?;
    api_data.global.version = version.to_string();
    save_api_data(file_manager, &api_data)
}

pub fn update_region_data(
    file_manager: &FileManager,
    region: &str,
    catalog_url: Option<&str>,
    addressable_url: Option<&str>,
    version: Option<&str>,
) -> Result<()> {
    let mut api_data: ApiData = get_api_data(file_manager)?;

    match region {
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
            if let Some(url) = addressable_url {
                api_data.global.addressable_url = url.to_string();
            }
            if let Some(ver) = version {
                api_data.global.version = ver.to_string();
            }
        }
        _ => return Err(anyhow::anyhow!("Invalid region: {}", region)),
    }

    save_api_data(file_manager, &api_data)
}
