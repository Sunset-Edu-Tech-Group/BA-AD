import platform
import re
import subprocess
from pathlib import Path

from rich.console import Console


class FlatbufGenerator:
    def __init__(self) -> None:
        self.root = Path(__file__).parent.parent
        self.console = Console()

        flatc_types = {
            'Windows': 'flatc_win.exe',
            'Linux': 'flatc_linux',
            'macOS': 'flatc_mac',
        }

        system = platform.system()
        flatc_type = flatc_types[system]

        if not flatc_type:
            self.console.print(f'[red]Unsupported system: {system}[/red]')
            raise SystemExit(1)

        self.flatc_path = self.root / 'lib' / 'flatbuf' / flatc_type

        self.types = {'bool', 'byte', 'int', 'long', 'uint', 'ulong', 'float', 'double', 'string'}
        self.type_converters = {
            'string': 'table_encryption.convert_string',
            'int': 'table_encryption.convert_int',
            'long': 'table_encryption.convert_long',
            'uint': 'table_encryption.convert_uint',
            'ulong': 'table_encryption.convert_ulong',
            'float': 'table_encryption.convert_float',
            'double': 'table_encryption.convert_double',
        }

        self.reEnum = re.compile(
            r"""// Namespace: FlatData
public enum (.{1,128}?) // TypeDefIndex: \d+?
{
	// Fields
	public (.+?) value__; // 0x0
(.+?)
}""",
            re.M | re.S,
        )
        self.reEnumField = re.compile(r'public const (.+?) (.+?) = (-?\d+?);')
        self.reStruct = re.compile(
            r"""struct (.{0,128}?) :.{0,128}?IFlatbufferObject.{0,128}?
\{
(.+?)
\}
""",
            re.M | re.S,
        )

        self.reStructProperty = re.compile(r"""public (.+) (.+?) { get; }""")
        self.reTableDataType = re.compile(r'public Nullable<(.+?)> DataList\(int j\) { }')

    @staticmethod
    def _write_enums_to_fbs(enums: dict, f) -> None:
        for name, enum in enums.items():
            enum_fields = ',\n    '.join(f'{key} = {value}' for value, key in enum['fields'].items())

            f.write(f'enum {name}: {enum["format"]}{{\n')
            f.write(f'    {enum_fields}\n')
            f.write('}\n\n')

    @staticmethod
    def _write_enum_class(name: str, enum: dict, f) -> None:
        f.write(f'class {name}(IntEnum):\n')

        for value, key in enum['fields'].items():
            if key == 'None':
                key = 'none'

            f.write(f'    {key} = {value}\n')
        f.write('\n')

    @staticmethod
    def _is_list_property(name: str) -> bool:
        return len(name) > 6 and name.endswith('Length')

    @staticmethod
    def _process_list_property(name: str, intern: str) -> tuple:
        list_name = name[:-6]
        pattern = f'public (.+?) {re.escape(list_name)}' + r'\(int j\) { }'

        if match := re.search(pattern, intern):
            return list_name, match[1], True
        return name, '', False

    @staticmethod
    def _remove_nullable(typ: str) -> str:
        return typ[9:-1] if typ.startswith('Nullable<') else typ

    def _process_property(self, name: str, typ: str, intern: str) -> tuple | None:
        if name == 'ByteBuffer':
            return None

        is_list = False
        if self._is_list_property(name):
            name, new_type, is_list = self._process_list_property(name, intern)
            typ = new_type or typ

        typ = self._remove_nullable(typ)
        if is_list:
            typ = f'[{typ}]'

        return name, typ

    def _extract_enums(self, data: str) -> dict:
        return {
            name: {
                'format': format,
                'fields': {num: file_name for _, file_name, num in self.reEnumField.findall(field_text)},
            }
            for name, format, field_text in self.reEnum.findall(data)
            if '.' not in name
        }

    def _extract_structs(self, data: str) -> dict:
        return {
            key: {
                name: typ
                for prop in self.reStructProperty.finditer(intern)
                for result in [self._process_property(prop[2], prop[1], intern)]
                if result is not None
                for name, typ in [result]
            }
            for key, intern in self.reStruct.findall(data)
            if any(self._process_property(prop[2], prop[1], intern) for prop in self.reStructProperty.finditer(intern))
        }

    def _write_structs_to_fbs(self, structs: dict, enums: dict, f) -> None:
        for key, struct in structs.items():
            f.write(f'table {key}{{\n')

            for pname, ptype in struct.items():
                if ptype[0] == '[':
                    typ = ptype[1:-1]

                    if typ.endswith('Length'):
                        typ = typ[:-6]

                    if pname == typ:
                        pname += '_'

                    if typ not in structs and typ not in enums and typ not in self.types:
                        continue

                if pname == ptype:
                    pname += '_'

                f.write(f'    {pname}: {ptype};\n')
            f.write('}\n\n')

    def _create_dumper_wrappers(self, structs: dict, enums: dict, f) -> None:
        f.write('from enum import IntEnum\n\n')
        f.write('from ..lib.TableEncryptionService import TableEncryptionService\n\n\n')
        f.write('def dump_table(obj) -> list:\n')
        f.write('    table_encryption = TableEncryptionService()\n\n')
        f.write('    typ_name = obj.__class__.__name__[:-5]\n')
        f.write("    dump_func = next(f for x, f in globals().items() if x.endswith(f'_{typ_name}'))\n")
        f.write('    password = table_encryption.create_key(typ_name[:-5])\n')
        f.write(
            '    return [\n        dump_func(obj.DataList(j), password)\n        for j in range(obj.DataListLength())\n    ]\n\n\n'
        )

        for name, struct in structs.items():
            if not name.endswith('Table'):
                self._write_struct_dumper(name, struct, enums, structs, f)

        for name, enum in enums.items():
            self._write_enum_class(name, enum, f)

    def _write_struct_dumper(self, name: str, struct: dict, enums: dict, structs: dict, f) -> None:
        f.write(f'def dump_{name}(obj, password) -> dict:\n')
        f.write('    table_encryption = TableEncryptionService()\n\n')
        f.write('    return {\n')

        for pname, ptype in struct.items():
            is_list = False

            if ptype.startswith('['):
                ptype = ptype[1:-1]
                is_list = True

            val_func = self._get_value_function(pname, ptype, enums, structs)

            val_func = (
                f"[{val_func.format('j')} for j in range(obj.{pname}Length())]" if is_list else val_func.format('')
            )

            f.write(f"        '{pname}': {val_func},\n")
        f.write('    }\n\n\n')

    def _get_value_function(self, pname: str, ptype: str, enums: dict, structs: dict) -> str:
        if ptype.startswith('Nullable<') and ptype.endswith('>'):
            inner_type = ptype[9:-1]
            inner_func = self._get_value_function(pname, inner_type, enums, structs)

            return f'None if obj.{pname}() is None else {inner_func}'

        if ptype in self.type_converters:
            convert = self.type_converters[ptype]

            return f'{convert}(obj.{pname}({{}}), password)'

        if ptype in enums:
            convert = self.type_converters[enums[ptype]['format']]

            if pname == ptype:
                pname += '_'
            return f'{ptype}({convert}(obj.{pname}({{}}), password)).name'

        if ptype == 'bool':
            return f'obj.{pname}({{}})'

        if ptype in structs:
            return f'dump_{ptype}(obj.{pname}({{}}), password)'

        raise NotImplementedError(f'{ptype}')

    def generate(self) -> None:
        structs, enums = self.dump_cs_to_structs_and_enums(self.root / 'lib' / 'flatbuf' / 'dump.cs')
        fbs_path = self.generate_fbs(structs, enums, self.root / 'lib' / 'flatbuf' / 'BlueArchive.fbs')

        self.compile_fbs_to_python(fbs_path)
        self.write_init_file()
        self.write_dump_helper(structs, enums)

    def dump_cs_to_structs_and_enums(self, dump_cs_filepath: Path) -> tuple:
        with open(dump_cs_filepath, 'rt', encoding='utf-8') as f:
            data = f.read()

        enums = self._extract_enums(data)
        structs = self._extract_structs(data)

        return structs, enums

    def generate_fbs(self, structs: dict, enums: dict, filepath: Path) -> Path:
        with open(filepath, 'wt', encoding='utf-8') as f:
            f.write('namespace FlatData;\n\n')

            self._write_enums_to_fbs(enums, f)
            self._write_structs_to_fbs(structs, enums, f)
        return filepath

    def compile_fbs_to_python(self, fbs_path: Path) -> None:
        res = subprocess.run(
            [
                str(self.flatc_path),
                '--python',
                '--no-warnings',
                '--scoped-enums',
                '-o',
                str(self.root),
                str(fbs_path),
            ],
            capture_output=True,
        )

        if res.returncode != 0:
            raise RuntimeError(f'Failed to compile FBS: {res.stderr.decode()}')

    def write_init_file(self) -> None:
        init = self.root / 'FlatData' / '__init__.py'

        with open(init, 'wt', encoding='utf-8') as f:
            file_names = [fn.stem for fn in init.parent.glob('*.py') if fn.name not in ['dump.py', '__init__.py']]
            file_names.sort()

            for file_name in file_names:
                f.write(f'from .{file_name} import {file_name}\n')

    def write_dump_helper(self, structs: dict, enums: dict) -> None:
        dump = self.root / 'FlatData' / 'dump.py'

        with open(dump, 'wt', encoding='utf-8') as f:
            self._create_dumper_wrappers(structs, enums, f)
