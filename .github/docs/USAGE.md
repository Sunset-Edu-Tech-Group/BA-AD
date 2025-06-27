```shell
>> baad --help

Usage: baad [OPTIONS] [COMMAND]

Commands:
  download  Download game files
  help      Print this message or the help of the given subcommand(s)

Options:
  -u, --update   Force update
  -c, --clean    Cleans the cache
  -v, --verbose  Enable verbose output
  -h, --help     Print help
  -V, --version  Print version

```


```shell
>> baad download --help

Download game files

Usage: baad download <COMMAND>

Commands:
  global  Download from Global server
  japan   Download from Japan server
  help    Print this message or the help of the given subcommand(s)

Options:
  -h, --help  Print help
```

```shell
>> baad download {japan|global} --help

Download from {Japan|Global} server

Usage: baad download japan [OPTIONS]

Options:
      --assets                         Download the assetbundles
      --tables                         Download the tablebundles
      --media                          Download the mediaresources
      --output <OUTPUT>                Output directory for the downloaded files [default: ./output]
      --limit <LIMIT>                  Set a limit on the concurrent downloads [default: 10]
      --retries <RETRIES>              Number of retry attempts for failed downloads [default: 10]
      --filter <FILTER>                Filter by name
      --filter-method <FILTER_METHOD>  Filter method to use [default: contains] [possible values: exact, contains, regex, fuzzy, glob, contains-ignore-case, starts-with, ends-with]
  -h, --help                           Print help

~/Documents/Rust/BA-AD/target/release on rs-2.0.0 [!+]
% >....                                                                                                                                                                                                                             
      --output <OUTPUT>                Output directory for the downloaded files [default: ./output]
      --limit <LIMIT>                  Set a limit on the concurrent downloads [default: 10]      
      --retries <RETRIES>              Number of retry attempts for failed downloads [default: 10]
      --filter <FILTER>                Filter by name                                                                                                                               
      --filter-method <FILTER_METHOD>  Filter method to use [default: contains] [possible values: exact, contains, regex, fuzzy, glob, contains-ignore-case, starts-with, ends-with]
  -h, --help                           Print help
```