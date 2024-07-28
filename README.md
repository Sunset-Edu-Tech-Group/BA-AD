<div align="center">
  <img src="baad/public/archive.png" width="500px" alt="logo">
  <h1>Blue Archive - Asset Downloader (WIP)</h1>
</div>

A tool that downloads and extracts the **Blue Archive JP** `AssetBundles`, `TableBundles`, `MediaResources`.

It downloads them directly from the **Yostar Servers**.

## Requirements

- Python 3.10+
- requests
- request-cache
- aiohttp
- xxhash
- pycryptodome
- UnityPy
- flatbuffers
- .Net Runtime 6.0 (Linux) | .Net Desktop Runtime 8.0 (Windows)

## ~~Installation~~ (WIP)
~~Download and install [`python`](https://www.python.org/downloads/). After that clone this repository~~

```
git clone https://github.com/Deathemonic/BA-AD.git
```

~~or just download as a zip by clicking `Code` > `Download Zip`. Then open `BA-AD` folder in your `Terminal` or `CMD`~~

~~Then install it using pip~~

```
pip install .
```

## Usage
Before you go downloading the game assets please read [Nexon's Terms and Service](https://m.nexon.com/terms/304) first. You are not allowed to sell the game files, models or use them for commercial purposes.

```
> baad --help
usage: baad [-h] [-v] [-u] [-g] {download,extract} ...

Blue Archive Asset Downloader

positional arguments:
  {download,extract}
    download          download game files
    extract           extract game files

options:
  -h, --help          show this help message and exit
  -v, --version       show program's version number and exit
  -u, --update        force update the apk
  -g, --generate      generate the flatbuf schema
```

#### Downloading

To download the assetsbundles, tablebundles, and media resources we need to initialize download mode, to do that we pass `download` so it will be like this `baad download`.

- `--assets` will download just the assetbundles only.
- `--tables` will download just the tablebundles only.
- `--media` will download just the media resources only.
- `--all` will download everything.
- `--limit` is the number of files will download concurrently (default is 5).
- `--output` is the path to save the downloaded files (default is `./output`).

Examples:

- Saves the files using Posix Path style
```
> baad download --tables --output ./Downloads
```

- Limit the concurrent download to 10 files
```
> baad download --assets --limit 10
```

- Saves the files using Windows Path style
```
> baad download --media --output C:\Users\User\ocuments
```

> [!NOTE]
> If you have low connection and download say error, rerun the program again it will retry downloading the remaining files. Don't worry it will not download the already downloaded files again

#### Extracting (WIP)

~~To extract the assetsbundles, and  tablebundles we need to initialize extract mode, to do that we pass `extract` so it will be like this `baad extract`.~~



### Dump
To get `dump.cs` you need to manually decompile the `libil2cpp.so`. I recommend following the instructions from [Auto-Il2cppDumper](https://github.com/AndnixSH/Auto-Il2cppDumper) or [Zygisk-Il2CppDumper](https://github.com/Perfare/Zygisk-Il2CppDumper). Also I recommend using a emulator like **MuMuPlayer** to get easy root access.

But you your lazy you can use [Il2CppDumper](Il2CppDumper) to dump it manually or automatically using a script. You gonna need the **Blue Archive JP** apk from **Qooapp**, then rename .apk to .zip and extract it. `libil2cpp.so` is located at `lib/arm64-v8a` and the `global-metadata.dat` is located at `assets/bin/Data/Managed/Metadata`.
Note that you will face a [ERROR: Can't use auto mode to process file, try manual mode](https://github.com/Perfare/Il2CppDumper?tab=readme-ov-file#error-cant-use-auto-mode-to-process-file-try-manual-mode) by doing this method.

### Acknowledgement
 - [hdk5/MoeXCOM](https://github.com/hdk5/MoeXCOM)
 - [espectZ/blue-archive-viewer](https://github.com/respectZ/blue-archive-viewer)
 - [fiseleo/Blue-Archive-JP-Downloader](https://github.com/fiseleo/Blue-Archive-JP-Downloader)
 - [K0lb3/Blue-Archive---Asset-Downloader](https://github.com/K0lb3/Blue-Archive---Asset-Downloader)
 - [lwd-temp/blue-archive-spine-production](https://github.com/lwd-temp/blue-archive-spine-production)


### Copyright
**Blue Archive** is a registered trademark of NAT GAMES Co., Ltd. and Yostar Co., Ltd. This repository is not affiliated with NEXON Korea Corp., NEXON GAMES Co., Ltd., and Yostar Co., Ltd. All game resources are copyrighted to their respective owners.
