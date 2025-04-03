use std::io::{self, Stdout};
use std::sync::{Arc, Mutex};
use std::thread::{self, JoinHandle};
use std::time::{Duration, Instant};

use anyhow::Result;
use crossterm::event::{self, Event, KeyCode, KeyEvent, KeyModifiers, poll};
use crossterm::execute;
use crossterm::terminal::{EnterAlternateScreen, LeaveAlternateScreen, disable_raw_mode, enable_raw_mode};
use ratatui::prelude::*;
use ratatui::style::{Modifier, Style};
use ratatui::widgets::{Block, Borders, List, ListDirection, ListItem, ListState, Paragraph};

use crate::helpers::logs::{self, LogLevel, LogMessage};
use crate::helpers::progress::{ProgressData, draw_progress};

lazy_static::lazy_static! {
    pub static ref PROGRESS_DATA: Mutex<ProgressData> = Mutex::new(ProgressData::default());
    pub static ref DOWNLOAD_START_TIME: Mutex<Option<Instant>> = Mutex::new(None);
    static ref UI_HANDLE: Mutex<Option<UiHandle>> = Mutex::new(None);

}

pub struct TerminalUI {
    terminal: Terminal<CrosstermBackend<Stdout>>,
    log_scroll_offset: usize,
    running: Arc<Mutex<bool>>,
    auto_scroll: bool,
    last_message_count: usize,
}

pub struct UiHandle {
    running: Arc<Mutex<bool>>,
    thread_handle: Option<JoinHandle<Result<()>>>,
}

impl UiHandle {
    pub fn new(running: Arc<Mutex<bool>>, thread_handle: JoinHandle<Result<()>>) -> Self {
        Self {
            running,
            thread_handle: Some(thread_handle),
        }
    }

    pub fn stop(&mut self) -> Result<()> {
        {
            let mut running = self.running.lock().unwrap();
            *running = false;
        }

        if let Some(thread_handle) = self.thread_handle.take() {
            thread_handle.join().unwrap()?;
        }

        Ok(())
    }

    #[allow(dead_code)]
    pub fn is_running(&self) -> bool {
        *self.running.lock().unwrap()
    }
}

impl Drop for UiHandle {
    fn drop(&mut self) {
        let _ = self.stop();
    }
}

impl TerminalUI {
    pub fn new() -> Result<Self> {
        enable_raw_mode()?;

        let mut stdout = io::stdout();

        execute!(stdout, EnterAlternateScreen)?;

        let backend = CrosstermBackend::new(stdout);
        let terminal = Terminal::new(backend)?;

        Ok(Self {
            terminal,
            log_scroll_offset: 0,
            running: Arc::new(Mutex::new(true)),
            auto_scroll: true,
            last_message_count: 0,
        })
    }

    pub fn start_in_background(mut self) -> UiHandle {
        let running = Arc::new(Mutex::new(true));

        let thread_handle = thread::spawn(move || {
            let result = self.run();
            result
        });

        UiHandle::new(running, thread_handle)
    }

    pub fn run(&mut self) -> Result<()> {
        let tick_rate = Duration::from_millis(1000);
        let mut last_tick = Instant::now();

        while *self.running.lock().unwrap() {
            let log_messages = logs::get_log_messages();
            let message_count = log_messages.len();

            if self.auto_scroll && message_count > self.last_message_count {
                self.log_scroll_offset = if message_count > 0 { message_count - 1 } else { 0 };
            }

            self.last_message_count = message_count;

            {
                let mut progress_data = PROGRESS_DATA.lock().unwrap();
                let start_time = *DOWNLOAD_START_TIME.lock().unwrap();
                if let Some(start) = start_time {
                    progress_data.update_elapsed(start.elapsed());
                }
            }

            let log_scroll_offset = self.log_scroll_offset;
            let progress_data = PROGRESS_DATA.lock().unwrap().clone();

            self.terminal.draw(|frame| {
                let chunks = Layout::default()
                    .direction(Direction::Vertical)
                    .constraints([Constraint::Min(5), Constraint::Length(3)])
                    .split(frame.area());

                draw_logs(frame, &log_messages, log_scroll_offset, chunks[0]);
                draw_progress(frame, chunks[1], &progress_data);
            })?;

            let timeout = tick_rate.checked_sub(last_tick.elapsed()).unwrap_or_else(|| Duration::from_secs(0));

            self.handle_events(timeout)?;

            if last_tick.elapsed() >= tick_rate {
                last_tick = Instant::now();
            }
        }

        Ok(())
    }

