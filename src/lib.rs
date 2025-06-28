pub mod apk;
pub mod catalog;
pub mod helpers;
pub mod utils;
pub mod download;
#[doc(hidden)]
pub mod cli;

pub use paris;

use std::sync::atomic::AtomicBool;
pub static VERBOSE: AtomicBool = AtomicBool::new(false);