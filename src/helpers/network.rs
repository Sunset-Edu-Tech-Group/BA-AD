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

pub fn format_speed(speed_kbps: u64) -> String {
    if speed_kbps >= 1024 * 1024 {
        format!("{:.2} Gbps", speed_kbps as f64 / (1024.0 * 1024.0))
    } else if speed_kbps >= 1024 {
        format!("{:.2} Mbps", speed_kbps as f64 / 1024.0)
    } else if speed_kbps > 0 {
        format!("{} kbps", speed_kbps)
    } else {
        "0 kbps".to_string()
    }
}

pub fn format_size(size: u64) -> String {
    const KB: f64 = 1024.0;
    const MB: f64 = KB * 1024.0;
    const GB: f64 = MB * 1024.0;
    const TB: f64 = GB * 1024.0;

    let size_f64 = size as f64;

    if size_f64 >= TB {
        format!("{:.2} TB", size_f64 / TB)
    } else if size_f64 >= GB {
        format!("{:.2} GB", size_f64 / GB)
    } else if size_f64 >= MB {
        format!("{:.2} MB", size_f64 / MB)
    } else if size_f64 >= KB {
        format!("{:.2} KB", size_f64 / KB)
    } else if size == 0 {
        "0 B".to_string()
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
