import streamlit as st
import plotly.express as px

from utils.data_loader import load_data


def show_healthcare():

    df = load_data()

    st.markdown(
        """
        <div class="hero">

        <h1>
        🏥 Healthcare Analytics
        </h1>

        <p style="color:#64748B;font-size:17px;">
        Analyze healthcare infrastructure, hospitals, beds and medical
        facilities across the districts of Punjab.
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Hospitals",
            f"{int(df['Hospitals'].sum()):,}"
        )

    with c2:
        st.metric(
            "Hospital Beds",
            f"{int(df['Beds'].sum()):,}"
        )

    with c3:
        st.metric(
            "Average Health Index",
            f"{df['HealthIndex'].mean():.2f}"
        )

    with c4:
        st.metric(
            "BHUs",
            f"{int(df['BHUs'].sum()):,}"
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        minimum = st.slider(
            "Minimum Health Index",
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

    filtered = df[df["HealthIndex"] >= minimum]

    if districts:
        filtered = filtered[
            filtered["District"].isin(districts)
        ]

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Top Hospital Districts")

        fig = px.bar(
            filtered.sort_values(
                "Hospitals",
                ascending=False
            ).head(10),
            x="District",
            y="Hospitals",
            color="Hospitals",
            text="Hospitals",
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

        st.subheader("Top Health Index")

        fig = px.bar(
            filtered.sort_values(
                "HealthIndex",
                ascending=False
            ).head(10),
            x="District",
            y="HealthIndex",
            color="HealthIndex",
            text="HealthIndex",
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

        st.subheader("Healthcare Facilities")

        facility = filtered.melt(
            id_vars="District",
            value_vars=[
                "Beds",
                "RHCs",
                "BHUs"
            ],
            var_name="Facility",
            value_name="Count"
        )

        fig = px.bar(
            facility,
            x="District",
            y="Count",
            color="Facility",
        )

        fig.update_layout(
            height=500
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("Health Index Distribution")

        fig = px.histogram(
            filtered,
            x="HealthIndex",
            nbins=10,
            color_discrete_sequence=["#10B981"],
        )

        fig.update_layout(
            height=500
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Hospital Beds vs Hospitals")

        fig = px.scatter(
            filtered,
            x="Hospitals",
            y="Beds",
            size="Population",
            color="HealthIndex",
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

        st.subheader("Punjab Healthcare Map")

        fig = px.scatter_map(
            filtered,
            lat="Latitude",
            lon="Longitude",
            size="Hospitals",
            color="HealthIndex",
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

        st.subheader("Top Healthcare Districts")

        st.dataframe(
            filtered.sort_values(
                "HealthIndex",
                ascending=False
            )[
                [
                    "District",
                    "HealthIndex",
                    "Hospitals",
                    "Beds",
                    "BHUs"
                ]
            ].head(10),
            hide_index=True,
            use_container_width=True,
        )

    with right:

        st.subheader("Needs Improvement")

        st.dataframe(
            filtered.sort_values(
                "HealthIndex"
            )[
                [
                    "District",
                    "HealthIndex",
                    "Hospitals",
                    "Beds",
                    "BHUs"
                ]
            ].head(10),
            hide_index=True,
            use_container_width=True,
        )

    st.divider()

    st.subheader("Healthcare Dataset")

    st.dataframe(
        filtered[
            [
                "District",
                "Hospitals",
                "Beds",
                "RHCs",
                "BHUs",
                "HealthIndex"
            ]
        ],
        hide_index=True,
        use_container_width=True,
    )

    st.download_button(
        "⬇ Download Healthcare Data",
        filtered.to_csv(index=False),
        file_name="Punjab_Healthcare_Data.csv",
        mime="text/csv",
        use_container_width=True,
    )