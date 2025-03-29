use crate::helpers::config::{APK_DOWNLOAD_URL_REGEX, APK_VERSION_REGEX, RegionConfig, http_headers};
use crate::helpers::download_manager::{DownloadManager, DownloadStrategy};
use crate::helpers::file::FileManager;
use crate::helpers::json;

use anyhow::{Context, Result, anyhow};
use regex::Regex;
use reqwest::{Client, Response};
use serde::{Deserialize, Serialize};
use std::fs;
use std::fs::File;
use std::io::{self, Cursor, Read};
use std::path::PathBuf;
use zip::ZipArchive;

#[derive(Serialize, Deserialize, Debug)]
pub struct RegionData {
    pub version: String,
    #[serde(rename = "catalog_url")]
    pub catalog_url: String,
    #[serde(rename = "addressable_url")]
    pub addressable_url: String,
}

#[derive(Serialize, Deserialize, Debug)]
pub struct GlobalRegionData {
    pub version: String,
    #[serde(rename = "addressable_url")]
    pub addressable_url: String,
}

#[derive(Serialize, Deserialize, Debug)]
pub struct ApiData {
    pub japan: RegionData,
    pub global: GlobalRegionData,
}

pub struct ApkParser<'a> {
    client: Client,
    file_manager: &'a FileManager,
    config: RegionConfig,
    download_manager: DownloadManager,
}

impl<'a> ApkParser<'a> {
    pub fn new(file_manager: &'a FileManager, config: &RegionConfig) -> Result<Self> {
        let client: Client = Client::builder().default_headers(http_headers()).build()?;
        let download_manager: DownloadManager = DownloadManager::with_config(client.clone(), 2 * 1024 * 1024, 10);

        Ok(Self {
            client,
            file_manager,
            config: config.clone(),
            download_manager,
        })
    }

    async fn check_version(&self) -> Result<Option<String>> {
        let versions_response: Response = self.client.get(&self.config.version_url).send().await?;
        if !versions_response.status().is_success() {
            return Err(anyhow!("Failed to get versions: {}", versions_response.status()));
        }

        let body: String = versions_response.text().await?;
        let new_version: String = self.extract_version(&body)?;

        json::update_japan_version(self.file_manager, &new_version)?;

        Ok(Some(new_version))
    }

    fn extract_version(&self, body: &str) -> Result<String> {
        let re_version: Regex = Regex::new(APK_VERSION_REGEX).unwrap();
        re_version
            .find(body)
            .map(|m| m.as_str().to_string())
            .ok_or_else(|| anyhow!("Failed to find version in response"))
    }

    fn extract_download_url(&self, body: &str) -> Result<String> {
        let re_url: Regex = Regex::new(APK_DOWNLOAD_URL_REGEX).unwrap();
        match re_url.captures(body) {
            Some(caps) if caps.len() >= 3 => Ok(caps.get(2).unwrap().as_str().to_string()),
            _ => Err(anyhow!("Failed to get download url")),
        }
    }

    async fn check_apk(&self, download_url: &str, apk_path: &PathBuf) -> Result<bool> {
        if !self.file_manager.file_exists(&apk_path.to_string_lossy()) {
            return Ok(true);
        }

        let local_size: u64 = match fs::metadata(apk_path) {
            Ok(metadata) => metadata.len(),
            Err(_) => return Ok(true),
        };

        let response: Response = self.client.get(download_url).header("Range", "bytes=0-0").send().await?;

        if !response.status().is_success() && response.status() != reqwest::StatusCode::PARTIAL_CONTENT {
            return Err(anyhow!("Failed to get file info: {}", response.status()));
        }

        let remote_size: u64 = if let Some(content_range) = response.headers().get("Content-Range") {
            content_range
                .to_str()
                .ok()
                .and_then(|range| range.split('/').last())
                .and_then(|size| size.parse::<u64>().ok())
                .unwrap_or(0)
        } else {
            response.content_length().unwrap_or(0).saturating_add(1)
        };

        if remote_size == 0 || local_size != remote_size {
            println!("APK is outdated");
            return Ok(true);
        }

        Ok(false)
    }

