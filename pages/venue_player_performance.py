import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

left,right,up=st.columns([1,2,1])
with right:
    st.image("logo.png")

st.title("🏟️ VENUE WISE PLAYER PERFORMANCE ANALYSIS")
st.write("Analyze how a player performs in specific stadium conditions")

df = pd.read_excel("TITAN VISION.xlsx", sheet_name="VENUE_WISE_PLAYER_PERFORMANCE")

# =========================
# GLOBAL STYLE (UPDATED COLORS)
# =========================
st.markdown("""
<style>
.card {
    background: linear-gradient(135deg, #111827, #1f2937);
    padding: 18px;
    border-radius: 16px;
    border: 1px solid #374151;
    box-shadow: 0 6px 18px rgba(0,0,0,0.25);
}
.card p {
    color: #e5e7eb;   /* 👈 FIXED TEXT COLOR */
    font-size: 15px;
}
.card h3 {
    margin-bottom: 10px;
}
.tag {
    display:inline-block;
    padding:5px 12px;
    border-radius:12px;
    font-size:12px;
    font-weight:600;
}
.good {background:#dcfce7;color:#166534;}
.avg {background:#fef9c3;color:#854d0e;}
.bad {background:#fee2e2;color:#991b1b;}

.bad {background:#fee2e2;color:#991b1b;}

/* 🔥 PREMIUM BUTTON */
.stButton > button {
    background: linear-gradient(135deg, #2563eb, #1e3a8a);
    color: white;
    border: none;
    padding: 10px 22px;
    font-size: 15px;
    border-radius: 10px;
    font-weight: 600;
    transition: 0.3s ease;
}

/* Hover */
.stButton > button:hover {
    background: linear-gradient(135deg, #1d4ed8, #172554);
    transform: scale(1.03);
}

/* Click */
.stButton > button:active {
    transform: scale(0.98);
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

        <p style="color:#38bdf8;margin:0;">
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

        st.divider()

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

            <p>⚾ Balls Faced: <b>{balls}</b></p>
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
            <p>🏏 Wickets: <b>{wickets}</b></p>
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