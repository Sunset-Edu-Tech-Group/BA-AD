import binascii
import json

from requests_cache import CachedSession, AnyResponse
from pathlib import Path

from table_parser import TableCatalog
from media_parser import MediaCatalog


class AssetDownloader:
    def __init__(self, version: str | None = None, output: str | None = None, extracted: str | None = None) -> None:
        self.version: str | None = version

        self.root_path: Path = Path(__file__).parent
        self.output: str | Path = output or self.root_path / 'output'
        self.extracted: str | Path = extracted or self.root_path / 'extracted'
        self.version = version
    
    def calculate_crc32(self, file_path: Path) -> int:
        with open(file=file_path, mode='rb') as f:
            buf: bytes = f.read()
        return binascii.crc32(buf) & 0xFFFFFFFF
    
    def fetch_version(self) -> str:
        session = CachedSession(cache_name='serverindex', use_temp=True)

        if self.version is None:
            server_index: str = 'https://prod-noticeindex.bluearchiveyostar.com/prod/index.json'
            server_data: dict = session.get(url=server_index).json()
            return server_data['LatestClientVersion']
        return self.version
    
    def fetch_catalogurl(self) -> str:
        session = CachedSession(cache_name='serverapi', use_temp=True)

        server_api = 'https://yostar-serverinfo.bluearchiveyostar.com/r69_46_mv2tty056kkdlcs88r73.json'
        server_data: dict = session.get(url=server_api).json()
        return server_data["ConnectionGroups"][0]['OverrideConnectionGroups'][-1]['AddressablesCatalogUrlRoot']

    def fetch_tablebytes(self, catalog: str) -> bytes:
        session = CachedSession(cache_name='tablebytes', use_temp=True)

        table_bytes: AnyResponse = session.get(url=f'{catalog}/TableBundles/TableCatalog.bytes')
        return table_bytes.content

    def fetch_mediabytes(self, catalog: str) -> bytes:
        session = CachedSession(cache_name='tablebytes', use_temp=True)

        table_bytes: AnyResponse = session.get(url=f'{catalog}/MediaResources/MediaCatalog.bytes')
        return table_bytes.content

    def fetch_catalogs(self) -> None:
        session = CachedSession(cache_name='catalogurl', use_temp=True)

        catalog_url: str = self.fetch_catalogurl()
        bundle_data: dict = session.get(url=f'{catalog_url}/Android/bundleDownloadInfo.json').json()
        
        with open(file=self.root_path / 'public' / 'data' / 'bundleDownloadInfo.json', mode='w', encoding='utf-8') as f:
            json.dump(obj=bundle_data, fp=f, indent=4)

        table_data: bytes = self.fetch_tablebytes(catalog=catalog_url)
        table_catalog: TableCatalog = TableCatalog.from_bytes(bytes_data=table_data, base_url=catalog_url)
        table_catalog.to_json(path=self.root_path / 'public' / 'data' / 'TableCatalog.json')

        media_data: bytes = self.fetch_mediabytes(catalog=catalog_url)
        media_catalog: MediaCatalog = MediaCatalog.from_bytes(bytes_data=media_data, base_url=catalog_url)
        media_catalog.to_json(path=self.root_path / 'public' / 'data' / 'MediaCatalog.json')
    
    def get_gamefiles(self) -> dict:
        catalog_url: str = self.fetch_catalogurl()
        bundle_data = json.load(fp=open(file=self.root_path / 'public' / 'data' / 'bundleDownloadInfo.json'))
        table_data = json.load(fp=open(file=self.root_path / 'public' / 'data' / 'TableCatalog.json'))
        media_data = json.load(fp=open(file=self.root_path / 'public' / 'data' / 'MediaCatalog.json'))
        
        return {
            'AssetBundles': [
                {
                    'url': f'{catalog_url}/Android/{asset["Name"]}',
                    'crc': asset.get('Crc', 0)
                } for asset in bundle_data['BundleFiles']
            ],
            'TableBundles': [
                {
                    'url': f'{catalog_url}/TableBundles/{key}',
                    'crc': asset.get('crc', 0)
                } for key, asset in table_data['Table'].items()
            ],
            'MediaResources': [
                {
                    'url': f'{catalog_url}/MediaResources/{value["path"]}',
                    'path': value['path'],
                    'crc': value.get('crc', 0)
                } for key, value in media_data['Table'].items()
            ]
        }
    
    def save_data(self, data: dict) -> None:
        with open(file=self.root_path / 'public' / 'data' / 'GameFiles.json', mode='w') as f:
            json.dump(obj=data, fp=f, indent=4)

    def download(self, update: bool = False, skip: bool = True, use_local: bool = False) -> None:
        # if update:
        #     game_data = self.save_data(self.get_gamefiles())

        # TODO: Implement the download function using asyncio
        self.save_data(data=self.get_gamefiles())


if __name__ == '__main__':
    AssetDownloader().download(update=False)
