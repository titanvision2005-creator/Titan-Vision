import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Opponent Analysis",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =====================================
# PREMIUM GT THEME
# =====================================

st.markdown("""
<style>

/* Hide Streamlit */
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.block-container{
    padding-top:1rem;
}

/* =========================
BACKGROUND
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

/* Sidebar */

[data-testid="stSidebar"]{

background:
linear-gradient(
180deg,
#07111F,
#0B1F3A,
#14213D
);

border-right:2px solid #D4AF37;

}

[data-testid="stSidebar"] *{
color:white;
}

/* =========================
SELECT BOX
========================= */

div[data-baseweb="select"]>div{

background:#162235 !important;

border:1px solid #D4AF37 !important;

border-radius:14px;

color:white !important;

}

/* Selected value */
div[data-baseweb="select"] span{
color:white !important;
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
METRIC CARDS
========================= */

[data-testid="stMetric"]{

background:
linear-gradient(
135deg,
#162235,
#1E293B
);

padding:18px;

border-radius:18px;

border:1px solid rgba(212,175,55,.30);

box-shadow:
0 10px 25px rgba(0,0,0,.35);

}

[data-testid="stMetricValue"]{

color:#FFD966 !important;

font-size:30px;

font-weight:800;

}

[data-testid="stMetricLabel"]{

color:#CBD5E1 !important;

}

/* =========================
HEADINGS
========================= */

h1,h2,h3,h4{

color:#F8FAFC !important;

}

p,label,span{

color:#CBD5E1;

}

/* Divider */

hr{

border:1px solid #334155;

}

/* Card */

.info-card{

background:
linear-gradient(
135deg,
#162235,
#1E293B
);

padding:22px;

border-radius:18px;

border:1px solid rgba(212,175,55,.25);

box-shadow:
0 10px 25px rgba(0,0,0,.35);

transition:.3s;

}

.info-card:hover{

transform:translateY(-5px);

border-color:#D4AF37;

box-shadow:
0 18px 35px rgba(212,175,55,.22);

}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

col1,col2,col3=st.columns([1,2,1])

with col2:

    st.image("logo.png",width=500)

    st.markdown("""
    <h1 style="
    text-align:center;
    font-size:50px;
    font-weight:900;
    margin-bottom:5px;">
    Opponent Intelligence
    </h1>

    <p style="
    text-align:center;
    color:#CBD5E1;
    font-size:18px;">
    Analyze Gujarat Titans Performance Against Every Opponent
    Across Different Venues
    </p>
    """,unsafe_allow_html=True)

# =====================================
# LOAD DATA
# =====================================

df=pd.read_excel(
"TITAN VISION.xlsx",
sheet_name="OPPONENT_DATA"
)

# =====================================
# FILTERS
# =====================================

c1,c2=st.columns(2)

with c1:

    team=df["OPPONENT"].dropna().unique()

    team1=st.selectbox(
        "Select Opponent",
        team,
        index=None,
        placeholder="Choose Opponent"
    )

with c2:

    venue_list=df["VENUE"].dropna().unique()

    venue=st.selectbox(
        "Select Venue",
        venue_list,
        index=None,
        placeholder="Choose Venue"
    )

Analyze=st.button("🚀 Generate Analysis")

if Analyze and team1 is None:

    st.warning("Please select an opponent.")

    st.stop()

# =====================================
# MAIN LOGIC
# =====================================

if Analyze:

    if venue is None:
        filtered = df[
            (df["OPPONENT"] == team1) &
            (df["VENUE"] == "OVERALL")
        ]
    else:
        filtered = df[
            (df["OPPONENT"] == team1) &
            (df["VENUE"] == venue)
        ]

    if filtered.empty:
        st.warning("No record found.")
        st.stop()

    row = filtered.iloc[0]

    # ==========================
    # VALUES
    # ==========================

    matches = row["MATCHES"]
    win = row["WINS"]
    lose = row["LOSSES"]

    winp = float(row["WIN%"])
    losep = float(row["LOSE%"])

    high = row["HIGHEST GT SCORE"]
    low = row["LOWEST GT SCORE"]
    avg = row["AVERAGE GT SCORE"]
    avgwkts = row["AVERAGE GT WICKETS"]
    avgovers = row["AVERAGE GT OVERS"]

    high1 = row["HIGHEST OPPONENT SCORE"]
    low1 = row["LOWEST OPPONENT SCORE"]
    avg1 = row["AVERAGE OPPONENT SCORE"]
    avg2 = row["AVERAGE OPPONENT WICKETS TAKEN"]
    avg3 = row["AVERAGE OPPONENT OVERS"]

    # ==========================
    # PAGE TITLE
    # ==========================

    st.markdown(f"""
    <h2 style="
    text-align:center;
    color:#FFD966;
    margin-top:20px;">
    📍 {team1} @ {venue if venue else "Overall"}
    </h2>
    """, unsafe_allow_html=True)

    # ==========================
    # KPI METRICS
    # ==========================

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric("🎯 Matches", matches)

    with m2:
        st.metric("✅ Wins", win)

    with m3:
        st.metric("❌ Losses", lose)

    with m4:
        st.metric("📊 Win Rate", f"{winp:.1f}%")

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================
    # INFORMATION CARDS
    # ==========================

    left, right = st.columns(2)

    with left:

        st.markdown("### 🏏 Gujarat Titans")

        st.markdown(f"""
        <div class="info-card">

        <h4 style="color:#FFD966;">
        Gujarat Titans Statistics
        </h4>

        <p style="color:#CBD5E1;">
        🔥 Highest Score :
        <b style="color:#FFD966;">{high}</b>
        </p>

        <p style="color:#CBD5E1;">
        📉 Lowest Score :
        <b style="color:#FFD966;">{low}</b>
        </p>

        <p style="color:#CBD5E1;">
        📊 Average Score :
        <b style="color:#FFD966;">{avg}</b>
        </p>

        <p style="color:#CBD5E1;">
        ⏱ Average Overs :
        <b style="color:#FFD966;">{avgovers}</b>
        </p>

        <p style="color:#CBD5E1;">
        🎯 Average Wickets :
        <b style="color:#FFD966;">{avgwkts}</b>
        </p>

        </div>
        """, unsafe_allow_html=True)

    with right:

        st.markdown("### ⚔️ Opponent")

        st.markdown(f"""
        <div class="info-card">

        <h4 style="color:#FFD966;">
        Opponent Statistics
        </h4>

        <p style="color:#CBD5E1;">
        🔥 Highest Score :
        <b style="color:#FFD966;">{high1}</b>
        </p>

        <p style="color:#CBD5E1;">
        📉 Lowest Score :
        <b style="color:#FFD966;">{low1}</b>
        </p>

        <p style="color:#CBD5E1;">
        📊 Average Score :
        <b style="color:#FFD966;">{avg1}</b>
        </p>

        <p style="color:#CBD5E1;">
        ⏱ Average Overs :
        <b style="color:#FFD966;">{avg3}</b>
        </p>

        <p style="color:#CBD5E1;">
        🎯 Average Wickets :
        <b style="color:#FFD966;">{avg2}</b>
        </p>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================
# PERFORMANCE OVERVIEW
# =====================================

    st.markdown("""
    <h2 style="
    color:#FFD966;
    margin-top:20px;">
    📊 Performance Overview
    </h2>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # =====================================
    # DONUT CHART
    # =====================================

    with col1:

        st.markdown("### Win Distribution")

        fig, ax = plt.subplots(figsize=(4,4))

        fig.patch.set_facecolor("#07111F")
        ax.set_facecolor("#07111F")

        wedges, _ = ax.pie(
            [win, lose],
            colors=["#D4AF37", "#EF4444"],
            startangle=90,
            wedgeprops=dict(
                width=0.35,
                edgecolor="#07111F"
            )
        )

        ax.text(
            0,
            0,
            f"{winp:.1f}%\nWin Rate",
            ha="center",
            va="center",
            fontsize=16,
            color="white",
            fontweight="bold"
        )

        ax.legend(
            wedges,
            [
                f"Wins ({win})",
                f"Losses ({lose})"
            ],
            loc="lower center",
            bbox_to_anchor=(0.5,-0.15),
            ncol=2,
            frameon=False,
            fontsize=10,
            labelcolor="white"
        )

        ax.axis("equal")

        st.pyplot(fig)

    # =====================================
    # BAR CHART
    # =====================================

    with col2:

        st.markdown("### Average Score Comparison")

        fig2, ax2 = plt.subplots(figsize=(5,4))

        fig2.patch.set_facecolor("#07111F")
        ax2.set_facecolor("#07111F")

        bars = ax2.bar(
            ["GT","Opponent"],
            [avg,avg1],
            color=[
                "#D4AF37",
                "#60A5FA"
            ],
            width=0.55
        )

        ax2.tick_params(colors="white")

        ax2.spines["bottom"].set_color("white")
        ax2.spines["left"].set_color("white")

        ax2.spines["top"].set_visible(False)
        ax2.spines["right"].set_visible(False)

        for bar in bars:

            h = bar.get_height()

            ax2.text(
                bar.get_x()+bar.get_width()/2,
                h+2,
                f"{h:.0f}",
                ha="center",
                fontsize=11,
                color="white"
            )

        st.pyplot(fig2)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================
    # PERFORMANCE STRENGTH
    # =====================================

    st.markdown("""
    <h2 style="
    color:#FFD966;">
    📈 Performance Strength
    </h2>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:

        st.write("**GT Average Score Strength**")

        st.progress(min(avg/250,1.0))

    with c2:

        st.write("**Opponent Average Score Strength**")

        st.progress(min(avg1/250,1.0))

    st.write("**Winning Probability**")

    st.progress(winp/100)

    st.caption(
        f"Win Probability : {winp:.1f}%"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================
    # MATCH INSIGHT
    # =====================================

    st.markdown("""
    <h2 style="
    color:#FFD966;">
    🧠 Match Insight
    </h2>
    """, unsafe_allow_html=True)

    if winp >= 70:

        st.success(
            "🔥 Gujarat Titans have historically dominated this matchup. The team has maintained a consistently high winning percentage, making this one of its strongest opponent records."
        )

    elif winp >= 50:

        st.success(
            "⚖️ Gujarat Titans hold a slight advantage in this contest. Historical performances indicate a competitive matchup with a favorable edge."
        )

    else:

        st.error(
            "⚠️ This has historically been a challenging matchup for Gujarat Titans. Strategic planning and player selection will be crucial to improve the team's chances."
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================
    # STRATEGIC RECOMMENDATION
    # =====================================

    st.markdown(f"""
    <div class="info-card">

    <h3 style="color:#FFD966;">
    🎯 Strategic Recommendation
    </h3>

    <p style="color:#CBD5E1;">

    Based on historical records against
    <b style="color:#FFD966;">{team1}</b>,
    Gujarat Titans currently maintain a
    <b style="color:#FFD966;">{winp:.1f}%</b>
    win rate.

    This analysis can assist in identifying
    venue-specific strengths, evaluating
    previous performances, and supporting
    smarter match preparation and tactical
    decision-making.

    </p>

    </div>
    """, unsafe_allow_html=True)