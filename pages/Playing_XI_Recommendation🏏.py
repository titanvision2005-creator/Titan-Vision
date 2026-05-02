import streamlit as st
import pandas as pd

st.set_page_config(page_title="Playing XI", layout="wide")

left, right, up = st.columns([1,2,1])

with right:
    st.image("logo.png")
    st.title("🏏 Playing XI Recommendation System")
    st.markdown("Generate the best team based on venue conditions")

# =========================
# LOAD DATA
# =========================
df = pd.read_excel("TITAN VISION.xlsx", sheet_name="PLAYING_XII_RECOMMENDATION")
df1 = pd.read_excel("TITAN VISION.xlsx", sheet_name="NEW_PLAYER_DATA")

# =========================
# STYLE
# =========================
st.markdown("""
<style>
.player-card {
    background: linear-gradient(135deg, #111827, #1f2937);
    padding: 16px;
    border-radius: 14px;
    border: 1px solid #374151;
    margin-bottom: 12px;
}
.player-name {
    color: #f9fafb;
    font-size: 18px;
    font-weight: 600;
}
.player-role {
    color: #38bdf8;
    font-size: 13px;
    margin-bottom: 6px;
}
.player-stats {
    color: #e5e7eb;
    font-size: 13px;
}
.reco-card {
    background: #111827;
    padding: 12px;
    border-radius: 10px;
    border-left: 4px solid #facc15;
    margin-bottom: 10px;
    color: #e5e7eb;
}
div.stButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    padding: 10px 22px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SELECT VENUE + BUTTON
# =========================
unique_venues = df["Venue"].dropna().unique()
venue = st.selectbox("Select Venue", unique_venues, index=None, placeholder="Select Venue")

generate = st.button("🚀 Generate Playing XI")

# Stop until user interacts
if not venue or not generate:
    st.stop()

# =========================
# MAIN LOGIC
# =========================
st.markdown(f"### 📍 Selected Venue: {venue}")

filtered = df[df["Venue"] == venue]

bat = filtered.dropna(subset=["Batting_Rank"]).sort_values("Batting_Rank").head(2)
ball = filtered.dropna(subset=["Bowling_Rank"]).sort_values("Bowling_Rank").head(4)
All = filtered.dropna(subset=["All_Rounder_Rank"]).sort_values("All_Rounder_Rank").head(4)
wk = filtered.dropna(subset=["Wk_Rank"]).sort_values("Wk_Rank").head(1)

squad = pd.concat([bat, wk, All, ball])

selected_rows = []
overseas_count = 0

for _, row in squad.iterrows():
    if row["NATIONALITY"] == "Indian":
        selected_rows.append(row)
    elif row["NATIONALITY"] == "Overseas" and overseas_count < 4:
        selected_rows.append(row)
        overseas_count += 1

squad = pd.DataFrame(selected_rows)

st.divider()

# =========================
# PLAYING XI DISPLAY
# =========================
st.markdown("### 🧾 Final Playing XI")

cols = st.columns(2)

for i, (_, row) in enumerate(squad.iterrows()):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="player-card">
            <div class="player-name">👤 {row['Player_Name']}</div>
            <div class="player-role">🎯 {row['Role']}</div>
            <div class="player-stats">
                ⚡ Strike Rate: {row['Strike_Rate']:.2f}<br>
                🔴 Economy: {row['Economy']:.2f}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# =========================
# RECOMMENDATIONS
# =========================
st.markdown("### 🔁 Suggested Improvements")

found = False

# ---- BOWLERS ----
bowlers = squad[squad["Role"] == "Bowler"]
Eco_low = bowlers[bowlers["Economy"] >= 10]

New_bowlers = df1[df1["Role"] == "Bowler"].sort_values(by="Economy").head(1)

for i in range(min(len(Eco_low), len(New_bowlers))):
    old = Eco_low.iloc[i]
    new = New_bowlers.iloc[i]

    found = True
    st.markdown(f"""
    <div class="reco-card">
    ⭐ Replace <b>{old['Player_Name']}</b> with <b>{new['Player_Name']}</b><br>
    <span style="color:#9ca3af;">Better economy ({old['Economy']:.2f} → {new['Economy']:.2f})</span>
    </div>
    """, unsafe_allow_html=True)

# ---- BATSMAN ----
batters = squad[squad["Role"] == "Batsman"]
All_low = batters[batters["Performance_Score"] >= 60]

New_All = df1[df1["Role"] == "Batsman"].sort_values(by="Batting_score").head(1)

for i in range(min(len(All_low), len(New_All))):
    old = All_low.iloc[i]
    new = New_All.iloc[i]

    found = True
    st.markdown(f"""
    <div class="reco-card">
    ⭐ Replace <b>{old['Player_Name']}</b> with <b>{new['Player_Name']}</b><br>
    <span style="color:#9ca3af;">Better performance score</span>
    </div>
    """, unsafe_allow_html=True)

# ---- ALLROUNDER ----
Allrounders = squad[squad["Role"] == "All Rounder"]
All_low1 = Allrounders[Allrounders["Performance_Score"] >= 20]

New_All1 = df1[df1["Role"] == "Allrounder"].sort_values(by="All_Rounder_score").head(1)

for i in range(min(len(All_low1), len(New_All1))):
    old = All_low1.iloc[i]
    new = New_All1.iloc[i]

    found = True
    st.markdown(f"""
    <div class="reco-card">
    ⭐ Replace <b>{old['Player_Name']}</b> with <b>{new['Player_Name']}</b><br>
    <span style="color:#9ca3af;">Better all-round performance</span>
    </div>
    """, unsafe_allow_html=True)

# ---- WK ----
Wk1 = squad[squad["Role"] == "WK-Batsman"]
All_low2 = Wk1[Wk1["Performance_Score"] >= 30]

New_All2 = df1[df1["Role"] == "WK-Batsman"].sort_values(by="Batting_score").head(1)

for i in range(min(len(All_low2), len(New_All2))):
    old = All_low2.iloc[i]
    new = New_All2.iloc[i]

    found = True
    st.markdown(f"""
    <div class="reco-card">
    ⭐ Replace <b>{old['Player_Name']}</b> with <b>{new['Player_Name']}</b><br>
    <span style="color:#9ca3af;">Better batting performance</span>
    </div>
    """, unsafe_allow_html=True)

if not found:
    st.info("No major improvements suggested. Current Playing XI looks balanced.")
