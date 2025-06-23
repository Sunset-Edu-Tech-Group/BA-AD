mod apk;
mod catalog;
mod download;
mod helpers;
mod utils;

use crate::apk::ApkFetcher;
use crate::helpers::{ServerConfig, ServerRegion};
use crate::utils::FileManager;

use anyhow::Result;

/// Testing purposes only not to be run
#[tokio::main]
async fn main() -> Result<()> {
    let file_manager = FileManager::new()?;
    let server_config = ServerConfig::new(ServerRegion::Japan)?;

    let apk_fetcher = ApkFetcher::new(&file_manager, &server_config)?;

    let _ = apk_fetcher.download_apk().await?;

    Ok(())
}
