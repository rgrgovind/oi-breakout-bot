# dashboard.py
import pandas as pd
import streamlit as st

st.set_page_config(page_title="OI Breakout Dashboard", layout="wide")

st.title("📈 OI Breakout Tracker")

try:
    df = pd.read_csv("logs/oi_breakouts.csv")
    st.dataframe(df.tail(20), use_container_width=True)
except Exception as e:
    st.error(f"Couldn't load log file: {e}")
