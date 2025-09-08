mod cli;

use cli::{parse, Args};
use baad_core::VERBOSE;

use anyhow::Result;
use clap::Parser;
use std::sync::atomic::Ordering;

#[tokio::main]
async fn main() -> Result<()> {
    let args = Args::parse();
    VERBOSE.store(args.verbose, Ordering::Relaxed);
    parse::run(args).await
}