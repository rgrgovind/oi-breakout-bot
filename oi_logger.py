import os
import csv
from datetime import datetime

LOG_FILE = "logs/oi_breakouts.csv"

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

def log_breakout(symbol, option_type, oi_change):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["Time", "Symbol", "OptionType", "OIChange"])
        writer.writerow([now, symbol, option_type, f"{oi_change:.2f}"])
