mod apk;
mod catalog;
mod download;
mod helpers;
mod utils;
mod cli;

use crate::cli::parse;
use crate::cli::Args;

use anyhow::Result;
use clap::Parser;

#[tokio::main]
async fn main() -> Result<()> {
    let args = Args::parse();
    parse::run(args)
}
