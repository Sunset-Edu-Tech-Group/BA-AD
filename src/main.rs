mod crypto;
mod helpers;
mod utils;

use helpers::args::{Cli, Commands, DownloadArgs, DownloadMode};
use helpers::config::RegionConfig;
use helpers::file::FileManager;
use helpers::json;
use utils::apk::{self, ApkParser};
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

    if args.clean && args.update {
        return Err(anyhow::anyhow!("Cannot use both --clean and --update"));
    }

    if args.clean {
        clean_operation(&file_manager)?;
        return Ok(());
    }

    if args.command.is_none() && args.update {
        update_operaation(&args, &file_manager).await?;
        return Ok(());
    }

    if let Some(ref command) = args.command {
        handle_command(command, &args, &file_manager).await?;
    }

    Ok(())
}

fn clean_operation(file_manager: &FileManager) -> Result<()> {
    println!("Cleaning data and cache directories...");

    fs::remove_dir_all(file_manager.data_dir()).ok();
    fs::remove_dir_all(file_manager.cache_dir()).ok();
    fs::create_dir_all(file_manager.data_dir())?;
    fs::create_dir_all(file_manager.cache_dir())?;

    println!("Directories cleaned successfully");

    return Ok(());
}

async fn update_operaation(args: &Cli, file_manager: &FileManager) -> Result<()> {
    println!("Updating APK only...");

    let japan_config: RegionConfig = RegionConfig::new("japan");
    let apk_parser: ApkParser<'_> = ApkParser::new(file_manager, &japan_config)?;

    fetch_apk(args, &apk_parser).await?;

    println!("APK updated successfully");

    return Ok(());
}

async fn handle_command(command: &Commands, args: &Cli, file_manager: &FileManager) -> Result<()> {
    match command {
        Commands::Download(download_args) => {
            download_command(download_args, args, file_manager).await?;
        }
        Commands::Search(_) => {
            println!("Search command not implemented yet");
        }
        Commands::Extract(_) => {
            println!("Extract command not implemented yet");
        }
    }
    Ok(())
}

async fn download_command(download_args: &DownloadArgs, args: &Cli, file_manager: &FileManager) -> Result<()> {
    if download_args.multithread > 0 && download_args.limit > 0 {
        return Err(anyhow::anyhow!("Cannot use both --multithread and --limit options together"));
    }

    if download_args.all && (download_args.assets || download_args.tables || download_args.media) {
        return Err(anyhow::anyhow!("Cannot use --all with specific resource type options"));
    }

    let region = match download_args.mode {
        DownloadMode::Japan => utils::downloader::Region::Japan,
        DownloadMode::Global => utils::downloader::Region::Global,
    };

    let config_str: &str = region.as_str();
    let config: RegionConfig = RegionConfig::new(config_str);
    let apk_parser: ApkParser<'_> = ApkParser::new(file_manager, &config)?;

    if args.clean {
        file_manager.clean_region_directories(&config.id)?;
    }

    if args.update {
        match region {
            utils::downloader::Region::Japan => {
                fetch_apk(args, &apk_parser).await?
            },
            utils::downloader::Region::Global => {
                fetch_global_catalogs(file_manager, &config).await?
            },
        }
    } else {
        match region {
            utils::downloader::Region::Japan => {
                check_apk_update(args, file_manager, &config, &apk_parser).await?
            },
            utils::downloader::Region::Global => {
                check_global_catalogs(file_manager, &config).await?
            },
        }
    }

    let mut categories = Vec::new();
    if download_args.all {
        categories.push(utils::downloader::ResourceCategory::All);
    } else {
        if download_args.assets {
            categories.push(utils::downloader::ResourceCategory::AssetBundles);
        }
        if download_args.tables {
            categories.push(utils::downloader::ResourceCategory::TableBundles);
        }
        if download_args.media {
            categories.push(utils::downloader::ResourceCategory::MediaResources);
        }
    }

    if categories.is_empty() {
        categories.push(utils::downloader::ResourceCategory::All);
    }

    let output_path: PathBuf = PathBuf::from(&download_args.output);

    let mut downloader = utils::downloader::ResourceDownloader::new(
        file_manager,
        region,
        None,
        Some(&output_path),
    )?;

    downloader.set_update(args.update);

    if download_args.multithread > 0 {
        println!("Using multithreaded downloads with {} threads", download_args.multithread);
        downloader.set_thread_count(download_args.multithread as usize);
    } 
    
    if download_args.limit > 0 {
        println!("Setting concurrent download limit to {}", download_args.limit);
        downloader.set_max_concurrent_downloads(download_args.limit as usize);
    }

    println!("Starting download to {}", output_path.display());
    downloader.download(&categories).await?;

    Ok(())
}

async fn handle_region(args: &Cli, file_manager: &FileManager, config: &RegionConfig, apk_parser: &ApkParser<'_>) -> Result<()> {
    match config.id.as_str() {
        "japan" => {
            if args.update {
                fetch_apk(args, &apk_parser).await?
            } else {
                check_apk_update(args, file_manager, config, apk_parser).await?
            }
        }
        "global" => {
            if args.update {
                fetch_global_catalogs(file_manager, config).await?
            } else {
                check_global_catalogs(file_manager, config).await?
            }
        }
        _ => return Err(anyhow::anyhow!("Invalid region: {}", config.id)),
    }

    Ok(())
}

async fn fetch_apk(args: &Cli, apk_parser: &ApkParser<'_>) -> Result<()> {
    apk_parser.download_apk(args.update).await?;
    Ok(())
}

async fn process_apk(file_manager: &FileManager, config: &RegionConfig, apk_parser: &ApkParser<'_>) -> Result<()> {
    println!("Extracting APK...");

    if !file_manager.data_path("data").exists() {
        let _ = file_manager.clean_directory("data");
    }

    apk_parser.extract_apk()?;
    fetch_japan_catalogs(file_manager, config).await?;

    Ok(())
}

async fn check_apk_update(args: &Cli, file_manager: &FileManager, config: &RegionConfig, apk_parser: &ApkParser<'_>) -> Result<()> {
    let game_files_path: String = config.catalog_file_path("GameFiles.json");
    let data_dir: PathBuf = file_manager.data_path("data");

    fetch_apk(args, &apk_parser).await?;

    if !data_dir.exists() {
        println!("APK not extracted, extracting...");

        process_apk(file_manager, config, &apk_parser).await?;

        return Ok(());
    }

    if !file_manager.file_exists(&game_files_path) {
        println!("GameFiles.json doesn't exist, fetching...");

        fetch_japan_catalogs(file_manager, config).await?;
        return Ok(());
    }

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
