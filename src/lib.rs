pub mod crypto;
pub mod helpers;
pub mod utils;

pub use helpers::config::RegionConfig;
pub use helpers::file::FileManager;
pub use utils::apk::{ApkParser, ApiData, RegionData, GlobalRegionData, ExtractionRule, ExtractionConfig};

pub type Result<T> = anyhow::Result<T>;

pub async fn create_apk_parser(file_manager: &FileManager, region: &str) -> Result<ApkParser<'_>> {
    let config = RegionConfig::new(region);
    ApkParser::new(file_manager, &config)
}

pub async fn init_file_manager() -> Result<FileManager> {
    FileManager::new().await
} 