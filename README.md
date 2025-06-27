<div align="center">
  <img src=".github/resources/archive.png" width="4062" alt="logo">
</div>

# Blue Archive - Asset Downloader
A tool and library that downloads the latest **Blue Archive** assets.

## Install

### Release
You can download the latest pre-build binaries at [Releases](https://github.com/Deathemonic/BA-AD/releases)

[Windows]() | [Linux]() | [MacOS]() 

### Cargo
```shell
cargo install --git "https://github.com/Deathemonic/BA-AD" --locked --features "logs,debug" --release
```

## Usage

Download all assets from `JP` server
```shell
baad download japan
```

Download all assets from `Global` server
```shell
baad download global
```

### Examples

```shell
# Force update the APK and fetches the latest catalogs
baad --update

# Downloads the TableBundles from JP server and save it in a folder named Downloads
baad download japan --tables --output ./Downloads

# Downloads the MediaResources from the Global server that contains CH0230 in it
baad download global --media --filter "CH0230"

# Downloads both AssetBundles and MediaResources from JP Server
baad download japan --assets --media

# Downloads the AssetBundles with a limit of 15 concurrent downloads
baad download global --assets --limit 15 

# Downloads all AssetBundles, TableBundles, and MediaResources from JP server that contains CH0069 in it using fuzzy search  
baad download japan --filter "CH0069" --filter-method fuzzy 
```

For more info check out [Usage](.github/docs/USAGE.md)


## Building

1. Install [rustup](https://rustup.rs)
2. Clone this repository
```sh
git clone https://github.com/Deathemonic/BA-AD
cd BA-AD
```
3. Build using `cargo`
```sh
cargo build --features "logs,debug"
```

## Library
```toml
baad = { git = "https://github.com/Deathemonic/BA-AD" }
```

For more info check out [Library](.github/docs/library)

### Other Projects

- [BA-CY](https://github.com/Deathemonic/BA-CY): Library for handling **Blue Archive** catalogs, tables, serialization/deserialization, encryption, and hashing.


### Contributing
Don't like my [shitty code](https://www.reddit.com/r/programminghorror) and what to change it? Feel free to contribute by submitting a pull request or issue. Always appreciate the help.


### Acknowledgement
- [hdk5/MoeXCOM](https://github.com/hdk5/MoeXCOM)
- [respectZ/blue-archive-viewer](https://github.com/respectZ/blue-archive-viewer)
- [fiseleo/Blue-Archive-JP-Downloader](https://github.com/fiseleo/Blue-Archive-JP-Downloader)
- [K0lb3/Blue-Archive---Asset-Downloader](https://github.com/K0lb3/Blue-Archive---Asset-Downloader)
- [lwd-temp/blue-archive-spine-production](https://github.com/lwd-temp/blue-archive-spine-production)
- [aelurum/AssetStudio](https://github.com/aelurum/AssetStudio)

### Copyright
Blue Archive is a registered trademark of NAT GAMES Co., Ltd., NEXON Korea Corp., and Yostar, Inc.
This project is not affiliated with, endorsed by, or connected to NAT GAMES Co., Ltd., NEXON Korea Corp., NEXON GAMES Co., Ltd., IODivision, Yostar, Inc., or any of their subsidiaries or affiliates.
All game assets, content, and materials are copyrighted by their respective owners and are used for informational and educational purposes only.