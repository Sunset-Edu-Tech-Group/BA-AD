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
                #[cfg(not(feature = "no_error"))]
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
                #[cfg(not(feature = "no_error"))]
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
                #[cfg(not(feature = "no_error"))]
                error!("File or directory not found");
                Error::from(err)
            }
            io::ErrorKind::PermissionDenied => {
                #[cfg(not(feature = "no_error"))]
                error!("Permission denied - check file/directory permissions");
                Error::from(err)
            }
            io::ErrorKind::AlreadyExists => {
                #[cfg(not(feature = "no_error"))]
                error!("File or directory already exists");
                Error::from(err)
            }
            io::ErrorKind::InvalidData => {
                #[cfg(not(feature = "no_error"))]
                error!("Invalid or corrupted data");
                Error::from(err)
            }
            io::ErrorKind::UnexpectedEof => {
                #[cfg(not(feature = "no_error"))]
                error!("Unexpected end of file - file may be truncated or corrupted");
                Error::from(err)
            }
            io::ErrorKind::WriteZero => {
                #[cfg(not(feature = "no_error"))]
                error!("Write operation failed - disk may be full");
                Error::from(err)
            }
            io::ErrorKind::Interrupted => {
                #[cfg(not(feature = "no_error"))]
                error!("Operation was interrupted");
                Error::from(err)
            }
            _ => {
                #[cfg(not(feature = "no_error"))]
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
                        #[cfg(not(feature = "no_error"))]
                        error!("Directory or file not found while walking directory tree");
                    }
                    io::ErrorKind::PermissionDenied => {
                        #[cfg(not(feature = "no_error"))]
                        error!("Permission denied while accessing directory or file");
                    }
                    io::ErrorKind::InvalidData => {
                        #[cfg(not(feature = "no_error"))]
                        error!("Invalid file system data encountered");
                    }
                    _ => {
                        #[cfg(not(feature = "no_error"))]
                        error!("I/O error while walking directory: {}", io_err);
                    }
                }
            } else if let Some(path) = err.path() {
                #[cfg(not(feature = "no_error"))]
                error!("Directory walk error at path '{}': {}", path.display(), err);
            } else {
                #[cfg(not(feature = "no_error"))]
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
                        io::ErrorKind::NotFound => {
                            #[cfg(not(feature = "no_error"))]
                            error!("ZIP file not found")
                        },
                        io::ErrorKind::PermissionDenied => {
                            #[cfg(not(feature = "no_error"))]
                            error!("Permission denied accessing ZIP file")
                        },
                        io::ErrorKind::UnexpectedEof => {
                            #[cfg(not(feature = "no_error"))]
                            error!("ZIP file is truncated or corrupted")
                        },
                        _ => {
                            #[cfg(not(feature = "no_error"))]
                            error!("I/O error while processing ZIP file: {}", io_err)
                        },
                    }
                }
                ZipError::InvalidArchive(msg) => {
                    #[cfg(not(feature = "no_error"))]
                    error!("Invalid ZIP archive: {}", msg);
                }
                ZipError::UnsupportedArchive(msg) => {
                    #[cfg(not(feature = "no_error"))]
                    error!("Unsupported ZIP archive format: {}", msg);
                }
                ZipError::FileNotFound => {
                    #[cfg(not(feature = "no_error"))]
                    error!("File not found in ZIP archive");
                }
                _ => {
                    #[cfg(not(feature = "no_error"))]
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
            #[cfg(not(feature = "no_error"))]
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
                    #[cfg(not(feature = "no_error"))]
                    error!("JSON I/O error - file may be corrupted or inaccessible");
                }
                serde_json::error::Category::Syntax => {
                    #[cfg(not(feature = "no_error"))]
                    error!("JSON syntax error at line {}, column {} - file contains invalid JSON", 
                           err.line(), err.column());
                }
                serde_json::error::Category::Data => {
                    #[cfg(not(feature = "no_error"))]
                    error!("JSON data error - structure doesn't match expected format");
                }
                serde_json::error::Category::Eof => {
                    #[cfg(not(feature = "no_error"))]
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
                #[cfg(not(feature = "no_error"))]
                error!("Request timed out - check your internet connection");
            } else if err.is_redirect() {
                #[cfg(not(feature = "no_error"))]
                error!("Too many redirects");
            } else if err.is_decode() {
                #[cfg(not(feature = "no_error"))]
                error!("Failed to decode response");
            } else if let Some(status) = err.status() {
                match status.as_u16() {
                    404 => {
                        #[cfg(not(feature = "no_error"))]
                        error!("Resource not found (404)")
                    },
                    403 => {
                        #[cfg(not(feature = "no_error"))]
                        error!("Access forbidden (403)")
                    },
                    401 => {
                        #[cfg(not(feature = "no_error"))]
                        error!("Unauthorized (401)")
                    },
                    429 => {
                        #[cfg(not(feature = "no_error"))]
                        error!("Too many requests (429) - rate limited")
                    },
                    500..=599 => {
                        #[cfg(not(feature = "no_error"))]
                        error!("Server error ({}) - try again later", status)
                    },
                    _ => {
                        #[cfg(not(feature = "no_error"))]
                        error!("HTTP error ({})", status)
                    },
                }
            } else {
                #[cfg(not(feature = "no_error"))]
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
                #[cfg(not(feature = "no_error"))]
                error!("File contains invalid text encoding");
            } else if err.to_string().contains("base64") {
                #[cfg(not(feature = "no_error"))]
                error!("Invalid base64 encoding");
            } else if err.to_string().contains("regex") || err.to_string().contains("pattern") {
                #[cfg(not(feature = "no_error"))]
                error!("Invalid regular expression or pattern");
            } else {
                //
            }
            err
        })
    }
}