    pub async fn download_apk(&self, force_update: bool) -> Result<()> {
        if self.config.apk_path.is_empty() || self.config.version_url.is_empty() {
            println!("The {} region doesn't support APK download", self.config.id);
            return Ok(());
        }

        println!("Checking for updates");

        let apk_path: PathBuf = self.file_manager.data_path(&self.config.apk_path);
        self.file_manager.create_dir(apk_path.parent().unwrap().to_str().unwrap())?;

        let new_version: String = match self.check_version().await? {
            Some(version) => version,
            None => return Ok(()),
        };

        if force_update && self.file_manager.file_exists(&apk_path.to_string_lossy()) {
            println!("Removing existing APK");
            self.file_manager.delete_file(&apk_path.to_string_lossy())?;
        }

        if force_update {
            println!("Force updating to version: {}", new_version);
        } else {
            println!("Latest version: {}", new_version);
        }

        let versions_response: Response = self.client.get(&self.config.version_url).send().await?;
        let body: String = versions_response.text().await?;
        let download_url: String = self.extract_download_url(&body)?;

        let need_download: bool = force_update || self.check_apk(&download_url, &apk_path).await?;

        if need_download {
            println!("Downloading apk");

            self.download_manager
                .download_file_with_strategy(&download_url, &apk_path, DownloadStrategy::MultiThread { thread_count: 0 })
                .await?;

            println!("Finished downloading apk");
        } else {
            println!("Skipping download - APK is up to date");
        }
        Ok(())
    }

    pub fn extract_apk(&self) -> Result<()> {
        if self.config.apk_path.is_empty() || self.config.asset_filter.is_empty() {
            println!("The {} region doesn't support APK extraction", self.config.id);
            return Ok(());
        }

        println!("Extracting app");

        let apk_path: PathBuf = self.file_manager.data_path(&self.config.apk_path);
        let mut archive: ZipArchive<File> = ZipArchive::new(File::open(&apk_path).with_context(|| format!("{} not found", apk_path.display()))?)
            .with_context(|| "Failed to open archive")?;

        let mut data_apk: zip::read::ZipFile<'_> = match archive.by_name("UnityDataAssetPack.apk") {
            Ok(file) => file,
            Err(_) => {
                return Err(anyhow!("UnityDataAssetPack.apk not found"));
            }
        };

        let mut buf: Vec<u8> = Vec::new();
        data_apk.read_to_end(&mut buf).with_context(|| "Failed to read UnityDataAssetPack")?;
        let mut cursor: Cursor<Vec<u8>> = Cursor::new(buf);

        let mut inner_archive: ZipArchive<&mut Cursor<Vec<u8>>> =
            ZipArchive::new(&mut cursor).with_context(|| "Failed to open UnityDataAssetPack")?;

        let output_path: PathBuf = self.file_manager.create_dir("data")?;

        for i in 0..inner_archive.len() {
            let mut file: zip::read::ZipFile<'_> = inner_archive.by_index(i)?;
            if !file.name().starts_with(&self.config.asset_filter) {
                continue;
            }

            let relative_path = file
                .name()
                .strip_prefix(&self.config.asset_filter)
                .ok_or_else(|| anyhow!("Failed to strip prefix from {}", file.name()))?;

            let outpath: PathBuf = output_path.join(relative_path);

            if let Some(p) = outpath.parent() {
                if !p.exists() {
                    fs::create_dir_all(p).with_context(|| "Failed to create directory")?;
                }
            }

            let mut outfile: File = File::create(&outpath).with_context(|| format!("Failed to create file: {}", outpath.display()))?;
            io::copy(&mut file, &mut outfile).with_context(|| "Failed to copy file")?;
        }

        println!("Finished extracting app");
        Ok(())
    }
}
