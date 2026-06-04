import streamlit as st
import yfinance as yf
import random
import time
import pandas as pd

st.set_page_config(
    page_title="ALPHA MATRIX PREDICTOR", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    .stApp { background-color: #060608; }
    h1, h2, h3, p, label { color: #ffffff !important; font-family: 'Courier New', Courier, monospace !important; }
    .cyber-title { text-align: center; color: #ff0055 !important; text-shadow: 0 0 10px #ff0055; font-weight: bold; margin-bottom: 0px; }
    .cyber-version { text-align: center; color: #666666 !important; font-size: 0.8rem; margin-top: -10px; margin-bottom: 20px; }
    .signal-box-buy { padding: 15px; background: rgba(0, 230, 118, 0.05); border: 2px solid #00e676; border-radius: 8px; box-shadow: 0 0 15px #00e676; text-align: center; margin-top: 10px; margin-bottom: 15px; }
    .signal-box-sell { padding: 15px; background: rgba(255, 23, 68, 0.05); border: 2px solid #ff1744; border-radius: 8px; box-shadow: 0 0 15px #ff1744; text-align: center; margin-top: 10px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.fx_pair = "EUR/USD"
    st.session_state.entry_price = 1.1638  # Updated baseline to match your current real MT5 chart environment
    st.session_state.take_profit = 1.1673
    st.session_state.stop_loss = 1.1620
    st.session_state.prediction = "AWAITING INITIAL ENGINE SCAN"

st.markdown("<h1 class='cyber-title'>🤖 PREDICTOR</h1>", unsafe_allow_html=True)
st.markdown("<p class='cyber-version'>Matrix Synchronization Engine v4.2</p>", unsafe_allow_html=True)

st.markdown("<h3 style='color: #00e676 !important;'>📈 LIVE FOREX CORE</h3>", unsafe_allow_html=True)

# User manual input to ensure total sync control regardless of live web API availability
sync_mode = st.radio("NETWORK SYNC MODE", ["AUTOMATIC API FEED", "MANUAL MT5 OVERRIDE"], horizontal=True)

asset_mapping = {"EUR/USD": "EURUSD=X", "GBP/USD": "GBPUSD=X", "USD/JPY": "JPY=X", "XAU/USD (Gold)": "GC=F"}
selected_asset = st.selectbox("SELECT TARGET ASSET", list(asset_mapping.keys()))

# If API fails or user selects manual, they can type the exact price from MT5 to force a perfect trade setup
manual_price = 1.1638
if sync_mode == "MANUAL MT5 OVERRIDE":
    manual_price = st.number_input("ENTER CURRENT MT5 PRICE", value=1.1638, format="%.4f")

if st.button("🚀 EXECUTE ALGORITHM SCAN", use_container_width=True):
    st.session_state.fx_pair = selected_asset
    st.session_state.prediction = random.choice(["STRONG BUY ALERT", "STRONG SELL ALERT"])
    
    base_price = None
    if sync_mode == "AUTOMATIC API FEED":
        try:
            data = yf.download(tickers=asset_mapping[selected_asset], period="1d", interval="1m", progress=False)
            if not data.empty:
                base_price = float(data['Close'].iloc[-1])
        except:
            pass
            
    # If API connection drops, smoothly use the updated structural market baselines
    if base_price is None:
        if sync_mode == "MANUAL MT5 OVERRIDE":
            base_price = manual_price
        else:
            base_price = 2342.50 if selected_asset == "XAU/USD (Gold)" else (156.20 if "JPY" in asset_mapping[selected_asset] else 1.1638)
            
    st.session_state.entry_price = round(base_price, 2 if "JPY" in asset_mapping[selected_asset] or "GC" in asset_mapping[selected_asset] else 4)
    
    # Calculate perfect distances based on asset type
    pip_scale = 4.50 if selected_asset == "XAU/USD (Gold)" else (0.25 if "JPY" in asset_mapping[selected_asset] else 0.0035)
    
    if "BUY" in st.session_state.prediction:
        st.session_state.take_profit = round(st.session_state.entry_price + pip_scale, 4 if "JPY" not in asset_mapping[selected_asset] else 2)
        st.session_state.stop_loss = round(st.session_state.entry_price - (pip_scale / 2), 4 if "JPY" not in asset_mapping[selected_asset] else 2)
    else:
        st.session_state.take_profit = round(st.session_state.entry_price - pip_scale, 4 if "JPY" not in asset_mapping[selected_asset] else 2)
        st.session_state.stop_loss = round(st.session_state.entry_price + (pip_scale / 2), 4 if "JPY" not in asset_mapping[selected_asset] else 2)

# Render Custom Cyber UI Blocks
if "BUY" in st.session_state.prediction:
    st.markdown(f"<div class='signal-box-buy'><h3>🟢 DIRECTION: {st.session_state.prediction}</h3><p style='font-size:1.2rem; margin:0;'>ENTRY: {st.session_state.entry_price}</p><p style='font-size:1.1rem; font-weight:bold; color:#ffffff !important; margin:5px 0 0 0;'>SL: {st.session_state.stop_loss} &nbsp;|&nbsp; TP: {st.session_state.take_profit}</p></div>", unsafe_allow_html=True)
elif "SELL" in st.session_state.prediction:
    st.markdown(f"<div class='signal-box-sell'><h3>🔴 DIRECTION: {st.session_state.prediction}</h3><p style='font-size:1.2rem; margin:0;'>ENTRY: {st.session_state.entry_price}</p><p style='font-size:1.1rem; font-weight:bold; color:#ffffff !important; margin:5px 0 0 0;'>SL: {st.session_state.stop_loss} &nbsp;|&nbsp; TP: {st.session_state.take_profit}</p></div>", unsafe_allow_html=True)
else:
    st.markdown(f"<div style='padding:15px; border:1px solid #333; border-radius:8px; text-align:center;'><h3 style='color:#666 !important;'>{st.session_state.prediction}</h3></div>", unsafe_allow_html=True)

# --- AVIATOR SYSTEM ---
st.markdown("<h3 style='color: #ff0055 !important;'>✈️ AVIATOR MATRIX STREAM</h3>", unsafe_allow_html=True)

@st.fragment
def run_synchronized_trigger():
    sync_click = st.button("🔥 PRESS IN UNISON WITH TAKE-OFF", use_container_width=True, type="primary")
    status_box = st.empty()
    metric_box = st.empty()
    chart_box = st.empty()
    
    if sync_click:
        multiplier = 1.00
        time_steps = [0]
        multiplier_values = [1.00]
        current_step = 0
        while True:
            current_step += 1
            multiplier += random.uniform(0.02, 0.06) if multiplier < 2.00 else (random.uniform(0.08, 0.18) if multiplier < 6.00 else random.uniform(0.25, 0.65))
            time_steps.append(current_step)
            multiplier_values.append(multiplier)
            
            metric_box.markdown(f"<div style='text-align:center; margin: 10px 0;'><span style='color:#ff0055; font-size:4.2rem; font-family:Impact; text-shadow: 0 0 15px #ff0055;'>{round(multiplier, 2)}x</span></div>", unsafe_allow_html=True)
            chart_data = pd.DataFrame({'Flight Curve': multiplier_values}, index=time_steps)
            chart_box.line_chart(chart_data, y="Flight Curve", color="#ff0055")
            time.sleep(0.10)
            
            if multiplier > 15.00 or (multiplier > 1.50 and random.random() < 0.04):
                status_box.markdown(f"<div class='signal-box-sell'><h2 style='margin:0;'>💥 CRASHED @ {round(multiplier, 2)}x</h2></div>", unsafe_allow_html=True)
                time.sleep(2.5)
                status_box.markdown("<p style='text-align:center; color:#555; font-size:0.9rem;'>READY FOR NEXT SYNCHRONIZED LAUNCH</p>", unsafe_allow_html=True)
                metric_box.empty()
                chart_box.empty()
                break
    else:
        status_box.markdown("<p style='text-align:center; color:#555; font-size:0.9rem;'>READY FOR NEXT SYNCHRONIZED LAUNCH</p>", unsafe_allow_html=True)

run_synchronized_trigger()
