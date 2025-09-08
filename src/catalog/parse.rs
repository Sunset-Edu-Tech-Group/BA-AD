use crate::helpers::{
    ApiData, AssetBundle,
    GameFiles, GameFilesBundles,
    GlobalCatalog, GlobalGameResources,
    HashValue, JapanGameResources,
    MediaResources, Platform, Resource,
    ServerConfig, ServerRegion, TableResources,
};
use crate::utils::{file, json};

use anyhow::Result;
use baad_core::{errors::{ErrorContext, ErrorExt}, info, success};
use bacy::{MediaCatalog, Packing, TableCatalog};
use reqwest::Client;
use std::path::Path;
use std::rc::Rc;

struct Paths {
    asset_path: Box<Path>,
    table_path: Box<Path>,
    media_path: Box<Path>,
    game_path: Box<Path>,
    resource_path: Box<Path>,
    api_path: Box<Path>,
    patch_pack_path: &'static str,
    platform_path: &'static str,
}

pub struct CatalogParser {
    client: Client,
    config: Rc<ServerConfig>,
    paths: Paths,
}

impl CatalogParser {
    pub fn new(config: Rc<ServerConfig>) -> Result<Self> {
        let data_dir = file::data_dir()?;
        let api_path = data_dir.join("api_data.json");

        let catalog_dir = match config.region {
            ServerRegion::Global => data_dir.join("catalog/global"),
            ServerRegion::Japan =>  data_dir.join("catalog/japan"),
        };
        
        let asset_path = catalog_dir.join("BundlePackingInfo.json");
        let table_path = catalog_dir.join("TableCatalog.json");
        let media_path = catalog_dir.join("MediaCatalog.json");
        let game_path = catalog_dir.join("GameFiles.json");
        let resource_path = catalog_dir.join("Resources.json");
        
        let patch_pack_path = match config.platform {
            Platform::Android => "Android_PatchPack",
            Platform::Ios => "iOS_PatchPack",
        };
        
        let platform_path = match config.platform {
            Platform::Android => "/Android/",
            Platform::Ios => "/iOS/",
        };
        
        Ok(Self {
            client: Client::new(),
            config,
            paths: Paths { 
                asset_path: asset_path.into_boxed_path(),
                table_path: table_path.into_boxed_path(),
                media_path: media_path.into_boxed_path(),
                game_path: game_path.into_boxed_path(),
                resource_path: resource_path.into_boxed_path(),
                api_path: api_path.into_boxed_path(),
                patch_pack_path, 
                platform_path 
            },
        })
    }

    async fn japan_data(&self, catalog_url: &str) -> Result<()> {
        let asset_data = self
            .client
            .get(format!("{}/{}/BundlePackingInfo.json", catalog_url, self.paths.patch_pack_path))
            .send()
            .await
            .handle_errors()?
            .json::<Packing>()
            .await
            .handle_errors()?;
        
        json::save_json(
            &self.paths.asset_path,
            &asset_data
        )
        .await?;

        success!("Saved AssetBundles catalog");

        let table_bytes = self
            .client
            .get(format!("{}/TableBundles/TableCatalog.bytes", catalog_url))
            .send()
            .await
            .handle_errors()?
            .bytes()
            .await
            .handle_errors()?;
        let table_data = TableCatalog::deserialize(&table_bytes, catalog_url).handle_errors()?;

        json::save_json(
            &self.paths.table_path,
            &table_data,
        )
            .await?;

        success!("Saved TableBundles catalog");

        let media_bytes = self
            .client
            .get(format!(
                "{}/MediaResources/Catalog/MediaCatalog.bytes",
                catalog_url
            ))
            .send()
            .await
            .handle_errors()?
            .bytes()
            .await
            .handle_errors()?;
        let media_data = MediaCatalog::deserialize(&media_bytes, catalog_url).handle_errors()?;

        json::save_json(
            &self.paths.media_path,
            &media_data,
        )
        .await?;

        success!("Saved MediaResources catalog");

        Ok(())
    }

