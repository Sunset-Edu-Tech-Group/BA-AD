use indicatif::{ProgressBar, ProgressStyle};
use std::time::Duration;

pub struct DownloadProgress {
    pub progress_bar: ProgressBar,
}

impl DownloadProgress {
    pub fn new(total_size: u64) -> Self {
        let progress_bar: ProgressBar = ProgressBar::new(total_size);
        progress_bar.set_style(
            ProgressStyle::default_bar()
                .template("{spinner:} [{elapsed_precise}] {bar:40} {bytes:>}/{total_bytes:<} {bytes_per_sec:>} eta {eta}")
                .unwrap()
                .progress_chars("━╾╴─"),
        );

        progress_bar.enable_steady_tick(Duration::from_millis(100));

        Self { progress_bar }
    }

    pub fn inc(&self, n: u64) {
        self.progress_bar.inc(n);
    }

    pub fn finish_with_message(&self, msg: &str) {
        self.progress_bar.finish_with_message(msg.to_string());
    }
}
