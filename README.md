# Blue Archive - Asset Downloader (WIP)

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

### Copyright
**Blue Archive** is a registered trademark of NAT GAMES Co., Ltd. and Yostar Co., Ltd. This repository is not affiliated with NEXON Korea Corp., NEXON GAMES Co., Ltd., and Yostar Co., Ltd. All game resources are copyrighted to their respective owners.