<div align="center">
  <img src="resources/github/archive.png" width="500px" alt="logo">
  <h1>Blue Archive - Asset Downloader</h1>
</div>

A tool that downloads and extracts **Blue Archive** Global and Japan `AssetBundles`, `TableBundles`, and `MediaResources`.

## Building
> If you want to try it out you can build it yourself. Note that this still a work in progress and something will break.

1. Install [rustup](https://rustup.rs)
2. Clone this repository
```sh
git clone https://github.com/Deathemonic/BA-AD -b rust
```
3. Build using `cargo`
```sh
cargo build
```


### TODO
- [X] Add global support
- [X] Multithreading download support
- [X] Add the asset downloader
- [X] UI and colorful messages
- [ ] Add search mode and filter mode
- [ ] Add extract media zips
- [ ] Add extract table zips, and db (low priority)
- [ ] Add extract assetbundle (low priority)
- [ ] ~Add download old apks~


### FAQ


Why the switch to rust?
- baad is getting slow, and I want to learn rust so I decided to make baad in rust and might as well add new stuff that I didn't add before like Global asset download.
