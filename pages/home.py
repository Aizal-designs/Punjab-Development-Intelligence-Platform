import streamlit as st

from utils.data_loader import load_data
from components.cards import metric_card
from components.charts import bar_chart


def show_home():

    df = load_data()

    
    # ==========================
    # HERO
    # ==========================

    st.markdown(
    """
<div class="hero">
<h1>Punjab Development Intelligence Platform</h1>

<p style="font-size:20px;color:#475569;">
Evidence Based Development Planning for Punjab
</p>

<p style="color:#64748B;">
Analyze district indicators, compare development trends,
and support evidence based planning across Punjab.
</p>

</div>
""",
unsafe_allow_html=True
)
    # ==========================
    # OVERVIEW CARDS
    # ==========================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card("Districts", "36", "📍")

    with c2:
        metric_card("Population", "127.7 M", "👥")

    with c3:
        metric_card("Hospitals", "339", "🏥")

    with c4:
        metric_card("Schools", "49,659", "🎓")

    st.divider()

    # ==========================
    # DISTRICT QUICK VIEW
    # ==========================

    st.subheader("District Quick View")

    district = st.selectbox(
        "Select District",
        sorted(df["District"].unique()),
    )

    row = df[df["District"] == district].iloc[0]

    a, b, c, d = st.columns(4)

    with a:
        st.metric(
            "Development Score",
            f"{float(row['DevelopmentScore']):.2f}",
        )

    with b:
        st.metric(
            "Literacy Rate",
            f"{row['LiteracyRate']}%",
        )

    with c:
        st.metric(
            "Population",
            f"{int(row['Population']):,}",
        )

    with d:
        st.metric(
            "Hospitals",
            int(row["Hospitals"]),
        )

    st.divider()

    # ==========================
    # TOP DISTRICTS
    # ==========================

    st.subheader("Top 10 Development Districts")

    top = (
        df.sort_values(
            "DevelopmentScore",
            ascending=False,
        )
        .head(10)
    )

    st.plotly_chart(
        bar_chart(
            top,
            "District",
            "DevelopmentScore",
            "Development Score Ranking",
        ),
        width="stretch",
    )

    st.divider()

    # ==========================
    # TABLE
    # ==========================

    left, right = st.columns([2, 1])

    with left:

        st.subheader("Top Performing Districts")

        st.dataframe(
            top[
                [
                    "District",
                    "DevelopmentScore",
                    "LiteracyRate",
                ]
            ],
            hide_index=True,
            width="stretch",
        )

    with right:

        st.subheader("Platform Modules")

        st.success("📍 District Explorer")

        st.info("📊 Analytics")

        st.info("📄 Reports")

        st.warning("🤖 AI Insights")

    st.divider()

    # ==========================
    # FOOTER CARD
    # ==========================

    st.markdown(
    """
<div class="metric-card">

<h3>AI Insight</h3>

<p style="color:#64748B;">
Punjab Development Intelligence Platform integrates
education, healthcare, population and infrastructure
indicators into a single decision support dashboard for
evidence based planning.
</p>

</div>
""",
unsafe_allow_html=True
)