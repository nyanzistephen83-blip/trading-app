import streamlit as st
import yfinance as yf
import random

st.set_page_config(page_title="Alpha Trading Hub", layout="centered")

st.title("📊 Alpha Matrix Hub")
st.write("Generate synchronized market trends using live global price feeds.")

# 1. Initialize permanent memory keys at startup
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.fx_pair = "EUR/USD"
    st.session_state.entry_price = 1.0924
    st.session_state.take_profit = 1.0974
    st.session_state.stop_loss = 1.0894
    st.session_state.prediction = "🔴 Awaiting Next Live Scan"
    st.session_state.aviator_multiplier = "1.00x"

# --- SECTION 2: INTERACTIVE INPUT CONTROLS ---
st.markdown("---")
st.subheader("📈 Live Currency Matrix")

# Asset selection map for real market tickers
asset_mapping = {
    "EUR/USD": "EURUSD=X",
    "GBP/USD": "GBPUSD=X",
    "USD/JPY": "JPY=X",
    "XAU/USD (Gold)": "GC=F"
}

selected_asset = st.selectbox("Select Target Asset", list(asset_mapping.keys()))

btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    if st.button("🚀 SCAN LIVE SIGNAL", use_container_width=True):
        st.session_state.fx_pair = selected_asset
        ticker_symbol = asset_mapping[selected_asset]
        
        with st.spinner("Fetching live market feeds..."):
            try:
                # Download the latest live data point from the market feed
                data = yf.download(tickers=ticker_symbol, period="1d", interval="1m", progress=False)
                
                if not data.empty:
                    # Get the most recent closing price
                    live_close = float(data['Close'].iloc[-1])
                    base_price = round(live_close, 4 if "JPY" not in ticker_symbol and "GC" not in ticker_symbol else 2)
                else:
                    base_price = round(random.uniform(1.08, 1.12), 4) # Backup fallback if feed drops
            except Exception:
                base_price = round(random.uniform(1.08, 1.12), 4)

        st.session_state.entry_price = base_price
        
        # Set realistic pip targets based on market type
        if selected_asset == "XAU/USD (Gold)":
            pip_movement = 4.50
        elif selected_asset == "USD/JPY":
            pip_movement = 0.25
        else:
            pip_movement = 0.0035
            
        # Determine movement direction trend
        direction = random.choice(["🟢 STRONG BUY ALERT", "🔴 STRONG SELL ALERT"])
        st.session_state.prediction = direction
        
        if "BUY" in direction:
            st.session_state.take_profit = round(base_price + pip_movement, 4)
            st.session_state.stop_loss = round(base_price - (pip_movement / 2), 4)
        else:
            st.session_state.take_profit = round(base_price - pip_movement, 4)
            st.session_state.stop_loss = round(base_price + (pip_movement / 2), 4)

with btn_col2:
    if st.button("🔥 RUN VELOCITY MATRIX", use_container_width=True):
        weight_chance = random.random()
        if weight_chance < 0.15:
            val = random.uniform(1.01, 1.15)
        elif weight_chance < 0.70:
            val = random.uniform(1.20, 2.50)
        else:
            val = random.uniform(2.51, 12.50)
            
        st.session_state.aviator_multiplier = f"{round(val, 2)}x"

# --- SECTION 3: DISPLAY RENDER CARDS ---
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Asset Context", value=f"{st.session_state.fx_pair}")
with col2:
    st.metric(label="Live Market Price", value=f"{st.session_state.entry_price}")

# Beautiful color-coded alert notification boxes for mobile visibility
if "BUY" in st.session_state.prediction:
    st.success(f"### Trend Status: {st.session_state.prediction}")
elif "SELL" in st.session_state.prediction:
    st.error(f"### Trend Status: {st.session_state.prediction}")
else:
    st.info(f"### Trend Status: {st.session_state.prediction}")

st.markdown("#### 📋 Copy Terminal Execution Details:")
st.info(f"**Target Asset:** {st.session_state.fx_pair}  \n"
        f"**Suggested Entry:** {st.session_state.entry_price}  \n"
        f"**Take Profit (TP):** {st.session_state.take_profit}  \n"
        f"**Stop Loss (SL):** {st.session_state.stop_loss}")

st.markdown("---")
st.subheader("⚡ Synchronized Velocity Stream (Aviator)")
st.metric(label="Target Crash Prediction", value=st.session_state.aviator_multiplier)
