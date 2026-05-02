import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# =========================
# PREMIUM BUTTON STYLE
# =========================
st.markdown("""
<style>
div.stButton > button {
    background: linear-gradient(90deg, #1f3b73, #2c5aa0);
    color: white;
    padding: 10px 24px;
    border-radius: 12px;
    border: none;
    font-weight: 600;
    transition: 0.3s;
}
div.stButton > button:hover {
    background: linear-gradient(90deg, #2c5aa0, #1f3b73);
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
right,left,up=st.columns([1,2,1])
with left:
    st.image("logo.png")

    st.title("Venue Wise Opponent Team Analysis")
    st.write("Analyze Gujarat Titans Overall Performance Against Opponents by Venue")

# =========================
# LOAD DATA
# =========================
df = pd.read_excel("TITAN VISION.xlsx", sheet_name="OPPONENT_DATA")

# =========================
# SELECTORS
# =========================
colA, colB = st.columns(2)

with colA:
    team = df["OPPONENT"].dropna().unique()
    team1 = st.selectbox("Select Opponent", team, index=None, placeholder="Select Opponent")

with colB:
    venue_list = df["VENUE"].dropna().unique()
    venue = st.selectbox("Select Venue", venue_list, index=None, placeholder="Select Venue")

# =========================
# BUTTON
# =========================
Analyze = st.button("🚀 Generate Analysis")

# =========================
# VALIDATION
# =========================
if Analyze and team1 is None:
    st.warning("Select Opponent First")
    st.stop()

# =========================
# MAIN LOGIC
# =========================
if Analyze:
    if venue is None:
        filtered = df[(df["OPPONENT"] == team1) & (df["VENUE"] == "OVERALL")]
    else:
        filtered = df[(df["OPPONENT"] == team1) & (df["VENUE"] == venue)]

    if filtered.empty:
        st.warning("No Record Found")
        st.stop()

    row = filtered.iloc[0]

    # =========================
    # VALUES
    # =========================
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

    # =========================
    # TITLE
    # =========================
    st.markdown(f"## 📍 {team1} @ {venue if venue else 'Overall'}")

    # =========================
    # METRICS
    # =========================
    c1, c2, c3, c4 = st.columns(4)

    c1.metric("🎯 Matches", matches)
    c2.metric("✅ Wins", win)
    c3.metric("❌ Losses", lose)
    c4.metric("📊 Win %", f"{winp:.1f}%")

    st.divider()

    # =========================
    # CARDS
    # =========================
    left, right = st.columns(2)

    with left:
        st.markdown("### 🏏 Gujarat Titans")
        st.markdown(f"""
        <div style="background:white;padding:20px;border-radius:12px;
        box-shadow:0 4px 15px rgba(0,0,0,0.06)">
        <p>🔥 Highest Score: <b>{high}</b></p>
        <p>📉 Lowest Score: <b>{low}</b></p>
        <p>📊 Average Score: <b>{avg}</b></p>
        <p>⏱ Avg Overs: <b>{avgovers}</b></p>
        <p>🎯 Avg Wickets: <b>{avgwkts}</b></p>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("### ⚔️ Opponent")
        st.markdown(f"""
        <div style="background:white;padding:20px;border-radius:12px;
        box-shadow:0 4px 15px rgba(0,0,0,0.06)">
        <p>🔥 Highest Score: <b>{high1}</b></p>
        <p>📉 Lowest Score: <b>{low1}</b></p>
        <p>📊 Average Score: <b>{avg1}</b></p>
        <p>⏱ Avg Overs: <b>{avg3}</b></p>
        <p>🎯 Avg Wickets: <b>{avg2}</b></p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # =========================
    # SIDE-BY-SIDE GRAPHS
    # =========================
    st.markdown("### 📊 Performance Overview")

    col1, col2 = st.columns(2)

    # DONUT
    with col1:
        st.markdown("#### Win Distribution")

        fig, ax = plt.subplots(figsize=(2,2))  # balanced size

# Data
        values = [win, lose]
        colors = ["#2ecc71", "#e74c3c"]  # green / red

# Donut
        wedges, _ = ax.pie(
            values,
            colors=colors,
            startangle=50,
            wedgeprops=dict(width=0.30, edgecolor='white')  # clean edges
        )

# Center text (PERFECT SIZE)
        ax.text(
            0, 0,
            f"{winp:.1f}%",
            ha="center",
            va="center",
            fontsize=10,
            fontweight="bold",
            color="#222"
        )

# Legend (SMALL + BELOW)
        ax.legend(
            wedges,
            [f"Wins ({win})", f"Losses ({lose})"],
            loc="lower center",
            bbox_to_anchor=(0.5, -0.2),  # push down properly
            ncol=2,
            frameon=False,
            fontsize=9
        )

# Remove extra stuff
        ax.set(aspect="equal")

# Render
        st.pyplot(fig)
    # BAR
    with col2:
        st.markdown("#### Score Comparison")

        fig2, ax2 = plt.subplots(figsize=(3,2))

        bars = ax2.bar(["GT", "Opponent"], [avg, avg1],
                       color=["#1f77b4", "#e74c3c"])
        ax2.tick_params(axis='both',labelsize=8)

        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2,
                     height+2,
                     f"{height:.0f}",
                     ha='center', va='bottom',fontsize=8)

        st.pyplot(fig2)

    st.divider()

    # =========================
    # PROGRESS BARS (BACK 🔥)
    # =========================
    st.markdown("### 📈 Performance Strength")

    p1, p2 = st.columns(2)

    with p1:
        st.write("GT Avg Score Strength")
        st.progress(avg / 250)

    with p2:
        st.write("Opponent Avg Score Strength")
        st.progress(avg1 / 250)

    st.write("Win Probability")
    st.progress(winp / 100)

    st.caption(f"Win Rate: {winp:.1f}%")

    st.divider()

    # =========================
    # INSIGHT
    # =========================
    st.markdown("### 🧠 Match Insight")

    if winp >= 70:
        st.success("🔥 Gujarat Titans dominate this matchup.")
    elif winp >= 50:
        st.success("⚖️ Balanced contest with slight GT advantage.")
    else:
        st.error("⚠️ Tough matchup. Opponent has the edge.")