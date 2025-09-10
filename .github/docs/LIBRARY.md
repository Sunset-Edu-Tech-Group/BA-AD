# Using BA-AD as a Library

## Getting Started

Add `baad` to your project's dependencies in `Cargo.toml`:

```toml
[dependencies]
baad = { git = "https://github.com/Deathemonic/BA-AD" }
```

## Basic Usage

Below are examples of common operations using the library:

```rust
use baad::apk::{ApkFetcher, ApkExtractor};
use baad::catalog::{CatalogFetcher, CatalogParser};
use baad::download::{ResourceDownloader, ResourceCategory, ResourceFilter};
use baad::helpers::{ServerConfig, ServerRegion, Platform, BuildType};

use eyre::Result;
use std::path::PathBuf;
use std::rc::Rc;

async fn example() -> Result<()> {
    // Configure for Japan server with default Android/Standard build
    let config = ServerConfig::new(ServerRegion::Japan, None, None)?;
    
    // Configure for Global server with iOS and Teen build
    let global_config = ServerConfig::new(
        ServerRegion::Global, 
        Some(Platform::Ios), 
        Some(BuildType::Teen)
    )?;

    // Check for APK updates and download if needed
    let apk_fetcher = ApkFetcher::new(config.clone())?;
    apk_fetcher.download_apk(false).await?;

    // Extract data from APK (Japan only)
    if config.region == ServerRegion::Japan {
        let extractor = ApkExtractor::new(config.clone())?;
        extractor.extract_data()?;
    }

    // Fetch game catalogs
    let catalog_fetcher = CatalogFetcher::new(config.clone(), apk_fetcher)?;
    catalog_fetcher.get_addressable().await?;
    catalog_fetcher.get_catalogs().await?;
    
    // Process catalogs into downloadable resources
    let catalog_parser = CatalogParser::new(config.clone())?;
    catalog_parser.process_catalogs().await?;

    // Download resources
    let downloader = ResourceDownloader::new(
        Some(PathBuf::from("./output")), 
        config.clone()
    ).await?;

    // Download all asset bundles
    downloader.download(ResourceCategory::Assets, None).await?;

    // Download specific resources using a filter
    let filter = ResourceFilter::contains("CH0230")?;
    downloader.download(ResourceCategory::Assets, Some(filter)).await?;

    Ok(())
}
```

## Core Components

### Logging

The baad automatically initializes logging with default settings when loaded. No additional setup is required for basic usage.

### Controlling Log Levels

Library users have several ways to control logging:

#### 1. Feature Flags (Recommended)
```toml
[dependencies]
# Default: info level logging
baad = { git = "https://github.com/Deathemonic/BA-AD" }

# Disable error level logging
baad = { git = "https://github.com/Deathemonic/BA-AD", features = ["no_error"] }

# Disable logging entirely
baad = { git = "https://github.com/Deathemonic/BA-AD", features = ["no_logs"] }

# Disable debug messages only
baad = { git = "https://github.com/Deathemonic/BA-AD", features = ["no_debug"] }
```

#### 2. Custom Logging Configuration

For advanced use cases, you can initialize logging before using the library:

```rust
use baad::helpers::{LoggingConfig, init_logging};

// Custom logging configuration - call this BEFORE using any library functions
let config = LoggingConfig {
    verbose_mode: true,
    enable_console: true,
    colored_output: true,
    ..LoggingConfig::default()
};

init_logging(config)?;

```

### ServerConfig

Configure which server, platform, and build type you want to download:

```rust
use baad::helpers::{ServerConfig, ServerRegion, Platform, BuildType};

// Japan server with default Android/Standard build
let japan_config = ServerConfig::new(ServerRegion::Japan, None, None)?;

// Japan server with iOS build
let japan_ios_config = ServerConfig::new(
    ServerRegion::Japan, 
    Some(Platform::Ios), 
    None
)?;

// Global server with default Android/Standard build
let global_config = ServerConfig::new(ServerRegion::Global, None, None)?;

// Global server with iOS build
let global_ios_config = ServerConfig::new(
    ServerRegion::Global, 
    Some(Platform::Ios), 
    None
)?;

// Global server with Teen build (Android)
let global_teen_config = ServerConfig::new(
    ServerRegion::Global, 
    None, 
    Some(BuildType::Teen)
)?;

// Global server with iOS Teen build
let global_ios_teen_config = ServerConfig::new(
    ServerRegion::Global, 
    Some(Platform::Ios), 
    Some(BuildType::Teen)
)?;

// Get market configuration (Global only)
if let Some(market_config) = global_config.get_market_config() {
    println!("Market ID: {}", market_config.market_game_id);
    println!("Market Code: {}", market_config.market_code);
}
```

