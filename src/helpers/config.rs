#![allow(dead_code)]

use anyhow::{Error, Result};
use reqwest::header::{HeaderMap, HeaderValue};

pub const JAPAN_REGEX_URL: &str = r"(X?APKJ)..(https?://(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*))";
pub const JAPAN_REGEX_VERSION: &str = r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)";

pub const GLOBAL_URL: &str = "https://play.google.com/store/apps/details?id=com.nexon.bluearchive";
pub const GLOBAL_REGEX_VERSION: &str = r"\d{1}\.\d{2}\.\d{6}";
pub const GLOBAL_API_URL: &str = "https://api-pub.nexon.com/patch/v1.1/version-check";

pub const API_FILENAME: &str = "api_data.json";
pub const GAME_CONFIG_PATTERN: &[u8] = &[
    0x47, 0x61, 0x6D, 0x65,
    0x4D, 0x61, 0x69, 0x6E,
    0x43, 0x6F, 0x6E, 0x66,
    0x69, 0x67, 0x00, 0x00,
    0x92, 0x03, 0x00, 0x00,
];

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum ServerRegion {
    Global,
    Japan,
}

#[derive(Clone)]
pub struct ServerConfig {
    pub region: ServerRegion,
    pub version_url: String,
    pub apk_path: String
}

impl ServerConfig {
    pub fn new(server: ServerRegion) -> Result<Self, Error> {
        match server {
            ServerRegion::Global => Ok(Self {
                region: server,
                version_url: String::new(),
                apk_path: String::new(),
            }),
            ServerRegion::Japan => Ok(Self {
                region: server,
                version_url: "https://api.pureapk.com/m/v3/cms/app_version?hl=en-US&package_name=com.YostarJP.BlueArchive".to_string(),
                apk_path: "apk/BlueArchive.xapk".to_string(),
            }),
        }
    }
}

pub fn apk_headers() -> HeaderMap {
    let mut headers: HeaderMap = HeaderMap::new();
    headers.insert("x-cv", HeaderValue::from_static("3172501"));
    headers.insert("x-sv", HeaderValue::from_static("29"));
    headers.insert(
        "x-abis",
        HeaderValue::from_static("arm64-v8a,armeabi-v7a,armeabi"),
    );
    headers.insert("x-gp", HeaderValue::from_static("1"));
    headers
}