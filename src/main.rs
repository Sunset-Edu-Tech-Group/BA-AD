mod apk;
mod catalog;
mod helpers;
mod utils;

use crate::apk::fetch::ApkFetcher;
use crate::helpers::config::ServerConfig;
use crate::utils::file::FileManager;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let filemanager = FileManager::new()?;
    let config = ServerConfig::new("japan")?;
    let apkfetcher = ApkFetcher::new(filemanager, config)?;

    apkfetcher.download_apk().await;
    Ok(())
}