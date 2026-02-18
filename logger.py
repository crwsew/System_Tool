from datetime import datetime

LOG_FILE = "log.txt"

def log_action(action: str):
    """Write user actions to log file with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {action}\n")