**Note**: The `--teen` build type is only available for the Global server. Attempting to use `BuildType::Teen` with `ServerRegion::Japan` will return an error.

### ApkFetcher

Check for updates and download the APK:

```rust
use baad::apk::ApkFetcher;

// Initialize fetcher
let apk_fetcher = ApkFetcher::new(config.clone())?;

// Check for updates
let new_version = apk_fetcher.check_version().await?;
if let Some(version) = new_version {
    println!("New version available: {}", version);
}

// Download APK (with force flag to override existing files)
apk_fetcher.download_apk(true).await?;
```

### CatalogFetcher & CatalogParser

Fetch and process game catalogs containing asset information:

```rust
use baad::catalog::{CatalogFetcher, CatalogParser};

let catalog_fetcher = CatalogFetcher::new(config.clone(), apk_fetcher)?;

// Get addressable data first
let addressable_json = catalog_fetcher.get_addressable().await?;

// Get catalog data
let catalog_json = catalog_fetcher.get_catalogs().await?;

// Process catalogs into downloadable resources
let catalog_parser = CatalogParser::new(config.clone())?;
catalog_parser.process_catalogs().await?;
```

### ResourceDownloader

Download game resources:

```rust
use baad::download::{ResourceDownloader, ResourceDownloadBuilder, ResourceCategory, ResourceFilter};

// Basic downloader
let downloader = ResourceDownloader::new(
    Some(PathBuf::from("./output")), 
    config.clone()
).await?;

// Or use the builder pattern for more options
let downloader = ResourceDownloadBuilder::new(config.clone())?
    .output(Some(PathBuf::from("./output")))
    .retries(5)
    .limit(10)
    .build()
    .await?;

// Download different resource categories
downloader.download(ResourceCategory::Assets, None).await?; // All assets
downloader.download(ResourceCategory::Tables, None).await?; // Game tables
downloader.download(ResourceCategory::Media, None).await?;  // Media files
downloader.download(ResourceCategory::All, None).await?;    // Everything

// Using multiple categories
let categories = ResourceCategory::multiple(vec![
    ResourceCategory::Assets,
    ResourceCategory::Tables
]);
downloader.download(categories, None).await?;

// Apply filters
use baad::download::FilterMethod;

let exact_filter = ResourceFilter::new("CharacterData", FilterMethod::Exact)?;
let contains_filter = ResourceFilter::new("sprite", FilterMethod::Contains)?;
let regex_filter = ResourceFilter::new(r"character_\d+\.bundle", FilterMethod::Regex)?;
let glob_filter = ResourceFilter::new("**/textures/*.png", FilterMethod::Glob)?;

// Download with filter
downloader.download(ResourceCategory::Assets, Some(contains_filter)).await?;
```

### APKExtractor

Extract specific files from APKs:

```rust
use baad::apk::{ApkExtractor, ExtractionRule};
use std::path::PathBuf;

let extractor = ApkExtractor::new(config.clone())?;

// Extract data files
extractor.extract_data()?;

// Extract libil2cpp.so and metadata.dat
extractor.extract_il2cpp()?;

// Custom extraction
let rule = ExtractionRule {
    apk: "com.YostarJP.BlueArchive.apk",
    path: &["assets", "bin", "Data"],
    pattern: "globalgamemanagers",
    output: PathBuf::from("./extracted").into_boxed_path(),
};
extractor.extract(rule)?;
```

## Configuration Options

The library can be configured with feature flags in your `Cargo.toml`:

```toml
[dependencies]
baad = { git = "https://github.com/your-repo/baad", features = ["no_logs", "no_debug", "no_error"] }
```

Available features:
- `no_logs`: Enable basic logging
- `no_debug`: Enable debug messages
- `no_error`: Disable error messages
