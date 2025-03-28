mod crypto;
mod helpers;
mod utils;

use anyhow::Result;
use clap::Parser;

use helpers::args::Cli;
use helpers::file::FileManager;

#[tokio::main]
async fn main() -> Result<()> {
    let args: Cli = Cli::parse();
    // let file_manager: FileManager = FileManager::new()?;

    if args.update {
        return Ok(());
    }

    if let Some(command) = args.command {
        match command {
            helpers::args::Commands::Download(download_args) => {
                println!("Download command received: {:?}", download_args);
            }
            helpers::args::Commands::Search(search_args) => {
                println!("Search command received: {:?}", search_args);
            }
            helpers::args::Commands::Extract(extract_args) => {
                println!("Extract command received: {:?}", extract_args);
            }
        }
    }

    Ok(())
}
