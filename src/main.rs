mod apk;
mod catalog;
mod helpers;
mod utils;

use crate::apk::fetch::ApkFetcher;
use crate::apk::extract::ApkExtractor;
use crate::catalog::parse::CatalogParser;
use crate::catalog::fetch::CatalogFetcher;
use crate::utils::file::FileManager;
use crate::helpers::config::ServerConfig;

/// Testing purposes only not to be run
#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let file_manager = FileManager::new()?;
    let server_config = ServerConfig::new("japan")?;
    
    let apk_fetcher = ApkFetcher::new(&file_manager, &server_config)?;
    let apk_extract = ApkExtractor::new(&file_manager, &server_config)?;
    let catalog_fetcher = CatalogFetcher::new(&file_manager, &server_config)?;
    let catalog_parser = CatalogParser::new(&file_manager, &server_config)?;
    
    // let _ = apk_fetcher.download_apk().await;
    // let _ = apk_extract.extract_data();

    // let _ = catalog_fetcher.global_addressable().await?;
    // let _ = catalog_fetcher.global_resources().await?;
    // let _ = catalog_parser.global_catalogs().await?;
    // let jp_addressable = catalog_fetcher.japan_addressable().await?;
    let jp_catalog = catalog_fetcher.japan_catalog().await?;
    
    info!("{jp_catalog}");
    // info!("{jp_catalog}");
    
    Ok(())
}