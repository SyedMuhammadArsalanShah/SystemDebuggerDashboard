# tkinter_app.py
import tkinter as tk
import logging
import random
import threading
import time

# Configure logging to file
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s',
    filemode='w'  # overwrite every run for demo
)

# Function to generate random logs every few seconds
def generate_logs():
    levels = [logging.INFO, logging.WARNING, logging.ERROR]
    messages = [
        "System running smoothly.",
        "Disk space getting low.",
        "Network latency detected.",
        "User login successful.",
        "Failed to connect to database.",
        "High memory usage detected.",
        "Service restarted.",
        "Unexpected error in module X."
    ]
    while True:
        level = random.choice(levels)
        msg = random.choice(messages)
        logging.log(level, msg)
        time.sleep(random.uniform(2, 5))

# Tkinter GUI (just a window with a label)
def start_tkinter_app():
    root = tk.Tk()
    root.title("Tkinter App with Logging")
    root.geometry("300x100")
    label = tk.Label(root, text="This Tkinter app logs system info to app.log")
    label.pack(pady=30)
    root.mainloop()

if __name__ == "__main__":
    # Start logging thread
    log_thread = threading.Thread(target=generate_logs, daemon=True)
    log_thread.start()
    # Start GUI mainloop
    start_tkinter_app()
