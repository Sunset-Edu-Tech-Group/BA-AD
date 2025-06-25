use crate::cli::args::{Args, Commands};
use crate::{debug, error, info, warn};

use anyhow::Result;

fn test_logging() {
    info!("This is an info message");
    warn!("This is a warning message");
    error!("This is an error message");
    debug!("This is a debug message that only appears with --verbose");
    debug!("Testing another debug message with some value: {}", 42);
}

pub fn run(args: Args) -> Result<()> {
    if args.verbose {
        info!("Verbose mode enabled");
    }

    if let Some(Commands::Download(download_args)) = args.command {
        if download_args.assets {
            info!("Assets download requested");
            test_logging();
        }
    }

    Ok(())
}