mod cli;

use cli::{parse, Args};
use baad::helpers::config::init_log;

use eyre::Result;
use clap::Parser;

#[tokio::main]
async fn main() -> Result<()> {
    let args = Args::parse();
    
    init_log(args.verbose)?;
    
    parse::run(args).await
}