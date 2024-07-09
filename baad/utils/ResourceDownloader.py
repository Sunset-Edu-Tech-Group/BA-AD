import asyncio
from pathlib import Path

import aiohttp
from rich.console import Console

from .CatalogParser import CatalogParser


class ResourceDownloader:
    def __init__(self, output: None | str = None, update: bool = False) -> None:
        self.root = Path(__file__).parent.parent
        self.output = Path(output) or self.root.parent / 'output'
        self.update = update

        self.semaphore = None
        self.console = Console()
        self.categories = {
            'asset': 'AssetBundles',
            'table': 'TableBundles',
            'media': 'MediaResources',
        }

    async def _download_file(self, session: aiohttp.ClientSession, url: str, file_path: Path) -> None:
        async with self.semaphore:
            try:
                async with session.get(url) as response:
                    if response.status != 200:
                        self.console.print(f'[red]Failed to download {url}[/red]')
                        return

                    file_path.parent.mkdir(parents=True, exist_ok=True)

                    # total_size = int(response.headers.get('content-length', 0))
                    # task_id = progress.add_task(f'[cyan]Downloading {file_path.name}[/cyan]', total=total_size)

                    with open(file_path, 'wb') as f:
                        async for chunk in response.content.iter_chunked(8192):
                            size = f.write(chunk)

                            # progress.update(task_id, advance=size)
                    # progress.remove_task(task_id)

            except (ConnectionError, TimeoutError) as e:
                self.console.print('[bold red]Error: Download failed.[/bold red]')
                raise SystemExit(1) from e

    async def _download_category(self, files: list, base_path: Path) -> None:
        async with aiohttp.ClientSession() as session:
            tasks = {
                self._download_file(
                    session,
                    file['url'],
                    base_path / (file['path'] or Path(file['url']).name),
                )
                for file in files
            }

            await asyncio.gather(*tasks)

    async def _download_all_categories(self, game_files: dict, categories: list) -> None:
        for category, files in game_files.items():
            if category in categories:
                await self._download_category(files, Path(self.output) / category)

    def _initialize_download(self) -> dict:
        catalog_parser = CatalogParser()
        catalog_parser.fetch_catalogs()

        # save_task = self.progress.add_task('[cyan]Saving game files...', total=100)

        result = catalog_parser.get_game_files()
        catalog_parser.save_json(self.root / 'public' / 'GameFiles.json', result)

        # self.progress.update(save_task, completed=100, description='[green]Game files saved!')

        return result

    def download(self, assets: bool = True, tables: bool = True, media: bool = True, limit: int | None = None) -> None:
        game_files = self._initialize_download()

        categories = [
            self.categories[cat] for cat, enabled in [('asset', assets), ('table', tables), ('media', media)] if enabled
        ]

        self.console.print(f'[cyan]Downloading files for categories: {", ".join(categories)}[/cyan]')
        self.semaphore = asyncio.Semaphore(limit if limit is not None else float('inf'))

        asyncio.run(self._download_all_categories(game_files, categories))

        self.console.print('[green]All specified files downloaded![/green]')
