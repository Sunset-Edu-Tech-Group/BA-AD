use std::time::Duration;

use anyhow::Result;
use reqwest::Client;

pub async fn get_content_length(client: &Client, download_url: &str) -> Result<u64> {
    let response = client.get(download_url).header("Range", "bytes=0-0").send().await?;

    let remote_size: u64 = if let Some(content_range) = response.headers().get("Content-Range") {
        content_range
            .to_str()
            .ok()
            .and_then(|range| range.split('/').last())
            .and_then(|size| size.parse::<u64>().ok())
            .unwrap_or(0)
    } else {
        response.content_length().unwrap_or(0).saturating_add(1)
    };

    Ok(remote_size)
}

pub fn format_size(size: u64) -> String {
    const KB: u64 = 1024;
    const MB: u64 = KB * 1024;
    const GB: u64 = MB * 1024;

    if size >= GB {
        format!("{:.2} GB", size as f64 / GB as f64)
    } else if size >= MB {
        format!("{:.2} MB", size as f64 / MB as f64)
    } else if size >= KB {
        format!("{:.2} KB", size as f64 / KB as f64)
    } else {
        format!("{} B", size)
    }
}

pub fn format_elapsed(elapsed: Duration) -> String {
    let hours: u64 = elapsed.as_secs() / 3600;
    let minutes: u64 = (elapsed.as_secs() % 3600) / 60;
    let seconds: u64 = elapsed.as_secs() % 60;

    format!("[{:02}:{:02}:{:02}]", hours, minutes, seconds)
}
