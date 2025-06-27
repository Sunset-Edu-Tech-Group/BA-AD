use reqwest::Response;

pub fn get_content_length(response: &Response) -> u64 {
    response.headers().get("Content-Range")
        .map_or_else(
            || response.content_length().unwrap_or(0).saturating_add(1),
            |content_range| {
                content_range
                    .to_str()
                    .ok()
                    .and_then(|range| range.split('/').next_back())
                    .and_then(|size| size.parse::<u64>().ok())
                    .unwrap_or(0)
            }
        )
}