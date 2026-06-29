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


/* =========================
   TITANVISION BACKGROUND
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

.main .block-container{

background:transparent;

color:white;

}

h1,h2,h3,h4,h5,h6{

color:#F8FAFC !important;

}

p,span,label{

color:#CBD5E1 !important;

}


/* Sidebar Background */
[data-testid="stSidebar"]{
    background:linear-gradient(
    180deg,
    #00112B,
    #0A1F44
    );

    border-right:2px solid #D4AF37;
}

[data-testid="stSidebar"] *{
    color:white;
}


/* Player Cards */
.player-card{

background:
linear-gradient(
135deg,
#162235,
#1E293B
);

padding:22px;

border-radius:18px;

border:1px solid #D4AF37;

margin-bottom:16px;

box-shadow:0 10px 25px rgba(0,0,0,.35);

}


/* Player Name */
.player-name {
    color: #ffffff;
    font-size: 19px;
    font-weight: 700;
}


/* Player Role */
.player-role {
    color: #FFD700;
    font-size: 14px;
    margin-bottom: 8px;
}


/* Player Stats */
.player-stats {
    color: #D1D5DB;
    font-size: 14px;
}


/* Recommendation Cards */
.reco-card{

background:
linear-gradient(
135deg,
#162235,
#1E293B
);

padding:20px;

border-radius:18px;

border-left:5px solid #FFD700;

border-top:1px solid #D4AF37;

margin-bottom:14px;

color:white;

box-shadow:0 10px 25px rgba(0,0,0,.35);

}


/* Buttons */
.stButton button{

width:100%;

height:48px;

background:#D4AF37;

color:#07111F;

font-weight:900;

border:none;

border-radius:14px;

}

.stButton button:hover{

background:#FFD966;

color:#07111F;

}


/* Select Box */
div[data-baseweb="select"]>div{

background:#162235 !important;

border:1px solid #D4AF37 !important;

border-radius:14px;

color:white !important;

}


/* Headings */
h1, h2, h3 {
    color: #FFFFFF;
}


/* Metric Cards */
div[data-testid="metric-container"] {
    background: #14233D;
    border: 1px solid #D4AF37;
    border-radius: 15px;
    padding: 15px;
}
            /* Select Box Label */
div[data-testid="stSelectbox"] label {
    color: #FFD700 !important;
    font-weight: 600;
}


/* Select Box Background */
div[data-baseweb="select"] > div {
    background-color: #14213D !important;
    border: 1px solid #D4AF37;
    border-radius: 10px;
}



/* Selected text inside select box */
div[data-baseweb="select"] [data-testid="stMarkdownContainer"],
div[data-baseweb="select"] span {
    color: #FFD700 !important;
}

/* Dropdown arrow */
div[data-baseweb="select"] svg {
    fill: #FFD700 !important;
}


/* Dropdown menu options */
ul[role="listbox"] {
    background-color: #14213D !important;
}


ul[role="listbox"] li {
    color: #FFD700 !important;
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

    # -----------------------
    # Captain / Vice Captain
    # -----------------------
    tag = ""

    if row["Player_Name"] == "Shubman Gill":
        tag = '<span style="display:inline-block;background:#FBBF24;color:#111827;padding:5px 14px;border-radius:18px;font-size:12px;font-weight:700;margin-top:8px;margin-bottom:8px;">👑 Captain</span>'

    elif row["Player_Name"] == "Rashid Khan":
        tag = '<span style="display:inline-block;background:#3B82F6;color:white;padding:5px 14px;border-radius:18px;font-size:12px;font-weight:700;margin-top:8px;margin-bottom:8px;">⭐ Vice Captain</span>'

    with cols[i % 2]:

        st.markdown(
            f"""
<div class="player-card">

<div class="player-name">
👤 {row['Player_Name']}
</div>

{tag}

<div class="player-role">
🎯 {row['Role']}
</div>

<div class="player-stats">
⚡ Strike Rate: {row['Strike_Rate']:.2f}<br>
🔴 Economy: {row['Economy']:.2f}
</div>

</div>
""",
            unsafe_allow_html=True,
        )

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