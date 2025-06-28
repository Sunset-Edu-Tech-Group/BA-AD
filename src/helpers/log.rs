#[macro_export]
macro_rules! info {
    ($($arg:tt)*) => {
        #[cfg(not(feature = "no_logs"))]
        $crate::paris::output::format_stdout(format!("<blue>[INFO]</> {}", format!($($arg)*)), "\n")
    }
}

#[macro_export]
macro_rules! debug {
    ($($arg:tt)*) => {
        #[cfg(not(any(feature = "no_debug", feature = "no_logs")))]
        {
            if $crate::VERBOSE.load(std::sync::atomic::Ordering::Relaxed) {
                $crate::paris::output::format_stdout(format!("<cyan>[DEBUG]</> {}", format!($($arg)*)), "\n")
            }
        }
    }
}

#[macro_export]
macro_rules! success {
    ($($arg:tt)*) => {
        #[cfg(not(feature = "no_logs"))]
        $crate::paris::output::format_stdout(format!("<green>[SUCCESS]</> {}", format!($($arg)*)), "\n")
    }
}

#[macro_export]
macro_rules! error {
    ($($arg:tt)*) => {
        #[cfg(not(any(feature = "no_error", feature = "no_logs")))]
        $crate::paris::output::format_stdout(format!("<red>[ERROR]</> {}", format!($($arg)*)), "\n")
    }
}

#[macro_export]
macro_rules! warn {
    ($($arg:tt)*) => {
        #[cfg(not(feature = "no_logs"))]
        $crate::paris::output::format_stdout(format!("<yellow>[WARN]</> {}", format!($($arg)*)), "\n")
    }
}