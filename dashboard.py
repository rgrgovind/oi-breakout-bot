# dashboard.py
import pandas as pd
import streamlit as st
import os
import pandas as pd
import streamlit as st

st.set_page_config(page_title="OI Breakout Dashboard", layout="wide")

st.title("📈 OI Breakout Tracker")

try:
    df = pd.read_csv("logs/oi_breakouts.csv")
    st.dataframe(df.tail(20), use_container_width=True)
except Exception as e:
    st.error(f"Couldn't load log file: {e}")
    import os
import pandas as pd
import streamlit as st

LOG_FILE = "logs/oi_breakouts.csv"

st.title("📈 OI Breakout Tracker")

if not os.path.exists(LOG_FILE):
    st.warning("No log file found yet.")
    st.stop()

try:
    df = pd.read_csv(LOG_FILE)
    if df.empty or df.columns.tolist() != ["Time", "Symbol", "OptionType", "OIChange"]:
        st.warning("Log file exists but it's empty or malformed. Waiting for data...")
        st.stop()
except Exception as e:
    st.error(f"Couldn't load log file: {e}")
    st.stop()

st.success("Data loaded successfully!")

# Your visualizations go here

