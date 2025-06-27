use crate::apk::{ApkExtractor, ApkFetcher};
use crate::catalog::{CatalogFetcher, CatalogParser};
use crate::cli::args::{Args, Commands, DownloadArgs, RegionCommands};
use crate::download::{FilterMethod, ResourceCategory, ResourceDownloadBuilder, ResourceFilter};
use crate::helpers::{ErrorContext, ServerConfig, ServerRegion};
use crate::utils::FileManager;

use anyhow::Result;

pub struct CommandHandler { args: Args }

impl CommandHandler {
    pub fn new(args: Args) -> Result<Self> { Ok(Self { args }) }

    pub async fn handle(&self) -> Result<()> {
        match &self.args.command {
            Some(Commands::Download { region }) => {
                self.handle_download(region).await
            }
            None => {
                if self.args.clean {
                    println!("Cleaning cache...");
                }
                if self.args.update {
                    println!("Forcing update...");
                }
                Ok(())
            }
        }
    }

    async fn handle_download(&self, region: &RegionCommands) -> Result<()> {
        match region {
            RegionCommands::Global(download_args) => {
                self.execute_download(ServerRegion::Global, download_args).await
            }
            RegionCommands::Japan(download_args) => {
                self.execute_download(ServerRegion::Japan, download_args).await
            }
        }
    }

    async fn execute_download(&self, region: ServerRegion, args: &DownloadArgs) -> Result<()> {
        let server_config = ServerConfig::new(region)?;
        let file_manager = FileManager::new()?;
        let apk_fetcher = ApkFetcher::new(file_manager.clone(), server_config.clone())?;
        let apk_extractor = ApkExtractor::new(file_manager.clone(), server_config.clone())?;
        let catalog_fetcher = CatalogFetcher::new(
            file_manager.clone(),
            server_config.clone(),
            apk_fetcher,
        );
        let catalog_parser = CatalogParser::new(file_manager.clone(), server_config.clone())?;

        let resource_downloader = ResourceDownloadBuilder::new(file_manager.clone(), server_config.clone())?
            .limit(args.limit as u64)
            .retries(args.retries)
            .output(Some(args.output.clone().into()))
            .build()?;

        let resource_category = self.resource_category(args);
        let resource_filter = self.resource_filter(args)?;
        resource_downloader.download(resource_category, resource_filter).await?;

        Ok(())
    }

    fn resource_category(&self, args: &DownloadArgs) -> ResourceCategory {
        let has_assets = args.assets;
        let has_tables = args.tables;
        let has_media = args.media;

        match (has_assets, has_tables, has_media) {
            (true, false, false) => ResourceCategory::Assets,
            (false, true, false) => ResourceCategory::Tables,
            (false, false, true) => ResourceCategory::Media,
            (true, true, true) => ResourceCategory::All,
            (false, false, false) => ResourceCategory::All,
            (true, true, false) => ResourceCategory::multiple(vec![
                ResourceCategory::Assets,
                ResourceCategory::Tables
            ]),
            (true, false, true) => ResourceCategory::multiple(vec![
                ResourceCategory::Assets,
                ResourceCategory::Media
            ]),
            (false, true, true) => ResourceCategory::multiple(vec![
                ResourceCategory::Tables,
                ResourceCategory::Media
            ]),
        }
    }


    fn resource_filter(&self, args: &DownloadArgs) -> Result<Option<ResourceFilter>> {
        let Some(filter_pattern) = &args.filter else {
            if !matches!(args.filter_method, FilterMethod::Contains) {
                let filter_method_name = format!("{:?}", args.filter_method).to_lowercase();
                return None.error_context(&format!(
                    "Filter method '{}' specified but no filter pattern provided. Use --filter to specify a pattern.",
                    filter_method_name
                ));
            }
            return Ok(None);
        };

        let filter = ResourceFilter::new(filter_pattern, args.filter_method.clone())?;
        Ok(Some(filter))
    }
}

pub async fn run(args: Args) -> Result<()> {
    let handler = CommandHandler::new(args)?;
    handler.handle().await
}