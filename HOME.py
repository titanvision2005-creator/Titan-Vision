import streamlit as st
import base64

st.set_page_config(page_title="TitanVision", layout="wide")

# =========================
# HIDE HEADER + SIDEBAR
# =========================
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
section[data-testid="stSidebar"] {display: none;}
</style>
""", unsafe_allow_html=True)

# =========================
# LOAD LOGO
# =========================
def get_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo = get_base64("MLOGO.png")

# =========================
# STYLE
# =========================
st.markdown(f"""
<style>
.hero {{
    text-align: center;
    margin-top: 40px;
    margin-bottom: 40px;
}}

.hero img {{
    width: 140px;
    border-radius: 50%;
    margin-bottom: 10px;
}}

.title {{
    font-size: 48px;
    font-weight: 800;
}}

.titan {{
    color: #0B1F5B;
}}

.vision {{
    color: #0B1F5B;
}}

.subtitle {{
    color: #666;
    font-size: 16px;
}}

.section {{
    text-align: center;
    padding: 25px;
    border-radius: 16px;
    background: white;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
}}

.icon {{
    font-size: 30px;
}}

.label {{
    font-size: 16px;
    font-weight: 600;
    margin-top: 8px;
    margin-bottom: 10px;
}}
</style>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================
st.markdown(f"""
<div class="hero">
    <img src="data:image/jpeg;base64,{logo}">
    <div class="title">
        <span class="titan">Titan</span><span class="vision">Vision</span>
    </div>
    <div class="subtitle">Cricket, Decoded 🏏</div>
</div>
""", unsafe_allow_html=True)

# =========================
# GRID (FINAL ORDER)
# =========================

# ROW 1 → Dashboard, Squad, Venue
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="section"><div class="icon">📊</div><div class="label">Dashboard</div></div>', unsafe_allow_html=True)
    if st.button("Open", key="dash"):
        st.switch_page("pages/dashboard.py")

with col2:
    st.markdown('<div class="section"><div class="icon">🧾</div><div class="label">Squad Explorer</div></div>', unsafe_allow_html=True)
    if st.button("Open", key="squad"):
        st.switch_page("pages/squad.py")

with col3:
    st.markdown('<div class="section"><div class="icon">🏟</div><div class="label">Venue Analysis</div></div>', unsafe_allow_html=True)
    if st.button("Open", key="venue"):
        st.switch_page("pages/venue_performance.py")


# ROW 2 → Opponent, Venue Player, Playing XI
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown('<div class="section"><div class="icon">⚔️</div><div class="label">Opponent Analysis</div></div>', unsafe_allow_html=True)
    if st.button("Open", key="opp"):
        st.switch_page("pages/opponent.py")

with col5:
    st.markdown('<div class="section"><div class="icon">👤</div><div class="label">Venue Player Analysis</div></div>', unsafe_allow_html=True)
    if st.button("Open", key="player"):
        st.switch_page("pages/venue_player_performance.py")

with col6:
    st.markdown('<div class="section"><div class="icon">🏏</div><div class="label">Playing XI</div></div>', unsafe_allow_html=True)
    if st.button("Open", key="xi"):
        st.switch_page("pages/playing_XI.py")