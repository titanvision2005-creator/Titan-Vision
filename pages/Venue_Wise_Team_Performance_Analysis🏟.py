import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

# ==========================================

# PAGE CONFIG

# ==========================================

st.set_page_config(
page_title="Venue Intelligence",
layout="wide"
)

# ==========================================

# LOAD DATA

# ==========================================

df = pd.read_excel(
"TITAN VISION.xlsx",
sheet_name="VENUE_PERFORMANCE"
)

# ==========================================

# GT PREMIUM CSS

# ==========================================

st.markdown("""
<style>

/* =========================
GT PREMIUM THEME
========================= */

.stApp{

background:
radial-gradient(
circle at top left,
#14213D,
#07111F 45%
);

color:white;

}

/* Remove Streamlit Header */
header{
visibility:hidden;
}

/* Title */
.hero-title{
font-size:52px;
font-weight:800;
text-align:center;
color:white;
margin-bottom:10px;
text-shadow:0px 2px 15px rgba(255,255,255,0.15);
}

.hero-sub{
font-size:18px;
text-align:center;
color:#d1d5db;
margin-bottom:30px;
}

/* Select Boxes */
.stSelectbox div[data-baseweb="select"]{
background:#142850;
border:1px solid #C9A44C;
border-radius:12px;
}

/* KPI Cards */
.metric-card{
background:rgba(255,255,255,0.05);
backdrop-filter:blur(12px);
padding:24px;
border-radius:20px;
text-align:center;
border:1px solid rgba(201,164,76,0.35);
box-shadow:0px 8px 30px rgba(0,0,0,0.25);
transition:0.3s;
}

.metric-card:hover{
transform:translateY(-5px);
border-color:#C9A44C;
}

.metric-value{
font-size:34px;
font-weight:800;
color:#F5D06F;
}

.metric-label{
font-size:14px;
color:white;
}

/* Info Cards */
.info-card{
background:rgba(255,255,255,0.05);
backdrop-filter:blur(12px);
padding:25px;
border-radius:20px;
border-left:5px solid #C9A44C;
box-shadow:0px 8px 25px rgba(0,0,0,0.25);
color:white;
}

.stadium-card{
background:rgba(255,255,255,0.05);
backdrop-filter:blur(12px);
padding:25px;
border-radius:20px;
border-left:5px solid #C9A44C;
box-shadow:0px 8px 25px rgba(0,0,0,0.25);
color:white;
}

/* Tags */
.tag{
display:inline-block;
padding:8px 18px;
border-radius:25px;
font-size:13px;
font-weight:700;
}

.good{
background:#14532d;
color:#86efac;
}

.bad{
background:#7f1d1d;
color:#fca5a5;
}

/* Section Titles */
h1,h2,h3,h4{
color:white !important;
}

/* Divider */
hr{
border:none;
height:2px;
background:linear-gradient(
90deg,
#C9A44C,
transparent
);
}

/* Sidebar */
section[data-testid="stSidebar"]{
background:#04122f;
border-right:2px solid #C9A44C;
}

/* Sidebar Text */
section[data-testid="stSidebar"] *{
color:white !important;
}

/* Buttons */
.stButton button{
background:#C9A44C;
color:black;
font-weight:700;
border:none;
border-radius:12px;
padding:10px 20px;
}

.stButton button:hover{
background:#F5D06F;
color:black;
}

/* Progress Bar */
.stProgress > div > div > div > div{
background:#C9A44C;
}

</style>
""", unsafe_allow_html=True)

# ==========================================

# HEADER

# ==========================================

col1,col2,col3 = st.columns([1,2,1])

with col2:
    st.image("logo.png", width=500)

st.markdown("""
<div class='hero-title'>
🏟 Venue Intelligence Center
</div>

<div class='hero-sub'>
Transforming Venue Data into Match-Winning Decisions
</div>
""", unsafe_allow_html=True)

# ==========================================

