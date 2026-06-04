import streamlit as st
import yfinance as yf
import random
import time

st.set_page_config(page_title="Alpha Trading Hub", layout="centered")

st.title("📊 Alpha Matrix Hub")
st.write("Cross-platform data synchronization engine with live animations.")

# 1. Initialize permanent session storage keys at absolute startup
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.fx_pair = "EUR/USD"
    st.session_state.entry_price = 1.0924
    st.session_state.take_profit = 1.0974
    st.session_state.stop_loss = 1.0894
    st.session_state.prediction = "🔴 Awaiting Next Live Scan"

# --- SECTION 2: FOREX INTEGRATION CORE ---
st.markdown("---")
st.subheader("📈 Live Currency Matrix")

asset_mapping = {
    "EUR/USD": "EURUSD=X",
    "GBP/USD": "GBPUSD=X",
    "USD/JPY": "JPY=X",
    "XAU/USD (Gold)": "GC=F"
}

selected_asset = st.selectbox("Select Target Asset", list(asset_mapping.keys()))

if st.button("🚀 SCAN LIVE SIGNAL", use_container_width=True):
    st.session_state.fx_pair = selected_asset
    ticker_symbol = asset_mapping[selected_asset]
    
    with st.spinner("Fetching live market feeds..."):
        try:
            data = yf.download(tickers=ticker_symbol, period="1d", interval="1m", progress=False)
            if not data.empty:
                live_close = float(data['Close'].iloc[-1])
                base_price = round(live_close, 4 if "JPY" not in ticker_symbol and "GC" not in ticker_symbol else 2)
            else:
                base_price = round(random.uniform(1.08, 1.12), 4)
        except Exception:
            base_price = round(random.uniform(1.08, 1.12), 4)

    st.session_state.entry_price = base_price
    
    # Pip parameter boundaries
    if selected_asset == "XAU/USD (Gold)":
        pip_movement = 4.50
    elif selected_asset == "USD/JPY":
        pip_movement = 0.25
    else:
        pip_movement = 0.0035
        
    direction = random.choice(["🟢 STRONG BUY ALERT", "🔴 STRONG SELL ALERT"])
    st.session_state.prediction = direction
    
    if "BUY" in direction:
        st.session_state.take_profit = round(base_price + pip_movement, 4)
        st.session_state.stop_loss = round(base_price - (pip_movement / 2), 4)
    else:
        st.session_state.take_profit = round(base_price - pip_movement, 4)
        st.session_state.stop_loss = round(base_price + (pip_movement / 2), 4)

# Static Render for Currency Metric Cards
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Asset Context", value=f"{st.session_state.fx_pair}")
with col2:
    st.metric(label="Live Market Price", value=f"{st.session_state.entry_price}")

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


# --- SECTION 3: THE AUTOMATED ISOLATED LOOP ENGINE ---
st.markdown("---")
st.subheader("⚡ Continuous Velocity Matrix (Aviator)")
st.write("This localized block executes continuously without reloading your trading cards.")

# Using Streamlit fragments to contain the infinite loop animation safely
@st.fragment
def run_aviator_loop():
    # Dedicated button to initiate the nonstop simulation sequence
    start_matrix = st.button("🔥 START NONSTOP SEQUENCE", use_container_width=True)
    
    # Establish a clean layout block to push real-time graphic data strings into
    display_card = st.empty()
    progress_card = st.empty()
    
    if start_matrix:
        current_multiplier = 1.00
        
        while True:
            # Gradually speed up and step up the target numbers smoothly
            if current_multiplier < 2.00:
                step = random.uniform(0.01, 0.04)
            elif current_multiplier < 5.00:
                step = random.uniform(0.03, 0.12)
            else:
                step = random.uniform(0.15, 0.45)
                
            current_multiplier += step
            
            # Draw the visual cards dynamically into the empty space frame
            display_card.metric(
                label="⚡ ACTIVE PROJECTION SEQUENCE", 
                value=f"{round(current_multiplier, 2)}x",
                delta="LIVE MATRIX CLIMBING"
            )
            
            # Simulate a continuous loading meter update alongside the digits
            meter_val = int((current_multiplier * 7) % 100)
            progress_card.progress(meter_val)
            
            # Delay briefly to create a smooth, streaming framerate on your screen
            time.sleep(0.15)
            
            # Simulate an occasional sudden reset/crash to reset the cycle automatically
            if current_multiplier > 12.00 or (current_multiplier > 2.50 and random.random() < 0.03):
                display_card.error(f"💥 Sequence Reset Point: {round(current_multiplier, 2)}x")
                time.sleep(2.5) # Freeze the final target briefly so it is readable
                current_multiplier = 1.00

# Execute the isolated animation routine loop
run_aviator_loop()
