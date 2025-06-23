mod apk;
mod catalog;
mod download;
mod helpers;
mod utils;

use crate::apk::extract::ApkExtractor;
use crate::apk::fetch::ApkFetcher;
use crate::catalog::fetch::CatalogFetcher;
use crate::catalog::parse::CatalogParser;
use crate::download::downloader::ResourceDownloader;
use crate::download::filter::{FilterMethod, ResourceFilter};
use crate::helpers::config::ServerConfig;
use crate::helpers::config::ServerRegion;
use crate::utils::file::FileManager;

/// Testing purposes only not to be run
#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let file_manager = FileManager::new()?;
    let server_config = ServerConfig::new(ServerRegion::Global)?;

    let apk_fetcher = ApkFetcher::new(&file_manager, &server_config)?;
    let apk_extract = ApkExtractor::new(&file_manager, &server_config)?;
    let catalog_fetcher = CatalogFetcher::new(&file_manager, &server_config)?;
    let catalog_parser = CatalogParser::new(&file_manager, &server_config)?;
    let filter = ResourceFilter::new("CH0230", FilterMethod::ContainsIgnoreCase)?;
    let resource_downloader = ResourceDownloader::new(
        None,
        &file_manager,
        &server_config,
    )?;

    // let _ = apk_fetcher.download_apk().await;
    // let _ = apk_extract.extract_data();

    // let _ = catalog_fetcher.get_addressable().await?;
    // let _ = catalog_fetcher.get_catalogs().await?;
    // let _ = catalog_parser.process_catalogs().await?;
    let _ = resource_downloader.download(None, Some(filter)).await?;

    Ok(())
}
