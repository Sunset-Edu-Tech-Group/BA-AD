use std::sync::Mutex;

use lazy_static::lazy_static;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum LogLevel {
    Info,
    Warning,
    Error,
    Debug,
}

#[derive(Debug, Clone)]
pub struct LogMessage {
    pub level: LogLevel,
    pub message: String,
}

lazy_static! {
    static ref LOGS: Mutex<Vec<LogMessage>> = Mutex::new(Vec::new());
    static ref VERBOSE_MODE: Mutex<bool> = Mutex::new(false);
}

pub fn set_verbose_mode(enabled: bool) {
    let mut verbose = VERBOSE_MODE.lock().unwrap();
    *verbose = enabled;
}

pub fn is_verbose_enabled() -> bool {
    *VERBOSE_MODE.lock().unwrap()
}

pub fn log(level: LogLevel, message: String) {
    // if level == LogLevel::Debug && !is_verbose_enabled() {
    //     return;
    // }

    // let log_message = LogMessage { level, message };

    // if let Ok(mut logs) = LOGS.lock() {
    //     logs.push(log_message);
    // }
}

pub fn get_log_messages() -> Vec<LogMessage> {
    LOGS.lock().unwrap().clone()
}
