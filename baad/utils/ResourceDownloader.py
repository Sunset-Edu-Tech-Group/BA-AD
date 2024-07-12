import asyncio
from pathlib import Path

import aiohttp
from rich.console import Console

from .ApkParser import ApkParser
from .CatalogParser import CatalogParser
from .Progress import create_live_display, create_progress_group


class ResourceDownloader:
    def __init__(self, update: bool = False, output: str | None = None) -> None:
        self.root = Path(__file__).parent.parent
        self.output = output or Path.cwd() / 'output'
        self.update = update

        self.semaphore = None
        self.console = Console()
        self.catalog_parser = CatalogParser()
        self.categories = {
            'asset': 'AssetBundles',
            'table': 'TableBundles',
            'media': 'MediaResources',
        }
        self.live = create_live_display()
        self.progress_group, self.download_progress, self.extract_progress = create_progress_group()

    @staticmethod
    def _get_file_path(file: dict) -> str | Path:
        if 'path' in file:
            return file['path']

        elif isinstance(file['url'], str):
            return Path(file['url']).name

        return Path(file['url'])

    async def _download_file(self, session: aiohttp.ClientSession, url: str, file_path: Path) -> None:
        async with self.semaphore:
            try:
                async with session.get(url) as response:
                    if response.status != 200:
                        self.console.print(f'[red]Failed to download {url}[/red]')
                        return

                    file_path.parent.mkdir(parents=True, exist_ok=True)
                    total_size = int(response.headers.get('content-length', 0))
                    download_task = self.download_progress.add_task(f'[cyan]{file_path.name}', total=total_size)

                    with self.live:
                        with open(file_path, 'wb') as f:
                            async for chunk in response.content.iter_chunked(8192):
                                f.write(chunk)
                                self.download_progress.update(download_task, advance=len(chunk))
                                self.live.update(self.progress_group)

                        self.download_progress.update(download_task, completed=total_size)
                        self.live.update(self.progress_group)

            except (ConnectionError, TimeoutError) as e:
                self.console.print(f'[bold red]Error: Download failed. {str(e)}[/bold red]')

    async def _download_category(self, files: list, base_path: Path) -> None:
        async with aiohttp.ClientSession() as session:
            tasks = [
                self._download_file(
                    session,
                    file['url'],
                    base_path / self._get_file_path(file),
                )
                for file in files
            ]

            await asyncio.gather(*tasks)

    async def _download_all_categories(self, game_files: dict, categories: list) -> None:
        for category, files in game_files.items():
            if category in categories:
                await self._download_category(files, Path(self.output) / category)

    def _initialize_download(self) -> dict:
        self.fetch_catalog_url()
        self.catalog_parser.fetch_catalogs()

        result = self.catalog_parser.get_game_files()
        self.catalog_parser.save_json(self.root / 'public' / 'GameFiles.json', result)

        return result

    def download(self, assets: bool = True, tables: bool = True, media: bool = True, limit: int | None = 5) -> None:
        try:
            game_files = self._initialize_download()

            categories = [
                self.categories[cat]
                for cat, enabled in [('asset', assets), ('table', tables), ('media', media)]
                if enabled
            ]

            self.semaphore = asyncio.Semaphore(limit if limit is not None else float('inf'))
            asyncio.run(self._download_all_categories(game_files, categories))

        finally:
            if self.live:
                self.live.stop()

    def fetch_catalog_url(self) -> None:
        ApkParser().download_apk(self.update)

        self.console.print('[cyan]Fetching catalog URL...[/cyan]')
        catalog_url = self.catalog_parser.fetch_catalog_url()
        self.console.print(f'[green]Catalog URL fetched: {catalog_url}[/green]')
