import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

left,right,up=st.columns([1,2,1])
with right:
    st.image("logo.png")

st.markdown("""
<h1 style="
text-align:center;
font-size:50px;
font-weight:900;
color:#F8FAFC;
margin-bottom:5px;">
Venue Player Intelligence
</h1>

<p style="
text-align:center;
color:#CBD5E1;
font-size:18px;">
Analyze Venue-Specific Player Performance and Match Impact
</p>
""", unsafe_allow_html=True)

df = pd.read_excel("TITAN VISION.xlsx", sheet_name="VENUE_WISE_PLAYER_PERFORMANCE")


st.markdown("""
<style>

/* Remove Streamlit white top bar */
header[data-testid="stHeader"] {
    background: transparent !important;
}

/* Main app background */


/* Remove white gap above content */
.block-container {
    padding-top: 1rem !important;
}

/* Hide Streamlit toolbar */
[data-testid="stToolbar"] {
    display: none;
}

/* Make top area same as background */

            

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
    color: #FFFFFF !important;
}

/* =========================
   PAGE BACKGROUND
========================= */

.stApp {
    background:
radial-gradient(
circle at top left,
#14213D,
#07111F 45%
);
    color: white;
}

/* =========================
   MAIN CARD
========================= */

.card{

background:
linear-gradient(
135deg,
#162235,
#1E293B
);

padding:22px;

border-radius:18px;

border:1px solid rgba(212,175,55,.30);

box-shadow:
0 10px 25px rgba(0,0,0,.35);

transition:.3s;

}

.card:hover{

transform:translateY(-5px);

border-color:#D4AF37;

box-shadow:
0 18px 35px rgba(212,175,55,.22);

}

/* =========================
   TAGS
========================= */

.tag {
    display:inline-block;
    padding:6px 14px;
    border-radius:12px;
    font-size:12px;
    font-weight:600;
}

.good {
    background:#14532d;
    color:#bbf7d0;
}

.avg {
    background:#E6B93C;
    color:#00112B;
}

.bad {
    background:#7f1d1d;
    color:#fecaca;
}

/* =========================
   BUTTON
========================= */

.stButton button{

width:100%;

height:48px;

background:#D4AF37;

color:#07111F;

font-weight:800;

border-radius:14px;

border:none;

transition:.3s;

}

.stButton button:hover{

background:#FFD966;

transform:translateY(-2px);

}

/* =========================
   SELECTBOX
========================= */

div[data-baseweb="select"]>div{

background:#162235 !important;

border:1px solid #D4AF37 !important;

border-radius:14px;

color:white !important;

}

div[data-baseweb="select"] span{

color:white !important;

}
/* =========================
   TITLE
========================= */

h1 {
    color: white !important;
    text-align: center;
    font-weight: 800;
}

/* =========================
   TEXT
========================= */

p,
span,
label {
    color: #D8E4FF;
}

[data-testid="stMetric"]{

background:
linear-gradient(
135deg,
#162235,
#1E293B
);

border:1px solid rgba(212,175,55,.30);

border-radius:18px;

padding:18px;

box-shadow:
0 10px 25px rgba(0,0,0,.35);

}

[data-testid="stMetricValue"]{

color:#FFD966 !important;

font-weight:800;

}

[data-testid="stMetricLabel"]{

color:#CBD5E1 !important;

}

</style>
""", unsafe_allow_html=True)

# =========================
# FILTERS
# =========================
unique_venues = df["Venue"].dropna().unique()
venue = st.selectbox("Select Venue", unique_venues, index=None, placeholder="Select Venue")

unique_players = df["Player_Name"].dropna().unique()
player = st.selectbox("Select Player", unique_players, index=None, placeholder="Select Player")

analyze = st.button("🚀 VIEW ANALYSIS")

