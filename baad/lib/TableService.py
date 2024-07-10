import os
from base64 import b64encode
from io import BytesIO
from typing import Union
from zipfile import ZipFile

from .MersenneTwister import MersenneTwister
from .XXHashService import calculate_hash


class TableZipFile(ZipFile):
    def __init__(self, file: Union[str, BytesIO], name: str = None) -> None:
        super().__init__(file)
        file_name = name if isinstance(file, BytesIO) else os.path.basename(file)
        self.password = self._generate_password(file_name)

    def _generate_password(self, file_name: str) -> bytes:
        hash_value = calculate_hash(file_name)
        twister = MersenneTwister(hash_value)
        return b64encode(twister.next_bytes(15))

    def open(self, name: str, mode: str = 'r', force_zip64: bool = False):
        return super().open(name, mode, pwd=self.password, force_zip64=force_zip64)
