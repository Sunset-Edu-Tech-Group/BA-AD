use crate::helpers::{ErrorExt, ServerConfig, ServerRegion};
use crate::utils::FileManager;
use crate::{error, info};

use anyhow::{Context, Result};
use glob::Pattern;
use std::fs::{self, File};
use std::io::{self, Cursor, Read};
use std::path::{Path, PathBuf};
use zip::ZipArchive;

#[derive(Clone)]
pub struct ExtractionRule {
    pub apk: String,
    pub path: Vec<String>,
    pub pattern: String,
    pub output: PathBuf,
}

pub struct ApkExtractor {
    config: ServerConfig,
    file_manager: FileManager,
}

impl ApkExtractor {
    pub fn new(file_manager: &FileManager, config: &ServerConfig) -> Result<Self> {
        Ok(Self {
            config: config.clone(),
            file_manager: file_manager.clone(),
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


        let mut target_apk = archive.by_name(&rule.apk).handle_errors()?;


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

        let pattern = Pattern::new(&rule.pattern).handle_errors()?;

        Ok(pattern.matches(file_name))
    }
    
    pub fn extract_data(&self) -> Result<()> {
        if !self.check_extract_support()? {
            return Ok(());
        }

        info!("Extracting game data...");
        
        let rule = ExtractionRule {
            apk: "UnityDataAssetPack.apk".to_string(),
            path: vec!["assets".to_string(), "bin".to_string(), "Data".to_string()],
            pattern: "*".to_string(),
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
            apk: "config.arm64_v8a.apk".to_string(),
            path: vec!["lib".to_string(), "arm64-v8a".to_string()],
            pattern: "libil2cpp.so".to_string(),
            output: self.file_manager.get_data_path("il2cpp"),
        };
        self.extract(lib_rule)?;

        let metadata_rule = ExtractionRule {
            apk: "UnityDataAssetPack.apk".to_string(),
            path: vec![
                "assets".to_string(),
                "bin".to_string(),
                "Data".to_string(),
                "Managed".to_string(),
                "Metadata".to_string(),
            ],
            pattern: "metadata.dat".to_string(),
            output: self.file_manager.get_data_path("il2cpp"),
        };
        self.extract(metadata_rule)?;

        Ok(())
    }
}