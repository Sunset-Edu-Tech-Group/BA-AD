from pathlib import Path
from zipfile import ZipFile

import requests
from rich.console import Console


class ApkParser:
    def __init__(self, apk_url: str, apk_path: str) -> None:
        self.apk_url = apk_url or 'https://api.qoo-app.com/v6/apps/com.YostarJP.BlueArchive/download'

        self.root = Path(__file__).parent.parent
        self.apk_path = Path(apk_path) or self.root / 'public' / 'BlueArchive.apk'

        self.console = Console()

    @staticmethod
    def _get_files(zip: ZipFile) -> set:
        return {file_info for file_info in zip.infolist() if file_info.filename.startswith('assets/bin/Data/')}

    def _get_response(self) -> requests.Response | SystemExit:
        try:
            return requests.get(self.apk_url, stream=True)

        except (ConnectionError, TimeoutError, requests.exceptions.RequestException) as e:
            self.console.print(f'[bold red]Error: {str(e)}[/bold red]')
            raise SystemExit(1) from e

    def _download_file(self, response: requests.Response) -> None:
        # total_size = int(response.headers.get('content-length', 0))
        # task = self.progress.add_task('[cyan]Downloading APK...', total=total_size)

        with open(self.apk_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

                    # self.progress.update(task, advance=len(chunk))
        self.console.print('[green]APK downloaded.[/green]')

    def _force_download(self) -> None:
        response = self._get_response()
        if response is None:
            return

        self._download_file(response)

    def _fetch_size(self) -> int:
        try:
            response = requests.get(self.apk_url, stream=True)
            return int(response.headers.get('content-length', 0))

        except (
            ConnectionError,
            TimeoutError,
            requests.exceptions.RequestException,
        ) as e:
            self.console.print(f'[bold red]Error: {str(e)}[/bold red]')
            raise SystemExit(1) from e

    def _log_size(self, local: int, remote: int) -> None:
        if local == remote:
            self.console.print('[green]Local APK is up to date. Skipping download.[/green]')
        elif local > remote:
            self.console.print('[yellow]Local APK is larger than remote APK. Skipping download.[/yellow]')

    def _extract_files(self, zip: ZipFile, extract: set) -> None:
        # task = self.progress.add_task('[cyan]Extracting APK...', total=len(extract))

        for file_info in extract:
            target_path = self.apk_path.parent / 'data' / Path(file_info.filename)
            target_path.parent.mkdir(parents=True, exist_ok=True)
            zip.extract(file_info, self.apk_path.parent / 'data')

            # self.progress.update(task, advance=1)
        self.console.print('[green]APK extracted.[/green]')

    def compare_apk(self) -> bool:
        remote_size = self._fetch_size()
        if remote_size is None:
            return False

        local_size = self.apk_path.stat().st_size
        if local_size < remote_size:
            return True

        self._log_size(local_size, remote_size)
        return False

    def download_apk(self, update: bool = False) -> None:
        if update or not self.apk_path.exists():
            self._force_download()
            self.extract_apk()
            return

        if self.compare_apk():
            self._force_download()
        self.extract_apk()

    def extract_apk(self):
        with ZipFile(self.apk_path, 'r') as zip:
            extract = self._get_files(zip)
            self._extract_files(zip, extract)
