use anyhow::Result;
use std::path::PathBuf;

pub fn calculate_crc32(path: PathBuf) -> Result<u32> {
    let data: Vec<u8> = std::fs::read(path)?;
    Ok(crc32fast::hash(&data))
}
