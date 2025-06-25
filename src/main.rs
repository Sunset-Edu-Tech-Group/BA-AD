mod apk;
mod catalog;
mod download;
mod helpers;
mod utils;
pub mod cli;

use crate::apk::{ApkExtractor, ApkFetcher};
use crate::helpers::{ServerConfig, ServerRegion};
use crate::utils::FileManager;

use anyhow::Result;

/// Testing purposes only not to be run
#[tokio::main]
async fn main() -> Result<()> {
    let file_manager = FileManager::new()?;
    let server_config = ServerConfig::new(ServerRegion::Japan)?;

    let apk_fetcher = ApkFetcher::new(file_manager.clone(), server_config.clone())?;
    let apk_extractor = ApkExtractor::new(file_manager.clone(), server_config.clone())?;

    let _ = apk_fetcher.download_apk().await?;
    let _ = apk_extractor.extract_data()?;

    Ok(())
}
