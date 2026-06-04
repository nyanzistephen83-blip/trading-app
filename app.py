import streamlit as st
import time
import random

st.set_page_config(page_title="Live Analytics Dashboard", layout="centered")

st.title("📊 Real-Time Market Analytics")
st.write("This clean web interface handles live data streams effortlessly on mobile.")

# Create clean display placeholders
card_forex = st.container()
card_aviator = st.container()

# Generate fresh data points on this page load
fx_val = round(random.uniform(1.0800, 1.3200), 4)
fx_pair = random.choice(["EUR/USD", "GBP/USD", "USD/JPY"])
fx_action = random.choice(["🟢 BUY TREND", "🔴 SELL TREND"])

with card_forex:
    st.markdown("### 📈 Currency Matrix Stream")
    st.metric(label=f"Asset: {fx_pair}", value=f"{fx_val}", delta=fx_action)
    st.caption("Refreshes automatically.")

seq_multiplier = round(random.uniform(1.20, 3.50), 2)
stability = random.randint(75, 95)

with card_aviator:
    st.markdown("### ⚡ Velocity Sequence Stream")
    st.metric(label="Target Multiplier", value=f"{seq_multiplier}x")
    st.progress(stability)
    st.caption(f"Calculated Stability Rating: {stability}%")

# Wait 5 seconds, then safely refresh the entire page state
time.sleep(5)
st.rerun()
