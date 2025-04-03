#[macro_export]
macro_rules! info {
    ($($arg:tt)*) => {
        // Instead of logging to UI, just print to stdout
        println!("[INFO] {}", format!($($arg)*))
    }
}

#[macro_export]
macro_rules! warn {
    ($($arg:tt)*) => {
        // Print to stderr for warnings
        eprintln!("[WARN] {}", format!($($arg)*))
    }
}

#[macro_export]
macro_rules! error {
    ($($arg:tt)*) => {
        // Print to stderr for errors
        eprintln!("[ERROR] {}", format!($($arg)*))
    }
}

#[macro_export]
macro_rules! debug {
    ($($arg:tt)*) => {
        // Only print debug when verbose mode is enabled
        if crate::helpers::logs::is_verbose_enabled() {
            println!("[DEBUG] {}", format!($($arg)*))
        }
    }
}
