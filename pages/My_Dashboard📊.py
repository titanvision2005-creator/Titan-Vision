import streamlit as st
import pandas as pd

st.set_page_config(page_title="TitanVision", layout="wide")

# =========================
# GLOBAL STYLE (PROFESSIONAL UI)
# =========================
st.markdown("""
<style>


/* Remove Streamlit white top bar */
header[data-testid="stHeader"] {
    background: transparent !important;
}



/* Remove white gap above content */
.block-container {
    padding-top: 1rem !important;
}

/* Hide Streamlit toolbar */
[data-testid="stToolbar"] {
    display: none;
}

/* Make top area same as background */

              
/* =========================
   PAGE BACKGROUND
========================= */

.stApp{
    background:
    radial-gradient(
        circle at top left,
        #14213D 0%,
        #07111F 45%,
        #050B16 100%
    );
    color:#F8FAFC;
}

/* Main content area */
.main .block-container{
    background: transparent;
    color: white;
}

/* Headers */
h1,h2,h3,h4,h5,h6{
    color:#F8FAFC !important;
}

/* Paragraphs */
p, span, label{
    color:#CBD5E1 !important;
}

[data-testid="stSidebar"] {
    background:
    linear-gradient(
    180deg,
    #07111F,
    #0B1F3A,
    #14213D
    );
    border-right: 2px solid #E6B93C;
}

[data-testid="stSidebar"] * {
    color: white;
}


.section-card {
    background:
    linear-gradient(
    135deg,
    #162235,
    #1E293B
    );
    padding: 22px;
    border-radius: 16px;
    border:1px solid rgba(212,175,55,.25);
    box-shadow:
    0 10px 25px rgba(0,0,0,.35);
    margin-bottom: 18px;
}

.section-card h3 {
    color: #f8fafc;
    margin-bottom: 10px;
}

.section-card p {
    color: #e2e8f0;
    font-size: 14px;
}

.highlight {
    font-size: 22px;
    font-weight: 700;
    color:#D4AF37;
}

.title-center {
    text-align: center;
}

/* ==========================
   CARD HOVER EFFECT
========================== */

.section-card{
    transition: .3s;
}

.section-card:hover{

    transform: translateY(-6px);

    border: 1px solid #D4AF37;

    box-shadow:
    0 18px 35px rgba(212,175,55,.22);

}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER (UNCHANGED STRUCTURE)
# =========================
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("logo.png")
    st.markdown("<h1 class='title-center'>Gujrat Titans Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<h4 class='title-center'>Champions • Squad • Stats • Legacy</h4>", unsafe_allow_html=True)

st.markdown("""
<hr style="
border:1px solid #D4AF37;
margin-top:20px;
margin-bottom:25px;
">
""", unsafe_allow_html=True)

# =========================
# ABOUT SECTION
# =========================
st.markdown("""
<h2 style="
color:#FFD966;
font-weight:800;
margin-bottom:20px;">
🏏 Gujarat Titans Overview
</h2>
""", unsafe_allow_html=True)

left, right = st.columns(2)

# =========================
# LEFT COLUMN
# =========================
with left:

    st.markdown("""
    <div class="section-card">
    <h3>👑 Leadership Corner</h3>
    <p><b>The leader shaping GT’s present and future on the field.</b></p>
    <h4>🧢 Shubman Gill</h4>
    <p>One of the brightest batting talents in world cricket, Gill leads Gujarat Titans with composure and a long-term vision for success.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">
    <h3>Gujarat Titans Ownership</h3>
    <p><b>The business foundation behind Gujarat Titans.</b></p>
    <p><b>Franchise Owner</b><br>TORRENT GROUP<br>CVC CAPITAL PARTNERS</p>
    <p><b>League Entry</b><br>Introduced in 2022</p>
    <p><b>Business Headquarters</b><br>Ahmedabad, Gujarat</p>
    <p><b>League</b><br>Indian Premier League (IPL)</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">
    <h3>🧠 Coaching Staff</h3>
    <p><b>Head Coach:</b> Ashish Nehra</p>
    <p><b>Director:</b> Vikram Solanki</p>
    <p><b>Batting Coach:</b> Matthew Hayden</p>
    <p><b>Bowling Coaches:</b> Aashish Kapoor, Naeem Amin</p>
    <p><b>Assistant Coaches:</b> Vijay Dahiya, Narender Negi</p>
    <p><b>Wicketkeeping Coach:</b> Matthew Wade</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">
    <h3>Team Strength Analysis</h3>
    <p>🔴 Strong Bowling Core</p>
    <p>⚖ Balanced Team Composition</p>
    <p>🧠 Smart Tactical Decisions</p>
    <p>🔥 Calm Under Pressure</p>
    <p>🚀 Explosive Match Winners</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# RIGHT COLUMN
# =========================
with right:

    st.markdown("""
    <div class="section-card">
    <h3>Important Stats</h3>
    <p><b>🏆 IPL Titles</b></p>
    <div class="highlight">1 (2022)</div>

    <p><b>⭐ Most Runs</b></p>
    <div class="highlight">Shubman Gill</div>

    <p><b>🔴 Most Wickets</b></p>
    <div class="highlight">Rashid Khan</div>

    <p><b>📈 Highest Total</b></p>
    <div class="highlight">233/3</div>

    <p><b>🏅 Best Finish</b></p>
    <div class="highlight">Champions 2022</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">
    <h3>⭐ Star Players</h3>
    <p><b>Shubman Gill</b> – Captain and consistent performer</p>
    <p><b>Rashid Khan</b> – World-class spinner</p>
    <p><b>Jos Buttler</b> – Explosive match-winner</p>
    <p><b>Sai Sudharsan</b> – Reliable top-order batter</p>
    <p><b>Prasidh Krishna</b> – Elite fast bowler</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">
    <h3>Sponsors</h3>
    <p><b>Principal:</b> JIO, BKT Tires</p>
    <p><b>Technology:</b> Google Pixel</p>
    <p><b>Real Estate:</b> Birla Estates</p>
    <p><b>Finance:</b> Equitas Bank</p>
    <p><b>Gaming:</b> Krafton</p>
    <p><b>Ticketing:</b> BookMyShow</p>
    <p><b>Travel:</b> AirAsia</p>
    <p><b>Sports Kit:</b> EM Sports</p>
    <p><b>Luxury:</b> IGI</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">
    <h3>📅 Timeline</h3>
    <p><b>2022:</b> Champions debut season</p>
    <p><b>2023:</b> Reached final again</p>
    <p><b>2024:</b> Transition phase</p>
    <p><b>2025:</b> Competitive rebuild</p>
    <p><b>2026:</b> New era begins</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# STADIUM SECTION
# =========================
st.markdown("""
<h2 style="
color:#FFD966;
font-weight:800;">
🏟 Home Fortress
</h2>
""", unsafe_allow_html=True)
st.write("GT Fortress")

st.image(
    "Stadium.jpg",
    use_container_width=True
)

st.markdown("""
<div class="section-card">
<p><b>Stadium Name</b></p>
<div class="highlight">Narendra Modi Stadium</div>

<p><b>Location</b></p>
<div class="highlight">Ahmedabad, Gujarat, India</div>

<p><b>Capacity</b></p>
<div class="highlight">1,32,000+</div>

<p><b>Nickname</b></p>
<div class="highlight">World's Largest Cricket Stadium</div>
</div>
""", unsafe_allow_html=True)
