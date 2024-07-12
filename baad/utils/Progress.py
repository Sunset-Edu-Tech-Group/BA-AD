from rich.console import Group
from rich.live import Live
from rich.progress import BarColumn, DownloadColumn, Progress, TextColumn, TimeRemainingColumn, TransferSpeedColumn


def create_progress_group() -> tuple:
    download_progress = Progress(
        TextColumn('[bold blue]{task.description}', justify='right'),
        BarColumn(bar_width=None),
        '[progress.percentage]{task.percentage:>3.1f}%',
        '•',
        DownloadColumn(),
        '•',
        TransferSpeedColumn(),
        '•',
        TimeRemainingColumn(),
        expand=True,
    )

    extract_progress = Progress(
        TextColumn('[bold green]{task.description}', justify='right'),
        BarColumn(bar_width=None),
        '[progress.percentage]{task.percentage:>3.1f}%',
        '•',
        TimeRemainingColumn(),
        expand=True,
    )

    progress_group = Group(download_progress, extract_progress)

    return progress_group, download_progress, extract_progress


def create_live_display() -> Live:
    return Live(create_progress_group()[0], refresh_per_second=10)
