use std::fs;
use std::path::{Path, PathBuf};
use std::time::{Duration, SystemTime, UNIX_EPOCH};

use anyhow::{Context, Result};
use platform_dirs::{AppDirs, UserDirs};

use crate::helpers::logs::{info, warn};

const APP_NAME: &str = "baad";
const APP_QUALIFIED: bool = true;

pub struct FileManager {
    app_dirs: AppDirs,
    user_dirs: UserDirs,
}

impl FileManager {
    pub fn new() -> Result<Self> {
        let app_dirs: AppDirs = AppDirs::new(Some(APP_NAME), APP_QUALIFIED).context("Failed to initialize application directories")?;
        let user_dirs: UserDirs = UserDirs::new().unwrap();

        fs::create_dir_all(&app_dirs.data_dir).context("Failed to create data directory")?;
        fs::create_dir_all(&app_dirs.cache_dir).context("Failed to create cache directory")?;
        fs::create_dir_all(&user_dirs.download_dir).context("Failed to create download directory")?;

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

    pub fn temp_dir(&self) -> Result<PathBuf> {
        let temp_dir: PathBuf = self.cache_path("temp");

        if !temp_dir.exists() {
            fs::create_dir_all(&temp_dir).context("Failed to create temp directory")?;
        }

        Ok(temp_dir)
    }

    pub fn temp_path(&self, filename: &str) -> PathBuf {
        self.temp_dir().unwrap().join(filename)
    }

    pub fn save_file(&self, filename: &str, content: &[u8]) -> Result<()> {
        let path: PathBuf = self.data_path(filename);

        path.parent()
            .filter(|parent| !parent.exists())
            .map(|parent| fs::create_dir_all(parent).context(format!("Failed to create directory: {}", parent.display())))
            .transpose()?;

        fs::write(&path, content).context(format!("Failed to save file: {}", path.display()))?;
        Ok(())
    }

    pub fn load_file(&self, filename: &str) -> Result<Vec<u8>> {
        let path: PathBuf = self.data_path(filename);
        fs::read(&path).context(format!("Failed to load file: {}", path.display()))
    }

    pub fn save_text(&self, filename: &str, text: &str) -> Result<()> {
        self.save_file(filename, text.as_bytes())
    }

    pub fn load_text(&self, filename: &str) -> Result<String> {
        let data: Vec<u8> = self.load_file(filename)?;
        String::from_utf8(data).context(format!("Failed to convert file content to UTF-8 string: {}", filename))
    }

    pub fn create_dir(&self, path: &PathBuf) -> Result<PathBuf> {
        fs::create_dir_all(&path).with_context(|| format!("Failed to create directory: {}", path.display()))?;
        Ok(path.clone())
    }

    pub fn create_temp_file(&self, prefix: &str, extension: &str) -> Result<PathBuf> {
        let temp_dir: PathBuf = self.temp_dir()?;
        let timestamp: u128 = SystemTime::now().duration_since(UNIX_EPOCH).unwrap_or_default().as_nanos();
        let filename: String = format!("{}_{}.{}", prefix, timestamp, extension);
        let path: PathBuf = temp_dir.join(filename);

        Ok(path)
    }

    pub fn cleanup_temp_files(&self) -> Result<()> {
        let temp_dir: PathBuf = self.temp_dir()?;
        if !temp_dir.exists() {
            return Ok(());
        }

        let cutoff: SystemTime = SystemTime::now() - Duration::from_secs(24 * 60 * 60);

        let entries: fs::ReadDir = match fs::read_dir(&temp_dir) {
            Ok(entries) => entries,
            Err(e) => {
                warn(&format!("Failed to read temp directory: {}", e));
                return Ok(());
            }
        };

        for entry_result in entries {
            let entry: fs::DirEntry = match entry_result {
                Ok(entry) => entry,
                Err(_) => continue,
            };

            if !entry.file_type().map(|ft| ft.is_file()).unwrap_or(false) {
                continue;
            }

            let should_delete: bool = entry
                .metadata()
                .ok()
                .and_then(|m| m.modified().ok())
                .map(|modified| modified < cutoff)
                .unwrap_or(false);

            should_delete.then(|| {
                if let Err(e) = fs::remove_file(&entry.path()) {
                    warn(&format!("Failed to delete temp file: {}", e));
                }
            });
        }

        Ok(())
    }

    pub fn clean_directory(&self, path: &PathBuf) -> Result<PathBuf> {
        match path.exists() {
            true => {
                info(&format!("Removing directory: {}", path.display()));
                fs::remove_dir_all(&path).with_context(|| format!("Failed to remove directory: {}", path.display()))?;
            }
            false => {}
        }

        self.create_dir(path)
    }

    pub fn clean_region_directories(&self, region: &str) -> Result<()> {
        self.clean_directory(&self.data_path("data"))?;

        let region_catalog_path = format!("catalogs/{}", region);
        self.clean_directory(&self.data_path(&region_catalog_path))?;

        Ok(())
    }

    pub fn get_filename(&self, path: &Path) -> String {
        path.file_name().and_then(|name| name.to_str()).unwrap_or("unknown file").to_string()
    }

    pub fn format_size(&self, size: u64) -> String {
        const KB: u64 = 1024;
        const MB: u64 = KB * 1024;
        const GB: u64 = MB * 1024;

        if size >= GB {
            format!("{:.2} GB", size as f64 / GB as f64)
        } else if size >= MB {
            format!("{:.2} MB", size as f64 / MB as f64)
        } else if size >= KB {
            format!("{:.2} KB", size as f64 / KB as f64)
        } else {
            format!("{} B", size)
        }
    }
}
