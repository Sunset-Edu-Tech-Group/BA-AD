use crate::helpers::{ApiData, GlobalData, JapanData, API_FILENAME};
use crate::utils::file;

use anyhow::Result;
use baad_core::errors::{ErrorContext, ErrorExt};
use serde::{de::DeserializeOwned, Serialize};
use std::path::Path;

pub async fn load_json<T: DeserializeOwned>(path: &Path) -> Result<T> {
    let bytes = file::load_file(path).await?;

    let json_data = String::from_utf8(bytes).error_context("Failed to convert file content to UTF-8")?;
    serde_json::from_str(&json_data).handle_errors()
}


pub async fn save_json<T: Serialize>(path: &Path, data: &T) -> Result<()> {
    let json_data = serde_json::to_string_pretty(data).handle_errors()?;

    file::create_parent_dir(&path).await?;
    file::save_file(path, json_data.as_bytes()).await?;

    Ok(())
}

pub async fn get_api_data() -> Result<ApiData> {
    let api_path = file::get_data_path(API_FILENAME)?;

    match api_path.exists() {
        true => load_json(&api_path).await,
        false => Ok(create_default_api_data()),
    }
}

pub async fn save_api_data(api_data: &ApiData) -> Result<()> {
    let api_path = file::get_data_path(API_FILENAME)?;

    save_json(&api_path, api_data).await
}

pub async fn update_api_data<F>(updater: F) -> Result<()>
where
    F: FnOnce(&mut ApiData),
{
    let mut api_data = get_api_data().await?;
    updater(&mut api_data);
    save_api_data(&api_data).await
}

pub fn create_default_api_data() -> ApiData {
    ApiData {
        japan: JapanData {
            version: String::new(),
            catalog_url: String::new(),
            addressable_url: String::new(),
            platform: "Android".to_string(),
        },
        global: GlobalData {
            version: String::new(),
            catalog_url: String::new(),
            platform: "Android".to_string(),
            build_type: "Standard".to_string(),
        },
    }
}