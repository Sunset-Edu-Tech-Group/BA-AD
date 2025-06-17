use anyhow::{anyhow, Result};
use regex::Regex;
use reqwest::{Client, Response};

use crate::helpers::config::{apk_headers, ServerConfig, JAPAN_REGEX_URL, JAPAN_REGEX_VERSION};

pub struct ApkFetcher {
    client: Client,
    config: ServerConfig,
}

impl ApkFetcher {
    pub fn new(config: ServerConfig) -> Result<Self> {
        let client: Client = Client::builder().default_headers(apk_headers()).build()?;

        Ok(Self { client, config })
    }

    pub fn extract_version(&self, body: &str) -> Result<String> {
        let version: Regex = Regex::new(JAPAN_REGEX_VERSION)?;
        version
            .find(body)
            .map(|m| m.as_str().to_string())
            .ok_or_else(|| anyhow!("Failed to find version in response"))
    }

    fn extract_download_url(&self, body: &str) -> Result<String> {
        let re_url: Regex = Regex::new(JAPAN_REGEX_URL)?;
        match re_url.captures(body) {
            Some(caps) if caps.len() >= 3 => Ok(caps.get(2).unwrap().as_str().to_string()),
            _ => Err(anyhow!("Failed to get download url")),
        }
    }

    async fn check_version(&self) -> Result<Option<String>> {
        let response: Response = self.client.get(&self.config.version_url).send().await?;
        if !response.status().is_success() {
            return Err(anyhow!(
                "Failed to get versions: {}",
                response.status()
            ));
        }

        let body: String = response.text().await?;
        let new_version: String = self.extract_version(&body)?;

        // json::update_japan_version(self.file_manager, &new_version).await?;

        Ok(Some(new_version))
    }
}
