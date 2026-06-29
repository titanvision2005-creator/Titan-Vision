import streamlit as st
import base64


st.set_page_config(
    page_title="TitanVision",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================
# HIDE STREAMLIT UI
# =========================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #00112B, #0A1F44);
    border-right: 2px solid #E6B93C;
}

[data-testid="stSidebar"] * {
    color: white;
}

</style>
""", unsafe_allow_html=True)



# =========================
# LOAD LOGO
# =========================

def get_base64(path):

    with open(path,"rb") as f:
        return base64.b64encode(f.read()).decode()


logo = get_base64("[logo].png")



# =========================
# THEME CSS
# =========================

st.markdown("""
<style>

/* BACKGROUND */

.stApp{

background:
radial-gradient(
circle at top left,
#14213D,
#07111F 45%
);

color:white;

}



/* HERO */

.hero{

text-align:center;
padding:35px;

}


.hero img{

width:140px;
border-radius:50%;

}


.hero-title{

font-size:58px;
font-weight:900;
color:#F8FAFC;

}


.hero-subtitle{

color:#CBD5E1;
font-size:18px;

}



/* STAT CARDS */


.stat-card{

background:#162235;

border-radius:18px;

padding:22px;

text-align:center;

border:1px solid #D4AF37;

}


.stat-number{

font-size:32px;

font-weight:900;

color:#D4AF37;

}


.stat-label{

color:#CBD5E1;

}





/* SECTION TITLE */


.section-title{

margin-top:40px;

font-size:30px;

font-weight:900;

color:#FFD966;

border-bottom:

2px solid #D4AF37;

padding-bottom:8px;

}





/* FEATURE CARD */


.feature-card{


background:

linear-gradient(
135deg,
#162235,
#1E293B
);


border-radius:22px;


padding:30px;


height:180px;


text-align:center;


border:1px solid #334155;


transition:.3s;


}



.feature-card:hover{


transform:translateY(-8px);


box-shadow:

0 15px 35px rgba(212,175,55,0.25);


border-color:#D4AF37;


}



.icon{

font-size:45px;

}



.feature-title{

color:#F8FAFC;

font-size:22px;

font-weight:800;

}



.feature-desc{

color:#94A3B8;

margin-top:8px;

}





/* PLAYING XI */


.xi-card{


background:

linear-gradient(
135deg,
#111827,
#1F2937
);


border-radius:28px;


padding:45px;


text-align:center;


border:

2px solid #D4AF37;


}



.xi-title{


font-size:42px;

font-weight:900;

color:#FFD966;


}



.xi-text{


font-size:18px;

color:#CBD5E1;


}




/* BUTTON */


.stButton button{


width:100%;


height:45px;


border-radius:14px;


background:#D4AF37;


color:#07111F;


font-weight:900;


border:none;


}



.stButton button:hover{


background:#FFD966;


color:#07111F;


}




</style>

""", unsafe_allow_html=True)





# =========================
# HERO
# =========================

st.markdown(f"""

<div class="hero">

<img src="data:image/png;base64,{logo}">

<div class="hero-title">
TitanVision
</div>


<div class="hero-subtitle">
Cricket Intelligence Platform 🏏
</div>


</div>


""",
unsafe_allow_html=True)





# =========================
# STATS
# =========================


c1,c2,c3,c4 = st.columns(4)



stats=[

("13","Venues"),

("700+","Players"),

("10","Squads"),

("1192","Matches")

]


for col,data in zip(
    [c1,c2,c3,c4],
    stats
):

    with col:

        st.markdown(f"""

        <div class="stat-card">

        <div class="stat-number">
        {data[0]}
        </div>


        <div class="stat-label">
        {data[1]}
        </div>


        </div>

        """,
        unsafe_allow_html=True)






# =========================
# INSIGHTS
# =========================


st.markdown(
"""
<div class="section-title">
📊 INSIGHTS
</div>
""",
unsafe_allow_html=True
)



a,b = st.columns(2)



with a:


    st.markdown("""
    <div class="feature-card">

    <div class="icon">📊</div>

    <div class="feature-title">
    Dashboard
    </div>

    <div class="feature-desc">
    Overall analytics and insights
    </div>

    </div>

    """,
    unsafe_allow_html=True)



    if st.button(
        "Open Dashboard"
    ):
        st.switch_page(
            "pages/My_Dashboard📊.py"
        )




with b:


    st.markdown("""
    <div class="feature-card">

    <div class="icon">👥</div>

    <div class="feature-title">
    Squad Explorer
    </div>

    <div class="feature-desc">
    Explore squads and combinations
    </div>

    </div>

    """,
    unsafe_allow_html=True)



    if st.button(
        "Open Squad Explorer"
    ):
        st.switch_page(
            "pages/Squad_Explorer🧾.py"
        )







# =========================
# TEAM PERFORMANCE
# =========================


st.markdown(
"""
<div class="section-title">
🏟 TEAM PERFORMANCE ANALYSIS
</div>
""",
unsafe_allow_html=True
)



a,b,c = st.columns(3)



cards=[

("🏟","Venue Analysis",
"Venue trends",
"pages/Venue_Wise_Team_Performance_Analysis🏟.py"),


("⚔️","Opponent Analysis",
"Opponent study",
"pages/Opponent_Wise_Venue_Wise_Team_Performance_Analysis⚔️.py"),


("🎯","Venue Specialists",
"Best performers",
"pages/Venue_Wise_Player_Performance_Analysis👤.py")

]



for col,item in zip(
    [a,b,c],
    cards
):

    with col:


        st.markdown(f"""

        <div class="feature-card">

        <div class="icon">
        {item[0]}
        </div>


        <div class="feature-title">
        {item[1]}
        </div>


        <div class="feature-desc">
        {item[2]}
        </div>


        </div>

        """,
        unsafe_allow_html=True)



        if st.button(
            "Open",
            key=item[1]
        ):

            st.switch_page(
                item[3]
            )







# =========================
# PLAYING XI
# =========================


st.markdown(
"""
<div class="section-title">
🏏 PLAYING XI
</div>
""",
unsafe_allow_html=True
)



st.markdown("""
<div class="xi-card">


<div class="xi-title">

Generate Best Playing XI

</div>


<br>


<div class="xi-text">

Create venue-based and opponent-specific
playing combinations using cricket intelligence.

</div>


</div>

""",
unsafe_allow_html=True)



if st.button(
    "🚀 Launch Playing XI Builder"
):

    st.switch_page(
        "pages/Playing_XI_Recommendation🏏.py"
    )
