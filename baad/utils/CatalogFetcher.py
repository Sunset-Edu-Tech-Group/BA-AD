import json
import os
import sys
from base64 import b64encode

from ApkParser import ApkParser

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.TableEncryptionService import TableEncryptionService


def decrypt_game_main_config(data):
    data = b64encode(data)
    encryption_service = TableEncryptionService()

    data = encryption_service.convert_string(
        data, encryption_service.create_key('GameMainConfig')
    )
    data = json.loads(data)
    crypted_key = encryption_service.new_encrypt_string(
        'ServerInfoDataUrl', encryption_service.create_key('ServerInfoDataUrl')
    )
    crypted_value = data[crypted_key]
    return encryption_service.convert_string(
        crypted_value, encryption_service.create_key('ServerInfoDataUrl')
    )


def find_game_main_config() -> None | bytes:
    pattern = bytes([
        0x47,
        0x61,
        0x6D,
        0x65,
        0x4D,
        0x61,
        0x69,
        0x6E,
        0x43,
        0x6F,
        0x6E,
        0x66,
        0x69,
        0x67,
        0x00,
        0x00,
        0x92,
        0x03,
        0x00,
        0x00,
    ])

    folder_path = ApkParser().file_path / 'data' / 'assets' / 'bin' / 'Data'

    for file_path in folder_path.rglob('*'):
        if file_path.is_file():
            content = file_path.read_bytes()

            if pattern in content:
                start_index = content.index(pattern)
                data = content[start_index + len(pattern) :]
                return data[:-2]
    return None


def catalog_url(update: bool = False) -> str:
    if update:
        ApkParser().download_apk(update)

    return decrypt_game_main_config(find_game_main_config())
