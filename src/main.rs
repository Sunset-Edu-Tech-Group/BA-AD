use crate::utils::apk;
use crate::utils::apk::ApkConfig;
use crate::lib::file::FileManager;
use anyhow::Result;
use clap::{Parser, Subcommand};

#[derive(Parser)]
#[command(name = "baad")]
#[command(author = "Blue Archive Asset Downloader")]
#[command(version = "0.1.0")]
#[command(about = "A tool for downloading and extracting Blue Archive APK assets", long_about = None)]
struct Cli {
    #[arg(long)]
    update: bool,
    
    #[arg(long)]
    extract: bool,
}

#[tokio::main]
async fn main() -> Result<()> {
    let cli: Cli = Cli::parse();
    let config: ApkConfig = ApkConfig::default();
    
    println!("BA-AD APK Downloader");
    
    let file_manager: FileManager = FileManager::new()?;
    println!("Data directory: {}", file_manager.data_dir().display());
    
    if cli.update {
        println!("Downloading the latest APK...");
        apk::download_apk(
            &file_manager,
            &config.version_url,
            &config.apk_dir,
            &config.apk_filename,
            &config.version_filename
        ).await?;
    }
    
    if cli.extract {
        let apk_path: String = format!("{}/{}", config.apk_dir, config.apk_filename);
        if file_manager.file_exists(&apk_path) {
            println!("Extracting APK assets...");
            apk::extract_apk(
                &file_manager,
                &apk_path,
                "extracted",
                &config.asset_filter
            )?;
        } else {
            println!("Error: No APK file found to extract. Run with --update first.");
        }
    }
    
    if !cli.update && !cli.extract {
        println!("No action specified.");
        println!("Usage:");
        println!("  baad --update    Download the latest APK");
        println!("  baad --extract   Extract assets from the downloaded APK");
        println!("  baad --update --extract   Download and extract in one step");
    }
    
    println!("Done!");
    Ok(())
}

mod utils;
mod lib;
