import json
import struct
from pathlib import Path
from typing import Dict, Any
from io import BytesIO

class Media:
    def __init__(self, path: str, file_name: str, bytes: int, crc: int, 
                 is_prologue: bool, is_split_download: bool, media_type: int) -> None:
        self.path: str = path
        self.file_name: str = file_name
        self.bytes: int = bytes
        self.crc: int = crc
        self.is_prologue: bool = is_prologue
        self.is_split_download: bool = is_split_download
        self.media_type: int = media_type

    def to_dict(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "file_name": self.file_name,
            "bytes": self.bytes,
            "crc": self.crc,
            "is_prologue": self.is_prologue,
            "is_split_download": self.is_split_download,
            "media_type": self.media_type
        }

class MediaCatalog:
    def __init__(self, base_url: str, table: Dict[str, Media]) -> None:
        self.base_url: str = base_url
        self.table: Dict[str, Media] = table

    @staticmethod
    def from_bytes(bytes_data: bytes, base_url: str) -> "MediaCatalog":
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
            return cursor.read(length).decode(encoding='utf-8', errors='replace')

        def read_media() -> tuple[str, Media]:
            _ = read_i32()  # Skip 4 bytes
            key = read_string()
            _ = read_i8()  # Skip 1 byte
            _ = read_i32()  # Skip 4 bytes
            path = read_string()
            _ = read_i32()  # Skip 4 bytes
            file_name = read_string()
            bytes_count = read_i64()
            crc = read_i64()
            is_prologue = read_bool()
            is_split_download = read_bool()
            media_type = read_i32()
            return key, Media(path=path, file_name=file_name, bytes=bytes_count, crc=crc, 
                             is_prologue=is_prologue, is_split_download=is_split_download, media_type=media_type)

        _ = read_i8()  # Skip 1 byte
        table_size = read_i32()
        table = {}
        for _ in range(table_size):
            key, value = read_media()
            table[key] = value

        return MediaCatalog(base_url=base_url, table=table)

    def to_json(self, path: Path) -> None:
        with open(file=path, mode='w', encoding='utf-8') as f:
            json.dump(obj={"Table": {k: v.to_dict() for k, v in self.table.items()}}, fp=f, indent=4, ensure_ascii=False)
