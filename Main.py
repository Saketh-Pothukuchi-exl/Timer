import streamlit as st
import time
from datetime import datetime

# Configure the Streamlit page
# st.set_page_config(page_title="Countdown Timer", layout="centered")

# Configure the Streamlit page
st.set_page_config(page_title="S&S's Countdown", layout="centered")



# Page title and header
# st.title("💖 Valentine's Day Countdown 💖")
st.markdown(
    """
    <div style="text-align: center;">
        <h1>💖 S&S's Countdown 💖</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

ph = st.empty()

# Calculate the number of seconds until the target date and time
N = int((datetime(2025, 2, 14, 18, 0, 0) - datetime.now()).total_seconds())

# Countdown loop
for secs in range(N, 0, -1):
    days = secs // 86400
    hh = (secs % 86400) // 3600
    mm = (secs % 3600) // 60
    ss = secs % 60
    # ph.metric("Countdown", f"{days}days {hh:02d}:{mm:02d}:{ss:02d}")
    ph.markdown(
        f"""
        <div style="text-align: center; font-size: 32px; font-weight: bold; color: #FF69B4;">
            {days}days <p style="text-align: center; font-size: 48px; font-weight: bold; color: #FF69B4;">{hh:02d}:{mm:02d}:{ss:02d}</p>
        </div>
        """,
        unsafe_allow_html=True,
        )
    time.sleep(1)
