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
- flatbuffers

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

```sh
> baad --help

Blue Archive Asset Downloader

positional arguments:
  {download,extract}
    download          download game files
    extract           extract game files

options:
  -h, --help          show this help message and exit
  -u, --update        force update the apk
  -g, --generate      generate the flatbuf schemas
```

### Dump
To get `dump.cs` you need to manually decompile the `libil2cpp.so`. I recommend following the instructions from [Auto-Il2cppDumper](https://github.com/AndnixSH/Auto-Il2cppDumper) or [Zygisk-Il2CppDumper](https://github.com/Perfare/Zygisk-Il2CppDumper). 

But you your lazy you can use [Il2CppDumper](Il2CppDumper) to dump it manually or automatically using a script. You gonna need the **Blue Archive JP** apk from **Qooapp**, then rename .apk to .zip and extract it. `libil2cpp.so` is located at `lib\arm64-v8a` and the `global-metadata.dat` is located at `assets\bin\Data\Managed\Metadata`.
Note that you will face a [ERROR: Can't use auto mode to process file, try manual mode.](https://github.com/Perfare/Il2CppDumper?tab=readme-ov-file#error-cant-use-auto-mode-to-process-file-try-manual-mode) by doing this method.

### Acknowledgement
 - [hdk5/MoeXCOM](https://github.com/hdk5/MoeXCOM)
 - [espectZ/blue-archive-viewer](https://github.com/respectZ/blue-archive-viewer)
 - [fiseleo/Blue-Archive-JP-Downloader](https://github.com/fiseleo/Blue-Archive-JP-Downloader)
 - [K0lb3/Blue-Archive---Asset-Downloader](https://github.com/K0lb3/Blue-Archive---Asset-Downloader)
 - [lwd-temp/blue-archive-spine-production](https://github.com/lwd-temp/blue-archive-spine-production)


### Copyright
**Blue Archive** is a registered trademark of NAT GAMES Co., Ltd. and Yostar Co., Ltd. This repository is not affiliated with NEXON Korea Corp., NEXON GAMES Co., Ltd., and Yostar Co., Ltd. All game resources are copyrighted to their respective owners.
