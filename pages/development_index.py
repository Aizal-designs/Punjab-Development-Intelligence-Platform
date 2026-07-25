import streamlit as st
import plotly.express as px

from utils.data_loader import load_data


def show_development_index():

    df = load_data()

    st.markdown(
        """
        <div class="hero">

        <h1>
        📈 Development Index
        </h1>

        <p style="color:#64748B;font-size:17px;">
        Evaluate the overall development performance of Punjab districts
        using education, healthcare and infrastructure indicators.
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Highest Score",
            f"{df['DevelopmentScore'].max():.2f}"
        )

    with c2:
        st.metric(
            "Average Score",
            f"{df['DevelopmentScore'].mean():.2f}"
        )

    with c3:
        st.metric(
            "Lowest Score",
            f"{df['DevelopmentScore'].min():.2f}"
        )

    with c4:
        st.metric(
            "Districts",
            len(df)
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        minimum = st.slider(
            "Minimum Development Score",
            0,
            100,
            0
        )

    with col2:

        districts = st.multiselect(
            "Districts",
            sorted(df["District"]),
            default=[]
        )

    filtered = df[df["DevelopmentScore"] >= minimum]

    if districts:
        filtered = filtered[
            filtered["District"].isin(districts)
        ]

    ranking = filtered.sort_values(
        "DevelopmentScore",
        ascending=False
    )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Development Ranking")

        fig = px.bar(
            ranking,
            x="District",
            y="DevelopmentScore",
            color="DevelopmentScore",
            text="DevelopmentScore",
        )

        fig.update_layout(
            height=450,
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("Development Distribution")

        fig = px.histogram(
            filtered,
            x="DevelopmentScore",
            nbins=10,
            color_discrete_sequence=["#6366F1"],
        )

        fig.update_layout(
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Education vs Health")

        fig = px.scatter(
            filtered,
            x="EducationIndex",
            y="HealthIndex",
            size="Population",
            color="DevelopmentScore",
            hover_name="District",
        )

        fig.update_layout(
            height=500
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("Punjab Development Map")

        fig = px.scatter_map(
            filtered,
            lat="Latitude",
            lon="Longitude",
            size="DevelopmentScore",
            color="DevelopmentScore",
            hover_name="District",
            zoom=6,
            height=500,
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Top 10 Districts")

        st.dataframe(
            ranking[
                [
                    "District",
                    "DevelopmentScore",
                    "EducationIndex",
                    "HealthIndex",
                    "InfrastructureIndex",
                    "Rank"
                ]
            ].head(10),
            hide_index=True,
            use_container_width=True,
        )

    with right:

        st.subheader("Bottom 10 Districts")

        st.dataframe(
            ranking[
                [
                    "District",
                    "DevelopmentScore",
                    "EducationIndex",
                    "HealthIndex",
                    "InfrastructureIndex",
                    "Rank"
                ]
            ].tail(10),
            hide_index=True,
            use_container_width=True,
        )

    st.divider()

    st.subheader("Development Dataset")

    st.dataframe(
        ranking[
            [
                "District",
                "DevelopmentScore",
                "EducationIndex",
                "HealthIndex",
                "InfrastructureIndex",
                "Population",
                "Rank"
            ]
        ],
        hide_index=True,
        use_container_width=True,
    )

    st.download_button(
        "⬇ Download Development Data",
        ranking.to_csv(index=False),
        file_name="Punjab_Development_Index.csv",
        mime="text/csv",
        use_container_width=True,
    )