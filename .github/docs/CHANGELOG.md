# Changelogs

## v2.4.1

### Fixes
- Changed the cache path from `baad_core` to `baad`

## v2.4.0

### Features
- Updated logging
  - Now uses `tracing` under the hood

### API Changes
- Now uses `eyre` for error handling
- Added logging configuration

### Fixes
- Remove the unnecessary panics 


## v2.3.1

### Features
- Added `--ios` flag
  - Downloads assets from iOS build instead of default Android build
- Added `--teen` flag
  - Downloads teen-rated assets (Global only)
- Added way to do search for actual AssetBundle name in JP

### API Changes
- `ServerConfig::new()` now accepts optional `Platform` and `BuildType` parameters
- Added `ServerConfig::get_market_config()` method for Global server market details
- Updated path-related functions to use `&Path` instead of `&PathBuf` for better performance
- Added platform and build type configuration system
  - New `Platform` enum (Android, iOS)
  - New `BuildType` enum (Standard, Teen)

### Fixes
- Improve path loading performance

## 2.2.0

### Changes
- Due to Blue Archive Japan changed how AssetBundle downloads, 
it now downloads via Patch Packs aka zip files
- Added the ability to download and extract Global apk
- Updated the File Manager
  - You don't need to pass `FileManager::new()` anymore

### Fixes
- Updated extraction method
- Fixed error `Failed to decode response`
- Fixed il2cpp path when extracting

### Misc
- Bump BA-CY to `1.3.5`
- Remove redundant code

## v2.0.3

### Fixes
- Fix where the apk doesn't download if it's outdated
- Fix logs features not properly handled
  - Removing logs in now opt in

### Misc
- Exposed paris module
- Updated build ci


## v2.0.0

### Features
- Rewrite the entire codebase
  - This is a port of ba-ad and also a rewrite of ba-ad-rs
- Added library support
    - You can now use baad in any language you want or even use it in your rust projects
- Added **Global** support
- Added `--clean` to quickly clean the cache
- Added `--filter` to filter out specific files 
  - Alternative to search mode
- Added `--filter-method`
  - You can now filter using `glob`, `fuzzy`, or `exact`
  - This is powered by `lazy-regex` and `nucleo` for performance
- Fully integrated with `BA-CY`
- Replaced the old download manager with `trauma`
- Improved performance
- Improved logging

### Fixes
- Fixed APK will extract regardless you already did it
- Fixed catalog always fetches even though it's already been cached
- Fixed table bundles files are set to numbers instead of their actual name

### Misc
- Removed extract mode
- Removed search mode
- Removed custom catalog url
- Removed custom apk version
- Moved crypto to `BA-CY`