    fn handle_events(&mut self, timeout: Duration) -> Result<()> {
        if poll(timeout)? {
            if let Event::Key(KeyEvent { code, modifiers, .. }) = event::read()? {
                match code {
                    KeyCode::Char('c') if modifiers.contains(KeyModifiers::CONTROL) => {
                        let mut running = self.running.lock().unwrap();
                        *running = false;
                    }
                    KeyCode::Up => {
                        if self.log_scroll_offset > 0 {
                            self.log_scroll_offset -= 1;
                            self.auto_scroll = false;
                        }
                    }
                    KeyCode::Down => {
                        let log_messages = logs::get_log_messages();
                        if !log_messages.is_empty() && self.log_scroll_offset < log_messages.len() - 1 {
                            self.log_scroll_offset += 1;

                            if self.log_scroll_offset >= log_messages.len() - 1 {
                                self.auto_scroll = true;
                            }
                        }
                    }
                    KeyCode::Char('a') => {
                        self.auto_scroll = !self.auto_scroll;
                    }
                    KeyCode::End => {
                        let log_messages = logs::get_log_messages();
                        if !log_messages.is_empty() {
                            self.log_scroll_offset = log_messages.len() - 1;
                            self.auto_scroll = true;
                        }
                    }
                    KeyCode::Home => {
                        self.log_scroll_offset = 0;
                        self.auto_scroll = false;
                    }
                    _ => {}
                }
            }
        }
        Ok(())
    }
}

fn draw_logs(frame: &mut Frame<'_>, log_messages: &[LogMessage], log_scroll_offset: usize, area: Rect) {
    let block = Block::default().borders(Borders::ALL).title("Blue Archive Asset Downloader");

    if log_messages.is_empty() {
        let no_logs_text = Paragraph::new("No logs to display").style(Style::default().fg(Color::Gray)).block(block);
        frame.render_widget(no_logs_text, area);
    } else {
        let items: Vec<ListItem> = log_messages
            .iter()
            .map(|msg| {
                let style = match msg.level {
                    LogLevel::Info => Style::default().fg(Color::Green),
                    LogLevel::Warning => Style::default().fg(Color::Yellow),
                    LogLevel::Error => Style::default().fg(Color::Red),
                    LogLevel::Debug => Style::default().fg(Color::Blue),
                };

                let prefix = match msg.level {
                    LogLevel::Info => "[INFO] ",
                    LogLevel::Warning => "[WARN] ",
                    LogLevel::Error => "[ERROR] ",
                    LogLevel::Debug => "[DEBUG] ",
                };

                ListItem::new(format!("{}{}", prefix, msg.message)).style(style)
            })
            .collect();

        let logs_list = List::new(items)
            .block(block)
            .highlight_style(Style::default().add_modifier(Modifier::BOLD))
            .direction(ListDirection::TopToBottom);

        let mut state = ListState::default();
        if !log_messages.is_empty() {
            state.select(Some(log_scroll_offset.min(log_messages.len() - 1)));
        }

        frame.render_stateful_widget(logs_list, area, &mut state);
    }
}

impl Drop for TerminalUI {
    fn drop(&mut self) {
        let _ = disable_raw_mode();
        let _ = execute!(self.terminal.backend_mut(), LeaveAlternateScreen);
    }
}

pub fn start_download_progress(total_files: usize, total_size: u64) {
    let mut progress_data = PROGRESS_DATA.lock().unwrap();
    progress_data.start_timer();
    progress_data.update_from_download(0, total_files, 0, total_size, 0, None);

    let mut start_time = DOWNLOAD_START_TIME.lock().unwrap();
    *start_time = Some(Instant::now());
}

pub fn update_download_progress(
    downloaded_files: usize,
    total_files: usize,
    downloaded_size: u64,
    total_size: u64,
    speed_kbps: u64,
    current_file: Option<String>,
) {
    let mut progress_data = PROGRESS_DATA.lock().unwrap();
    progress_data.update_from_download(downloaded_files, total_files, downloaded_size, total_size, speed_kbps, current_file);
}

pub fn start_detailed_progress(total_size: u64) {
    let mut progress_data = PROGRESS_DATA.lock().unwrap();
    progress_data.set_detailed();
    progress_data.start_timer();
    progress_data.update_from_download(0, 1, 0, total_size, 0, None);

    let mut start_time = DOWNLOAD_START_TIME.lock().unwrap();
    *start_time = Some(Instant::now());
}

pub fn start_simple_progress(total_files: usize) {
    let mut progress_data = PROGRESS_DATA.lock().unwrap();
    progress_data.set_simple();
    progress_data.start_timer();
    progress_data.update_from_download(0, total_files, 0, 0, 0, None);

    let mut start_time = DOWNLOAD_START_TIME.lock().unwrap();
    *start_time = Some(Instant::now());
}

pub fn reset_download_progress() {
    let mut progress_data = PROGRESS_DATA.lock().unwrap();
    progress_data.set_empty();

    let mut start_time = DOWNLOAD_START_TIME.lock().unwrap();
    *start_time = None;
}

pub fn init_ui() -> Result<()> {
    // let ui: TerminalUI = TerminalUI::new()?;
    // let handle: UiHandle = ui.start_in_background();

    // let mut ui_handle = UI_HANDLE.lock().unwrap();
    // *ui_handle = Some(handle);

    Ok(())
}

#[allow(dead_code)]
pub fn is_ui_running() -> bool {
    let ui_handle = UI_HANDLE.lock().unwrap();
    ui_handle.as_ref().map_or(false, |handle| handle.is_running())
}
pub fn shutdown_ui() -> Result<()> {
    // let mut ui_handle = UI_HANDLE.lock().unwrap();
    // if let Some(mut handle) = ui_handle.take() {
    //     handle.stop()?;
    // }
    Ok(())
}
