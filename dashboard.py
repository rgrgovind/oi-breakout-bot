import pandas as pd
import streamlit as st
import os

LOG_FILE = "logs/oi_breakouts.csv"

st.title("📈 OI Breakout Tracker")

if not os.path.exists(LOG_FILE):
    st.warning("Log file does not exist.")
else:
    try:
        df = pd.read_csv(LOG_FILE)

        if df.empty or df.columns.tolist() != ['Time', 'Symbol', 'OptionType', 'OIChange']:
            st.warning("Log file exists but it's empty or malformed. Waiting for data...")
        else:
            st.dataframe(df)
    except Exception as e:
        st.error(f"Error reading log file: {e}")
