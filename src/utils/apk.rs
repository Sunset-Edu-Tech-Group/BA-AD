use crate::helpers::config::{APK_DOWNLOAD_URL_REGEX, APK_VERSION_REGEX, RegionConfig, http_headers};
use crate::helpers::file::FileManager;
use crate::helpers::json;
use crate::helpers::progress::DownloadProgress;

use anyhow::{Context, Result, anyhow};
use regex::Regex;
use reqwest::{Client, Response};
use serde::{Deserialize, Serialize};
use std::fs;
use std::fs::File;
use std::io::{self, Cursor, Read, Seek, Write};
use std::path::PathBuf;
use std::sync::Arc;
use tokio::sync::Mutex;
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
}

impl<'a> ApkParser<'a> {
    pub fn new(file_manager: &'a FileManager, region: &str) -> Result<Self> {
        let client: Client = Client::builder().default_headers(http_headers()).build()?;
        Ok(Self {
            client,
            file_manager,
            config: RegionConfig::new(region),
        })
    }

    async fn check_version(&self, force_update: bool) -> Result<Option<String>> {
        let api_data = json::get_api_data(self.file_manager)?;

        let versions_response: Response = self.client.get(&self.config.version_url).send().await?;
        if !versions_response.status().is_success() {
            return Err(anyhow!("Failed to get versions: {}", versions_response.status()));
        }

        let body: String = versions_response.text().await?;
        let new_version: String = self.extract_version(&body)?;

        if new_version == api_data.japan.version && !force_update {
            println!("App is up to date");
            return Ok(None);
        }

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

    async fn prepare_download(&self, url: &str) -> Result<(u64, Response)> {
        let response: Response = self.client.get(url).send().await?;
        let total_size: u64 = response.content_length().unwrap_or(0);
        Ok((total_size, response))
    }

    async fn download_chunk(
        client: Client,
        url: String,
        start: u64,
        end: u64,
        progress: Arc<DownloadProgress>,
        file: Arc<Mutex<File>>,
    ) -> Result<()> {
        let mut response: Response = client
            .get(&url)
            .header("Range", format!("bytes={}-{}", start, end - 1))
            .send()
            .await?;

        let mut buffer = Vec::new();
        while let Some(chunk) = response.chunk().await? {
            buffer.extend_from_slice(&chunk);
            progress.inc(chunk.len() as u64);
        }

        let mut file = file.lock().await;
        file.seek(std::io::SeekFrom::Start(start))?;
        file.write_all(&buffer)?;

        Ok(())
    }

    async fn download_file(&self, url: &str, total_size: u64, output_path: &PathBuf) -> Result<()> {
        let progress: Arc<DownloadProgress> = Arc::new(DownloadProgress::new(total_size));
        let file: File = File::create(output_path)?;
        let file: Arc<Mutex<File>> = Arc::new(Mutex::new(file));

        const CHUNK_SIZE: u64 = 1024 * 1024;
        let num_chunks: u64 = (total_size + CHUNK_SIZE - 1) / CHUNK_SIZE;
        let mut tasks: Vec<tokio::task::JoinHandle<std::result::Result<(), anyhow::Error>>> = Vec::new();

        for i in 0..num_chunks {
            let start: u64 = i * CHUNK_SIZE;
            let end: u64 = std::cmp::min(start + CHUNK_SIZE, total_size);

            let client: Client = self.client.clone();
            let url: String = url.to_string();
            let progress: Arc<DownloadProgress> = Arc::clone(&progress);
            let file: Arc<Mutex<File>> = Arc::clone(&file);

            let task: tokio::task::JoinHandle<std::result::Result<(), anyhow::Error>> =
                tokio::spawn(async move { Self::download_chunk(client, url, start, end, progress, file).await });

            tasks.push(task);
        }

        for task in tasks {
            task.await??;
        }

        progress.finish_with_message("Download complete!");
        Ok(())
    }

    pub async fn download_apk(&self, force_update: bool) -> Result<()> {
        if self.config.apk_path.is_empty() || self.config.version_url.is_empty() {
            println!("The {} region doesn't support APK download", self.config.id);
            return Ok(());
        }

        println!("Checking for updates");

        let apk_path: PathBuf = self.file_manager.data_path(&self.config.apk_path);
        self.file_manager.create_dir(apk_path.parent().unwrap().to_str().unwrap())?;

        let new_version: String = match self.check_version(force_update).await? {
            Some(version) => version,
            None => return Ok(()),
        };

        if self.file_manager.file_exists(&apk_path.to_string_lossy()) {
            println!("Removing existing APK...");
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

        println!("Downloading app");
        let (total_size, _): (u64, Response) = self.prepare_download(&download_url).await?;
        self.download_file(&download_url, total_size, &apk_path).await?;

        println!("Finished downloading app");
        Ok(())
    }

    pub fn extract_apk(&self) -> Result<()> {
        // Skip if this region doesn't have APK or asset filter
        if self.config.apk_path.is_empty() || self.config.asset_filter.is_empty() {
            println!("The {} region doesn't support APK extraction", self.config.id);
            return Ok(());
        }

        println!("Extracting app");

        let apk_path: PathBuf = self.file_manager.data_path(&self.config.apk_path);
        let mut archive: ZipArchive<File> =
            ZipArchive::new(File::open(&apk_path).with_context(|| format!("{} not found", apk_path.display()))?)
                .with_context(|| "Failed to open archive")?;

        let mut data_apk: zip::read::ZipFile<'_> = match archive.by_name("UnityDataAssetPack.apk") {
            Ok(file) => file,
            Err(_) => {
                return Err(anyhow!("UnityDataAssetPack.apk not found"));
            }
        };

        let mut buf: Vec<u8> = Vec::new();
        data_apk
            .read_to_end(&mut buf)
            .with_context(|| "Failed to read UnityDataAssetPack")?;
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

            let mut outfile: File =
                File::create(&outpath).with_context(|| format!("Failed to create file: {}", outpath.display()))?;
            io::copy(&mut file, &mut outfile).with_context(|| "Failed to copy file")?;
        }

        println!("Finished extracting app");
        Ok(())
    }
}
