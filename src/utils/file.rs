use anyhow::{Error, Result};
use baad_core::errors::{ErrorContext, ErrorExt};
use platform_dirs::AppDirs;
use std::path::PathBuf;
use std::rc::Rc;
use std::{env, fs};

#[allow(dead_code)]
const APP_NAME: &str = env!("CARGO_CRATE_NAME");

#[derive(Clone, Default)]
pub struct FileManagerConfig {
    pub data_dir: Option<PathBuf>,
    pub cache_dir: Option<PathBuf>,
    pub app_name: Option<String>,
}

pub struct FileManager {
    cache_dir: PathBuf,
    data_dir: PathBuf,
}

impl FileManager {
    pub fn new() -> Result<Rc<Self>> {
        Ok(Rc::new(Self::with_config(FileManagerConfig {
            data_dir: None,
            cache_dir: None,
            app_name: Some(APP_NAME.to_string()),
        })?))
    }

    pub fn with_config(config: FileManagerConfig) -> Result<Self> {
        let app_dirs = if let Some(app_name) = config.app_name {
            AppDirs::new(Some(&app_name), true)
                .error_context("Failed to create app directories with name")?
        } else {
            AppDirs::new(None, true)
                .error_context("Failed to create app directories")?
        };

        let data_dir = config.data_dir.unwrap_or(app_dirs.data_dir);
        let cache_dir = config.cache_dir.unwrap_or(app_dirs.cache_dir);

        fs::create_dir_all(&data_dir).handle_errors()?;
        fs::create_dir_all(&cache_dir).handle_errors()?;

        Ok(Self {
            cache_dir,
            data_dir,
        })
    }

    pub fn save_file(&self, filename: &str, content: &[u8]) -> Result<()> {
        let file_path = self.data_dir.join(filename);
        fs::write(file_path, content).handle_errors()?;
        Ok(())
    }

    pub fn load_file(&self, filename: &str) -> Result<Vec<u8>> {
        let file_path = self.data_dir.join(filename);
        fs::read(file_path).handle_errors()
    }

    pub fn create_parent_dir(path: impl AsRef<std::path::Path>) -> Result<()> {
        if let Some(parent) = path.as_ref().parent() {
            fs::create_dir_all(parent).handle_errors()?;
        }
        Ok(())
    }

    pub fn get_output_dir(path: Option<PathBuf>) -> Result<PathBuf, Error> {
        let output_dir = match path {
            Some(path) => path,
            None => env::current_dir().handle_errors()?.join("output"),
        };

        fs::create_dir_all(&output_dir).handle_errors()?;
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
        self.cache_dir.join(filename)
    }

    pub fn clear_all(&self) -> Result<()> {
        if self.data_dir.exists() {
            fs::remove_dir_all(&self.data_dir).handle_errors()?;
            fs::create_dir_all(&self.data_dir).handle_errors()?;
        }

        if self.cache_dir.exists() {
            fs::remove_dir_all(&self.cache_dir).handle_errors()?;
            fs::create_dir_all(&self.cache_dir).handle_errors()?;
        }

        Ok(())
    }

    pub fn is_dir_empty(&self, path: &str) -> bool {
        let dir_path = self.data_dir.join(path);
        !dir_path.exists() || 
            dir_path.read_dir().map_or(true, |mut entries| entries.next().is_none())
    }
}