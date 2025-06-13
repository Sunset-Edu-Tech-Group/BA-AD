use std::fs;
use std::fs::File;
use std::io::{self, Cursor, Read};
use std::path::PathBuf;

use anyhow::{Context, Result, anyhow};
use regex::Regex;
use reqwest::{Client, Response};
use serde::{Deserialize, Serialize};
use zip::ZipArchive;

use crate::helpers::config::{APK_DOWNLOAD_URL_REGEX, APK_VERSION_REGEX, RegionConfig, http_headers};
use crate::helpers::download_manager::DownloadManager;
use crate::helpers::file::FileManager;
use crate::helpers::interface::reset_download_progress;
use crate::helpers::json;
use crate::{info, warn};

#[derive(Debug, Clone)]
pub struct ExtractionRule {
    pub source_apk: String,
    pub internal_path: String,
    pub output_path: String,
    pub is_required: bool,
}

impl ExtractionRule {
    pub fn new(source_apk: &str, internal_path: &str, output_path: &str, is_required: bool) -> Self {
        Self {
            source_apk: source_apk.to_string(),
            internal_path: internal_path.to_string(),
            output_path: output_path.to_string(),
            is_required,
        }
    }
}

#[derive(Debug, Clone)]
pub struct ExtractionConfig {
    pub rules: Vec<ExtractionRule>,
    pub preserve_original: bool,
}

impl Default for ExtractionConfig {
    fn default() -> Self {
        Self {
            rules: vec![],
            preserve_original: true,
        }
    }
}

impl ExtractionConfig {
    pub fn new() -> Self {
        Self::default()
    }

    pub fn add_rule(&mut self, rule: ExtractionRule) {
        self.rules.push(rule);
    }

    pub fn with_rule(mut self, rule: ExtractionRule) -> Self {
        self.add_rule(rule);
        self
    }
}

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
    extraction_config: Option<ExtractionConfig>,
}

impl<'a> ApkParser<'a> {
    pub fn new(file_manager: &'a FileManager, config: &RegionConfig) -> Result<Self> {
        let client: Client = Client::builder().default_headers(http_headers()).build()?;
        let download_manager = DownloadManager::new(client.clone(), 0, 1);

        Ok(Self {
            client,
            file_manager,
            config: config.clone(),
            download_manager,
            extraction_config: None,
        })
    }

    pub fn set_extraction_config(&mut self, config: ExtractionConfig) {
        self.extraction_config = Some(config);
    }

    async fn extract_from_zip<R: Read + io::Seek>(
        &self,
        archive: &mut ZipArchive<R>,
        rule: &ExtractionRule,
        base_output_path: &PathBuf,
    ) -> Result<()> {
        let file = match archive.by_name(&rule.internal_path) {
            Ok(file) => file,
            Err(_) => {
                if rule.is_required {
                    return Err(anyhow!("Required file {} not found", rule.internal_path));
                }
                return Ok(());
            }
        };

        let outpath = base_output_path.join(&rule.output_path);
        if let Some(p) = outpath.parent() {
            if !p.exists() {
                fs::create_dir_all(p).with_context(|| "Failed to create directory")?;
            }
        }

        let mut outfile = File::create(&outpath)
            .with_context(|| format!("Failed to create file: {}", outpath.display()))?;
        io::copy(&mut archive.by_name(&rule.internal_path)?, &mut outfile)
            .with_context(|| "Failed to copy file")?;

        Ok(())
    }

    async fn process_nested_apk(
        &self,
        nested_apk_name: &str,
        base_output_path: &PathBuf,
    ) -> Result<()> {
        let apk_path = self.file_manager.data_path(&self.config.apk_path);
        let mut archive = ZipArchive::new(File::open(&apk_path)
            .with_context(|| format!("{} not found", apk_path.display())))?;

        let mut nested_apk = match archive.by_name(nested_apk_name) {
            Ok(file) => file,
            Err(_) => return Err(anyhow!("{} not found", nested_apk_name)),
        };

        let mut buf = Vec::new();
        nested_apk.read_to_end(&mut buf)
            .with_context(|| format!("Failed to read {}", nested_apk_name))?;
        
        let mut cursor = Cursor::new(buf);
        let mut inner_archive = ZipArchive::new(&mut cursor)
            .with_context(|| format!("Failed to open {}", nested_apk_name))?;

        if let Some(config) = &self.extraction_config {
            for rule in &config.rules {
                if rule.source_apk == nested_apk_name {
                    self.extract_from_zip(&mut inner_archive, rule, base_output_path).await?;
                }
            }

            if config.preserve_original {
                self.extract_original_files(&mut inner_archive, base_output_path).await?;
            }
        }

        Ok(())
    }

