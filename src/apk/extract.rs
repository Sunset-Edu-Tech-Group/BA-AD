use crate::helpers::{
    ServerConfig, ServerRegion,
    ASSET_APK, CONFIG_APK, DATA_APK,
    DATA_PATH, DATA_PATTERN,
    LIBIL2CPP_PATH, LIBIL2CPP_PATTERN,
    METADATA_PATH, METADATA_PATTERN
};
use crate::utils::FileManager;

use anyhow::Result;
use baad_core::{error, errors::ErrorExt, info};
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
    pub output: PathBuf,
}

pub struct ApkExtractor {
    config: Rc<ServerConfig>,
    file_manager: Rc<FileManager>,
}

impl ApkExtractor {
    pub fn new(file_manager: Rc<FileManager>, config: Rc<ServerConfig>) -> Result<Self> {
        Ok(Self {
            config,
            file_manager,
        })
    }
    
    fn check_extract_support(&self) -> Result<bool> {
        match &self.config.region { 
            ServerRegion::Global => {
                error!("Global server doesn't support APK extraction");
                Ok(false)
            }
            ServerRegion::Japan => {
                Ok(true)
            }
        }
    }

    pub fn extract(&self, rule: ExtractionRule) -> Result<()> {
        if !self.check_extract_support()? {
            return Ok(());
        }

        info!("Extracting apk...");

        let apk_path = self.file_manager.get_data_path(&self.config.apk_path);
        let mut archive = ZipArchive::new(
            File::open(&apk_path)
                .handle_errors()?
        ).handle_errors()?;
        
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
        let components: Vec<_> = file_path.components()
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

        let file_name = file_path.file_name()
            .and_then(|n| n.to_str())
            .unwrap_or("");

        let pattern = Pattern::new(rule.pattern).handle_errors()?;

        Ok(pattern.matches(file_name))
    }
    
    pub fn extract_data(&self) -> Result<()> {
        if !self.check_extract_support()? {
            return Ok(());
        }

        info!("Extracting game data...");
        
        let rule = ExtractionRule {
            apk: ASSET_APK,
            path: DATA_PATH,
            pattern: DATA_PATTERN,
            output: self.file_manager.get_data_path("data")
        };

        self.extract(rule)
    }
    
    pub fn extract_il2cpp(&self) -> Result<()> {
        if !self.check_extract_support()? {
            return Ok(());
        }

        info!("Extracting IL2CPP files...");
        
        
        let lib_rule = ExtractionRule {
            apk: CONFIG_APK,
            path: LIBIL2CPP_PATH,
            pattern: LIBIL2CPP_PATTERN,
            output: self.file_manager.get_data_path("il2cpp"),
        };
        self.extract(lib_rule)?;

        let metadata_rule = ExtractionRule {
            apk: DATA_APK,
            path: METADATA_PATH,
            pattern: METADATA_PATTERN,
            output: self.file_manager.get_data_path("il2cpp"),
        };
        self.extract(metadata_rule)?;

        Ok(())
    }
}