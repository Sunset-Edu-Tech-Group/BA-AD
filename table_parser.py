import json
import struct
from pathlib import Path
from typing import Dict, List, Any
from io import BytesIO

class TableCatalog:
    def __init__(self, base_url: str, table: dict) -> None:
        self.base_url: str = base_url
        self.table: Dict[str, Any] = table

    @staticmethod
    def from_bytes(bytes_data: bytes, base_url: str) -> "TableCatalog":
        cursor = BytesIO(initial_bytes=bytes_data)

        def read_i8():
            return struct.unpack('b', cursor.read(1))[0]

        def read_i32():
            return struct.unpack('i', cursor.read(4))[0]

        def read_i64():
            return struct.unpack('q', cursor.read(8))[0]

        def read_bool():
            return struct.unpack('?', cursor.read(1))[0]

        def read_string() -> str:
            length = read_i32()
            return cursor.read(length).decode('utf-8', errors='replace')

        def read_includes() -> List[str]:
            size = read_i32()
            if size == -1:
                return []
            _ = read_i32()  # Skip 4 bytes
            includes: list = []
            for _ in range(size):
                includes.append(read_string())
                if _ != size - 1:
                    _ = read_i32()  # Skip 4 bytes
            return includes

        def read_table() -> tuple[str, dict[str, Any]]:
            _ = read_i32()  # Skip 4 bytes
            key: str = read_string()
            _ = read_i8()  # Skip 1 byte
            _ = read_i32()  # Skip 4 bytes
            name: str = read_string()
            size = read_i64()
            crc = read_i64()
            is_in_build = read_bool()
            is_changed = read_bool()
            is_prologue = read_bool()
            is_split_download = read_bool()
            includes: List[str] = read_includes()
            return key, {
                'name': name,
                'size': size,
                'crc': crc,
                'is_in_build': is_in_build,
                'is_changed': is_changed,
                'is_prologue': is_prologue,
                'is_split_download': is_split_download,
                'includes': includes
            }

        _ = read_i8()  # Skip 1 byte
        table_size = read_i32()
        table: dict = {}
        for _ in range(table_size):
            key, value = read_table()
            table[key] = value

        return TableCatalog(base_url=base_url, table=table)

    def to_json(self, path: Path) -> None:
        with open(path, mode='w', encoding='utf-8') as f:
            json.dump(obj={"Table": self.table}, fp=f, indent=4, ensure_ascii=False)
