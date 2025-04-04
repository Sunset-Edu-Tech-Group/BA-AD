use std::time::Duration;

use ratatui::prelude::*;
use ratatui::style::{Color, Style};
use ratatui::widgets::{Block, Borders, Gauge, Paragraph};

use crate::helpers::network;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum ProgressState {
    Empty,
    Simple,
    Detailed,
}

impl Default for ProgressState {
    fn default() -> Self {
        ProgressState::Empty
    }
}

#[derive(Debug, Clone)]
pub struct ProgressData {
    pub state: ProgressState,
    pub elapsed: Duration,
    pub downloaded_files: usize,
    pub total_files: usize,
    pub downloaded_size: u64,
    pub total_size: u64,
    pub speed: u64,
    pub current_file: String,
}

impl Default for ProgressData {
    fn default() -> Self {
        Self {
            state: ProgressState::default(),
            elapsed: Duration::from_secs(0),
            downloaded_files: 0,
            total_files: 0,
            downloaded_size: 0,
            total_size: 0,
            speed: 0,
            current_file: String::new(),
        }
    }
}

impl ProgressData {
    pub fn progress_ratio(&self) -> f64 {
        match self.state {
            ProgressState::Empty => 0.0,
            ProgressState::Simple => {
                if self.total_files == 0 {
                    0.0
                } else {
                    self.downloaded_files as f64 / self.total_files as f64
                }
            }
            ProgressState::Detailed => {
                if self.total_size == 0 {
                    0.0
                } else {
                    self.downloaded_size as f64 / self.total_size as f64
                }
            }
        }
    }

    pub fn update_progress(
        &mut self,
        downloaded_files: usize,
        total_files: usize,
        downloaded_size: u64,
        total_size: u64,
        speed: u64,
        current_file: Option<String>,
    ) {
        self.downloaded_files = downloaded_files;
        self.total_files = total_files;
        self.downloaded_size = downloaded_size;
        self.total_size = total_size;
        self.speed = speed;

        if let Some(file) = current_file {
            self.current_file = file;
        }
    }

    pub fn start_timer(&mut self) {
        self.elapsed = Duration::from_secs(0);
    }

    pub fn update_elapsed(&mut self, elapsed: Duration) {
        self.elapsed = elapsed;
    }

    pub fn set_empty(&mut self) {
        self.state = ProgressState::Empty;
        self.reset();
    }

    pub fn set_simple(&mut self) {
        self.state = ProgressState::Simple;
    }

    pub fn set_detailed(&mut self) {
        self.state = ProgressState::Detailed;
    }

    fn reset(&mut self) {
        self.downloaded_files = 0;
        self.total_files = 0;
        self.downloaded_size = 0;
        self.total_size = 0;
        self.speed = 0;
        self.current_file = String::new();
    }
}

pub fn draw_progress(frame: &mut Frame<'_>, area: Rect, progress_data: &ProgressData) {
    let block = Block::default()
        .title("Progress")
        .borders(Borders::ALL)
        .border_style(Style::default().fg(Color::Yellow));

    match progress_data.state {
        ProgressState::Empty => {
            let text = Paragraph::new("No downloads in progress")
                .block(block)
                .alignment(Alignment::Center)
                .style(Style::default().fg(Color::Gray));

            frame.render_widget(text, area);
        }
        ProgressState::Simple => {
            let percent = (progress_data.progress_ratio() * 100.0) as u16;
            let elapsed = network::format_elapsed(progress_data.elapsed);

            let label = format!(
                "{} | {} | {}% | {}/{}",
                elapsed,
                network::format_speed(progress_data.speed),
                percent,
                progress_data.downloaded_files,
                progress_data.total_files
            );

            let gauge = Gauge::default()
                .block(block)
                .gauge_style(Style::default().fg(Color::Blue).bg(Color::Black))
                .ratio(progress_data.progress_ratio())
                .label(label)
                .use_unicode(true);

            frame.render_widget(gauge, area);
        }
        ProgressState::Detailed => {
            let percent = (progress_data.progress_ratio() * 100.0) as u16;
            let elapsed = network::format_elapsed(progress_data.elapsed);
            let downloaded_size = network::format_size(progress_data.downloaded_size);
            let total_size = network::format_size(progress_data.total_size);

            let label = if !progress_data.current_file.is_empty() {
                format!(
                    "{} | {}/{} | {} | {}% | {}",
                    elapsed,
                    downloaded_size,
                    total_size,
                    network::format_speed(progress_data.speed),
                    percent,
                    progress_data.current_file
                )
            } else {
                format!(
                    "{} | {}/{} | {} | {}%",
                    elapsed,
                    downloaded_size,
                    total_size,
                    network::format_speed(progress_data.speed),
                    percent
                )
            };

            let gauge = Gauge::default()
                .block(block)
                .gauge_style(Style::default().fg(Color::Green).bg(Color::Black))
                .ratio(progress_data.progress_ratio())
                .label(label)
                .use_unicode(true);

            frame.render_widget(gauge, area);
        }
    }
}
