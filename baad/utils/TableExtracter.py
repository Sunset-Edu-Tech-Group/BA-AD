import json
from pathlib import Path

from rich.console import Console

from .. import FlatData
from ..FlatData.dump import dump_table
from ..lib.StringCipher import decrypt
from ..lib.TableEncryptionService import TableEncryptionService
from ..lib.TableService import TableZipFile
from .Progress import create_live_display, create_progress_group


class TableExtracter:
    def __init__(self, output: str) -> None:
        self.table_path = output or Path.cwd() / 'output' / 'TableBundles'
        self.lower_name_to_module_dict = self._get_lower_name_to_module_dict()
        self.console = Console()
        self.live = create_live_display()
        self.progress_group, self.download_progress, self.extract_progress = create_progress_group()

    @staticmethod
    def _get_lower_name_to_module_dict() -> dict:
        return {key.lower(): value for key, value in FlatData.__dict__.items()}

    @staticmethod
    def _process_json_file(name: str, data: bytes) -> bytes:
        if name == 'logiceffectdata.json':
            return decrypt(data, 'LogicEffectData').encode('utf-8')

        elif name == 'newskilldata.json':
            return decrypt(data, 'NewSkillData').encode('utf-8')
        return data

    def _process_excel_file(self, name: str, data: bytes) -> tuple:
        flatbuffer_cls = self.lower_name_to_module_dict[name[:-6]]
        data = TableEncryptionService().xor(flatbuffer_cls.__name__, data)
        flatbuffer = flatbuffer_cls.GetRootAs(data)

        processed_data = json.dumps(dump_table(flatbuffer), indent=4, ensure_ascii=False).encode('utf-8')
        new_name = f'{flatbuffer_cls.__name__}.json'

        return processed_data, new_name

    def extract_table(self, table_file: Path) -> None:
        table_dir_fp = self.table_path / table_file.stem
        table_dir_fp.mkdir(exist_ok=True)

        with TableZipFile(table_file) as tz:
            extract_task = self.extract_progress.add_task(
                f'[green]Extracting {table_file.name}', total=len(tz.namelist())
            )

            for name in tz.namelist():
                self.console.print(f'[cyan]Extracted {name}.[/cyan]')
                data = tz.read(name)

                try:
                    if name.endswith('.json'):
                        data = self._process_json_file(name, data)

                    elif table_file.name == 'Excel.zip':
                        data, name = self._process_excel_file(name, data)

                except Exception as e:
                    self.console.print(f'[red]Error processing {name}: {e}[/red]')
                    continue

                fp = table_dir_fp / name
                fp.write_bytes(data)
                self.extract_progress.update(extract_task, advance=1)
                self.live.update(self.progress_group)

    def extract_all_tables(self) -> None:
        table_files = list(self.table_path.glob('*.zip'))
        extract_all_task = self.extract_progress.add_task('[cyan]Extracting all tables...', total=len(table_files))

        try:
            with self.live:
                for table_file in table_files:
                    self.extract_table(table_file)
                    self.extract_progress.update(extract_all_task, advance=1)
                    self.live.update(self.progress_group)

        finally:
            if self.live:
                self.live.stop()
