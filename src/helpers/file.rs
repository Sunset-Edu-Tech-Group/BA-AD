use anyhow::{Context, Result};
use platform_dirs::AppDirs;
use std::fs;
use std::path::{Path, PathBuf};

const APP_NAME: &str = "baad";
const APP_QUALIFIED: bool = true;

pub struct FileManager {
    app_dirs: AppDirs,
}

impl FileManager {
    pub fn new() -> Result<Self> {
        let app_dirs: AppDirs =
            AppDirs::new(Some(APP_NAME), APP_QUALIFIED).context("Failed to initialize application directories")?;

        fs::create_dir_all(&app_dirs.data_dir).context("Failed to create data directory")?;
        fs::create_dir_all(&app_dirs.cache_dir).context("Failed to create cache directory")?;

        Ok(Self { app_dirs })
    }

    pub fn data_dir(&self) -> &Path {
        &self.app_dirs.data_dir
    }

    pub fn data_path(&self, filename: &str) -> PathBuf {
        self.app_dirs.data_dir.join(filename)
    }

    pub fn cache_dir(&self) -> &Path {
        &self.app_dirs.cache_dir
    }

    pub fn cache_path(&self, filename: &str) -> PathBuf {
        self.app_dirs.cache_dir.join(filename)
    }

    pub fn save_file(&self, filename: &str, content: &[u8]) -> Result<()> {
        let path: PathBuf = self.data_path(filename);

        if let Some(parent) = path.parent() {
            if !parent.exists() {
                fs::create_dir_all(parent).context(format!("Failed to create directory: {}", parent.display()))?;
            }
        }

        fs::write(&path, content).context(format!("Failed to write file: {}", path.display()))?;

        Ok(())
    }

    pub fn load_file(&self, filename: &str) -> Result<Vec<u8>> {
        let path: PathBuf = self.data_path(filename);
        fs::read(&path).context(format!("Failed to read file: {}", path.display()))
    }

    pub fn save_text(&self, filename: &str, text: &str) -> Result<()> {
        self.save_file(filename, text.as_bytes())
    }

    pub fn load_text(&self, filename: &str) -> Result<String> {
        let data: Vec<u8> = self.load_file(filename)?;
        String::from_utf8(data).context(format!(
            "Failed to convert file content to UTF-8 string: {}",
            self.data_path(filename).display()
        ))
    }

    pub fn file_exists(&self, filename: &str) -> bool {
        self.data_path(filename).exists()
    }

    pub fn delete_file(&self, filename: &str) -> Result<()> {
        let path: PathBuf = self.data_path(filename);

        if path.exists() {
            fs::remove_file(&path).context(format!("Failed to delete file: {}", path.display()))?;
        }

        Ok(())
    }

    pub fn create_dir(&self, dirname: &str) -> Result<PathBuf> {
        let path: PathBuf = self.data_path(dirname);
        fs::create_dir_all(&path).context(format!("Failed to create directory: {}", path.display()))?;
        Ok(path)
    }

    pub fn format_size(size: u64) -> String {
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

    pub fn get_temp_dir(&self) -> Result<PathBuf> {
        let temp_dir: PathBuf = self.cache_path("temp");
        if !temp_dir.exists() {
            std::fs::create_dir_all(&temp_dir).context(format!("Failed to create temp directory: {}", temp_dir.display()))?;
        }
        Ok(temp_dir)
    }

    pub fn create_temp_file(&self, prefix: &str, extension: &str) -> Result<PathBuf> {
        let temp_dir: PathBuf = self.get_temp_dir()?;

        let timestamp: u128 = std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .unwrap_or_default()
            .as_nanos();

        let filename: String = format!("{}_{}.{}", prefix, timestamp, extension);
        let path: PathBuf = temp_dir.join(filename);

        Ok(path)
    }

    pub fn cleanup_temp_files(&self) -> Result<()> {
        let temp_dir: PathBuf = self.cache_path("temp");

        if !temp_dir.exists() {
            return Ok(());
        }

        let cutoff: std::time::SystemTime = std::time::SystemTime::now() - std::time::Duration::from_secs(24 * 60 * 60);

        let entries: fs::ReadDir = match std::fs::read_dir(&temp_dir) {
            Ok(entries) => entries,
            Err(e) => {
                eprintln!("Warning: Could not read temp directory: {}", e);
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

            if should_delete {
                let path: PathBuf = entry.path();
                if let Err(e) = std::fs::remove_file(&path) {
                    eprintln!("Warning: Failed to delete temp file {}: {}", path.display(), e);
                }
            }
        }

        Ok(())
    }
}
