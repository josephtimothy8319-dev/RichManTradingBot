#!/usr/bin/env python3
"""
RichManBot Launcher - Simple GUI to start the bot
Just run: python launcher.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
import os
import threading
import webbrowser
from pathlib import Path

class RichManBotLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("RichManBot Launcher 🤖")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # Set background color
        self.root.configure(bg='#1e1e2e')
        
        self.server_process = None
        self.is_running = False
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        
        # Main frame with dark background
        main_frame = tk.Frame(self.root, bg='#1e1e2e')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="🤖 RichManBot",
            font=("Arial", 28, "bold"),
            fg="#00d4ff",
            bg="#1e1e2e"
        )
        title_label.pack(pady=10)
        
        # Subtitle
        subtitle_label = tk.Label(
            main_frame,
            text="Professional Crypto Trading Dashboard",
            font=("Arial", 12),
            fg="#b0b0c3",
            bg="#1e1e2e"
        )
        subtitle_label.pack(pady=5)
        
        # Status frame
        status_frame = tk.Frame(main_frame, bg='#2d2d44', relief=tk.RIDGE, bd=1)
        status_frame.pack(fill=tk.X, pady=20)
        
        status_label = tk.Label(
            status_frame,
            text="Status:",
            font=("Arial", 11, "bold"),
            fg="#ffffff",
            bg="#2d2d44"
        )
        status_label.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.status_text = tk.Label(
            status_frame,
            text="⚫ Stopped",
            font=("Arial", 11, "bold"),
            fg="#ff006e",
            bg="#2d2d44"
        )
        self.status_text.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Info text
        info_text = tk.Label(
            main_frame,
            text="Click 'Start Bot' to launch the dashboard.\nOnce started, your browser will open automatically.",
            font=("Arial", 10),
            fg="#b0b0c3",
            bg="#1e1e2e",
            justify=tk.CENTER
        )
        info_text.pack(pady=10)
        
        # Buttons frame
        button_frame = tk.Frame(main_frame, bg='#1e1e2e')
        button_frame.pack(fill=tk.X, pady=20)
        
        # Start button
        self.start_btn = tk.Button(
            button_frame,
            text="🚀 Start Bot",
            font=("Arial", 12, "bold"),
            bg="#00ff41",
            fg="#000000",
            padx=20,
            pady=10,
            command=self.start_bot,
            cursor="hand2"
        )
        self.start_btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        # Stop button
        self.stop_btn = tk.Button(
            button_frame,
            text="🛑 Stop Bot",
            font=("Arial", 12, "bold"),
            bg="#ff006e",
            fg="#ffffff",
            padx=20,
            pady=10,
            command=self.stop_bot,
            state=tk.DISABLED,
            cursor="hand2"
        )
        self.stop_btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        # Open Browser button
        self.open_btn = tk.Button(
            button_frame,
            text="🌐 Open Browser",
            font=("Arial", 12, "bold"),
            bg="#00d4ff",
            fg="#000000",
            padx=20,
            pady=10,
            command=self.open_browser,
            state=tk.DISABLED,
            cursor="hand2"
        )
        self.open_btn.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        # Log frame
        log_label = tk.Label(
            main_frame,
            text="Server Log:",
            font=("Arial", 10, "bold"),
            fg="#ffffff",
            bg="#1e1e2e"
        )
        log_label.pack(anchor=tk.W, pady=(10, 5))
        
        # Log text area
        self.log_text = tk.Text(
            main_frame,
            height=8,
            width=70,
            bg="#2d2d44",
            fg="#00ff41",
            font=("Courier", 9),
            relief=tk.SUNKEN,
            bd=1
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar for log
        scrollbar = tk.Scrollbar(self.log_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.log_text.yview)
        
        self.log("RichManBot Launcher Ready")
        self.log("Click 'Start Bot' to begin...")
        
    def log(self, message):
        """Add message to log"""
        self.log_text.insert(tk.END, f"> {message}\n")
        self.log_text.see(tk.END)
        self.root.update()
        
    def start_bot(self):
        """Start the FastAPI server"""
        self.log("Starting RichManBot...")
        
        try:
            # Check if dependencies are installed
            self.log("Checking dependencies...")
            import fastapi
            import uvicorn
            self.log("✓ Dependencies found")
        except ImportError:
            self.log("⚠ Installing dependencies (this may take a moment)...")
            try:
                subprocess.run(
                    [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                    check=True,
                    capture_output=True
                )
                self.log("✓ Dependencies installed")
            except subprocess.CalledProcessError as e:
                self.log(f"❌ Error installing dependencies: {e}")
                messagebox.showerror("Error", "Failed to install dependencies")
                return
        
        # Start the server in a separate thread
        thread = threading.Thread(target=self._run_server, daemon=True)
        thread.start()
        
        # Update UI
        self.is_running = True
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.open_btn.config(state=tk.NORMAL)
        self.status_text.config(text="🟢 Running", fg="#00ff41")
        self.log("✓ Bot started successfully!")
        self.log("Dashboard: http://localhost:8000/static/index.html")
        
    def _run_server(self):
        """Run the FastAPI server"""
        try:
            self.server_process = subprocess.Popen(
                [sys.executable, "backend/main.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )
            
            # Read output
            for line in self.server_process.stdout:
                if line.strip():
                    self.log(line.strip())
                    
        except Exception as e:
            self.log(f"❌ Error: {e}")
            self.is_running = False
            self.start_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)
            self.open_btn.config(state=tk.DISABLED)
            self.status_text.config(text="⚫ Stopped", fg="#ff006e")
            
    def stop_bot(self):
        """Stop the FastAPI server"""
        if self.server_process:
            self.log("Stopping bot...")
            self.server_process.terminate()
            try:
                self.server_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.server_process.kill()
            self.log("✓ Bot stopped")
        
        # Update UI
        self.is_running = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.open_btn.config(state=tk.DISABLED)
        self.status_text.config(text="⚫ Stopped", fg="#ff006e")
        
    def open_browser(self):
        """Open the dashboard in browser"""
        self.log("Opening browser...")
        webbrowser.open("http://localhost:8000/static/index.html")
        
    def on_closing(self):
        """Handle window close"""
        if self.is_running:
            if messagebox.askyesno("Exit", "Bot is still running. Stop it before closing?"):
                self.stop_bot()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = RichManBotLauncher(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
