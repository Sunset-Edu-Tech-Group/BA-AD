# Changelogs

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
- Moved crypto to `BA-CY`