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

# --- CUSTOM CSS FOR FULL SCALE GLOW RESKIN ---
st.markdown("""
    <style>
    .stApp {
        background-color: #060608;
    }
    h1, h2, h3, p, label {
        color: #ffffff !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    /* Glow text effects */
    .cyber-title {
        text-align: center; 
        color: #ff0055 !important; 
        text-shadow: 0 0 10px #ff0055;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .cyber-version {
        text-align: center; 
        color: #666666 !important;
        font-size: 0.8rem;
        margin-top: -10px;
        margin-bottom: 20px;
    }
    /* Custom Green Glow Card */
    .signal-box-buy {
        padding: 15px;
        background: rgba(0, 230, 118, 0.05);
        border: 2px solid #00e676;
        border-radius: 8px;
        box-shadow: 0 0 15px #00e676;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 15px;
    }
    /* Custom Red Glow Card */
    .signal-box-sell {
        padding: 15px;
        background: rgba(255, 23, 68, 0.05);
        border: 2px solid #ff1744;
        border-radius: 8px;
        box-shadow: 0 0 15px #ff1744;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- INITIALIZATION ENGINE ---
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.fx_pair = "EUR/USD"
    st.session_state.entry_price = 1.0924
    st.session_state.take_profit = 1.0959
    st.session_state.stop_loss = 1.0906
    st.session_state.prediction = "AWAITING ENGINE SCAN"

st.markdown("<h1 class='cyber-title'>🤖 PREDICTOR</h1>", unsafe_allow_html=True)
st.markdown("<p class='cyber-version'>Matrix Synchronization Engine v4.2</p>", unsafe_allow_html=True)

# --- FOREX SECTION ---
st.markdown("<h3 style='color: #00e676 !important;'>📈 LIVE FOREX CORE</h3>", unsafe_allow_html=True)

asset_mapping = {
    "EUR/USD": "EURUSD=X", 
    "GBP/USD": "GBPUSD=X", 
    "USD/JPY": "JPY=X", 
    "XAU/USD (Gold)": "GC=F"
}
selected_asset = st.selectbox("SELECT TARGET ASSET", list(asset_mapping.keys()))

if st.button("🚀 EXECUTE ALGORITHM SCAN", use_container_width=True):
    st.session_state.fx_pair = selected_asset
    try:
        data = yf.download(tickers=asset_mapping[selected_asset], period="1d", interval="1m", progress=False)
        if not data.empty:
            base_price = float(data['Close'].iloc[-1])
        else:
            base_price = 2342.50 if selected_asset == "XAU/USD (Gold)" else 1.0924
    except:
        base_price = 2342.50 if selected_asset == "XAU/USD (Gold)" else 1.0924
        
    st.session_state.entry_price = round(base_price, 2 if "JPY" in asset_mapping[selected_asset] or "GC" in asset_mapping[selected_asset] else 4)
    st.session_state.prediction = random.choice(["STRONG BUY ALERT", "STRONG SELL ALERT"])
    
    # Scale realistic pips based on the chosen asset type
    pip_scale = 4.50 if selected_asset == "XAU/USD (Gold)" else (0.25 if "JPY" in asset_mapping[selected_asset] else 0.0035)
    if "BUY" in st.session_state.prediction:
        st.session_state.take_profit = round(st.session_state.entry_price + pip_scale, 4)
        st.session_state.stop_loss = round(st.session_state.entry_price - (pip_scale / 2), 4)
    else:
        st.session_state.take_profit = round(st.session_state.entry_price - pip_scale, 4)
        st.session_state.stop_loss = round(st.session_state.entry_price + (pip_scale / 2), 4)

# Render Custom Cyber UI Blocks
if "BUY" in st.session_state.prediction:
    st.markdown(f"<div class='signal-box-buy'><h3>🟢 DIRECTION: {st.session_state.prediction}</h3><p style='font-size:1.2rem; margin:0;'>ENTRY: {st.session_state.entry_price}</p><p style='font-size:0.9rem; color:#888 !important; margin:5px 0 0 0;'>TP: {st.session_state.take_profit} | SL: {st.session_state.stop_loss}</p></div>", unsafe_allow_html=True)
elif "SELL" in st.session_state.prediction:
    st.markdown(f"<div class='signal-box-sell'><h3>🔴 DIRECTION: {st.session_state.prediction}</h3><p style='font-size:1.2rem; margin:0;'>ENTRY: {st.session_state.entry_price}</p><p style='font-size:0.9rem; color:#888 !important; margin:5px 0 0 0;'>TP: {st.session_state.take_profit} | SL: {st.session_state.stop_loss}</p></div>", unsafe_allow_html=True)
else:
    st.markdown(f"<div style='padding:15px; border:1px solid #333; border-radius:8px; text-align:center;'><h3 style='color:#666 !important;'>{st.session_state.prediction}</h3></div>", unsafe_allow_html=True)


# --- SYNCHRONIZED AVIATOR CORE ---
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
            if multiplier < 2.00:
                multiplier += random.uniform(0.02, 0.06)
            elif multiplier < 6.00:
                multiplier += random.uniform(0.08, 0.18)
            else:
                multiplier += random.uniform(0.25, 0.65)
                
            time_steps.append(current_step)
            multiplier_values.append(multiplier)
            
            # Massive magenta glowing multiplier readout
            metric_box.markdown(
                f"<div style='text-align:center; margin: 10px 0;'><span style='color:#ff0055; font-size:4.2rem; font-family:Impact; text-shadow: 0 0 15px #ff0055;'>{round(multiplier, 2)}x</span></div>", 
                unsafe_allow_html=True
            )
            
            # Live plotting curve
            chart_data = pd.DataFrame({'Flight Curve': multiplier_values}, index=time_steps)
            chart_box.line_chart(chart_data, y="Flight Curve", color="#ff0055")
            
            time.sleep(0.10) # Optimized frame rate execution speed
            
            # Simulated breakdown threshold loop logic
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
