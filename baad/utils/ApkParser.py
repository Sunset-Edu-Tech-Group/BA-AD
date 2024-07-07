from pathlib import Path
from zipfile import ZipFile

import requests
from Progress import create_progress_bar
from rich.console import Console


class ApkParser:
    def __init__(
        self, apk_url: str | None = None, file_path: Path | None = None
    ) -> None:
        self.apk_url = (
            apk_url
            or 'https://api.qoo-app.com/v6/apps/com.YostarJP.BlueArchive/download'
        )
        self.root = Path(__file__).parent.parent
        self.file_path = file_path or self.root / 'public'
        self.apk_path = self.file_path / 'BlueArchive.apk'
        self.console = Console()

    def compare_apk(self, update: bool = False) -> bool:
        response = requests.get(self.apk_url, stream=True)
        remote_size = int(response.headers.get('content-length', 0))
        local_size = self.apk_path.stat().st_size if self.apk_path.exists() else 0

        if update or local_size < remote_size:
            return True

        if local_size == remote_size:
            self.console.print(
                '[green]Local APK is up to date. Skipping download.[/green]'
            )
        elif local_size > remote_size:
            self.console.print(
                '[yellow]Local APK is larger than remote APK. Skipping download.[/yellow]'
            )
        return False

    def download_apk(self, update: bool = False) -> None:
        if not self.compare_apk(update):
            return

        with create_progress_bar() as progress:
            response = requests.get(self.apk_url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            task = progress.add_task('[cyan]Downloading APK...', total=total_size)

            with open(self.apk_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        progress.update(task, advance=len(chunk))

        self.console.print('[green]APK downloaded.[/green]')
        self.extract_apk()

    def extract_apk(self) -> None:
        with ZipFile(self.apk_path, 'r') as zip_ref:
            files_to_extract = [
                file_info
                for file_info in zip_ref.infolist()
                if file_info.filename.startswith('assets/bin/Data/')
            ]

            with create_progress_bar() as progress:
                task = progress.add_task(
                    '[cyan]Extracting APK...', total=len(files_to_extract)
                )

                for file_info in files_to_extract:
                    target_path = self.file_path / 'data' / Path(file_info.filename)
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    zip_ref.extract(file_info, self.file_path / 'data')
                    progress.update(task, advance=1)

                self.console.print('[green]APK extracted.[/green]')
