use crate::error;

use anyhow::{Context, Error, Result};
use glob::PatternError;
use serde_json::{Error as JsonError, Result as JsonResult};
use std::io;
use walkdir::Error as WalkDirError;
use zip::result::{ZipError, ZipResult};

pub trait ErrorExt<T, E> {
    fn handle_errors(self) -> Result<T>;
}

pub trait ErrorContext<T> {
    fn error_context(self, msg: &str) -> Result<T>;
}

impl<T, E> ErrorContext<T> for Result<T, E>
where
    E: Into<Error>,
{
    fn error_context(self, msg: &str) -> Result<T> {
        self.map_err(|e| e.into())
            .with_context(|| {
                let msg = msg.to_string();
                error!("{}", msg);
                msg
            })
    }
}

impl<T> ErrorContext<T> for Option<T> {
    fn error_context(self, msg: &str) -> Result<T> {
        match self {
            Some(value) => Ok(value),
            None => {
                error!("{}", msg);
                Err(anyhow::anyhow!("{}", msg))
            }
        }
    }
}

impl<T> ErrorExt<T, io::Error> for io::Result<T> {
    fn handle_errors(self) -> Result<T> {
        self.map_err(|err| match err.kind() {
            io::ErrorKind::NotFound => {
                error!("File or directory not found");
                Error::from(err)
            }
            io::ErrorKind::PermissionDenied => {
                error!("Permission denied - check file/directory permissions");
                Error::from(err)
            }
            io::ErrorKind::AlreadyExists => {
                error!("File or directory already exists");
                Error::from(err)
            }
            io::ErrorKind::InvalidData => {
                error!("Invalid or corrupted data");
                Error::from(err)
            }
            io::ErrorKind::UnexpectedEof => {
                error!("Unexpected end of file - file may be truncated or corrupted");
                Error::from(err)
            }
            io::ErrorKind::WriteZero => {
                error!("Write operation failed - disk may be full");
                Error::from(err)
            }
            io::ErrorKind::Interrupted => {
                error!("Operation was interrupted");
                Error::from(err)
            }
            _ => {
                error!("I/O error: {}", err);
                Error::from(err)
            }
        })
    }
}

impl<T> ErrorExt<T, WalkDirError> for Result<T, WalkDirError> {
    fn handle_errors(self) -> Result<T> {
        self.map_err(|err| {
            if let Some(io_err) = err.io_error() {
                match io_err.kind() {
                    io::ErrorKind::NotFound => {
                        error!("Directory or file not found while walking directory tree");
                    }
                    io::ErrorKind::PermissionDenied => {
                        error!("Permission denied while accessing directory or file");
                    }
                    io::ErrorKind::InvalidData => {
                        error!("Invalid file system data encountered");
                    }
                    _ => {
                        error!("I/O error while walking directory: {}", io_err);
                    }
                }
            } else if let Some(path) = err.path() {
                error!("Directory walk error at path '{}': {}", path.display(), err);
            } else {
                error!("Directory walk error: {}", err);
            }
            Error::from(err)
        })
    }
}

impl<T> ErrorExt<T, ZipError> for ZipResult<T> {
    fn handle_errors(self) -> Result<T> {
        self.map_err(|err| {
            match &err {
                ZipError::Io(io_err) => {
                    match io_err.kind() {
                        io::ErrorKind::NotFound => error!("ZIP file not found"),
                        io::ErrorKind::PermissionDenied => error!("Permission denied accessing ZIP file"),
                        io::ErrorKind::UnexpectedEof => error!("ZIP file is truncated or corrupted"),
                        _ => error!("I/O error while processing ZIP file: {}", io_err),
                    }
                }
                ZipError::InvalidArchive(msg) => {
                    error!("Invalid ZIP archive: {}", msg);
                }
                ZipError::UnsupportedArchive(msg) => {
                    error!("Unsupported ZIP archive format: {}", msg);
                }
                ZipError::FileNotFound => {
                    error!("File not found in ZIP archive");
                }
                _ => {
                    error!("ZIP archive error: {}", err);
                }
            }
            Error::from(err)
        })
    }
}

impl<T> ErrorExt<T, PatternError> for Result<T, PatternError> {
    fn handle_errors(self) -> Result<T> {
        self.map_err(|err| {
            error!("Invalid glob pattern: {}", err);
            Error::from(err)
        })
    }
}

impl<T> ErrorExt<T, JsonError> for JsonResult<T> {
    fn handle_errors(self) -> Result<T> {
        self.map_err(|err| {
            match err.classify() {
                serde_json::error::Category::Io => {
                    error!("JSON I/O error - file may be corrupted or inaccessible");
                }
                serde_json::error::Category::Syntax => {
                    error!("JSON syntax error at line {}, column {} - file contains invalid JSON", 
                           err.line(), err.column());
                }
                serde_json::error::Category::Data => {
                    error!("JSON data error - structure doesn't match expected format");
                }
                serde_json::error::Category::Eof => {
                    error!("JSON parse error - unexpected end of file");
                }
            }
            Error::from(err)
        })
    }
}

impl<T> ErrorExt<T, reqwest::Error> for reqwest::Result<T> {
    fn handle_errors(self) -> Result<T> {
        self.map_err(|err| {
            if err.is_timeout() || err.is_connect(){
                error!("Request timed out - check your internet connection");
            } else if err.is_redirect() {
                error!("Too many redirects");
            } else if err.is_decode() {
                error!("Failed to decode response");
            } else if let Some(status) = err.status() {
                match status.as_u16() {
                    404 => error!("Resource not found (404)"),
                    403 => error!("Access forbidden (403)"),
                    401 => error!("Unauthorized (401)"),
                    429 => error!("Too many requests (429) - rate limited"),
                    500..=599 => error!("Server error ({}) - try again later", status),
                    _ => error!("HTTP error ({})", status),
                }
            } else {
                error!("Network error: {}", err);
            }
            Error::from(err)
        })
    }
}

impl<T> ErrorExt<T, Error> for Result<T> {
    fn handle_errors(self) -> Result<T> {
        self.map_err(|err| {
            if err.to_string().contains("UTF-8") || err.to_string().contains("utf8") {
                error!("File contains invalid text encoding");
            } else if err.to_string().contains("base64") {
                error!("Invalid base64 encoding");
            } else if err.to_string().contains("regex") || err.to_string().contains("pattern") {
                error!("Invalid regular expression or pattern");
            } else {
                //
            }
            err
        })
    }
}