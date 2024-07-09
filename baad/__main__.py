from argparse import ArgumentParser, ArgumentTypeError

from rich.console import Console
from rich.traceback import Traceback

from .utils.ResourceDownloader import ResourceDownloader


def arguments():  # sourcery skip: extract-duplicate-method
    parser = ArgumentParser(description='Blue Archive Asset Downloader')
    sub_parser = parser.add_subparsers(dest='commands')

    parser.add_argument(
        '-u',
        '--update',
        action='store_true',
        help='force update the apk',
    )
    parser.add_argument(
        '-g',
        '--generate',
        action='store_true',
        help='generate the flatbuf schemas',
    )

    download = sub_parser.add_parser(
        'download',
        help='download game files',
    )
    extract = sub_parser.add_parser(
        'extract',
        help='extract game files',
    )

    download.add_argument(
        '--output',
        type=str,
        help='output directory for the downloaded files (default: public/data/output)',
    )
    download.add_argument(
        '--limit',
        type=int,
        help='set a limit the download limit',
    )
    download.add_argument(
        '--assets',
        action='store_true',
        help='download the assetbundles',
    )
    download.add_argument(
        '--tables',
        action='store_true',
        help='download the tablebundles',
    )
    download.add_argument(
        '--media',
        action='store_true',
        help='download the mediaresources',
    )
    download.add_argument(
        '-a',
        '--all',
        action='store_true',
        help='download all game files',
    )

    extract.add_argument(
        '--output',
        type=str,
        help='output directory for the extracted files (default: public/data/extracted)',
    )
    extract.add_argument(
        '--assets',
        action='store_true',
        help='extract the assetbundles',
    )
    extract.add_argument(
        '--tables',
        action='store_true',
        help='extract the tablebundles',
    )
    extract.add_argument(
        '-a',
        '--all',
        action='store_true',
        help='extract all game files',
    )

    args = parser.parse_args()
    if hasattr(args, 'commands') and args.commands in ['download', 'extract'] and (args.all and (args.assets or args.tables or args.media)):
        console = Console(stderr=True)
        console.print(
            Traceback.from_exception(
                type(ArgumentTypeError),
                ArgumentTypeError("'--all' cannot be used with other download options"),
                None,
            )
        )
        raise SystemExit(1)
    return args


def resource_downloader(args):
    if args.update:
        ResourceDownloader(update=args.update).fetch_catalogurl()

    if hasattr(args, 'commands') and args.commands == 'download':
        downloader_args = {'update': args.update}

        if args.output:
            downloader_args['output'] = args.output
        downloader = ResourceDownloader(**downloader_args)

        if args.all:
            args.assets = args.tables = args.media = True

        downloader.download(
            assets=args.assets,
            tables=args.tables,
            media=args.media,
            limit=getattr(args, 'limit', None),
        )

    return downloader


def main():
    args = arguments()

    if args.update or (hasattr(args, 'commands') and args.commands == 'download'):
        resource_downloader(args)


if __name__ == '__main__':
    main()
