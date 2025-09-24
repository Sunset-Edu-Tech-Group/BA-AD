use thiserror::Error;

#[derive(Error, Debug)]
pub enum ServerConfigError {
    #[error("Teen build is only available for Global server")]
    TeenNotAvailable,

    #[error("Unsupported platform and build type combination")]
    UnsupportedCombination,
}

#[derive(Error, Debug)]
pub enum NetworkError {
    #[error("{0}")]
    Reqwest(#[from] reqwest::Error)
}

#[derive(Error, Debug)]
pub enum JsonError {
    #[error("{0}")]
    SerdeJson(#[from] serde_json::Error),

    #[error("{0}")]
    Io(#[from] std::io::Error),

    #[error("{0}")]
    File(#[from] baad_core::error::FileError),

    #[error("Failed to convert file content to UTF-8")]
    InvalidUtf8,

    #[error("Failed to get file path")]
    PathError,
}

#[derive(Error, Debug)]
pub enum FilterError {
    #[error("Invalid regex pattern: {pattern}")]
    InvalidRegex { pattern: Box<str> },

    #[error("Invalid glob pattern: {pattern}")]
    InvalidGlob { pattern: Box<str> },
}

#[derive(Error, Debug)]
pub enum DownloadError {
    #[error("{0}")]
    Json(#[from] JsonError),

    #[error("{0}")]
    File(#[from] baad_core::error::FileError),

    #[error("{0}")]
    Network(#[from] NetworkError),

    #[error("Retry count cannot be zero")]
    RetryCountZero,

    #[error("Download limit cannot be zero")]
    DownloadLimitZero,

    #[error("No files matched filter criteria")]
    NoFilesMatched,
}

#[derive(Error, Debug)]
pub enum CatalogError {
    #[error("{0}")]
    Json(#[from] JsonError),

    #[error("{0}")]
    File(#[from] baad_core::error::FileError),

    #[error("{0}")]
    Apk(#[from] ApkError),

    #[error("{0}")]
    Reqwest(#[from] reqwest::Error),

    #[error("{0}")]
    Network(#[from] NetworkError),

    #[error("{0}")]
    SerdeJson(#[from] serde_json::Error),

    #[error("{0}")]
    WalkDir(#[from] walkdir::Error),

    #[error("{0}")]
    Io(#[from] std::io::Error),

    #[error("Catalog URL is empty for {region} region")]
    EmptyCatalogUrl { region: Box<str> },

    #[error("Failed to deserialize catalog data")]
    DeserializationFailed,
}

#[derive(Error, Debug)]
pub enum ApkError {
    #[error("{0}")]
    Json(#[from] JsonError),

    #[error("{0}")]
    File(#[from] baad_core::error::FileError),

    #[error("{0}")]
    Network(#[from] NetworkError),

    #[error("{0}")]
    Reqwest(#[from] reqwest::Error),

    #[error("{0}")]
    Url(#[from] url::ParseError),

    #[error("{0}")]
    Zip(#[from] zip::result::ZipError),

    #[error("{0}")]
    Glob(#[from] glob::PatternError),

    #[error("{0}")]
    Io(#[from] std::io::Error),

    #[error("Failed to extract version from server response")]
    VersionExtractionFailed,

    #[error("Failed to get download URL")]
    DownloadUrlExtractionFailed,

    #[error("Failed to get APK info")]
    ApkInfoFailed,
}
