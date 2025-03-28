use anyhow::{Context, Result};
use platform_dirs::AppDirs;
use serde::{de::DeserializeOwned, Serialize};
use std::fs;
use std::path::{Path, PathBuf};

const APP_NAME: &str = "baad";
const APP_QUALIFIED: bool = true;

pub struct FileManager {
    app_dirs: AppDirs,
}

impl FileManager {
    pub fn new() -> Result<Self> {
        let app_dirs: AppDirs = AppDirs::new(Some(APP_NAME), APP_QUALIFIED)
            .context("Failed to initialize application directories")?;

        fs::create_dir_all(&app_dirs.data_dir).context("Failed to create data directory")?;

        Ok(Self { app_dirs })
    }

    pub fn data_dir(&self) -> &Path {
        &self.app_dirs.data_dir
    }

    pub fn data_path(&self, filename: &str) -> PathBuf {
        self.app_dirs.data_dir.join(filename)
    }

    pub fn save_file(&self, filename: &str, content: &[u8]) -> Result<()> {
        let path: PathBuf = self.data_path(filename);

        if let Some(parent) = path.parent() {
            if !parent.exists() {
                fs::create_dir_all(parent)
                    .context(format!("Failed to create directory: {}", parent.display()))?;
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

    pub fn save_json<T: Serialize>(&self, filename: &str, data: &T) -> Result<()> {
        let json_string = serde_json::to_string_pretty(data)
            .context("Failed to serialize data to JSON")?;
        self.save_text(filename, &json_string)
    }

    pub fn load_json<T: DeserializeOwned>(&self, filename: &str) -> Result<T> {
        let json_string = self.load_text(filename)?;
        serde_json::from_str(&json_string)
            .with_context(|| format!("Failed to parse JSON from file: {}", filename))
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
        fs::create_dir_all(&path)
            .context(format!("Failed to create directory: {}", path.display()))?;
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
}
