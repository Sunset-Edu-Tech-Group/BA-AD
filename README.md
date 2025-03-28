<div align="center">
  <img src="resources/github/archive.png" width="500px" alt="logo">
  <h1>Blue Archive - Asset Downloader (Rust)</h1>
</div>

This is a WIP port of BA-AD to rust. It will be blazingly fast 🚀*.


Currently this doesn't do anything, it just fetches catalogs.


## Building
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
- [/] Add global support
- [ ] Add the asset downloader
- [ ] Add search mode and filter mode
- [ ] Add extract media zips
- [ ] Add extract table zips, and db (low priority)
- [ ] Add extract assetbundle (low priority)
- [X] Add download old apks


### FAQ


Why the switch to rust?
- baad is getting slow, and I want to learn rust so I decided to make baad in rust and might as well add new stuff that I didn't add before like Global asset download.
