use anyhow::Result;
use platform_dirs::AppDirs;
use std::fs;
use std::path::PathBuf;

#[allow(dead_code)]
const APP_NAME: &str = env!("CARGO_CRATE_NAME");

#[derive(Clone)]
pub struct FileManager {
    cache_dir: PathBuf,
    data_dir: PathBuf,
}

impl FileManager {
    pub fn new() -> Result<Self> {
        let app_dirs: AppDirs = AppDirs::new(Some(APP_NAME), true).unwrap();
        
        fs::create_dir_all(&app_dirs.cache_dir)?;
        fs::create_dir_all(&app_dirs.data_dir)?;
        
        Ok(Self {
            cache_dir: app_dirs.cache_dir,
            data_dir: app_dirs.data_dir,
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