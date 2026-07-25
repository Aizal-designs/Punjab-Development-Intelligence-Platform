import streamlit as st
import plotly.express as px

from utils.data_loader import load_data


def show_analytics():

    df = load_data()

    st.markdown(
        """
        <div class="hero">

        <h1>
        📉 Advanced Analytics
        </h1>

        <p style="color:#64748B;font-size:17px;">
        Perform statistical analysis, discover correlations and visualize
        development trends across Punjab districts.
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Districts",
            len(df)
        )

    with c2:
        st.metric(
            "Average Development",
            f"{df['DevelopmentScore'].mean():.2f}"
        )

    with c3:
        st.metric(
            "Average Literacy",
            f"{df['LiteracyRate'].mean():.2f}%"
        )

    with c4:
        st.metric(
            "Average Health",
            f"{df['HealthIndex'].mean():.2f}"
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

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Development Score Distribution")

        fig = px.histogram(
            filtered,
            x="DevelopmentScore",
            nbins=10,
            color_discrete_sequence=["#3B82F6"]
        )

        fig.update_layout(height=450)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("Development Score Spread")

        fig = px.box(
            filtered,
            y="DevelopmentScore",
            points="all",
            color_discrete_sequence=["#10B981"]
        )

        fig.update_layout(height=450)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Literacy vs Development")

        fig = px.scatter(
            filtered,
            x="LiteracyRate",
            y="DevelopmentScore",
            size="Population",
            color="EducationIndex",
            hover_name="District",
        )

        fig.update_layout(height=500)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("Health vs Development")

        fig = px.scatter(
            filtered,
            x="HealthIndex",
            y="DevelopmentScore",
            size="Population",
            color="InfrastructureIndex",
            hover_name="District",
        )

        fig.update_layout(height=500)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    st.subheader("Correlation Heatmap")

    numeric = filtered.select_dtypes(include="number")

    corr = numeric.corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        aspect="auto"
    )

    fig.update_layout(height=700)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Top Development Districts")

        st.dataframe(
            filtered.sort_values(
                "DevelopmentScore",
                ascending=False
            )[
                [
                    "District",
                    "DevelopmentScore",
                    "EducationIndex",
                    "HealthIndex",
                    "InfrastructureIndex"
                ]
            ].head(10),
            hide_index=True,
            use_container_width=True,
        )

    with right:

        st.subheader("Statistical Summary")

        st.dataframe(
            filtered[
                [
                    "Population",
                    "LiteracyRate",
                    "Hospitals",
                    "Beds",
                    "EducationIndex",
                    "HealthIndex",
                    "InfrastructureIndex",
                    "DevelopmentScore"
                ]
            ].describe().round(2),
            use_container_width=True,
        )

    st.divider()

    st.subheader("Analytics Dataset")

    st.dataframe(
        filtered,
        hide_index=True,
        use_container_width=True,
    )

    st.download_button(
        "⬇ Download Analytics Data",
        filtered.to_csv(index=False),
        file_name="Punjab_Analytics.csv",
        mime="text/csv",
        use_container_width=True,
    )