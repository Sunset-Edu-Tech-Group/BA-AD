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
use baad::utils::FileManager;
use baad::apk::{ApkFetcher, ApkExtractor};
use baad::catalog::CatalogFetcher;
use baad::download::{ResourceDownloader, ResourceCategory, ResourceFilter};
use baad::helpers::{ServerConfig, ServerRegion};

use anyhow::Result;
use std::path::PathBuf;

async fn example() -> Result<()> {
    // Configure for Japan or Global server
    let config = ServerConfig::new(ServerRegion::Japan)?; 

    // Check for APK updates and download if needed
    let apk_fetcher = ApkFetcher::new(file_manager.clone(), config.clone())?;
    let (version, apk_path, updated) = apk_fetcher.download_apk(false).await?;
    println!("APK version: {}, updated: {}", version, updated);

    // Extract data from APK
    if updated {
        let extractor = ApkExtractor::new(config.clone())?;
        extractor.extract_data()?;
    }

    // Fetch game catalogs
    let catalog_fetcher = CatalogFetcher::new(config.clone(), apk_fetcher.clone())?;
    let catalog_data = catalog_fetcher.get_catalogs().await?;

    // Download resources
    let downloader = ResourceDownloader::new(
        Some(PathBuf::from("./output")), 
        file_manager.clone(), 
        config.clone()
    )?;

    // Download all asset bundles
    downloader.download(ResourceCategory::Assets, None).await?;

    // Download specific resources using a filter
    let filter = ResourceFilter::contains("CH0230")?;
    downloader.download(ResourceCategory::Assets, Some(filter)).await?;

    Ok(())
}
```

## Core Components

### ServerConfig

Here you can set which server you want to download:

```rust
use baad::helpers::ServerConfig;
use baad::helpers::ServerRegion;

// JP server
let japan_config = ServerConfig::new(ServerRegion::Japan)?;

// Global server
let global_config = ServerConfig::new(ServerRegion::Global)?;
```

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
let (version, apk_path, updated) = apk_fetcher.download_apk(true).await?;
```

### CatalogFetcher

Fetch and process game catalogs containing asset information:

```rust
use baad::catalog::CatalogFetcher;

let catalog_fetcher = CatalogFetcher::new(
    config.clone(), 
    apk_fetcher.clone()
)?;

// Get catalog data
let catalog_json = catalog_fetcher.get_catalogs().await?;

// Get addressable data
let addressable_json = catalog_fetcher.get_addressable().await?;
```

### ResourceDownloader

Download game resources:

```rust
use baad::download::{ResourceDownloader, ResourceDownloadBuilder, ResourceCategory, ResourceFilter};

// Basic downloader
let downloader = ResourceDownloader::new(
    Some(PathBuf::from("./output")), 
    config.clone()
)?;

// Or use the builder pattern for more options
let downloader = ResourceDownloadBuilder::new(config.clone())?
    .output(Some(PathBuf::from("./output")))
    .retries(5)
    .limit(10)
    .build()?;

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
let exact_filter = ResourceFilter::exact("CharacterData")?;
let contains_filter = ResourceFilter::contains("sprite")?;
let regex_filter = ResourceFilter::regex(r"character_\d+\.bundle")?;
let glob_filter = ResourceFilter::glob("**/textures/*.png")?;

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
    output: PathBuf::from("./extracted"),
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