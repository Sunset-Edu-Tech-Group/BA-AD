mod apk;
mod catalog;
mod helpers;
mod utils;

use crate::catalog::parse::CatalogParser;
use crate::catalog::fetch::CatalogFetcher;
use crate::utils::file::FileManager;
use crate::helpers::config::ServerConfig;

/// Testing purposes only not to be run
#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let file_manager = FileManager::new()?;
    let server_config = ServerConfig::new("global")?;
    
    let catalog_fetcher = CatalogFetcher::new(&file_manager, &server_config)?;
    let catalog_parser = CatalogParser::new(&file_manager, &server_config)?;

    let a = catalog_fetcher.global_addressable().await?;
    let b = catalog_fetcher.global_resources().await?;
    let c = catalog_parser.global_catalogs().await?;
    
    Ok(())
}