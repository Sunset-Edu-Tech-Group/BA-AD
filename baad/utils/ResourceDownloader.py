import asyncio
import binascii
import json
from pathlib import Path
from typing import Dict, List, Optional

import aiohttp
from CatalogFetcher import catalog_url
from lib.MediaParser import MediaCatalog
from lib.TableParser import TableCatalog
from requests_cache import CachedSession
from rich.console import Console
from utils.Progress import create_download_progress_bar, create_progress_bar


class ResourceDownloader:
    def __init__(
        self,
        version: Optional[str] = None,
        output: Optional[str] = None,
        update: bool = False,
    ) -> None:
        self.version: Optional[str] = version
        self.root_path: Path = Path(__file__).parent.parent
        self.output: Path = (
            Path(output) if output else self.root_path / 'public' / 'data' / 'output'
        )
        self.semaphore: Optional[asyncio.Semaphore] = None
        self.console = Console()
        self.update = update
        self.categories = {
            'asset': 'AssetBundles',
            'table': 'TableBundles',
            'media': 'MediaResources',
        }

    def calculate_crc32(self, file_path: Path) -> int:
        with open(file_path, 'rb') as f:
            return binascii.crc32(f.read()) & 0xFFFFFFFF

    def fetch_version(self) -> str:
        if self.version:
            return self.version

        with CachedSession(cache_name='serverindex', use_temp=True) as session:
            server_index = (
                'https://prod-noticeindex.bluearchiveyostar.com/prod/index.json'
            )
            server_data = session.get(server_index).json()
            return server_data['LatestClientVersion']

    def fetch_catalogurl(self) -> str:
        with CachedSession(cache_name='serverapi', use_temp=True) as session:
            server_api = catalog_url(self.update)
            server_data = session.get(server_api).json()
            return server_data['ConnectionGroups'][0]['OverrideConnectionGroups'][-1][
                'AddressablesCatalogUrlRoot'
            ]

    def fetch_bytes(self, catalog: str, file: str, cache: str) -> bytes:
        with CachedSession(cache, use_temp=True) as session:
            return session.get(f'{catalog}{file}').content

    def fetch_tablebytes(self, catalog: str) -> bytes:
        return self.fetch_bytes(
            catalog, '/TableBundles/TableCatalog.bytes', 'tablebytes'
        )

    def fetch_mediabytes(self, catalog: str) -> bytes:
        return self.fetch_bytes(
            catalog, '/MediaResources/MediaCatalog.bytes', 'mediabytes'
        )

    def fetch_catalogs(self, progress, task) -> None:
        catalog_url = self.fetch_catalogurl()
        progress.update(task, completed=20, description='[cyan]Fetching catalog URL')

        with CachedSession(cache_name='catalogurl', use_temp=True) as session:
            bundle_data = session.get(
                f'{catalog_url}/Android/bundleDownloadInfo.json'
            ).json()
        progress.update(task, completed=40, description='[cyan]Fetching bundle data')

        self.save_json(
            self.root_path / 'public' / 'bundleDownloadInfo.json', bundle_data
        )

        table_data = self.fetch_tablebytes(catalog=catalog_url)
        table_catalog = TableCatalog.from_bytes(table_data, catalog_url)
        table_catalog.to_json(self.root_path / 'public' / 'TableCatalog.json')
        progress.update(task, completed=60, description='[cyan]Fetching table data')

        media_data = self.fetch_mediabytes(catalog=catalog_url)
        media_catalog = MediaCatalog.from_bytes(media_data, catalog_url)
        media_catalog.to_json(self.root_path / 'public' / 'MediaCatalog.json')
        progress.update(task, completed=80, description='[cyan]Fetching media data')

    def get_gamefiles(self) -> Dict[str, List[Dict[str, str]]]:
        catalog_url = self.fetch_catalogurl()

        bundle_data = self.load_json(
            self.root_path / 'public' / 'bundleDownloadInfo.json'
        )
        table_data = self.load_json(self.root_path / 'public' / 'TableCatalog.json')
        media_data = self.load_json(self.root_path / 'public' / 'MediaCatalog.json')

        return {
            'AssetBundles': [
                {
                    'url': f'{catalog_url}/Android/{asset["Name"]}',
                    'crc': asset.get('Crc', 0),
                }
                for asset in bundle_data['BundleFiles']
            ],
            'TableBundles': [
                {'url': f'{catalog_url}/TableBundles/{key}', 'crc': asset.get('crc', 0)}
                for key, asset in table_data['Table'].items()
            ],
            'MediaResources': [
                {
                    'url': f'{catalog_url}/MediaResources/{value["path"]}',
                    'path': value['path'],
                    'crc': value.get('crc', 0),
                }
                for key, value in media_data['Table'].items()
            ],
        }

    def save_json(self, file_path: Path, data: Dict) -> None:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def load_json(self, file_path: Path) -> Dict:
        with open(file_path, 'r') as f:
            return json.load(f)

    async def download_file(
        self, session: aiohttp.ClientSession, url: str, file_path: Path, progress
    ) -> None:
        async with self.semaphore:
            async with session.get(url) as response:
                if response.status != 200:
                    self.console.print(f'[red]Failed to download {url}[/red]')
                    return

                file_path.parent.mkdir(parents=True, exist_ok=True)
                total_size = int(response.headers.get('content-length', 0))

                task_id = progress.add_task(
                    f'[cyan]Downloading {file_path.name}[/cyan]', total=total_size
                )
                with open(file_path, 'wb') as f:
                    async for chunk in response.content.iter_chunked(8192):
                        size = f.write(chunk)
                        progress.update(task_id, advance=size)
                progress.remove_task(task_id)

    async def download_category(
        self, files: List[Dict[str, str]], base_path: Path, progress
    ) -> None:
        async with aiohttp.ClientSession() as session:
            tasks = [
                self.download_file(
                    session,
                    file['url'],
                    base_path / (file.get('path') or Path(file['url']).name),
                    progress,
                )
                for file in files
            ]
            await asyncio.gather(*tasks)

    async def download_all_categories(
        self,
        game_files: Dict[str, List[Dict[str, str]]],
        categories_to_download: List[str],
    ) -> None:
        progress = create_download_progress_bar()
        with progress:
            for category, files in game_files.items():
                if category in categories_to_download:
                    await self.download_category(
                        files, Path(self.output) / category, progress
                    )

    def initialize_download(self, progress) -> Dict[str, List[Dict[str, str]]]:
        fetch_task = progress.add_task('[cyan]Fetching catalogs...', total=100)
        self.fetch_catalogs(progress, fetch_task)
        progress.update(
            fetch_task, completed=100, description='[green]Catalogs fetched!'
        )

        save_task = progress.add_task('[cyan]Saving game files...', total=100)
        result = self.get_gamefiles()
        self.save_json(self.root_path / 'public' / 'GameFiles.json', result)
        progress.update(
            save_task, completed=100, description='[green]Game files saved!'
        )

        progress.update(fetch_task, visible=False)
        progress.update(save_task, visible=False)

        return result

    def download(
        self,
        asset: bool = True,
        table: bool = True,
        media: bool = True,
        limit: Optional[int] = None,
    ) -> None:
        with create_progress_bar() as progress:
            game_files = self.initialize_download(progress)

        categories_to_download = [
            self.categories[cat]
            for cat, enabled in [('asset', asset), ('table', table), ('media', media)]
            if enabled
        ]

        self.console.print(
            f'[cyan]Downloading files for categories: {", ".join(categories_to_download)}[/cyan]'
        )
        self.semaphore = asyncio.Semaphore(limit if limit is not None else float('inf'))
        asyncio.run(self.download_all_categories(game_files, categories_to_download))
        self.console.print('[green]All specified files downloaded![/green]')
