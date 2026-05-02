import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# =========================
# LOAD DATA
# =========================
df = pd.read_excel("TITAN VISION.xlsx", sheet_name="VENUE_PERFORMANCE")

left, right, up = st.columns([1,2,1])
with right:
    st.image("logo.png")
    st.markdown("## 🏟 Venue Wise Performance Analysis")
    st.write("Select Venue to View Team Performance")

# =========================
# SELECT VENUE
# =========================
venues = ["Select venue"] + sorted(df["Venue"].unique().tolist())
select_venue = st.selectbox("Select Venue", venues)

# =========================
# BUTTON STYLE
# =========================
st.markdown("""
<style>
div.stButton > button {
    background-color: #2b6cb0;
    color: white;
    border-radius: 10px;
    padding: 10px 24px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# =========================
# GENERATE BUTTON
# =========================
generate = st.button("🚀 Generate Analysis")

# =========================
# STOP UNTIL BUTTON CLICK
# =========================
if select_venue == "Select venue" or not generate:
    st.stop()

# =========================
# FILTER DATA
# =========================
filtered_df = df[df["Venue"] == select_venue]

if filtered_df.empty:
    st.warning("No data available")
    st.stop()

row = filtered_df.iloc[0]

matches = int(row["Matches played"])
wins = int(row["Wins"])
losses = int(row["Losses"])
win_percent = round(float(row["Win%"]), 1)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

.title {
    font-size: 34px;
    font-weight: 700;
}

.metric-card {
    background: white;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    text-align: center;
}

.metric-value {
    font-size: 26px;
    font-weight: 700;
}

.metric-label {
    color: #777;
    font-size: 14px;
}

.insight-card {
    background: white;
    padding: 22px;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}

.tag {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
}

.good {
    background: #e6f7ee;
    color: #1e8e5a;
}

.bad {
    background: #fdeaea;
    color: #d93025;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown(f"<div class='title'>📍 {select_venue}</div>", unsafe_allow_html=True)

# =========================
# PERFORMANCE TAG
# =========================
if win_percent >= 60:
    st.markdown("<span class='tag good'>🔥 Strong Venue</span>", unsafe_allow_html=True)
elif win_percent >= 40:
    st.markdown("<span class='tag good'>⚖️ Balanced</span>", unsafe_allow_html=True)
else:
    st.markdown("<span class='tag bad'>⚠️ Weak Venue</span>", unsafe_allow_html=True)

st.markdown("---")

# =========================
# METRICS
# =========================
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{matches}</div>
        <div class="metric-label">🎯 Matches</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{wins}</div>
        <div class="metric-label">✅ Wins</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{losses}</div>
        <div class="metric-label">❌ Losses</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{win_percent}%</div>
        <div class="metric-label">📊 Win Rate</div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# MAIN LAYOUT
# =========================
left, right = st.columns([1.1, 1])

# =========================
# LEFT SIDE
# =========================
with left:
    st.markdown("### 📌 Venue Insights")

    st.markdown(f"""
    <div class="insight-card">
        <b>🎯 Matches Played:</b> {matches}<br><br>
        <b>✅ Wins:</b> {wins}<br><br>
        <b>❌ Losses:</b> {losses}<br><br>
        <b>📊 Win Rate:</b> {win_percent}%
    </div>
    """, unsafe_allow_html=True)

    if win_percent >= 75:
        st.success(f"🏟️ This venue has been a fortress — dominant performances with a {win_percent}% win rate.")
    elif win_percent >= 60:
        st.success(f"💪 Strong performance here with a {win_percent}% win rate.")
    elif win_percent >= 45:
        st.warning("⚖️ Balanced venue — unpredictable results.")
    elif win_percent >= 30:
        st.warning("📉 Struggled at this venue.")
    else:
        st.error("🚫 Very poor performance at this venue.")

# =========================
# RIGHT SIDE (DONUT)
# =========================
with right:
    st.markdown("### 📊 Performance Split")

    fig, ax = plt.subplots(figsize=(3.5, 3.5))

    ax.pie(
        [wins, losses],
        colors=["#2ecc71", "#ff6b6b"],
        startangle=90,
        wedgeprops=dict(width=0.35)
    )

    ax.text(0, 0, f"{win_percent}%", ha='center', va='center', fontsize=20, fontweight='bold')
    ax.axis("equal")

    st.pyplot(fig, use_container_width=False)

    st.markdown(f"""
    <div style="text-align:center; font-size:14px; margin-top:-10px;">
        <span style="color:#2ecc71;">● Wins ({wins})</span> &nbsp;&nbsp;&nbsp;
        <span style="color:#ff6b6b;">● Losses ({losses})</span>
    </div>
    """, unsafe_allow_html=True)

