use anyhow::{anyhow, Context, Result};
use crate::lib::file::FileManager;
use regex::Regex;
use reqwest::header::{HeaderMap, HeaderValue};
use reqwest::{Client, Response};
use reqwest::Url;
use std::fs;
use std::fs::File;
use std::io::{self, Cursor, Read};
use std::path::PathBuf;
use trauma::download::Download;
use trauma::downloader::DownloaderBuilder;
use zip::ZipArchive;

pub const APK_DOWNLOAD_URL_REGEX: &str = r"(X?APKJ)..(https?://(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*))";
pub const APK_VERSION_REGEX: &str = r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)";

pub struct ApkConfig {
    pub version_url: String,
    pub apk_dir: String,
    pub apk_filename: String,
    pub version_filename: String,
    pub asset_filter: String,
}

impl Default for ApkConfig {
    fn default() -> Self {
        Self {
            version_url: "https://api.pureapk.com/m/v3/cms/app_version?hl=en-US&package_name=com.YostarJP.BlueArchive".to_string(),
            apk_dir: "apk".to_string(),
            apk_filename: "bluearchive.apk".to_string(),
            version_filename: "version.txt".to_string(),
            asset_filter: "assets/bin/Data/".to_string(),
        }
    }
}

fn http_headers() -> HeaderMap {
    let mut headers: HeaderMap = HeaderMap::new();
    headers.insert("x-cv", HeaderValue::from_static("3172501"));
    headers.insert("x-sv", HeaderValue::from_static("29"));
    headers.insert(
        "x-abis",
        HeaderValue::from_static("arm64-v8a,armeabi-v7a,armeabi"),
    );
    headers.insert("x-gp", HeaderValue::from_static("1"));
    headers
}

pub async fn download_apk(
    file_manager: &FileManager,
    version_url: &str, 
    apk_dir: &str, 
    apk_filename: &str, 
    version_filename: &str
) -> Result<()> {
    println!("Checking for updates");
    
    let output_path: PathBuf = file_manager.create_dir(apk_dir)?;
    
    let current_version: String = if file_manager.file_exists(version_filename) {
        file_manager.load_text(version_filename)?
    } else {
        String::new()
    };
    
    let client: Client = Client::builder().default_headers(http_headers()).build()?;
    let versions_response: Response = client.get(version_url).send().await?;

    match versions_response.status() {
        reqwest::StatusCode::OK => {}
        _ => {
            return Err(anyhow!(
                "Failed to get versions: {}",
                versions_response.status()
            ));
        }
    }

    let body: String = versions_response.text().await?;
    let re_version: Regex = Regex::new(APK_VERSION_REGEX).unwrap();
    
    let new_version: &str = match re_version.find(body.as_str()) {
        Some(m) => m.as_str(),
        None => return Err(anyhow!("Failed to find version in response")),
    };

    if new_version == current_version {
        println!("App is up to date");
        return Ok(());
    }

    let apk_path: String = format!("{}/{}", apk_dir, apk_filename);
    if file_manager.file_exists(&apk_path) {
        file_manager.delete_file(&apk_path)?;
    }

    println!("Latest version: {}", new_version);

    let re_url: Regex = Regex::new(APK_DOWNLOAD_URL_REGEX).unwrap();
    let download_url: &str = match re_url.captures(body.as_str()) {
        Some(caps) if caps.len() >= 3 => caps.get(2).unwrap().as_str(),
        _ => {
            return Err(anyhow!("Failed to get download url"));
        }
    };

    println!("Downloading app");
    let downloader: trauma::downloader::Downloader = DownloaderBuilder::new()
        .directory(output_path)
        .build();
    let downloads: Vec<Download> = vec![Download {
        url: Url::parse(download_url).unwrap(),
        filename: apk_filename.to_string(),
    }];
    downloader.download(&downloads).await;
    println!("Finished downloading app");
    
    file_manager.save_text(version_filename, new_version)?;
    Ok(())
}

pub fn extract_apk(
    file_manager: &FileManager,
    apk_filename: &str, 
    extract_dir: &str, 
    asset_filter: &str
) -> Result<()> {
    println!("Extracting app");

    let apk_path: PathBuf = file_manager.data_path(apk_filename);
    let mut archive: ZipArchive<File> = ZipArchive::new(
        File::open(&apk_path)
            .with_context(|| format!("{} not found", apk_path.display()))?,
    )
    .with_context(|| "Failed to open archive")?;

    let mut unity_apk: zip::read::ZipFile<'_> = match archive.by_name("UnityDataAssetPack.apk") {
        Ok(file) => file,
        Err(_) => {
            return Err(anyhow!("UnityDataAssetPack.apk not found"));
        }
    };

    let mut buf: Vec<u8> = Vec::new();
    unity_apk
        .read_to_end(&mut buf)
        .with_context(|| "Failed to read UnityDataAssetPack")?;
    let mut cursor: Cursor<Vec<u8>> = Cursor::new(buf);

    let mut inner_archive: ZipArchive<&mut Cursor<Vec<u8>>> =
        ZipArchive::new(&mut cursor).with_context(|| "Failed to open UnityDataAssetPack")?;

    let output_path: PathBuf = file_manager.create_dir(extract_dir)?;

    for i in 0..inner_archive.len() {
        let mut file = inner_archive.by_index(i)?;
        if !file.name().starts_with(asset_filter) {
            continue;
        }
        
        let outpath: PathBuf = match file.enclosed_name() {
            Some(path) => output_path.join(path),
            None => continue,
        };
        
        if let Some(p) = outpath.parent() {
            if !p.exists() {
                fs::create_dir_all(p).with_context(|| "Failed to create directory")?;
            }
        }

        let mut outfile: File = File::create(&outpath).with_context(|| format!("Failed to create file: {}", outpath.display()))?;
        io::copy(&mut file, &mut outfile).with_context(|| "Failed to copy file")?;
    }

    println!("Finished extracting app");
    Ok(())
}
