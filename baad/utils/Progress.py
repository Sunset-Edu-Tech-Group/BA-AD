from rich.progress import (
    BarColumn,
    DownloadColumn,
    Progress,
    TextColumn,
    TimeRemainingColumn,
    TransferSpeedColumn,
)


def create_progress_bar():
    return Progress(
        TextColumn('[progress.description]{task.description}'),
        BarColumn(),
        DownloadColumn(),
        TransferSpeedColumn(),
        TextColumn('[progress.percentage]{task.percentage:>3.0f}%'),
        TimeRemainingColumn(),
    )


def create_download_progress_bar():
    return Progress(
        TextColumn('[progress.description]{task.description}'),
        BarColumn(),
        DownloadColumn(),
        TransferSpeedColumn(),
        TextColumn('[progress.percentage]{task.percentage:>3.0f}%'),
        TimeRemainingColumn(),
        expand=True,
    )
