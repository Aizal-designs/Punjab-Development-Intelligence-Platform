import streamlit as st
import pandas as pd

from utils.data_loader import load_data
from components.charts import bar_chart


def show_district_explorer():

    df = load_data()


    st.title("📍 District Explorer")

    st.write(
        "Explore district level development indicators, analyze performance and compare districts across Punjab."
    )


    st.divider()


    search = st.text_input(
        "🔍 Search District",
        placeholder="Enter district name..."
    )


    districts = sorted(
        df["District"].unique()
    )


    if search:

        districts = [
            d for d in districts
            if search.lower() in d.lower()
        ]


        if not districts:

            st.warning(
                "District not found."
            )

            return


    selected = st.selectbox(
        "Select District",
        districts
    )


    district = df[
        df["District"] == selected
    ].iloc[0]


    st.divider()


    st.subheader(
        f"{selected} Profile"
    )


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.metric(
            "Population",
            f"{int(district['Population']):,}"
        )


    with c2:

        st.metric(
            "Literacy Rate",
            f"{district['LiteracyRate']:.2f}%"
        )


    with c3:

        st.metric(
            "Hospitals",
            int(district["Hospitals"])
        )


    with c4:

        st.metric(
            "Schools",
            int(district["TotalSchools"])
        )


    st.divider()


    left, right = st.columns([1, 2])


    with left:


        score = float(
            district["DevelopmentScore"]
        )


        st.subheader(
            "Development Score"
        )


        st.metric(
            "Overall Score",
            f"{score:.2f}"
        )


        st.progress(
            min(score / 100, 1.0)
        )


        if score >= 70:

            st.success(
                "High Development"
            )

        elif score >= 40:

            st.info(
                "Moderate Development"
            )

        else:

            st.warning(
                "Needs Improvement"
            )


        st.metric(
            "Punjab Rank",
            f"#{int(district['Rank'])}"
        )


    with right:


        st.subheader(
            "Indicator Overview"
        )


        chart_df = pd.DataFrame(
            {
                "Indicator": [
                    "Hospitals",
                    "Schools"
                ],

                "Value": [
                    district["Hospitals"],
                    district["TotalSchools"]
                ]
            }
        )


        st.plotly_chart(
            bar_chart(
                chart_df,
                "Indicator",
                "Value",
                "District Indicators"
            ),
            use_container_width=True
        )


    st.divider()


    st.subheader(
        "District Information"
    )


    info = pd.DataFrame(
        {
            "Metric": [

                "Development Score",
                "Punjab Rank",
                "Population",
                "Area (km²)",
                "Population Density",
                "Urban Population %",
                "Literacy Rate",
                "Hospitals",
                "Schools"

            ],

            "Value": [

                district["DevelopmentScore"],
                district["Rank"],
                f"{int(district['Population']):,}",
                district["Area"],
                district["Density"],
                f"{district['UrbanPercent']}%",
                f"{district['LiteracyRate']:.2f}%",
                district["Hospitals"],
                district["TotalSchools"]

            ]
        }
    )


    st.dataframe(
        info,
        hide_index=True,
        use_container_width=True
    )


    st.divider()


    st.subheader(
        "District Location"
    )


    map_df = pd.DataFrame(
        {
            "lat": [
                district["Latitude"]
            ],

            "lon": [
                district["Longitude"]
            ]
        }
    )


    st.map(
        map_df
    )


    st.divider()


    st.subheader(
        "Quick Access"
    )


    a, b, c = st.columns(3)


    with a:

        st.button(
            "🎓 Education",
            use_container_width=True
        )


    with b:

        st.button(
            "🏥 Healthcare",
            use_container_width=True
        )


    with c:

        st.button(
            "📊 Analytics",
            use_container_width=True
        )