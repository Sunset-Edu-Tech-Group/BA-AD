#[macro_export]
macro_rules! info {
    ($($arg:tt)*) => {
        #[cfg(feature = "logs")]
        paris::output::format_stdout(format!("<blue>[INFO]</> {}", format!($($arg)*)), "\n")
    }
}

#[macro_export]
macro_rules! debug {
    ($($arg:tt)*) => {
        #[cfg(feature = "debug")]
        paris::output::format_stdout(format!("<cyan>[DEBUG]</> {}", format!($($arg)*)), "\n")
    }
}

#[macro_export]
macro_rules! success {
    ($($arg:tt)*) => {
        #[cfg(feature = "logs")]
        paris::output::format_stdout(format!("<green>[SUCCESS]</> {}", format!($($arg)*)), "\n")
    }
}

#[macro_export]
macro_rules! error {
    ($($arg:tt)*) => {
        #[cfg(not(feature = "no_error"))]
        paris::output::format_stdout(format!("<red>[ERROR]</> {}", format!($($arg)*)), "\n")
    }
}

#[macro_export]
macro_rules! warn {
    ($($arg:tt)*) => {
        #[cfg(feature = "logs")]
        paris::output::format_stdout(format!("<yellow>[WARN]</> {}", format!($($arg)*)), "\n")
    }
}