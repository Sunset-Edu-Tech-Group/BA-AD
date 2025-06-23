use anyhow::{Error, Result};
use platform_dirs::AppDirs;
use std::path::PathBuf;
use std::{env, fs};

#[allow(dead_code)]
const APP_NAME: &str = env!("CARGO_CRATE_NAME");

#[derive(Clone)]
pub struct FileManagerConfig {
    pub data_dir: Option<PathBuf>,
    pub cache_dir: Option<PathBuf>,
    pub app_name: Option<String>,
}

#[derive(Clone)]
pub struct FileManager {
    cache_dir: PathBuf,
    data_dir: PathBuf,
}

impl FileManager {
    pub fn new() -> Result<Self> {
        Self::with_config(FileManagerConfig {
            data_dir: None,
            cache_dir: None,
            app_name: Some(APP_NAME.to_string()),
        })
    }

    pub fn with_config(config: FileManagerConfig) -> Result<Self> {
        let app_dirs = if let Some(app_name) = config.app_name {
            AppDirs::new(Some(&app_name), true).unwrap()
        } else {
            AppDirs::new(None, true).unwrap()
        };

        let data_dir = config.data_dir.unwrap_or(app_dirs.data_dir);
        let cache_dir = config.cache_dir.unwrap_or(app_dirs.cache_dir);

        fs::create_dir_all(&data_dir)?;
        fs::create_dir_all(&cache_dir)?;
        
        Ok(Self {
            cache_dir,
            data_dir,
        })
    }
    
    pub fn save_file(&self, filename: &str, content: &[u8]) -> Result<()> {
        let file_path = self.data_dir.join(filename);
        fs::write(file_path, content)?;
        Ok(())
    }
    
    pub fn load_file(&self, filename: &str) -> Result<Vec<u8>> {
        let file_path = self.data_dir.join(filename);
        let content = fs::read(file_path)?;
        Ok(content)
    }

    pub fn create_parent_dir(path: impl AsRef<std::path::Path>) -> Result<()> {
        if let Some(parent) = path.as_ref().parent() {
            fs::create_dir_all(parent)?;
        }
        Ok(())
    }

    pub fn get_output_dir(path: Option<PathBuf>) -> Result<PathBuf, Error> {
        let output_dir = match path {
            Some(path) => path,
            None => env::current_dir()?.join("output"),
        };

        fs::create_dir_all(&output_dir)?;

        Ok(output_dir)
    }
    
    pub fn get_data_dir(&self) -> &PathBuf {
        &self.data_dir
    }
    
    pub fn get_cache_dir(&self) -> &PathBuf {
        &self.cache_dir
    }

    pub fn get_data_path(&self, filename: &str) -> PathBuf {
        self.data_dir.join(filename)
    }

    pub fn get_cache_path(&self, filename: &str) -> PathBuf {
        self.data_dir.join(filename)
    }
}