import streamlit as st
import plotly.express as px

from utils.data_loader import load_data


def show_education():

    df = load_data()

    st.markdown(
        """
        <div class="hero">

        <h1>
        🎓 Education Analytics
        </h1>

        <p style="color:#64748B;font-size:17px;">
        Analyze literacy, school infrastructure and education performance
        across all districts of Punjab.
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Average Literacy",
            f"{df['LiteracyRate'].mean():.1f}%"
        )

    with c2:
        st.metric(
            "Total Schools",
            f"{int(df['TotalSchools'].sum()):,}"
        )

    with c3:
        st.metric(
            "Primary Schools",
            f"{int(df['PrimarySchools'].sum()):,}"
        )

    with c4:
        st.metric(
            "Education Index",
            f"{df['EducationIndex'].mean():.2f}"
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        minimum = st.slider(
            "Minimum Literacy Rate",
            0,
            100,
            40
        )

    with col2:

        districts = st.multiselect(
            "Districts",
            sorted(df["District"]),
            default=[]
        )

    filtered = df[df["LiteracyRate"] >= minimum]

    if districts:
        filtered = filtered[
            filtered["District"].isin(districts)
        ]

    st.divider()

    left, right = st.columns(2)

    with left:

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

    with right:

        st.subheader("Top Education Index")

        fig = px.bar(
            filtered.sort_values(
                "EducationIndex",
                ascending=False
            ).head(10),
            x="District",
            y="EducationIndex",
            color="EducationIndex",
            text="EducationIndex",
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

        st.subheader("School Distribution")

        school_data = filtered.melt(
            id_vars="District",
            value_vars=[
                "PrimarySchools",
                "MiddleSchools",
                "HighSchools"
            ],
            var_name="School Type",
            value_name="Count"
        )

        fig = px.bar(
            school_data,
            x="District",
            y="Count",
            color="School Type",
        )

        fig.update_layout(height=500)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("Literacy Distribution")

        fig = px.histogram(
            filtered,
            x="LiteracyRate",
            nbins=10,
            color_discrete_sequence=["#3B82F6"],
        )

        fig.update_layout(height=500)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Top Education Districts")

        st.dataframe(
            filtered.sort_values(
                "EducationIndex",
                ascending=False
            )[
                [
                    "District",
                    "EducationIndex",
                    "LiteracyRate",
                    "TotalSchools"
                ]
            ].head(10),
            hide_index=True,
            use_container_width=True,
        )

    with right:

        st.subheader("Needs Improvement")

        st.dataframe(
            filtered.sort_values(
                "EducationIndex"
            )[
                [
                    "District",
                    "EducationIndex",
                    "LiteracyRate",
                    "TotalSchools"
                ]
            ].head(10),
            hide_index=True,
            use_container_width=True,
        )

    st.divider()

    st.subheader("Education Dataset")

    st.dataframe(
        filtered[
            [
                "District",
                "LiteracyRate",
                "EducationIndex",
                "PrimarySchools",
                "MiddleSchools",
                "HighSchools",
                "TotalSchools"
            ]
        ],
        hide_index=True,
        use_container_width=True,
    )

    st.download_button(
        "⬇ Download Education Data",
        filtered.to_csv(index=False),
        file_name="Punjab_Education_Data.csv",
        mime="text/csv",
        use_container_width=True,
    )