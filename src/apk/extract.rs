use crate::helpers::{
    ServerConfig, ServerRegion, ASSET_APK, CONFIG_APK, DATA_PATH, DATA_PATTERN, GLOBAL_DATA_APK,
    JP_DATA_APK, LIBIL2CPP_PATH, LIBIL2CPP_PATTERN, METADATA_PATH, METADATA_PATTERN,
};
use crate::utils::file;

use anyhow::Result;
use baad_core::{errors::ErrorExt, info};
use glob::Pattern;
use std::fs::{self, File};
use std::io::{self, Cursor, Read};
use std::path::{Path, PathBuf};
use std::rc::Rc;
use zip::ZipArchive;

pub struct ExtractionRule<'a> {
    pub apk: &'a str,
    pub path: &'a [&'a str],
    pub pattern: &'a str,
    pub output: Box<Path>,
}

pub struct ApkExtractor {
    config: Rc<ServerConfig>,
}

impl ApkExtractor {
    pub fn new(config: Rc<ServerConfig>) -> Result<Self> {
        Ok(Self { config })
    }

    pub fn extract(&self, rule: ExtractionRule) -> Result<()> {
        info!("Extracting apk...");

        let apk_path = file::get_data_path(&self.config.apk_path)?;
        let mut archive =
            ZipArchive::new(File::open(&apk_path).handle_errors()?).handle_errors()?;

        let mut target_apk = archive.by_name(rule.apk).handle_errors()?;

        let mut buf = Vec::new();
        target_apk.read_to_end(&mut buf).handle_errors()?;
        let mut cursor = Cursor::new(buf);

        let mut inner_archive = ZipArchive::new(&mut cursor).handle_errors()?;

        fs::create_dir_all(&rule.output)?;

        for i in 0..inner_archive.len() {
            let mut file = inner_archive.by_index(i).handle_errors()?;
            let file_path = PathBuf::from(file.name());

            if self.matches_rule(&file_path, &rule)? {
                let out = rule.output.join(file_path.file_name().unwrap());

                let mut outfile = File::create(&out).handle_errors()?;
                io::copy(&mut file, &mut outfile).handle_errors()?;
            }
        }

        Ok(())
    }

    fn matches_rule(&self, file_path: &Path, rule: &ExtractionRule) -> Result<bool> {
        let components: Vec<_> = file_path
            .components()
            .map(|c| c.as_os_str().to_string_lossy().to_string())
            .collect();

        if components.len() < rule.path.len() {
            return Ok(false);
        }

        for (i, target) in rule.path.iter().enumerate() {
            if &components[i] != target {
                return Ok(false);
            }
        }

        let file_name = file_path.file_name().and_then(|n| n.to_str()).unwrap_or("");

        let pattern = Pattern::new(rule.pattern).handle_errors()?;

        Ok(pattern.matches(file_name))
    }

    pub fn extract_data(&self) -> Result<()> {
        info!("Extracting game data...");

        let rule = ExtractionRule {
            apk: match self.config.region {
                ServerRegion::Global => GLOBAL_DATA_APK,
                ServerRegion::Japan => ASSET_APK,
            },
            path: DATA_PATH,
            pattern: DATA_PATTERN,
            output: file::get_data_path("data")?.into_boxed_path(),
        };

        self.extract(rule)
    }

    pub fn extract_il2cpp(&self) -> Result<()> {
        let il2cpp_path: PathBuf = match self.config.region {
            ServerRegion::Global => file::get_data_path("il2cpp/global")?,
            ServerRegion::Japan => file::get_data_path("il2cpp/japan")?,
        };

        info!("Extracting IL2CPP files...");

        let lib_rule = ExtractionRule {
            apk: CONFIG_APK,
            path: LIBIL2CPP_PATH,
            pattern: LIBIL2CPP_PATTERN,
            output: il2cpp_path.clone().into_boxed_path(),
        };
        self.extract(lib_rule)?;

        let metadata_rule = ExtractionRule {
            apk: match self.config.region {
                ServerRegion::Global => GLOBAL_DATA_APK,
                ServerRegion::Japan => JP_DATA_APK,
            },
            path: METADATA_PATH,
            pattern: METADATA_PATTERN,
            output: il2cpp_path.into_boxed_path(),
        };
        self.extract(metadata_rule)?;

        Ok(())
    }
}
