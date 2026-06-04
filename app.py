import streamlit as st
import yfinance as yf
import random
import time
import pandas as pd

# Set page config and apply a dark stealth theme natively
st.set_page_config(
    page_title="ALPHA MATRIX PREDICTOR", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS FOR THE PREMIUM HI-TECH LOOK ---
st.markdown("""
    <style>
    /* Force pitch black background and cyber fonts */
    .stApp {
        background-color: #060608;
    }
    h1, h2, h3, p, label {
        color: #ffffff !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    /* Glow styling for metrics */
    div[data-testid="stMetricValue"] {
        font-size: 3rem !important;
        font-weight: bold !important;
        font-family: 'Impact', sans-serif !important;
    }
    /* Custom Red Glow Card */
    .signal-box-sell {
        padding: 15px;
        background: rgba(255, 23, 68, 0.1);
        border: 2px solid #ff1744;
        border-radius: 10px;
        box-shadow: 0 0 15px #ff1744;
        text-align: center;
        margin-bottom: 20px;
    }
    /* Custom Green Glow Card */
    .signal-box-buy {
        padding: 15px;
        background: rgba(0, 230, 118, 0.1);
        border: 2px solid #00e676;
        border-radius: 10px;
        box-shadow: 0 0 15px #00e676;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- INITIALIZATION ENGINE ---
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.fx_pair = "EUR/USD"
    st.session_state.entry_price = 1.0924
    st.session_state.prediction = "AWAITING ENGINE SCAN"

st.markdown("<h1 style='text-align: center; color: #ff0055 !important; text-shadow: 0 0 10px #ff0055;'>🤖 CASHBET AI PREDICTOR</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center; color: #888888 !important;'>Matrix Synchronization Engine v4.2</p>", unsafe_allow_html=True)

# --- FOREX SECTION ---
st.markdown("<h3 style='color: #00e676 !important;'>📈 LIVE FOREX CORE</h3>", unsafe_allow_html=True)
asset_mapping = {"EUR/USD": "EURUSD=X", "GBP/USD": "GBPUSD=X", "USD/JPY": "JPY=X", "XAU/USD (Gold)": "GC=F"}
selected_asset = st.selectbox("SELECT TARGET ASSET", list(asset_mapping.keys()))

if st.button("🚀 EXECUTE ALGORITHM SCAN", use_container_width=True):
    st.session_state.fx_pair = selected_asset
    try:
        data = yf.download(tickers=asset_mapping[selected_asset], period="1d", interval="1m", progress=False)
        base_price = round(float(data['Close'].iloc[-1]), 4 if "JPY" not in asset_mapping[selected_asset] else 2)
    except:
        base_price = 1.0924
    st.session_state.entry_price = base_price
    st.session_state.prediction = random.choice(["STRONG BUY ALERT", "STRONG SELL ALERT"])

# Display matching visual cards
if "BUY" in st.session_state.prediction:
    st.markdown(f"<div class='signal-box-buy'><h3>🟢 DIRECTION: {st.session_state.prediction}</h3><p>ENTRY: {st.session_state.entry_price}</p></div>", unsafe_allow_html=True)
elif "SELL" in st.session_state.prediction:
    st.markdown(f"<div class='signal-box-sell'><h3>🔴 DIRECTION: {st.session_state.prediction}</h3><p>ENTRY: {st.session_state.entry_price}</p></div>", unsafe_allow_html=True)
else:
    st.markdown(f"<div style='padding:15px; border:1px solid #444; border-radius:10px; text-align:center;'><h3>{st.session_state.prediction}</h3></div>", unsafe_allow_html=True)


# --- SYNCHRONIZED AVIATOR SYSTEM ---
st.markdown("---")
st.markdown("<h3 style='color: #ff0055 !important;'>✈️ AVIATOR MATRIX STREAM</h3>", unsafe_allow_html=True)

@st.fragment
def run_synchronized_trigger():
    # Large execution pad button mimicking a betting app interface
    sync_click = st.button("🔥 PRESS IN UNISON WITH TAKE-OFF", use_container_width=True, type="primary")
    
    status_box = st.empty()
    metric_box = st.empty()
    chart_box = st.empty() # Placeholder for the climbing flight line
    
    if sync_click:
        status_box.markdown("<p style='color: #ff0055; text-align:center;'>⚠️ LIVE DATA PATTERN STREAMING...</p>", unsafe_allow_html=True)
        multiplier = 1.00
        
        # Lists to keep track of chart coordinates
        time_steps = [0]
        multiplier_values = [1.00]
        current_step = 0
        
        # Continuous flight curve loop
        while True:
            current_step += 1
            if multiplier < 2.00:
                multiplier += random.uniform(0.02, 0.05)
            elif multiplier < 5.00:
                multiplier += random.uniform(0.06, 0.15)
            else:
                multiplier += random.uniform(0.20, 0.60)
                
            time_steps.append(current_step)
            multiplier_values.append(multiplier)
            
            # Format custom html text string for a magenta neon look
            metric_box.markdown(
                f"<div style='text-align:center;'><span style='color:#ff0055; font-size:4.5rem; font-family:Impact; text-shadow: 0 0 15px #ff0055;'>{round(multiplier, 2)}x</span></div>", 
                unsafe_allow_html=True
            )
            
            # Draw a beautiful climbing curve graph right inside the card area
            chart_data = pd.DataFrame({'Flight Curve': multiplier_values}, index=time_steps)
            chart_box.line_chart(chart_data, y="Flight Curve", color="#ff0055")
            
            time_sleep_duration = 0.12
            time.sleep(time_sleep_duration)
            
            # Mathematical algorithm random cutoff sequence logic
            if multiplier > 15.00 or (multiplier > 1.80 and random.random() < 0.035):
                status_box.markdown(f"<div class='signal-box-sell'><h2>💥 CRASHED @ {round(multiplier, 2)}x</h2></div>", unsafe_allow_html=True)
                time.sleep(3.0) # Lock result on screen briefly
                status_box.markdown("<p style='text-align:center; color:#888;'>READY FOR NEXT SYNCHRONIZED LAUNCH</p>", unsafe_allow_html=True)
                metric_box.empty()
                chart_box.empty()
                break
    else:
        status_box.markdown("<p style='text-align:center; color:#888;'>READY FOR NEXT SYNCHRONIZED LAUNCH</p>", unsafe_allow_html=True)

run_synchronized_trigger()
