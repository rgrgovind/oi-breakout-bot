import os
import pandas as pd
import streamlit as st

LOG_FILE = "logs/oi_breakouts.csv"

st.title("📈 OI Breakout Tracker")

# Check if log file exists
if not os.path.exists(LOG_FILE):
    st.warning("No breakout data found yet.")
    st.stop()

# Try loading the log file
try:
    df = pd.read_csv(LOG_FILE)

    # Validate column headers
    expected_columns = ["Time", "Symbol", "OptionType", "OIChange"]
    if df.empty or list(df.columns) != expected_columns:
        st.warning("Log file exists but it's empty or malformed. Waiting for data...")
        st.stop()

except Exception as e:
    st.error(f"Couldn't load log file: {e}")
    st.stop()

# Display the data
st.success("Latest Breakouts:")
st.dataframe(df)
