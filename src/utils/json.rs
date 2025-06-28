use crate::helpers::{ApiData, GlobalData, JapanData, API_FILENAME};
use crate::utils::FileManager;

use anyhow::Result;
use baad_core::errors::{ErrorContext, ErrorExt};
use serde::{de::DeserializeOwned, Serialize};

pub async fn load_json<T: DeserializeOwned>(file_manager: &FileManager, filename: &str) -> Result<T> {
    let bytes = file_manager.load_file(filename).handle_errors()?;
    let json_data = String::from_utf8(bytes)
        .error_context("Failed to convert file content to UTF-8")?;
    serde_json::from_str(&json_data).handle_errors()
}


pub async fn save_json<T: Serialize>(file_manager: &FileManager, filename: &str, data: &T) -> Result<()> {
    let json_data = serde_json::to_string_pretty(data).handle_errors()?;
    let file_path = file_manager.get_data_path(filename);
    FileManager::create_parent_dir(&file_path).handle_errors()?;
    file_manager.save_file(filename, json_data.as_bytes()).handle_errors()
}


pub async fn get_api_data(file_manager: &FileManager) -> Result<ApiData> {
    match file_manager.get_data_path(API_FILENAME).exists() {
        true => load_json(file_manager, API_FILENAME).await,
        false => Ok(create_default_api_data()),
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