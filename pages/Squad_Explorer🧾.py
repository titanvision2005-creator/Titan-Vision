import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
left,right,up=st.columns([1,2,1])

with right:
    st.image("logo.png")
    st.markdown("""
    <h1 style="
    font-size:52px;
    font-weight:900;
    color:#F8FAFC;
    margin-bottom:5px;
    ">
    SQUAD EXPLORER 2026
    </h1>

    <p style="
    color:#CBD5E1;
    font-size:18px;
    ">
    Complete Gujarat Titans Squad Analysis & Player Profiles
    </p>
    """,unsafe_allow_html=True)
    st.write("Gujarat Titans 2026 Squad Full Player Profiles")

df = pd.read_excel("TITAN VISION.xlsx", sheet_name="MY_SQUAD")

# =========================
# 🔍 SEARCH BAR (NEW)
# =========================
search = st.text_input("🔍 Search Player by Name")

if search:
    df = df[df["Player_Name"].str.contains(search, case=False, na=False)]

# =========================
# GLOBAL STYLE
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

            
            /* Main Background */
.stApp{

background:
radial-gradient(
circle at top left,
#14213D 0%,
#07111F 45%,
#050B16 100%
);

background-attachment:fixed;

color:#F8FAFC;

}

/* Sidebar */
            
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


//* Vertical Gold Line */
.vertical-line {
    border-left: 2px solid #D4AF37;
    height: 100%;
    margin: 0 auto;
}


/* Role Tag */
.role-tag {
    display:inline-block;
    background: linear-gradient(135deg, #D4AF37, #FACC15);
    color:#06142B !important;
    padding:5px 14px;
    border-radius:14px;
    font-size:12px;
    font-weight:700;
}


/* Search Box */
div[data-baseweb="input"] > div {
    background:#162235;
    border: 1px solid #D4AF37;
    border-radius: 12px;
}


input {
    color:#FFFFFF !important;
}


/* Labels */
label {
    color:#FFD700 !important;
}


/* Player Section Heading */
h2, h3 {
    color:#FFFFFF !important;
    font-weight:700;
}


/* Player Card */
.player-card {
    background: linear-gradient(135deg,#111F38,#172A4A);
    border:1px solid #D4AF37;
    border-radius:16px;
    padding:18px;
    margin-bottom:15px;
    color:#FFFFFF;
}


/* Player Name */
.player-name {
    color:#FFFFFF !important;
    font-size:20px;
    font-weight:700;
}


/* Player Role */
.player-role {
    color:#06142B !important;
    background:#FFD700;
    padding:5px 12px;
    border-radius:12px;
    font-size:14px;
}


/* Player Stats */
.player-stats {
    color:#E5E7EB !important;
    font-size:14px;
}


/* All normal text */
.stMarkdown, 
.stMarkdown p {
    color:#FFFFFF !important;
}

.player-card{
transition:.35s;
}

.player-card:hover{

transform:translateY(-5px);

box-shadow:
0 18px 35px rgba(212,175,55,.20);

border-color:#D4AF37;

}
""", unsafe_allow_html=True)

# =========================
# 🔥 ROLE GROUPING (NEW)
# =========================
roles = ["Batsman", "WK-Batsman", "All Rounder", "Bowler"]

for role in roles:

    role_df = df[df["Role"] == role]

    if role_df.empty:
        continue

    # Section Header
    st.markdown(f"## {role}")
    st.divider()

    # =========================
    # LOOP INSIDE ROLE
    # =========================
    for index, rows in role_df.iterrows():

        # =========================
        # PLAYER HEADER
        # =========================
        st.markdown(
            f"""
        <div style="background:linear-gradient(135deg, #0b1d3a, #172554);
                    padding:20px;
                    border-radius:18px;
                    border:1px solid #1e3a8a;
                    margin-bottom:12px;
                    box-shadow:0 10px 30px rgba(0,0,0,0.4);">

        <h2 style="color:#f8fafc; margin:0;">👤 {rows['Player_Name']}</h2>

        <p style="margin-top:8px;">
        <span style="background:#fde68a;
                     color:#92400e;
                     padding:4px 12px;
                     border-radius:12px;
                     font-size:12px;
                     font-weight:600;">
        {rows['Role']}
        </span>

        &nbsp;&nbsp;

        <span style="color:#bfdbfe; font-size:14px; font-weight:500;">
        🌍 {rows['Nationality']}
        </span>
        </p>

        <p style="color:#38bdf8; margin:0;">
        📊 Matches Played: {rows['Matches']}
        </p>

        </div>
        """,
            unsafe_allow_html=True
        )

        # =========================
        # 3-COLUMN (LEFT | LINE | RIGHT)
        # =========================
        col1, mid, col2 = st.columns([1, 0.05, 1])

        # =========================
        # LEFT → BATTING
        # =========================
        with col1:
            st.markdown(f"""
            <div style="
                background:linear-gradient(135deg, #0f172a, #1e293b);
                padding:18px;
                border-radius:16px;
                border:1px solid #334155;
                box-shadow:0 8px 20px rgba(0,0,0,0.3);">
            <h4 style="color:#22c55e;">🏏 Batting Performance</h4>
            <p style="color:#e2e8f0;">Batting Style: <b>{rows['Batting Style']}</b></p>
            <p style="color:#e2e8f0;">Runs: <b>{rows['Runs']}</b></p>
            <p style="color:#e2e8f0;">50s/100s: <b>{rows['50S/100S']}</b></p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("**Strike Rate**")
            st.progress(min(float(rows['Strike Rate']) / 200, 1.0))
            st.caption(rows['Strike Rate'])

            st.markdown("**Average**")
            st.progress(min(float(rows['Average']) / 100, 1.0))
            st.caption(rows['Average'])

        # =========================
        # MIDDLE LINE
        # =========================
        with mid:
            st.markdown('<div class="vertical-line"></div>', unsafe_allow_html=True)

        # =========================
        # RIGHT → BOWLING
        # =========================
        with col2:
            if rows["Wickets"] == 0:
                st.markdown(f"""
                <div style="
                    background:linear-gradient(135deg, #0f172a, #1e293b);
                    padding:18px;
                    border-radius:16px;
                    border:1px solid #334155;
                    box-shadow:0 8px 20px rgba(0,0,0,0.3);">
                <h4 style="color:#f87171;">🔴 Bowling Performance</h4>
                <p style="color:#e2e8f0;">Primarily a batsman – minimal bowling impact.</p>
                </div>
                """, unsafe_allow_html=True)

            else:
                st.markdown(f"""
                <div style="
                    background:linear-gradient(135deg, #0f172a, #1e293b);
                    padding:18px;
                    border-radius:16px;
                    border:1px solid #334155;
                    box-shadow:0 8px 20px rgba(0,0,0,0.3);">

                <h4 style="color:#f87171;">🔴 Bowling Performance</h4>

                <p style="color:#e2e8f0;">Wickets: <b>{rows['Wickets']}</b></p>
                <p style="color:#e2e8f0;">Economy: <b>{rows['Economy']}</b></p>
                <p style="color:#e2e8f0;">4Ws/5Ws: <b>{rows['4WS/5WS']}</b></p>

                </div>
                """, unsafe_allow_html=True)

        # progress stays outside (correct)
                st.markdown("**Economy Control**")
                st.progress(min(float(rows['Economy']) / 10, 1.0))
                st.caption(rows['Economy'])

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <hr style="
        border:1px solid #D4AF37;
        margin-top:15px;
        margin-bottom:25px;
        ">
        """,unsafe_allow_html=True)