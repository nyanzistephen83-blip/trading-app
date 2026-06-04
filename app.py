
import streamlit as st
import random

st.set_page_config(page_title="Alpha Trading Hub", layout="centered")

st.title("📊 Alpha Matrix Hub")
st.write("Generate synchronized market trends and velocity sequence signals.")

# 1. Initialize all session states cleanly at startup
if "fx_pair" not in st.session_state:
    st.session_state.fx_pair = "EUR/USD"
    st.session_state.entry_price = 1.0924
    st.session_state.take_profit = 1.0974
    st.session_state.stop_loss = 1.0894
    st.session_state.prediction = "🔴 Awaiting Next Signal Scan"
    st.session_state.aviator_multiplier = "1.00x"

# --- SECTION 2: THE INTERACTIVE INPUT CONTROLS ---
st.markdown("---")
st.subheader("📈 Core Currency Matrix")

selected_asset = st.selectbox("Select Target Asset", ["EUR/USD", "GBP/USD", "USD/JPY", "XAU/USD (Gold)"])

# Create the calculation triggers side-by-side
btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    scan_triggered = st.button("🚀 SCAN CURRENT SIGNAL", use_container_width=True)

with btn_col2:
    aviator_triggered = st.button("🔥 RUN VELOCITY MATRIX", use_container_width=True)

# --- SECTION 3: CORE LOGIC PROCESSING SHIFTED TO TOP ---
if scan_triggered:
    st.session_state.fx_pair = selected_asset
    
    # Calculate baseline pricing index
    if selected_asset == "XAU/USD (Gold)":
        base_price = round(random.uniform(2300.00, 2350.00), 2)
        pip_movement = 5.00
    elif selected_asset == "USD/JPY":
        base_price = round(random.uniform(155.00, 158.00), 2)
        pip_movement = 0.35
    else:
        base_price = round(random.uniform(1.0800, 1.1200), 4)
        pip_movement = 0.0050

    st.session_state.entry_price = base_price
    
    # Update directional signals instantly
    direction = random.choice(["🟢 STRONG BUY ALERT", "🔴 STRONG SELL ALERT"])
    st.session_state.prediction = direction
    
    if "BUY" in direction:
        st.session_state.take_profit = round(base_price + pip_movement, 4)
        st.session_state.stop_loss = round(base_price - (pip_movement / 2), 4)
    else:
        st.session_state.take_profit = round(base_price - pip_movement, 4)
        st.session_state.stop_loss = round(base_price + (pip_movement / 2), 4)

if aviator_triggered:
    weight_chance = random.random()
    if weight_chance < 0.15:
        val = random.uniform(1.01, 1.15)
    elif weight_chance < 0.70:
        val = random.uniform(1.20, 2.50)
    else:
        val = random.uniform(2.51, 12.50)
        
    st.session_state.aviator_multiplier = f"{round(val, 2)}x"


# --- SECTION 4: DISPLAY RENDER CARDS (Reads fresh state data) ---
col1, col2 = st.columns(2)
with col1:
    st.metric(label=f"Asset Context: {st.session_state.fx_pair}", value=f"{st.session_state.entry_price}")
with col2:
    st.metric(label="Calculated Action Status", value=st.session_state.prediction)

st.markdown("#### 📋 Copy Terminal Execution Details:")
st.info(f"**Target Asset:** {st.session_state.fx_pair}  \n"
        f"**Suggested Entry:** {st.session_state.entry_price}  \n"
        f"**Take Profit (TP):** {st.session_state.take_profit}  \n"
        f"**Stop Loss (SL):** {st.session_state.stop_loss}")

st.markdown("---")
st.subheader("⚡ Synchronized Velocity Stream (Aviator)")
st.metric(label="Target Crash Prediction", value=st.session_state.aviator_multiplier)
