import asyncio
import json
from pathlib import Path
from zipfile import BadZipFile

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
        self.live = create_live_display()
        self.progress_group, _, self.extract_progress, self.print_progress, self.console = create_progress_group()

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

    async def extract_table(self, table_file: Path | str, task: int) -> None:
        try:
            with TableZipFile(table_file) as tz:
                file_list = tz.namelist()
                create_dir = len(file_list) > 1

                if create_dir:
                    table_dir_fp = self.extracted_path / table_file.stem
                    table_dir_fp.mkdir(parents=True, exist_ok=True)

                for name in tz.namelist():
                    data = tz.read(name)

                    try:
                        if name.endswith('.json'):
                            data = await asyncio.to_thread(self._process_json_file, name, data)

                        elif table_file.name == 'Excel.zip':
                            data, name = await asyncio.to_thread(self._process_excel_file, name, data)

                    except Exception as e:
                        self.print_progress.add_task(f'[yellow]Warning processing {name}: {e}[/yellow]')
                        continue

                    fp = table_dir_fp / name if create_dir else self.extracted_path / name
                    fp.parent.mkdir(parents=True, exist_ok=True)
                    fp.write_bytes(data)

                    await asyncio.to_thread(fp.write_bytes, data)

                    self.extract_progress.update(task, advance=1)
                    self.live.update(self.progress_group)

        except BadZipFile:
            self.console.log(f'[red]Error: {table_file} is not a valid zip file.[/red]')

    async def extract_all_tables(self) -> None:
        table_files = list(Path(self.table_path).glob('*.zip'))
        extract_task = self.extract_progress.add_task('[green]Extracting...', total=len(table_files))

        try:
            with self.live:
                task = [self.extract_table(table_file, extract_task) for table_file in table_files]
                await asyncio.gather(*task)
                self.print_progress.add_task('[green]Extraction completed![/green]')

        finally:
            self.live.stop()
