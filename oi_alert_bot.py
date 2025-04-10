// === CONFIGURATION ===
const apiKey = 'plrmtvjimvvnwp80';
const accessToken = '2A9GNEPHe1YKsxcLmj5DBwx6mJU137Ob';
const telegramBotToken = '7890655719:AAHA2tKd3JJ4PHcEeDuwWOAlksda5765o5g';
const telegramChatId = '5563148192';

// === SYMBOL SETTINGS ===
const symbols = {
  "NIFTY": "NSE:NIFTY 50",
  "BANKNIFTY": "NSE:NIFTY BANK",
  "MARUTI": "NSE:MARUTI",
  "SENSEX": "BSE:SENSEX"
};

// === MAIN FUNCTION ===
function sendMarketSnapshot() {
  let message = "?? *OI Live Snapshot* ??\n\n";
  
  for (let [name, fullSymbol] of Object.entries(symbols)) {
    const data = getLTP(fullSymbol);
    if (data && data.last_price && data.change !== undefined) {
      const arrow = data.change >= 0 ? "??" : "??";
      const color = data.change >= 0 ? "??" : "??";
      message += `*${name}* - ?${data.last_price} ${arrow} ${Math.abs(data.change)} ${color}\n`;
    } else {
      message += `*${name}* - ? Error fetching data\n`;
    }
  }
  
  sendToTelegram(message);
}

// === LTP FETCH FUNCTION ===
function getLTP(symbol) {
  const url = `https://api.kite.trade/quote/ltp?i=${encodeURIComponent(symbol)}`;
  const headers = {
    "X-Kite-Version": "3",
    "Authorization": `token ${apiKey}:${accessToken}`
  };

  const response = UrlFetchApp.fetch(url, { "headers": headers });
  const json = JSON.parse(response.getContentText());
  const data = json.data[symbol];
  
  if (data) {
    const change = (Math.random() * 100 - 50).toFixed(2); // Simulated change
    return {
      last_price: data.last_price.toFixed(2),
      change: parseFloat(change)
    };
  }
  return null;
}

// === TELEGRAM SEND FUNCTION ===
function sendToTelegram(message) {
  const url = `https://api.telegram.org/bot${telegramBotToken}/sendMessage`;
  const payload = {
    chat_id: telegramChatId,
    text: message,
    parse_mode: "Markdown"
  };
  
  UrlFetchApp.fetch(url, {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify(payload)
  });
}

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
        writer.writerow([now, symbol, option_type, f"{oi_change:.2f}%"])
