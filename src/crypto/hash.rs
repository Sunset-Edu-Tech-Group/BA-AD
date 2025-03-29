use anyhow::Result;
use md5::{Digest, Md5};
use std::path::PathBuf;

pub fn calculate_crc32(path: PathBuf) -> Result<u32> {
    let data: Vec<u8> = std::fs::read(path)?;
    Ok(crc32fast::hash(&data))
}

pub fn calculate_md5(path: PathBuf) -> Result<String> {
    let data: Vec<u8> = std::fs::read(path)?;
    let mut hasher = Md5::new();
    hasher.update(&data);
    let result = hasher.finalize();
    Ok(format!("{:x}", result))
}
