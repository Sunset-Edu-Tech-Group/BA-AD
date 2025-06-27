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
    // Initialize the file manager
    let file_manager = FileManager::new()?; 

    // Configure for Japan or Global server
    let config = ServerConfig::new(ServerRegion::Japan)?; 

    // Check for APK updates and download if needed
    let apk_fetcher = ApkFetcher::new(file_manager.clone(), config.clone())?;
    let (version, apk_path, updated) = apk_fetcher.download_apk(false).await?;
    println!("APK version: {}, updated: {}", version, updated);

    // Extract data from APK
    if updated {
        let extractor = ApkExtractor::new(file_manager.clone(), config.clone())?;
        extractor.extract_data()?;
    }

    // Fetch game catalogs
    let catalog_fetcher = CatalogFetcher::new(file_manager.clone(), config.clone(), apk_fetcher.clone())?;
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

### FileManager

The `FileManager` handles file system operations, including data and cache directories:

```rust
use baad::utils::FileManager;

// Basic initialization
let file_manager = FileManager::new()?; 

// Custom configuration
let config = baad::utils::FileManagerConfig {
    data_dir: Some(PathBuf::from("/some/path")),
    cache_dir: Some(PathBuf::from("/some/cache/path")),
    app_name: Some("my_app".to_string()),
};
let file_manager = FileManager::with_config(config)?; 

// Save and load files
file_manager.save_file("config.json", json_content.as_bytes())?;
let content = file_manager.load_file("config.json")?;
```

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
let apk_fetcher = ApkFetcher::new(file_manager.clone(), config.clone())?;

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
    file_manager.clone(), 
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
    file_manager.clone(), 
    config.clone()
)?;

// Or use the builder pattern for more options
let downloader = ResourceDownloadBuilder::new(file_manager.clone(), config.clone())?
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

### Error Handling

The library provides rich error handling extensions:

```rust
use baad::helpers::ErrorExt;
use baad::helpers::ErrorContext;

use anyhow::Result;
use std::fs::read_to_string;

// Handle errors with context
let result = some_operation()
    .error_context("Failed to perform the operation");

// For standard result types
let io_result = read_to_string("file.txt")
    .handle_errors();

// For optional values
let value = optional_operation()
    .error_context("Required value was not found");
```

### APKExtractor

Extract specific files from APKs:

```rust
use baad::apk::{ApkExtractor, ExtractionRule};
use std::path::PathBuf;

let extractor = ApkExtractor::new(file_manager.clone(), config.clone())?;

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
baad = { git = "https://github.com/your-repo/baad", features = ["logs", "debug"] }
```

Available features:
- `logs`: Enable basic logging
- `debug`: Enable debug logging (implies `logs`)
- `no_error`: Disable error messages

## Logging

The library provides macros for logging:

```rust
use baad::{info, debug, success, error, warn};

info!("Processing file: {}", filename);
debug!("Detailed debug info: {:?}", data);
success!("Operation completed successfully");
warn!("Resource might be outdated");
error!("Failed to download: {}", err);
```

## Working with JSON

Helpers for working with game data in JSON format:

```rust
use baad::helpers::{ApiData, load_json, save_json, update_api_data};

// Load JSON data
let api_data: ApiData = load_json(file_manager.as_ref(), "api_data.json").await?;

// Save JSON data
save_json(file_manager.as_ref(), "api_data.json", &api_data).await?;

// Update JSON data with a closure
update_api_data(file_manager.as_ref(), |data| {
    data.japan.version = "1.45.0".to_string();
}).await?;
```

## Async

The library is built on `tokio` for asynchronous operations.

```rust
#[tokio::main]
async fn main() -> Result<()> {
    // Your library code here
    Ok(())
}
```