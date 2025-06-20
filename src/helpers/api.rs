use std::collections::HashMap;
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
pub struct JapanData {
    pub version: String,
    pub catalog_url: String,
    pub addressable_url: String,
}

#[derive(Serialize, Deserialize)]
pub struct GlobalData {
    pub version: String,
    pub catalog_url: String,
}

#[derive(Serialize, Deserialize)]
pub struct ApiData {
    pub japan: JapanData,
    pub global: GlobalData,
}

#[derive(Deserialize, Serialize)]
pub struct GlobalApi {
    pub api_version: String,
    pub market_game_id: String,
    pub latest_build_version: String,
    pub latest_build_number: String,
    pub min_build_version: String,
    pub min_build_number: String,
    pub patch: GlobalPatch,
}

#[derive(Deserialize, Serialize)]
pub struct GlobalPatch {
    pub patch_version: i32,
    pub resource_path: String,
    pub bdiff_path: Vec<HashMap<String, String>>,
}

#[derive(Serialize, Deserialize)]
pub struct GlobalCatalog {
    pub id: i32,
    pub market_game_id: String,
    pub build_id: Vec<i32>,
    pub patch_version: i32,
    pub name: String,
    pub patch_state: String,
    pub security_checked: bool,
    pub multi_language: bool,
    pub multi_texture_encode: bool,
    pub multi_texture_quality: bool,
    pub description: String,
    pub register: String,
    pub register_date: String,
    pub updater: String,
    pub update_date: String,
    pub compress: bool,
    pub size: i64,
    pub count: i32,
    pub use_multi_resource: bool,
    pub category: Category,
    pub category_mapping: Vec<CategoryMapping>,
    pub resources: Vec<Resource>,
}

#[derive(Serialize, Deserialize)]
pub struct Category {
    pub lang: Option<String>,
    pub texture_encode_type: Option<String>,
    pub texture_quality_level: Option<String>,
    pub group: Vec<String>,
}

#[derive(Serialize, Deserialize)]
pub struct CategoryMapping {
    pub group: String,
    pub paths: Vec<String>,
}

#[derive(Serialize, Deserialize)]
pub struct Resource {
    pub group: String,
    pub resource_path: String,
    pub resource_size: i64,
    pub resource_hash: String,
}

#[derive(Serialize, Deserialize)]
pub struct AssetBundle {
    #[serde(rename = "AssetBundles")]
    pub asset_bundles: Vec<Resource>,
}

#[derive(Serialize, Deserialize)]
pub struct MediaResources {
    #[serde(rename = "MediaResources")]
    pub media_resources: Vec<Resource>,
}

#[derive(Serialize, Deserialize)]
pub struct TableResources {
    #[serde(rename = "TableBundles")]
    pub table_bundles: Vec<Resource>,
}