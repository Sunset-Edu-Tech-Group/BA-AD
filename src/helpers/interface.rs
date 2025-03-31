use std::io::{self, Stdout};
use std::sync::{Arc, Mutex};
use std::thread::{self, JoinHandle};
use std::time::{Duration, Instant};

use anyhow::Result;
use crossterm::event::{self, Event, KeyCode, KeyEvent, KeyModifiers};
use crossterm::terminal::{disable_raw_mode, enable_raw_mode, EnterAlternateScreen, LeaveAlternateScreen};
use crossterm::execute;
use ratatui::prelude::*;
use ratatui::style::{Style, Modifier};
use ratatui::widgets::{Block, Borders, List, ListItem, ListDirection, ListState, Paragraph};

use crate::helpers::logs::{self, LogLevel};

pub struct TerminalUI {
    terminal: Terminal<CrosstermBackend<Stdout>>,
    log_scroll_offset: usize,
    running: Arc<Mutex<bool>>,
    auto_scroll: bool,
    last_message_count: usize,
}

lazy_static::lazy_static! {
    static ref UI_HANDLE: Mutex<Option<UiHandle>> = Mutex::new(None);
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
        
        if let Some(handle) = self.thread_handle.take() {
            handle.join().unwrap()?;
        }
        
        Ok(())
    }

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
        let running = self.running.clone();
        
        let thread_handle = thread::spawn(move || {
            let result = self.run();
            result
        });
        
        UiHandle::new(running, thread_handle)
    }

    pub fn run(&mut self) -> Result<()> {
        let tick_rate = Duration::from_millis(100);
        let mut last_tick = Instant::now();

        while *self.running.lock().unwrap() {
            let log_messages = logs::get_log_messages();
            let message_count = log_messages.len();

            if self.auto_scroll && message_count > self.last_message_count {
                self.log_scroll_offset = if message_count > 0 { message_count - 1 } else { 0 };
            }
            
            self.last_message_count = message_count;

            self.terminal.draw(|frame| {
                let size = frame.area();
                let block = Block::default()
                    .borders(Borders::ALL)
                    .title("Blue Archive Asset Downloader");
                
                if log_messages.is_empty() {
                    let no_logs_text = Paragraph::new("No logs to display")
                        .style(Style::default().fg(Color::Gray))
                        .block(block);
                    frame.render_widget(no_logs_text, size);
                } else {
                    let items: Vec<ListItem> = log_messages.iter()
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
                            
                            ListItem::new(format!("{}{}", prefix, msg.message))
                                .style(style)
                        })
                        .collect();
                    
                    let logs_list = List::new(items)
                        .block(block)
                        .highlight_style(Style::default().add_modifier(Modifier::BOLD))
                        .direction(ListDirection::TopToBottom); // Show oldest logs at the top
                    
                    let mut state = ListState::default();
                    if !log_messages.is_empty() {
                        state.select(Some(self.log_scroll_offset.min(log_messages.len() - 1)));
                    }
                    
                    frame.render_stateful_widget(logs_list, size, &mut state);
                }
            })?;

            let timeout = tick_rate
                .checked_sub(last_tick.elapsed())
                .unwrap_or_else(|| Duration::from_secs(0));

            if crossterm::event::poll(timeout)? {
                if let Event::Key(KeyEvent { code, modifiers, .. }) = event::read()? {
                    match code {
                        KeyCode::Char('c') if modifiers.contains(KeyModifiers::CONTROL) => {
                            let mut running = self.running.lock().unwrap();
                            *running = false;
                            break;
                        },
                        KeyCode::Up => {
                            if self.log_scroll_offset > 0 {
                                self.log_scroll_offset -= 1;
                                self.auto_scroll = false;
                            }
                        },
                        KeyCode::Down => {
                            let log_messages = logs::get_log_messages();
                            if !log_messages.is_empty() && self.log_scroll_offset < log_messages.len() - 1 {
                                self.log_scroll_offset += 1;
                                
                                if self.log_scroll_offset >= log_messages.len() - 1 {
                                    self.auto_scroll = true;
                                }
                            }
                        },
                        KeyCode::Char('a') => {
                            self.auto_scroll = !self.auto_scroll;
                        },
                        KeyCode::End => {
                            let log_messages = logs::get_log_messages();
                            if !log_messages.is_empty() {
                                self.log_scroll_offset = log_messages.len() - 1;
                                self.auto_scroll = true;
                            }
                        },
                        KeyCode::Home => {
                            self.log_scroll_offset = 0;
                            self.auto_scroll = false;
                        },
                        _ => {}
                    }
                }
            }

            if last_tick.elapsed() >= tick_rate {
                last_tick = Instant::now();
            }
        }

        Ok(())
    }
}

impl Drop for TerminalUI {
    fn drop(&mut self) {
        let _ = disable_raw_mode();
        let _ = execute!(self.terminal.backend_mut(), LeaveAlternateScreen);
    }
}

pub fn init_ui() -> Result<()> {
    let ui: TerminalUI = TerminalUI::new()?;
    let handle: UiHandle = ui.start_in_background();
    
    let mut ui_handle = UI_HANDLE.lock().unwrap();
    *ui_handle = Some(handle);
    
    Ok(())
}

pub fn is_ui_running() -> bool {
    let ui_handle = UI_HANDLE.lock().unwrap();
    ui_handle.as_ref().map_or(false, |handle| handle.is_running())
}

pub fn shutdown_ui() -> Result<()> {
    let mut ui_handle = UI_HANDLE.lock().unwrap();
    if let Some(mut handle) = ui_handle.take() {
        handle.stop()?;
    }
    Ok(())
}