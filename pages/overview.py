import streamlit as st
import plotly.express as px

from utils.data_loader import load_data


def show_overview():

    df = load_data()

    st.markdown(
        """
        <div class="hero">

        <h1>
        📊 Punjab Overview
        </h1>

        <p style="color:#64748B;font-size:17px;">
        Province wide overview of development, education,
        healthcare and demographic indicators across Punjab.
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
            "Population",
            f"{df['Population'].sum()/1000000:.1f} M"
        )

    with c3:
        st.metric(
            "Average Literacy",
            f"{df['LiteracyRate'].mean():.1f}%"
        )

    with c4:
        st.metric(
            "Average Development",
            f"{df['DevelopmentScore'].mean():.1f}"
        )

    st.divider()

    st.subheader("Quick Filters")

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

        st.subheader("Top Development Districts")

        fig = px.bar(
            filtered.sort_values(
                "DevelopmentScore",
                ascending=False
            ).head(10),
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

        st.subheader("Top Literacy Districts")

        fig = px.bar(
            filtered.sort_values(
                "LiteracyRate",
                ascending=False
            ).head(10),
            x="District",
            y="LiteracyRate",
            color="LiteracyRate",
            text="LiteracyRate",
        )

        fig.update_layout(
            height=450,
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Population vs Development")

        fig = px.scatter(
            filtered,
            x="Population",
            y="DevelopmentScore",
            size="Population",
            color="LiteracyRate",
            hover_name="District",
        )

        fig.update_layout(height=500)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("Punjab District Map")

        fig = px.scatter_map(
            filtered,
            lat="Latitude",
            lon="Longitude",
            hover_name="District",
            color="DevelopmentScore",
            size="Population",
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

        st.subheader("Top 10 Population")

        fig = px.pie(
            filtered.nlargest(
                10,
                "Population"
            ),
            names="District",
            values="Population",
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
            color_discrete_sequence=["#4F46E5"],
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Top Performing Districts")

        st.dataframe(
            filtered.sort_values(
                "DevelopmentScore",
                ascending=False
            )[
                [
                    "District",
                    "DevelopmentScore",
                    "LiteracyRate",
                ]
            ].head(10),
            hide_index=True,
            use_container_width=True,
        )

    with right:

        st.subheader("Needs Improvement")

        st.dataframe(
            filtered.sort_values(
                "DevelopmentScore"
            )[
                [
                    "District",
                    "DevelopmentScore",
                    "LiteracyRate",
                ]
            ].head(10),
            hide_index=True,
            use_container_width=True,
        )

    st.divider()

    st.subheader("Complete Dataset")

    st.dataframe(
        filtered,
        hide_index=True,
        use_container_width=True,
    )

    st.download_button(
        "⬇ Download Dataset",
        filtered.to_csv(index=False),
        file_name="Punjab_District_Data.csv",
        mime="text/csv",
        use_container_width=True,
    )