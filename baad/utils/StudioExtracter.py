import subprocess
from pathlib import Path

from .Progress import create_live_display, create_progress_group


# WIP
class AssetStudioExtracter:
    def __init__(self, input_path: Path, output_path: Path = None, asset_studio_path: Path = None) -> None:
        self.input_path = input_path
        self.output_path = output_path or Path.cwd() / 'output' / 'AssetExtracted'
        self.asset_studio_path = asset_studio_path or Path.cwd() / 'AssetStudioModCLI'

        self.live = create_live_display()
        self.progress_group, _, self.extract_progress, self.print_progress, self.console = create_progress_group()

    def _run_asset_studio_command(self, command: list) -> subprocess.CompletedProcess:
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return result
        except subprocess.CalledProcessError as e:
            self.console.log(f'[red]Error running AssetStudio: {e}[/red]')
            self.console.log(f'[red]Error output: {e.stderr}[/red]')
            raise

    def extract_assets(
        self, asset_types: list = None, group_option: str = 'container', filename_format: str = 'assetName'
    ) -> None:
        command = [
            str(self.asset_studio_path),
            str(self.input_path),
            '-o',
            str(self.output_path),
            '-g',
            group_option,
            '-f',
            filename_format,
        ]

        if asset_types:
            command.extend(['-t', ','.join(asset_types)])

        try:
            with self.live:
                self.console.log('[cyan]Starting asset extraction...[/cyan]')
                extract_task = self.extract_progress.add_task('[green]Extracting assets...', total=100)

                result = self._run_asset_studio_command(command)

                # Parse the output to update progress
                for line in result.stdout.splitlines():
                    if 'Exporting asset' in line:
                        self.extract_progress.update(extract_task, advance=1)
                        self.live.update(self.progress_group)

                self.extract_progress.update(extract_task, completed=100)
                self.print_progress.add_task('[green]Asset extraction completed![/green]')

        finally:
            self.live.stop()

    def get_asset_info(self) -> None:
        command = [str(self.asset_studio_path), str(self.input_path), '-m', 'info']

        try:
            with self.live:
                self.console.log('[cyan]Fetching asset information...[/cyan]')
                result = self._run_asset_studio_command(command)
                self.console.log(result.stdout)
                self.print_progress.add_task('[green]Asset information fetched![/green]')
        finally:
            self.live.stop()

    def extract_live2d(self) -> None:
        command = [str(self.asset_studio_path), str(self.input_path), '-m', 'live2d', '-o', str(self.output_path)]

        try:
            with self.live:
                self.console.log('[cyan]Extracting Live2D assets...[/cyan]')
                extract_task = self.extract_progress.add_task('[green]Extracting Live2D...', total=100)

                result = self._run_asset_studio_command(command)

                # Parse the output to update progress
                for line in result.stdout.splitlines():
                    if 'Exporting' in line:
                        self.extract_progress.update(extract_task, advance=10)
                        self.live.update(self.progress_group)

                self.extract_progress.update(extract_task, completed=100)
                self.print_progress.add_task('[green]Live2D extraction completed![/green]')
        finally:
            self.live.stop()
