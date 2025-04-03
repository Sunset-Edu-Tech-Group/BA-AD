#[macro_export]
macro_rules! info {
    ($($arg:tt)*) => {
        crate::helpers::logs::log(crate::helpers::logs::LogLevel::Info, format!($($arg)*));
    }
}

#[macro_export]
macro_rules! warn {
    ($($arg:tt)*) => {
        crate::helpers::logs::log(crate::helpers::logs::LogLevel::Warning, format!($($arg)*));
    }
}

#[macro_export]
macro_rules! error {
    ($($arg:tt)*) => {
        crate::helpers::logs::log(crate::helpers::logs::LogLevel::Error, format!($($arg)*));
    }
}

#[macro_export]
macro_rules! debug {
    ($($arg:tt)*) => {
        if crate::helpers::logs::is_verbose_enabled() {
            crate::helpers::logs::log(crate::helpers::logs::LogLevel::Debug, format!($($arg)*));
        }
    }
}