# VENUE SELECTOR

# ==========================================

venues = ["Select Venue"] + sorted(
df["Venue"].unique().tolist()
)

venue = st.selectbox(
"Select Venue",
venues
)

if venue == "Select Venue":
    st.stop()

# ==========================================

# LOADING

# ==========================================

with st.spinner("Analyzing venue performance..."):
    time.sleep(1)

filtered = df[df["Venue"] == venue]

if filtered.empty:
    st.warning("No Data Available")
    st.stop()

row = filtered.iloc[0]

matches = int(row["Matches played"])
wins = int(row["Wins"])
losses = int(row["Losses"])
win_percent = round(float(row["Win%"]),1)

# ==========================================

# VENUE HEADER

# ==========================================

st.markdown(
    f"## 📍 {venue}"
)

if win_percent >= 60:
    st.markdown(
        "<span class='tag good'>🔥 Strong Venue</span>",
        unsafe_allow_html=True
    )
else:
    st.markdown(
        "<span class='tag bad'>⚠️ Challenging Venue</span>",
        unsafe_allow_html=True
    )

st.write("")

# ==========================================
# KPI CARDS
# ==========================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-value">{matches}</div>
            <div class="metric-label">🏏 Matches</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-value">{wins}</div>
            <div class="metric-label">✅ Wins</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-value">{losses}</div>
            <div class="metric-label">❌ Losses</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-value">{win_percent}%</div>
            <div class="metric-label">📊 Win Rate</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

# ==========================================
# VENUE STRENGTH
# ==========================================

st.subheader("🎯 Venue Strength")

rating = min(round(win_percent / 10, 1), 10)

st.progress(rating / 10)

st.caption(
    f"Venue Rating : {rating}/10"
)

st.write("")

# ==========================================

# MAIN LAYOUT

# ==========================================

left,right = st.columns([1.1,1])

with left:

    st.markdown("""
    <div class="stadium-card">

    <h4 style="color:#0B1F5B;">
    🏟 Venue Overview
    </h4>

    Historical Gujarat Titans performance
    at this venue based on match results.

    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-card">

    <h4 style="color:#0B1F5B;">
    🧠 Executive Summary
    </h4>

    Gujarat Titans have played
    <b>{matches}</b> matches at
    <b>{venue}</b>.

    The team has secured
    <b>{wins}</b> victories and
    recorded a win percentage of
    <b>{win_percent}%</b>.

    This performance reflects
    the overall effectiveness
    of the team at this venue.

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if win_percent >= 75:
        st.success(
            "🏆 Exceptional venue record with consistently dominant performances."
        )

    elif win_percent >= 60:
        st.success(
            "💪 Strong venue with a positive historical record."
        )

    elif win_percent >= 45:
        st.warning(
            "⚖️ Balanced venue with mixed results."
        )

    elif win_percent >= 30:
        st.warning(
            "📉 Below average performance record."
        )

    else:
        st.error(
            "🚫 Historically challenging venue."
        )

with right:

    st.subheader("📊 Performance Split")

    fig, ax = plt.subplots(
        figsize=(4.5,4.5)
    )

    ax.pie(
        [wins,losses],
        labels=None,
        colors=[
            "#0B1F5B",
            "#C9A44C"
        ],
        startangle=90,
        wedgeprops=dict(width=0.35)
    )

    ax.text(
        0,
        0,
        f"{win_percent}%",
        ha="center",
        va="center",
        fontsize=22,
        fontweight="bold"
    )

    ax.axis("equal")

    st.pyplot(
        fig,
        use_container_width=False
    )

    st.markdown(
        f"""
        <div style="text-align:center;">

        <span style="color:#0B1F5B;">
        ● Wins ({wins})
        </span>

        &nbsp;&nbsp;&nbsp;

        <span style="color:#C9A44C;">
        ● Losses ({losses})
        </span>

        </div>
        """,
        unsafe_allow_html=True
    )