use anyhow::{anyhow, Error, Result};
use baad_core::errors::{ErrorContext, ErrorExt};
use std::env;
use std::path::PathBuf;
use platform_dirs::AppDirs;
use tokio::fs;
use once_cell::sync::Lazy;

const APP_NAME: &str = env!("CARGO_CRATE_NAME");
static APP_DIRS: Lazy<Result<AppDirs>> = Lazy::new(|| {
    AppDirs::new(Option::from(APP_NAME), true)
        .error_context("Failed to create app directories with name")
});

pub fn data_dir() -> Result<PathBuf> {
    (&*APP_DIRS)
        .as_ref()
        .map(|dirs| dirs.data_dir.clone())
        .map_err(|e| anyhow!(e.to_string()))
}

pub fn get_data_path(filename: &str) ->  Result<PathBuf> {
    let data_dir = data_dir()?;
    Ok(data_dir.join(filename))
}

pub async fn load_file(path: &PathBuf) -> Result<Vec<u8>> {
    fs::read(path).await.handle_errors()
}

pub async fn save_file(path: &PathBuf, content: &[u8]) -> Result<()> {
    fs::write(path, content).await.handle_errors()?;
    Ok(())
}

pub async fn create_parent_dir(path: &PathBuf) -> Result<()> {
    if let Some(parent) = path.parent() {
        fs::create_dir_all(parent).await.handle_errors()?;
    }
    Ok(())
}

pub async fn get_output_dir(path: Option<PathBuf>) -> Result<PathBuf, Error> {
    let output_dir = match path {
        Some(path) => path,
        None => env::current_dir().handle_errors()?.join("output"),
    };

    fs::create_dir_all(&output_dir).await.handle_errors()?;
    Ok(output_dir)
}

pub async fn is_dir_empty(path: &PathBuf) -> Result<bool> {
    Ok(!path.exists()
        || path
        .read_dir()
        .map_or(true, |mut entries| entries.next().is_none()))
}

pub async fn clear_all(dir: &PathBuf) -> Result<()> {
    if dir.exists() {
        fs::remove_dir_all(dir).await.handle_errors()?;
        fs::create_dir_all(dir).await.handle_errors()?;
    }

    Ok(())
}