    async fn extract_original_files<R: Read + io::Seek>(
        &self,
        archive: &mut ZipArchive<R>,
        output_path: &PathBuf,
    ) -> Result<()> {
        for i in 0..archive.len() {
            let mut file = archive.by_index(i)?;
            if !file.name().starts_with(&self.config.asset_filter) {
                continue;
            }

            let relative_path = file
                .name()
                .strip_prefix(&self.config.asset_filter)
                .ok_or_else(|| anyhow!("Failed to strip prefix from {}", file.name()))?;

            let outpath = output_path.join(relative_path);

            if let Some(p) = outpath.parent() {
                if !p.exists() {
                    fs::create_dir_all(p).with_context(|| "Failed to create directory")?;
                }
            }

            let mut outfile = File::create(&outpath)
                .with_context(|| format!("Failed to create file: {}", outpath.display()))?;
            io::copy(&mut file, &mut outfile).with_context(|| "Failed to copy file")?;
        }

        Ok(())
    }

    pub async fn extract_apk(&self) -> Result<()> {
        if self.config.apk_path.is_empty() {
            warn!("The {} region doesn't support APK extraction", self.config.id);
            return Ok(());
        }

        info!("Extracting app");

        let data_path = self.file_manager.data_path("data");
        let output_path = self.file_manager.create_dir(&data_path).await?;

        let apk_path = self.file_manager.data_path(&self.config.apk_path);
        let mut main_archive = ZipArchive::new(File::open(&apk_path)
            .with_context(|| format!("{} not found", apk_path.display())))?;

        if let Some(config) = &self.extraction_config {
            for rule in &config.rules {
                if rule.source_apk.is_empty() || rule.source_apk == "main" {
                    self.extract_from_zip(&mut main_archive, rule, &output_path).await?;
                }
            }
        }

        self.process_nested_apk("UnityDataAssetPack.apk", &output_path).await?;
        self.process_nested_apk("config.arm64_v8a.apk", &output_path).await?;

        info!("Finished extracting app");
        Ok(())
    }

    async fn check_version(&self) -> Result<Option<String>> {
        let versions_response: Response = self.client.get(&self.config.version_url).send().await?;
        if !versions_response.status().is_success() {
            return Err(anyhow!("Failed to get versions: {}", versions_response.status()));
        }

        let body: String = versions_response.text().await?;
        let new_version: String = self.extract_version(&body)?;

        json::update_japan_version(self.file_manager, &new_version).await?;

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
        if !self.file_manager.data_path(&apk_path.to_string_lossy()).exists() {
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
            warn!("APK is outdated or incomplete",);
            return Ok(true);
        }

        Ok(false)
    }

    pub async fn download_apk(&self, force_update: bool) -> Result<()> {
        if self.config.apk_path.is_empty() || self.config.version_url.is_empty() {
            warn!("The {} region doesn't support APK download", self.config.id);
            return Ok(());
        }

        info!("Checking for updates");

        let apk_path: PathBuf = self.file_manager.data_path(&self.config.apk_path);
        let apk_dir: PathBuf = apk_path.parent().unwrap().to_path_buf();
        self.file_manager.create_dir(&apk_dir).await?;

        let new_version: String = match self.check_version().await? {
            Some(version) => version,
            None => return Ok(()),
        };

        if force_update && self.file_manager.data_path(&apk_path.to_string_lossy()).exists() {
            info!("Removing existing APK");
            self.file_manager.clean_path_dir(&apk_path).await?;
        }

        if force_update {
            info!("Force updating to version: {}", new_version);
        } else {
            info!("Latest version: {}", new_version);
        }

        let versions_response: Response = self.client.get(&self.config.version_url).send().await?;
        let body: String = versions_response.text().await?;
        let download_url: String = self.extract_download_url(&body)?;
        let need_download: bool = force_update || self.check_apk(&download_url, &apk_path).await?;

        if need_download {
            info!("Downloading APK...");
            self.download_manager.download_large_file(&download_url, &apk_path).await?;

            reset_download_progress();
            info!("Finished downloading apk");
        } else {
            info!("Skipping download - APK is up to date");
        }
        Ok(())
    }
}
