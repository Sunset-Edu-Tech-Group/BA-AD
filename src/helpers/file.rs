#![allow(dead_code)]

use std::path::{Path, PathBuf};
use std::time::{Duration, SystemTime, UNIX_EPOCH};

use anyhow::{Context, Result};
use platform_dirs::{AppDirs, UserDirs};
use tokio::fs;

use crate::{info, warn};

const APP_NAME: &str = "baad";
const APP_QUALIFIED: bool = true;

pub struct FileManager {
    app_dirs: AppDirs,
    user_dirs: UserDirs,
}

impl FileManager {
    pub async fn new() -> Result<Self> {
        let app_dirs: AppDirs = AppDirs::new(Some(APP_NAME), APP_QUALIFIED).context("Failed to initialize application directories")?;
        let user_dirs: UserDirs = UserDirs::new().unwrap();

        fs::create_dir_all(&app_dirs.data_dir).await.context("Failed to create data directory")?;
        fs::create_dir_all(&app_dirs.cache_dir)
            .await
            .context("Failed to create cache directory")?;
        fs::create_dir_all(&user_dirs.download_dir)
            .await
            .context("Failed to create download directory")?;

        Ok(Self { app_dirs, user_dirs })
    }

    pub fn data_dir(&self) -> &PathBuf {
        &self.app_dirs.data_dir
    }

    pub fn data_path(&self, filename: &str) -> PathBuf {
        self.app_dirs.data_dir.join(filename)
    }

    pub fn cache_dir(&self) -> &PathBuf {
        &self.app_dirs.cache_dir
    }

    pub fn cache_path(&self, filename: &str) -> PathBuf {
        self.app_dirs.cache_dir.join(filename)
    }

    pub fn download_dir(&self) -> &PathBuf {
        &self.user_dirs.download_dir
    }

    pub fn download_path(&self, filename: &str) -> PathBuf {
        self.user_dirs.download_dir.join(filename)
    }

    pub async fn temp_dir(&self) -> Result<PathBuf> {
        let temp_dir: PathBuf = self.cache_path("temp");

        if !temp_dir.exists() {
            fs::create_dir_all(&temp_dir).await.context("Failed to create temp directory")?;
        }

        Ok(temp_dir)
    }

    pub async fn temp_path(&self, filename: &str) -> PathBuf {
        self.temp_dir().await.unwrap().join(filename)
    }

    pub async fn save_file(&self, filename: &str, content: &[u8]) -> Result<()> {
        let path: PathBuf = self.data_path(filename);

        if let Some(parent) = path.parent() {
            if !parent.exists() {
                fs::create_dir_all(parent)
                    .await
                    .context(format!("Failed to create directory: {}", parent.display()))?;
            }
        }

        fs::write(&path, content)
            .await
            .context(format!("Failed to save file: {}", path.display()))?;
        Ok(())
    }

    pub async fn load_file(&self, filename: &str) -> Result<Vec<u8>> {
        let path: PathBuf = self.data_path(filename);
        fs::read(&path).await.context(format!("Failed to load file: {}", path.display()))
    }

    pub async fn save_text(&self, filename: &str, text: &str) -> Result<()> {
        self.save_file(filename, text.as_bytes()).await
    }

    pub async fn load_text(&self, filename: &str) -> Result<String> {
        let data: Vec<u8> = self.load_file(filename).await?;
        String::from_utf8(data).context(format!("Failed to convert file content to UTF-8 string: {}", filename))
    }

    pub async fn create_dir(&self, path: &PathBuf) -> Result<PathBuf> {
        fs::create_dir_all(&path)
            .await
            .with_context(|| format!("Failed to create directory: {}", path.display()))?;
        Ok(path.clone())
    }

    pub async fn create_temp_file(&self, prefix: &str, extension: &str) -> Result<PathBuf> {
        let temp_dir: PathBuf = self.temp_dir().await?;
        let timestamp: u128 = SystemTime::now().duration_since(UNIX_EPOCH).unwrap_or_default().as_nanos();
        let filename: String = format!("{}_{}.{}", prefix, timestamp, extension);
        let path: PathBuf = temp_dir.join(filename);

        Ok(path)
    }

    pub async fn cleanup_temp_files(&self) -> Result<()> {
        let temp_dir: PathBuf = self.temp_dir().await?;
        if !temp_dir.exists() {
            return Ok(());
        }

        let cutoff: SystemTime = SystemTime::now() - Duration::from_secs(24 * 60 * 60);

        let mut entries = fs::read_dir(&temp_dir).await.map_err(|e| {
            warn!("Failed to read temp directory: {}", e);
            anyhow::anyhow!("Failed to read temp directory: {}", e)
        })?;

        while let Some(entry_result) = entries.next_entry().await.transpose() {
            let entry = match entry_result {
                Ok(entry) => entry,
                Err(_) => continue,
            };

            let file_type = match entry.file_type().await {
                Ok(ft) => ft,
                Err(_) => continue,
            };

            if !file_type.is_file() {
                continue;
            }

            let metadata = match entry.metadata().await {
                Ok(m) => m,
                Err(_) => continue,
            };

            let modified = match metadata.modified() {
                Ok(time) => time,
                Err(_) => continue,
            };

            if modified < cutoff {
                if let Err(e) = fs::remove_file(&entry.path()).await {
                    warn!("Failed to delete temp file: {}", e);
                }
            }
        }

        Ok(())
    }

    pub async fn clean_dir(&self, path: &PathBuf) -> Result<PathBuf> {
        match path.exists() {
            true => {
                info!("Removing directory: {}", path.display());
                fs::remove_dir_all(&path)
                    .await
                    .with_context(|| format!("Failed to remove directory: {}", path.display()))?;
            }
            false => {}
        }

        self.create_dir(path).await
    }

    pub async fn clean_path_dir(&self, path: &PathBuf) -> Result<PathBuf> {
        if let Some(parent) = path.parent() {
            self.clean_dir(&parent.to_path_buf()).await
        } else {
            Err(anyhow::anyhow!("Failed to get parent directory for path: {}", path.display()))
        }
    }

    pub async fn clean_region_directories(&self, region: &str) -> Result<()> {
        self.clean_dir(&self.data_path("data")).await?;

        let region_catalog_path = format!("catalogs/{}", region);
        self.clean_dir(&self.data_path(&region_catalog_path)).await?;

        Ok(())
    }
}

pub fn get_filename(path: &Path) -> String {
    path.file_name().and_then(|name| name.to_str()).unwrap_or("unknown file").to_string()
}

pub async fn canonical_path(path: &PathBuf) -> Result<PathBuf> {
    match fs::canonicalize(path).await {
        Ok(canonical) => Ok(canonical),
        Err(e) => {
            warn!("Failed to canonicalize path {}: {}", path.display(), e);

            let absolute_path = if path.is_absolute() {
                path.clone()
            } else {
                let current_dir = std::env::current_dir()?;
                current_dir.join(path)
            };

            fs::create_dir_all(&absolute_path).await?;

            Ok(absolute_path)
        }
    }
}
