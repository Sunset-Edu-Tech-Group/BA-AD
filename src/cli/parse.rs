use crate::cli::args::Args;
use crate::info;

use anyhow::Result;

pub fn run(args: Args) -> Result<()> {
    if args.verbose {
        info!("Verbose enabled");
    }

    Ok(())
}