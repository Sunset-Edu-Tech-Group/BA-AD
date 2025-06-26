use crate::download::FilterMethod;

use clap::{Parser, Subcommand};

#[derive(Parser)]
#[command(name = "baad")]
#[command(about = "Blue Archive Asset Downloader")]
#[command(version)]
pub struct Args {
    #[command(subcommand)]
    pub command: Option<Commands>,

    /// Force update
    #[arg(short, long)]
    pub update: bool,

    /// Cleans the cache
    #[arg(short, long)]
    pub clean: bool,

    /// Enable verbose output
    #[arg(short, long)]
    pub verbose: bool,
}

#[derive(Subcommand)]
pub enum Commands {
    /// Download game files
    Download {
        #[command(subcommand)]
        region: RegionCommands,
    },
}

#[derive(Subcommand)]
pub enum RegionCommands {
    /// Download from Global server
    Global(DownloadArgs),
    /// Download from Japan server
    Japan(DownloadArgs),
}

#[derive(Parser)]
pub struct DownloadArgs {
    /// Download the assetbundles
    #[arg(long)]
    pub assets: bool,

    /// Download the tablebundles
    #[arg(long)]
    pub tables: bool,

    /// Download the mediaresources
    #[arg(long)]
    pub media: bool,

    /// Output directory for the downloaded files
    #[arg(long, default_value = "./output")]
    pub output: String,

    /// Set a limit on the concurrent downloads
    #[arg(long, default_value = "10")]
    pub limit: u32,

    /// Number of retry attempts for failed downloads
    #[arg(long, default_value = "10")]
    pub retries: u32,

    /// Filter by name
    #[arg(long)]
    pub filter: Option<String>,

    /// Filter method to use
    #[arg(long, value_enum, default_value = "contains")]
    pub filter_method: FilterMethod,
}

impl DownloadArgs {
}