# =========================
# MAIN LOGIC
# =========================
if analyze and venue is not None and player is not None:

    filtered = df[(df["Venue"] == venue) & (df["Player_Name"] == player)]

    if filtered.empty:
        st.warning("Selected Player has no record in this venue")
    else:
        rows = filtered.iloc[0]

        Name = rows['Player_Name']
        Role = rows['Role']
        Matches = rows['Matches_played']

        runs = rows['Runs']
        balls = rows['Balls']
        runs_conceded = rows['Runs_Conceded']
        wickets = rows['Wickets']
        Overs = rows['Overs']
        Economy = rows['Economy']
        sr = rows['Strike rate']
        avg = rows['Average']

        # =========================
        # HEADER CARD
        # =========================
        st.markdown(f"""
        <div class="card">
        <h2 style="color:#f9fafb;margin:0;">👤 {Name}</h2>

        <p style="margin-top:8px;">
        <span class="tag avg">{Role}</span>
        &nbsp;&nbsp; 🏟️ {venue}
        </p>

        <p style="color:#CBD5E1;margin:0;">
        📊 Matches Played: {Matches}
        </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # =========================
        # PERFORMANCE TAGS
        # =========================
        col_tag1, col_tag2 = st.columns(2)

        with col_tag1:
            if sr > 140:
                st.success("🔥 Aggressive batting impact at this venue")
            elif sr < 100:
                st.warning("⚠️ Low scoring rate at this venue")
            else:
                st.info("⚖️ Balanced batting performance")

        with col_tag2:
            if Economy < 7 and Economy > 0:
                st.success("🎯 Highly economical bowling")
            elif Economy > 9:
                st.error("⚠️ Expensive bowling performance")
            elif Economy == 0:
                st.info("No Bowling Record Found")
            else:
                st.info("⚖️ Average bowling control")

        st.markdown("""
        <hr style="
        border:1px solid #334155;
        margin-top:20px;
        margin-bottom:20px;
        ">
        """, unsafe_allow_html=True)
        # =========================
        # 2 COLUMN LAYOUT
        # =========================
        col1, col2 = st.columns(2)

        # =========================
        # BATTING CARD
        # =========================
        with col1:
            st.markdown(f"""
            <div class="card">
            <h3 style="color:#22c55e;">🏏 Batting Performance</h3>

            <p style="color:#CBD5E1;">
            ⚾ Balls Faced :
            <b style="color:#FFD966;">{balls}</b>
            </p>
            <p>⚡ Runs: <b>{runs}</b></p>
            <p>🚀 Strike Rate: <b>{sr:.2f}</b></p>
            <p>📈 Average: <b>{avg:.2f}</b></p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("**Strike Rate Impact**")
            st.progress(min(sr / 200, 1.0))
            st.caption(f"{sr:.2f}")

            st.markdown("**Consistency (Average)**")
            st.progress(min(avg / 100, 1.0))
            st.caption(f"{avg:.2f}")

            if runs > 50:
                st.success("🏟️ Strong batting venue for player")
            else:
                st.warning("📉 Limited batting impact here")

        # =========================
        # BOWLING CARD
        # =========================
        with col2:
            st.markdown(f"""
            <div class="card">
            <h3 style="color:#f87171;">🔴 Bowling Performance</h3>

            <p>⚾ Overs Bowled: <b>{Overs}</b></p>
            <p>💥 Runs Conceded: <b>{runs_conceded}</b></p>
            <p>📉 Economy: <b>{Economy:.2f}</b></p>
            <p style="color:#CBD5E1;">
            🏏 Wickets :
            <b style="color:#FFD966;">{wickets}</b>
            </p>
            </div>
            """, unsafe_allow_html=True)

            if wickets > 0:
                st.markdown("**Economy Control**")
                st.progress(min(Economy / 10, 1.0))
                st.caption(f"{Economy:.2f}")

                if wickets >= 3:
                    st.success("🔥 Strong wicket-taking performance")
                else:
                    st.info("⚖️ Moderate bowling impact")

        st.markdown("<br>", unsafe_allow_html=True)

        # =========================
        # FINAL INSIGHT
        # =========================
        st.markdown("### 🧠 Match Insight")

        if "Batsman" in Role or "WK" in Role:
            if runs > 50:
                st.success("Strong batting contribution at this venue.")
            else:
                st.info("Limited batting impact at this venue.")

        elif "Bowler" in Role:
            if wickets >= 3:
                st.success("High impact bowling performance at this venue.")
            else:
                st.info("Moderate bowling contribution.")

        else:
            if runs > runs_conceded:
                st.success("Balanced player with batting advantage.")
            else:
                st.info("Balanced contribution across skills.")