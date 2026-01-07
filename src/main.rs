mod cli;

use cli::{parse, Args};

use baad_core::config::{init_logging, LoggingConfig};
use clap::Parser;
use eyre::Result;

#[tokio::main]
async fn main() -> Result<()> {
    let args = Args::parse();

    let config = LoggingConfig {
        verbose_mode: args.verbose,
        enable_debug: args.verbose,
        enable_async_writer: false,
        ..LoggingConfig::default()
    };
    init_logging(config)?;

    parse::run(args).await
}
