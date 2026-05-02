import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
left,right,up=st.columns([1,2,1])

with right:
    st.image("logo.png")
    st.header("SQUAD EXPLORER 2026")
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
.vertical-line {
    border-left: 1px solid #475569;
    height: 100%;
    margin: 0 auto;
}
.role-tag {
    display:inline-block;
    background:#fde68a;
    color:#92400e;
    padding:4px 12px;
    border-radius:12px;
    font-size:12px;
    font-weight:600;
}
</style>
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
        st.divider()
