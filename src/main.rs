mod crypto;
mod helpers;
mod utils;

use helpers::args::{Cli, Commands, DownloadMode};
use helpers::config::RegionConfig;
use helpers::file::FileManager;
use helpers::json;
use utils::apk::ApkParser;
use utils::catalog_fetcher::CatalogFetcher;
use utils::catalog_parser::CatalogParser;

use anyhow::Result;
use clap::Parser;
use std::fs;
use std::path::PathBuf;

#[tokio::main]
async fn main() -> Result<()> {
    let args: Cli = Cli::parse();
    let file_manager: FileManager = FileManager::new()?;

    if args.clean {
        println!("Cleaning data and cache directories...");
        fs::remove_dir_all(file_manager.data_dir()).ok();
        fs::remove_dir_all(file_manager.cache_dir()).ok();
        fs::create_dir_all(file_manager.data_dir())?;
        fs::create_dir_all(file_manager.cache_dir())?;
        println!("Directories cleaned successfully");
        if args.command.is_none() && !args.update {
            return Ok(());
        }
    }

    if args.command.is_none() && args.update {
        println!("Updating APK only...");
        let japan_config: RegionConfig = RegionConfig::new("japan");
        let apk_parser: ApkParser<'_> = ApkParser::new(&file_manager, &japan_config)?;
        apk_parser.download_apk(true).await?;
        println!("APK updated successfully");
        return Ok(());
    }

    if let Some(command) = args.command {
        match command {
            Commands::Download(download_args) => {
                let region: &str = match download_args.mode {
                    DownloadMode::Japan => "japan",
                    DownloadMode::Global => "global",
                };
                let config: RegionConfig = RegionConfig::new(region);

                println!("Processing download command for {} region...", region);

                match region {
                    "japan" => {
                        if args.clean {
                            file_manager.clean_region_directories(&config.id)?;
                        }

                        if args.update {
                            update_japan_and_process(&file_manager, &config).await?;
                        } else {
                            handle_japan_check_update(&file_manager, &config, download_args.all).await?;
                        }
                    }
                    "global" => {
                        if args.clean {
                            file_manager.clean_region_directories(&config.id)?;
                        }

                        if args.update || download_args.all {
                            fetch_global_catalogs(&file_manager, &config).await?;
                        } else {
                            check_global_catalogs(&file_manager, &config).await?;
                        }
                    }
                    _ => println!("Unsupported region: {}", region),
                }
            }
            Commands::Search(_) => {
                println!("Search command not implemented yet");
            }
            Commands::Extract(_) => {
                println!("Extract command not implemented yet");
            }
        }
    }

    Ok(())
}

async fn update_japan_and_process(file_manager: &FileManager, config: &RegionConfig) -> Result<()> {
    println!("Downloading APK...");
    let apk_parser: ApkParser<'_> = ApkParser::new(file_manager, config)?;
    apk_parser.download_apk(true).await?;

    println!("Extracting APK...");
    apk_parser.extract_apk()?;

    fetch_japan_catalogs(file_manager, config).await?;

    println!("APK updated, extracted and catalogs processed successfully");
    Ok(())
}

async fn handle_japan_check_update(file_manager: &FileManager, config: &RegionConfig, check_catalogs: bool) -> Result<()> {
    let apk_parser: ApkParser<'_> = ApkParser::new(file_manager, config)?;
    let apk_path: PathBuf = file_manager.data_path(&config.apk_path);
    let data_dir: PathBuf = file_manager.data_path("data");

    if !apk_path.exists() {
        println!("APK doesn't exist, downloading...");
        apk_parser.download_apk(false).await?;
        apk_parser.extract_apk()?;
        fetch_japan_catalogs(file_manager, config).await?;
        return Ok(());
    }

    if !data_dir.exists() {
        println!("APK not extracted, extracting...");
        apk_parser.extract_apk()?;
        fetch_japan_catalogs(file_manager, config).await?;
        return Ok(());
    }

    if check_catalogs {
        let game_files_path: String = config.catalog_file_path("GameFiles.json");
        if !file_manager.file_exists(&game_files_path) {
            println!("Catalogs don't exist, fetching...");
            fetch_japan_catalogs(file_manager, config).await?;
        } else {
            println!("Using existing catalogs");
        }
    }

    println!("Japan APK and catalogs are up to date");
    Ok(())
}

async fn fetch_japan_catalogs(file_manager: &FileManager, config: &RegionConfig) -> Result<()> {
    println!("Fetching catalog URL...");
    let catalog_fetcher: CatalogFetcher<'_> = CatalogFetcher::new(file_manager);
    let catalog_url: String = catalog_fetcher.get_catalog_url(&config.id).await?;

    println!("Fetching and processing catalogs...");
    let mut catalog_parser: CatalogParser<'_> = CatalogParser::new(file_manager, Some(catalog_url), config);
    catalog_parser.fetch_catalogs().await?;
    catalog_parser.save_game_files().await?;

    println!("Catalogs processed successfully");
    Ok(())
}

async fn check_global_catalogs(file_manager: &FileManager, config: &RegionConfig) -> Result<()> {
    let game_files_path: String = config.catalog_file_path("GameFiles.json");
    let resources_path_json: String = config.catalog_file_path("resources_path.json");

    if !file_manager.file_exists(&game_files_path) || !file_manager.file_exists(&resources_path_json) {
        println!("Global catalogs don't exist, fetching...");
        fetch_global_catalogs(file_manager, config).await?;
    } else {
        println!("Using existing global catalogs");
    }

    Ok(())
}

async fn fetch_global_catalogs(file_manager: &FileManager, config: &RegionConfig) -> Result<()> {
    file_manager.create_dir(&config.catalogs_path())?;

    let should_fetch: bool = match json::get_api_data(file_manager) {
        Ok(api_data) => {
            let catalog_fetcher: CatalogFetcher<'_> = CatalogFetcher::new(file_manager);
            let current_url: String = catalog_fetcher.get_catalog_url(&config.id).await?;
            let saved_url: String = api_data.global.addressable_url;
            current_url != saved_url
        }
        Err(_) => true,
    };

    if should_fetch {
        println!("Fetching new global catalogs...");
        let mut catalog_parser: CatalogParser<'_> = CatalogParser::new(file_manager, None, config);
        catalog_parser.fetch_catalogs().await?;
        catalog_parser.save_game_files().await?;
        println!("Global catalogs updated successfully");
    } else {
        println!("Using existing global catalogs (addressable URL unchanged)");
        let resources_path_json: String = config.catalog_file_path("resources_path.json");
        if !file_manager.file_exists(&resources_path_json) {
            println!("resources_path.json doesn't exist, fetching catalogs...");
            let mut catalog_parser: CatalogParser<'_> = CatalogParser::new(file_manager, None, config);
            catalog_parser.fetch_catalogs().await?;
            catalog_parser.save_game_files().await?;
            println!("Global catalogs fetched successfully");
        }
    }

    Ok(())
}
