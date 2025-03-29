use clap::{Args, Parser, Subcommand};

#[derive(Debug, Parser)]
#[command(
    name = "baad",
    author,
    version,
    about = "Blue Archive Asset Downloader",
    long_about = None
)]
pub struct Cli {
    #[command(subcommand)]
    pub command: Option<Commands>,

    /// Clean cache and data
    #[arg(short = 'c', long = "clean", global = true)]
    pub clean: bool,

    /// Force update the apk
    #[arg(short = 'u', long = "update", global = true)]
    pub update: bool,
}

#[derive(Debug, Subcommand)]
pub enum Commands {
    /// Download game files
    Download(DownloadArgs),

    /// Search mode
    Search(SearchArgs),

    /// Extract game files
    Extract(ExtractArgs),
}

#[derive(Debug, Args)]
pub struct DownloadArgs {
    /// Download mode (global or japan)
    #[arg(value_enum)]
    pub mode: DownloadMode,

    /// Download the assetbundles
    #[arg(long = "assets")]
    pub assets: bool,

    /// Download the tablebundles
    #[arg(long = "tables")]
    pub tables: bool,

    /// Download the mediaresources
    #[arg(long = "media")]
    pub media: bool,

    /// Download all game files
    #[arg(short = 'a', long = "all")]
    pub all: bool,

    /// Output directory for the downloaded files
    #[arg(long = "output", default_value = "./output")]
    pub output: String,

    /// Set a limit for the download limit
    #[arg(long = "limit", default_value = "5")]
    pub limit: u32,

    /// Filter by name
    #[arg(long = "filter")]
    pub filter: Option<String>,
}

#[derive(Debug, clap::ValueEnum, Clone)]
pub enum DownloadMode {
    /// Global version assets
    Global,

    /// Japan version assets
    Japan,
}

#[derive(Debug, Args)]
pub struct SearchArgs {
    // Add search-specific arguments here
}

#[derive(Debug, Args)]
pub struct ExtractArgs {
    // Add extract-specific arguments here
}
