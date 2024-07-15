import json
from itertools import chain
from pathlib import Path
from typing import Generator
from zipfile import BadZipFile

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
        self.extracted_path = Path(self.table_path).parent / 'TableExtracted'
        self.lower_name_to_module_dict = self._get_lower_name_to_module_dict()
        self.console = Console()
        self.live = create_live_display()
        self.progress_group, _, self.extract_progress = create_progress_group()

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

    def _process_file(self, name: str, data: bytes, table_file: Path | str) -> tuple:
        if name.endswith('.json'):
            return self._process_json_file(name, data), name

        elif table_file.name == 'Excel.zip':
            return self._process_excel_file(name, data)
        return data, name

    def _process_zip(self, table_file: str | Path) -> Generator | None:
        try:
            with TableZipFile(table_file) as tz:
                contents = [(name, tz.read(name)) for name in tz.namelist()]
            return ((table_file, name, data) for name, data in contents)

        except BadZipFile:
            self.console.print(f'[red]Error: {table_file} is not a valid zip file.[/red]')
            return

    def extract_tables(self) -> Generator:
        table_files = list(Path(self.table_path).glob('*.zip'))
        total_files = sum(len(TableZipFile(tf).namelist()) for tf in table_files)
        extract_task = self.extract_progress.add_task('[green]Extracting...', total=total_files)

        for table_file, name, data in chain.from_iterable(map(self._process_zip, table_files)):
            if name is None:
                yield f'Error: {table_file} is not a valid zip file.'
                continue

            table_dir_fp = self.extracted_path / table_file.stem
            table_dir_fp.mkdir(parents=True, exist_ok=True)

            try:
                processed_data, new_name = self._process_file(name, data, table_file)
                fp = table_dir_fp / new_name
                fp.write_bytes(processed_data)

            except Exception as e:
                yield f'Error processing {name}: {e}'

            finally:
                self.extract_progress.update(extract_task, advance=1)
                self.live.update(self.progress_group)

    def extract_all_tables(self) -> None:
        try:
            with self.live:
                errors = list(self.extract_tables())

                for error in errors:
                    self.console.print(error)

        finally:
            if self.live:
                self.live.stop()
