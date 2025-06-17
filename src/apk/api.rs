use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize, Debug)]
pub struct JapanData {
    pub version: String,
    pub catalog_url: String,
    pub addressable_url: String,
}

#[derive(Serialize, Deserialize, Debug)]
pub struct GlobalData {
    pub version: String,
    pub addressable_url: String,
}

#[derive(Serialize, Deserialize, Debug)]
pub struct ApiData {
    pub japan: JapanData,
    pub global: GlobalData,
}