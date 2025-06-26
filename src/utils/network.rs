use reqwest::Response;

pub fn get_content_length(response: &Response) -> u64 {
    if let Some(content_range) = response.headers().get("Content-Range") {
        content_range
            .to_str()
            .ok()
            .and_then(|range| range.split('/').next_back())
            .and_then(|size| size.parse::<u64>().ok())
            .unwrap_or(0)
    } else {
        response.content_length().unwrap_or(0).saturating_add(1)
    }
}