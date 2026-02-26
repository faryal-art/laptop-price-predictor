import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

# ── Page config (must be first) ────────────────────────────────────
st.set_page_config(
    page_title="LaptopIQ — Price Predictor",
    page_icon="💻",
    layout="centered"
)

# ── Custom CSS ─────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #0a0a0f;
    color: #e8e8f0;
}
.stApp {
    background: radial-gradient(ellipse at 20% 0%, #1a1040 0%, #0a0a0f 50%),
                radial-gradient(ellipse at 80% 100%, #0d2040 0%, transparent 60%);
    background-color: #0a0a0f;
}
#MainMenu, footer, header {visibility: hidden;}
.block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 780px; }

.hero {
    text-align: center;
    padding: 3rem 0 2rem 0;
}
.hero-badge {
    display: inline-block;
    background: linear-gradient(135deg, #6c3bff22, #3b82f622);
    border: 1px solid #6c3bff55;
    border-radius: 100px;
    padding: 6px 18px;
    font-size: 0.75rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #a78bfa;
    margin-bottom: 1.2rem;
}
.hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: 3.2rem;
    font-weight: 800;
    line-height: 1.1;
    background: linear-gradient(135deg, #ffffff 30%, #a78bfa 70%, #60a5fa 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0 0 0.8rem 0;
}
.hero p {
    color: #8888aa;
    font-size: 1.05rem;
    font-weight: 300;
    margin: 0;
}
.section-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #6c3bff;
    margin: 2rem 0 1rem 0;
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, #6c3bff33, transparent);
}
div[data-testid="stSelectbox"] label,
div[data-testid="stSlider"] label,
div[data-testid="stNumberInput"] label {
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    color: #9999bb !important;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}
div[data-testid="stSelectbox"] > div > div {
    background-color: #13131f !important;
    border: 1px solid #2a2a3f !important;
    border-radius: 10px !important;
    color: #e8e8f0 !important;
}
div[data-testid="stSelectbox"] > div > div:hover {
    border-color: #6c3bff88 !important;
}
div[data-testid="stNumberInput"] input {
    background-color: #13131f !important;
    border: 1px solid #2a2a3f !important;
    border-radius: 10px !important;
    color: #e8e8f0 !important;
}
div[data-testid="stButton"] > button {
    width: 100%;
    background: linear-gradient(135deg, #6c3bff, #3b82f6) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.9rem 2rem !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.05em !important;
    cursor: pointer !important;
    margin-top: 1rem;
}
div[data-testid="stButton"] > button:hover {
    box-shadow: 0 8px 30px #6c3bff55 !important;
}
.result-box {
    background: linear-gradient(135deg, #6c3bff18, #3b82f618);
    border: 1px solid #6c3bff44;
    border-radius: 16px;
    padding: 2.5rem 2rem;
    text-align: center;
    margin-top: 1.5rem;
}
.result-label {
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #a78bfa;
    margin-bottom: 0.5rem;
}
.result-price {
    font-family: 'Syne', sans-serif;
    font-size: 3.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #ffffff, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
}
.result-note {
    font-size: 0.8rem;
    color: #55556a;
    margin-top: 0.8rem;
}
div[data-testid="column"] { padding: 0 0.4rem !important; }
</style>
""", unsafe_allow_html=True)

# ── Load model & data ──────────────────────────────────────────────
@st.cache_resource
def load_model():
    return pickle.load(open(os.path.join(os.path.dirname(__file__), 'pipe.pkl'), 'rb'))

@st.cache_data
def load_data():
    return pickle.load(open(os.path.join(os.path.dirname(__file__), 'df.pkl'), 'rb'))

pipe = load_model()
df   = load_data()

# ── Hero ───────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">✦ AI Powered</div>
    <h1>Laptop Price<br>Predictor</h1>
    <p>Configure your specs below and get an instant price estimate</p>
</div>
""", unsafe_allow_html=True)

# ── Brand & Category ───────────────────────────────────────────────
st.markdown('<div class="section-label">Brand & Category</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    company   = st.selectbox("Brand", sorted(df['Company'].unique()))
with col2:
    type_name = st.selectbox("Laptop Type", sorted(df['TypeName'].unique()))

# ── Display ────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Display</div>', unsafe_allow_html=True)
col3, col4 = st.columns(2)
with col3:
    screen_size = st.slider("Screen Size (inches)", 10.0, 18.0, 15.6, 0.1)
    touchscreen = st.selectbox("Touchscreen", ["No", "Yes"])
with col4:
    resolution = st.selectbox("Resolution", [
        "1920x1080", "1366x768", "1600x900",
        "3840x2160", "3200x1800", "2560x1440",
        "2560x1600", "2304x1440"
    ])
    ips = st.selectbox("IPS Display", ["No", "Yes"])

# ── Performance ────────────────────────────────────────────────────
st.markdown('<div class="section-label">Performance</div>', unsafe_allow_html=True)
col5, col6 = st.columns(2)
with col5:
    cpu_brand = st.selectbox("CPU Brand", sorted(df['Cpu brand'].unique()))
    ram       = st.selectbox("RAM (GB)", sorted(df['Ram'].unique()))
with col6:
    gpu_brand = st.selectbox("GPU Brand", sorted(df['Gpu brand'].unique()))
    os_input  = st.selectbox("Operating System", sorted(df['os'].unique()))

# ── Storage & Build ────────────────────────────────────────────────
st.markdown('<div class="section-label">Storage & Build</div>', unsafe_allow_html=True)
col7, col8, col9 = st.columns(3)
with col7:
    ssd = st.selectbox("SSD (GB)", sorted(df['SSD'].unique()))
with col8:
    hdd = st.selectbox("HDD (GB)", sorted(df['HDD'].unique()))
with col9:
    weight = st.number_input("Weight (kg)", min_value=0.5, max_value=5.0, value=1.5, step=0.1)

# ── Predict ────────────────────────────────────────────────────────
st.markdown("")
if st.button("⚡  Predict Price"):

    touchscreen_val = 1 if touchscreen == "Yes" else 0
    ips_val         = 1 if ips == "Yes" else 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi   = ((X_res**2 + Y_res**2) ** 0.5) / screen_size

    query = pd.DataFrame([[
        company, type_name, ram,
        weight, touchscreen_val, ips_val,
        ppi, cpu_brand, ssd, hdd, gpu_brand, os_input
    ]], columns=[
        'Company', 'TypeName', 'Ram',
        'Weight', 'Touchscreen', 'IPS',
        'ppi', 'Cpu brand', 'SSD', 'HDD', 'Gpu brand', 'os'
    ])

    predicted_price = int(np.exp(pipe.predict(query)[0]))

    st.markdown(f"""
    <div class="result-box">
        <div class="result-label">Estimated Price</div>
        <div class="result-price">₹ {predicted_price:,}</div>
        <div class="result-note">Based on {len(df)} laptops · Prediction may vary ±10%</div>
    </div>
    """, unsafe_allow_html=True)