    async fn japan_gamefiles(&self, catalog_url: &str) -> Result<()> {
        let bundle_info: Packing =
            json::load_json(&self.paths.asset_path).await?;
        let table_catalog: TableCatalog =
            json::load_json(&self.paths.table_path).await?;
        let media_catalog: MediaCatalog =
            json::load_json(&self.paths.media_path).await?;

        let game_resources = JapanGameResources {
            asset_bundles: bundle_info.full_patch_packs.iter()
                .chain(bundle_info.update_packs.iter())
                .map(|patch| GameFilesBundles {
                    url: format!("{}/{}/{}", catalog_url, self.paths.patch_pack_path, patch.pack_name),
                    path: format!("AssetBundles/{}", patch.pack_name),
                    hash: HashValue::Crc(patch.crc),
                    size: patch.pack_size,
                    bundle_files: patch.bundle_files.iter().map(|bundle| bundle.name.clone()).collect(),
                })
                .collect(),

            table_bundles: table_catalog
                .table
                .into_values()
                .map(|entry| GameFiles {
                    url: format!("{}/TableBundles/{}", catalog_url, entry.name),
                    path: format!("TableBundles/{}", entry.name),
                    hash: HashValue::Crc(entry.crc),
                    size: entry.size,
                })
                .collect(),

            media_resources: media_catalog
                .table
                .into_values()
                .map(|entry| {
                    let path = entry.path.replace('\\', "/");
                    GameFiles {
                        url: format!("{}/MediaResources/{}", catalog_url, path),
                        path: format!("MediaResources/{}", path),
                        hash: HashValue::Crc(entry.crc),
                        size: entry.bytes,
                    }
                })
                .collect(),
        };

        json::save_json(
            &self.paths.game_path,
            &game_resources
        )
        .await?;

        success!("Saved GameFiles");
        
        Ok(())
    }

    async fn global_data(&self, resources: &[Resource]) -> Result<()> {
        let asset_bundles: Vec<Resource> = resources
            .iter()
            .filter(|r| r.resource_path.contains(self.paths.platform_path))
            .cloned()
            .collect();

        let media_resources: Vec<Resource> = resources
            .iter()
            .filter(|r| r.resource_path.contains("/MediaResources/"))
            .cloned()
            .collect();


        let table_bundles: Vec<Resource> = resources
            .iter()
            .filter(|r| r.resource_path.contains("/TableBundles/"))
            .cloned()
            .collect();
        
        if !asset_bundles.is_empty() {
            let asset_data = AssetBundle { asset_bundles };
            json::save_json(
                &self.paths.asset_path,
                &asset_data
            )
            .await?;

            success!("Saved AssetBundles catalog");
        }

        if !table_bundles.is_empty() {
            let table_data = TableResources { table_bundles };
            json::save_json(
                &self.paths.table_path,
                &table_data
            )
            .await?;

            success!("Saved TableBundles catalog");
        }

        if !media_resources.is_empty() {
            let media_data = MediaResources { media_resources };
            json::save_json(
                &self.paths.media_path,
                &media_data
            )
                .await?;

            success!("Saved MediaResources catalog");
        }

        Ok(())
    }

    async fn global_gamefiles(&self, catalog_url: &str, resources: &[Resource]) -> Result<()> {
        let game_resources = GlobalGameResources {
            asset_bundles: resources
                .iter()
                .filter(|r| r.resource_path.contains(self.paths.platform_path))
                .map(|r| self.resource_to_gamefiles(r, catalog_url, "AssetBundles"))
                .collect(),

            table_bundles: resources
                .iter()
                .filter(|r| r.resource_path.contains("/TableBundles/"))
                .map(|r| self.resource_to_gamefiles(r, catalog_url, "TableBundles"))
                .collect(),

            media_resources: resources
                .iter()
                .filter(|r| r.resource_path.contains("/MediaResources/"))
                .map(|r| self.resource_to_gamefiles(r, catalog_url, "MediaResources"))
                .collect(),
        };

        json::save_json(
            &self.paths.game_path,
            &game_resources
        ).await?;

        success!("Saved GameFiles");
        
        Ok(())
    }

    fn resource_to_gamefiles(&self, resource: &Resource, catalog_url: &str, prefix: &str) -> GameFiles {
        GameFiles {
            url: format!("{}/{}", catalog_url, resource.resource_path),
            path: format!("{}/{}", prefix, resource.resource_path),
            hash: HashValue::Md5(resource.resource_hash.clone()),
            size: resource.resource_size,
        }
    }

    pub async fn process_catalogs(&self) -> Result<()> {
        let api_data: ApiData = json::load_json(&self.paths.api_path).await?;
        
        info!("Processing catalogs...");

        match self.config.region {
            ServerRegion::Japan => {
                let catalog_url = &api_data.japan.catalog_url;

                if catalog_url.is_empty() {
                    return None.error_context("Japan catalog URL is empty - run CatalogFetcher first");
                }

                self.japan_data(catalog_url).await?;
                self.japan_gamefiles(catalog_url).await?;
            }
            ServerRegion::Global => {
                let resources: GlobalCatalog =
                    json::load_json(&self.paths.resource_path).await?;
                let catalog_url = &api_data
                    .global
                    .catalog_url
                    .trim_end_matches("/resource-data.json");

                if catalog_url.is_empty() {
                    return None.error_context("Global catalog URL is empty - run CatalogFetcher first");
                }

                self.global_data(&resources.resources).await?;
                self.global_gamefiles(catalog_url, &resources.resources)
                    .await?;
            }
        }

        Ok(())
    }
}