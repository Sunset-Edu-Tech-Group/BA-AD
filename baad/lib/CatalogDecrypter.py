import json
import struct
from io import BytesIO
from pathlib import Path
from typing import Any, Dict, List


class CatalogDecrypter:
    def __init__(self, base_url: str, data: dict) -> None:
        self.base_url: str = base_url
        self.data: Dict[str, Any] = data

    @staticmethod
    def from_bytes(bytes_data: bytes, base_url: str, media: bool) -> Any:
        cursor = BytesIO(initial_bytes=bytes_data)

        def read_i8() -> Any:
            return struct.unpack('b', cursor.read(1))[0]

        def read_i32() -> Any:
            return struct.unpack('i', cursor.read(4))[0]

        def read_i64() -> Any:
            return struct.unpack('q', cursor.read(8))[0]

        def read_bool() -> Any:
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
                'includes': includes,
            }
        
        def read_media() -> tuple[str, dict[str, Any]]:
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
            
            return key, {
                'path': path,
                'file_name': file_name,
                'bytes': bytes_count,
                'crc': crc,
                'is_prologue': is_prologue,
                'is_split_download': is_split_download,
                'media_type': media_type,
            }

        _ = read_i8()  # Skip 1 byte
        data_size = read_i32()
        data: dict = {}

        if media:
            for _ in range(data_size):
                key, value = read_media()
                data[key] = value
        
        if not media:
            for _ in range(data_size):
                key, value = read_table()
                data[key] = value

        return CatalogDecrypter(base_url=base_url, data=data)

    def to_json(self, path: Path, media: bool) -> None:
        with open(path, mode='w', encoding='utf-8') as f:
            json.dump(
                obj={'TableBundles': self.data} if not media else {'MediaResources': self.data},
                fp=f,
                indent=4,
                ensure_ascii=False,
            )
