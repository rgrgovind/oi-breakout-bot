import os
import pandas as pd
import streamlit as st

LOG_FILE = "logs/oi_breakouts.csv"

st.title("📈 OI Breakout Tracker")

if not os.path.exists(LOG_FILE):
    st.warning("No breakout data found yet.")
    st.stop()

try:
    df = pd.read_csv(LOG_FILE)
    if df.empty or df.columns.tolist() != ["Time", "Symbol", "OptionType", "OIChange"]:
        st.warning("Log file exists but it's empty or malformed. Waiting for data...")
        st.stop()
except Exception as e:
    st.error(f"Couldn't load log file: {e}")
    st.stop()

st.dataframe(df)
