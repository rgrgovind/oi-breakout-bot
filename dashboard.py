import os
import pandas as pd
import streamlit as st

LOG_FILE = "logs/oi_breakouts.csv"

st.set_page_config(page_title="OI Breakout Tracker", layout="wide")
st.title("📈 OI Breakout Tracker")

# Check if file exists
if not os.path.exists(LOG_FILE):
    st.warning("No breakout data found yet.")
    st.stop()

# Load the log data
try:
    df = pd.read_csv(LOG_FILE)

    # Check if it has the right structure
    expected_columns = ["Time", "Symbol", "OptionType", "OIChange"]
    if df.empty or not all(col in df.columns for col in expected_columns):
        st.warning("Log file exists but it's empty or malformed. Waiting for data...")
        st.stop()
    
    # Optional: Format OIChange if it's a string like "12.3%"
    if df["OIChange"].dtype == object:
        df["OIChange"] = df["OIChange"].str.replace('%', '').astype(float)

    # Display data
    st.dataframe(df.sort_values(by="Time", ascending=False), use_container_width=True)

    # Optional: Simple bar chart
    st.subheader("📊 OI Change (%) by Symbol and OptionType")
    chart_df = df.groupby(["Symbol", "OptionType"])["OIChange"].mean().reset_index()
    st.bar_chart(chart_df.set_index(["Symbol", "OptionType"]))

except Exception as e:
    st.error(f"Couldn't load log file: {e}")
    st.stop()
