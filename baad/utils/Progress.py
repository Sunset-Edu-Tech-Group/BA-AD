from rich.progress import Progress, TaskID


class ProgressManager:
    def __init__(self) -> None:
        self.progress = Progress()
        self.tasks = {}

    def start(self) -> None:
        self.progress.start()

    def stop(self) -> None:
        self.progress.stop()

    def add_task(self, description: str, total: float = 100) -> TaskID:
        return self.progress.add_task(description, total=total)

    def update(self, task_id: TaskID, advance: float = None, completed: float = None, description: str = None) -> None:
        self.progress.update(task_id, advance=advance, completed=completed, description=description)

    def remove_task(self, task_id: TaskID) -> None:
        self.progress.remove_task(task_id)

    def add_download_task(self, filename: str, total_size: int) -> TaskID:
        return self.progress.add_task(f'Downloading {filename}', total=total_size, unit='B', unit_scale=True)


def progress_manager():
    return ProgressManager()
