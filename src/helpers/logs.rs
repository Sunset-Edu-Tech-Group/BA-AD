use std::sync::{Arc, Mutex};
use std::time::SystemTime;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum LogLevel {
    Info,
    Warning,
    Error,
    Debug,
}

#[derive(Debug, Clone)]
pub struct LogMessage {
    pub timestamp: SystemTime,
    pub level: LogLevel,
    pub message: String,
}

pub struct Logger {
    messages: Arc<Mutex<Vec<LogMessage>>>,
    max_messages: usize,
}

impl Default for Logger {
    fn default() -> Self {
        Self::new(100)
    }
}

impl Logger {
    pub fn new(max_messages: usize) -> Self {
        Self {
            messages: Arc::new(Mutex::new(Vec::new())),
            max_messages,
        }
    }

    pub fn log(&self, level: LogLevel, message: &str) {
        let log_message = LogMessage {
            timestamp: SystemTime::now(),
            level,
            message: message.to_string(),
        };

        let mut messages = self.messages.lock().unwrap();
        messages.push(log_message);

        let messages_length: usize = messages.len();
        if messages_length > self.max_messages {
            let to_remove = messages_length - self.max_messages;
            messages.drain(0..to_remove);
        }
    }

    pub fn info(&self, message: &str) {
        self.log(LogLevel::Info, message);
    }

    pub fn warn(&self, message: &str) {
        self.log(LogLevel::Warning, message);
    }

    pub fn error(&self, message: &str) {
        self.log(LogLevel::Error, message);
    }

    pub fn debug(&self, message: &str) {
        self.log(LogLevel::Debug, message);
    }

    pub fn get_messages(&self) -> Vec<LogMessage> {
        let messages = self.messages.lock().unwrap();
        messages.clone()
    }

    pub fn clear(&self) {
        let mut messages = self.messages.lock().unwrap();
        messages.clear();
    }
}

lazy_static::lazy_static! {
    static ref LOGGER: Logger = Logger::default();
}

pub fn info(message: &str) {
    LOGGER.info(message);
}

pub fn warn(message: &str) {
    LOGGER.warn(message);
}

pub fn error(message: &str) {
    LOGGER.error(message);
}

pub fn debug(message: &str) {
    LOGGER.debug(message);
}

pub fn get_log_messages() -> Vec<LogMessage> {
    LOGGER.get_messages()
}

pub fn clear_logs() {
    LOGGER.clear();
}
