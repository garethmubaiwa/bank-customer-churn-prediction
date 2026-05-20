# STREAM_CHUNK: Importing dependencies and configuring page...
import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# PAGE CONFIG - Institutional Grade
st.set_page_config(
    page_title="Phylax Consultants | Institutional Portfolio Risk",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --navy:         #050c18;
    --navy-mid:     #0b1626;
    --navy-light:   #122035;
    --gold:         #c9a84c;
    --text-primary: #f8f9fa;
    --text-muted:   #8fa3bc;
    --border:       rgba(201, 168, 76, 0.2);
    --card-bg:      rgba(15, 25, 42, 0.7);
}

/* Elite Base Styles */
html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--navy) !important;
    font-family: 'DM Sans', sans-serif;
    color: var(--text-primary);
}

[data-testid="stHeader"] { background-color: var(--navy) !important; }

/* Sidebar - The Vault */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #050c18 0%, #0a1424 100%) !important;
    border-right: 1px solid var(--border);
}

/* Metric Tiles - High-End Glassmorphism */
[data-testid="stMetric"] {
    background: var(--card-bg) !important;
    border: 1px solid var(--border) !important;
    border-radius: 4px !important;
    padding: 1.5rem !important;
    backdrop-filter: blur(12px) !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4) !important;
}

[data-testid="stMetricValue"] {
    font-family: 'Playfair Display', serif !important;
    font-size: 2.2rem !important;
    letter-spacing: -0.02em !important;
    color: var(--gold) !important;
}

[data-testid="stMetricLabel"] {
    text-transform: uppercase !important;
    letter-spacing: 0.15em !important;
    font-size: 0.65rem !important;
    color: var(--text-muted) !important;
}

/* Typography & Dashboard Branding */
.dashboard-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.8rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 0px;
}

.dashboard-subtitle {
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.3em;
    color: var(--gold);
    margin-bottom: 2rem;
    font-weight: 500;
}

.section-label {
    color: var(--gold);
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.25em;
    font-weight: 600;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 1rem;
}

.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--border), transparent);
}

/* Institutional Button */
div.stButton > button {
    background: transparent !important;
    color: var(--gold) !important;
    border: 1px solid var(--gold) !important;
    border-radius: 2px !important;
    padding: 0.8rem 2rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.2em !important;
    font-size: 0.75rem !important;
    transition: all 0.4s ease !important;
    width: 100%;
}

div.stButton > button:hover {
    background: var(--gold) !important;
    color: var(--navy) !important;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style="padding: 2rem 0; border-bottom: 1px solid rgba(201, 168, 76, 0.2); margin-bottom: 2rem; text-align: center;">
        <div style="font-size:1.5rem; color:#c9a84c; margin-bottom: 0.5rem;">🛡️</div>
        <div style="font-family:'Playfair Display',serif; font-size:1.2rem; color:#f8f9fa; font-weight:600; letter-spacing: 0.05em;">
            PHYLAX CONSULTANTS
        </div>
        <div style="font-size:0.6rem; color:#8fa3bc; text-transform:uppercase; letter-spacing:0.4em; margin-top: 0.5rem;">
            Institutional Portfolio Risk
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">Intelligence Engine</div>', unsafe_allow_html=True)
    model_type = st.selectbox("Model Framework", ["xgboost", "random_forest"], format_func=lambda x: x.upper())
    custom_threshold = st.slider("Risk Sensitivity", 0.20, 0.80, 0.42)

    try:
        model = joblib.load(f'models/churn_{model_type}_model.joblib')
        features = joblib.load(f'models/churn_{model_type}_model_features.joblib')
        st.success("System: Secure Link Established")
    except:
        st.error("System: Data Encrypted/Missing")
        st.stop()

st.markdown("""
<div style="margin-top: 1rem;">
    <div class="dashboard-title">Phylax Intelligence</div>
    <div class="dashboard-subtitle">Portfolio Attrition & Capital Preservation Analysis</div>
</div>
""", unsafe_allow_html=True)

with st.expander("PROPRIETARY ACCOUNT DATA INPUT", expanded=True):
    c1, c2, c3 = st.columns(3)
    with c1:
        credit_score = st.number_input("Credit Rating", 300, 900, 720)
        balance = st.number_input("Portfolio Balance (£)", 0.0, value=250000.0)
    with c2:
        age = st.number_input("Client Age", 18, 100, 45)
        geography = st.selectbox("Market Region", ["France", "Germany", "Spain"])
    with c3:
        num_of_products = st.number_input("Product Exposure", 1, 4, 2)
        card_type = st.selectbox("Account Tier", ["DIAMOND", "PLATINUM", "GOLD", "SILVER"])

    st.markdown("<br>", unsafe_allow_html=True)
    predict_clicked = st.button("Execute Quantitative Attrition Assessment")

if predict_clicked:
    # Logic placeholder for UI display (Actual model prediction would go here)
    prob = 0.18 
    risk_pct = prob * 100

    st.markdown('<div class="section-label">Executive Risk Summary</div>', unsafe_allow_html=True)
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Attrition Probability", f"{prob:.1%}")
    m2.metric("Portfolio Rating", "Stable / Low Risk" if prob < 0.2 else "Review Required")
    m3.metric("Projected Capital Variance", f"£{balance * prob:,.0f}")

    # Elite Gauge Visualization
    fig = go.Figure(go.Indicator(
        mode="gauge+number", value=risk_pct,
        number={'font': {'color': '#c9a84c', 'family': 'Playfair Display', 'size': 50}, 'suffix': '%'},
        gauge={
            'bar': {'color': '#c9a84c'},
            'axis': {'range': [0, 100], 'tickcolor': '#8fa3bc', 'tickfont': {'color': '#8fa3bc'}},
            'bgcolor': 'rgba(255,255,255,0.02)',
            'steps': [
                {'range': [0, 30], 'color': 'rgba(201, 168, 76, 0.05)'},
                {'range': [70, 100], 'color': 'rgba(224, 92, 92, 0.05)'}
            ]
        }
    ))
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=300, margin=dict(t=0, b=0))
    st.plotly_chart(fig, use_container_width=True)

current_year = datetime.now().year
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.markdown(f"""
<div style="text-align:center; padding: 1.5rem 0 3rem 0;">
    <div style="color:#c9a84c; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.4em; font-weight:700; margin-bottom: 0.8rem;">
        © {current_year} Phylax Consultants
    </div>
    <div style="color:#4a6180; font-size:0.68rem; letter-spacing:0.12em; line-height:2; max-width: 900px; margin: 0 auto; text-transform: uppercase;">
        Predictions are probabilistic estimates intended to support, not replace, human judgement
        &nbsp;&nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;&nbsp;&nbsp;
        Retrain periodically to maintain model currency
        &nbsp;&nbsp;&nbsp;&nbsp;·&nbsp;&nbsp;&nbsp;&nbsp;
        Confidential Institutional Intelligence
    </div>
</div>
""", unsafe_allow_html=True)