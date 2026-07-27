import streamlit as st


def load_css():

    st.markdown(
        """
<style>

/* =========================
GOOGLE FONT
========================= */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');


/* =========================
GLOBAL
========================= */

html,
body,
[class*="css"]{

    font-family:'Inter',sans-serif;
    background:#F5F7FA;
}


/* Main page */

.block-container{

    padding-top:1.8rem;
    padding-left:2.2rem;
    padding-right:2.2rem;
    padding-bottom:2rem;

    max-width:1600px;

}


/* Hide Streamlit Menu */

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}


/* IMPORTANT
Don't hide header.
Otherwise sidebar toggle disappears.
*/


/* =========================
SIDEBAR
========================= */

[data-testid="stSidebar"]{

    background:#0B5D3A;

}


[data-testid="stSidebar"] > div{

    padding-top:18px;

}


[data-testid="stSidebar"] *{

    color:white;

}


/* Hide Default Pages Navigation */

[data-testid="stSidebarNav"]{

    display:none;

}


/* Radio */

div[role="radiogroup"] label{

    padding:12px;

    border-radius:12px;

    margin-bottom:5px;

}


/* =========================
CARDS
========================= */

.metric-card{

    background:white;

    border-radius:18px;

    padding:22px;

    border:1px solid #E2E8F0;

    box-shadow:

    0px 6px 18px rgba(0,0,0,.05);

}


/* =========================
HERO
========================= */

.hero{

    background:white;

    border-radius:22px;

    padding:45px;

    border-left:8px solid #0B5D3A;

    box-shadow:

    0px 10px 25px rgba(0,0,0,.05);

}


/* =========================
BUTTON
========================= */

.stButton>button{

    background:#0B5D3A;

    color:white;

    border:none;

    border-radius:12px;

    font-weight:600;

    height:48px;

    width:100%;

}


.stButton>button:hover{

    background:#095132;

}


/* =========================
METRIC
========================= */

[data-testid="metric-container"]{

    background:white;

    border-radius:16px;

    border:1px solid #E5E7EB;

    padding:18px;

}


/* =========================
TABLE
========================= */

[data-testid="stDataFrame"]{

    border-radius:16px;

    overflow:hidden;

}


/* =========================
SELECTBOX
========================= */

div[data-baseweb="select"]{

    border-radius:12px;

}


/* =========================
HEADINGS
========================= */

h1{

    color:#111827;

    font-weight:800;

}


h2{

    color:#111827;

    font-weight:700;

}


h3{

    color:#334155;

}


/* =========================
INFO BOX
========================= */

.stAlert{

    border-radius:14px;

}

</style>

        """,
        unsafe_allow_html=True
    )