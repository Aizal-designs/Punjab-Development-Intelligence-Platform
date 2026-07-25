import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from utils.data_loader import load_data


def show_comparison():

    df = load_data()

    st.markdown(
        """
        <div class="hero">

        <h1>
        ⚖ District Comparison
        </h1>

        <p style="color:#64748B;font-size:17px;">
        Compare the performance of two Punjab districts across population,
        education, healthcare, infrastructure and development indicators.
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    districts = sorted(df["District"].unique())

    c1, c2 = st.columns(2)

    with c1:

        district_a = st.selectbox(
            "District A",
            districts
        )

    with c2:

        district_b = st.selectbox(
            "District B",
            districts,
            index=1
        )

    data_a = df[df["District"] == district_a].iloc[0]
    data_b = df[df["District"] == district_b].iloc[0]

    st.divider()

    a, b, c, d = st.columns(4)

    with a:
        st.metric(
            district_a,
            f"{data_a['DevelopmentScore']:.2f}"
        )

    with b:
        st.metric(
            district_b,
            f"{data_b['DevelopmentScore']:.2f}"
        )

    with c:
        winner = district_a if data_a["DevelopmentScore"] > data_b["DevelopmentScore"] else district_b

        st.metric(
            "Higher Score",
            winner
        )

    with d:

        diff = abs(
            data_a["DevelopmentScore"] -
            data_b["DevelopmentScore"]
        )

        st.metric(
            "Difference",
            f"{diff:.2f}"
        )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Development Comparison")

        chart = pd.DataFrame({

            "District":[district_a, district_b],

            "Development Score":[
                data_a["DevelopmentScore"],
                data_b["DevelopmentScore"]
            ]

        })

        fig = px.bar(
            chart,
            x="District",
            y="Development Score",
            color="District",
            text="Development Score",
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

        st.subheader("Radar Comparison")

        categories = [
            "Education",
            "Health",
            "Infrastructure",
            "Development"
        ]

        fig = go.Figure()

        fig.add_trace(
            go.Scatterpolar(
                r=[
                    data_a["EducationIndex"],
                    data_a["HealthIndex"],
                    data_a["InfrastructureIndex"],
                    data_a["DevelopmentScore"],
                ],
                theta=categories,
                fill="toself",
                name=district_a,
            )
        )

        fig.add_trace(
            go.Scatterpolar(
                r=[
                    data_b["EducationIndex"],
                    data_b["HealthIndex"],
                    data_b["InfrastructureIndex"],
                    data_b["DevelopmentScore"],
                ],
                theta=categories,
                fill="toself",
                name=district_b,
            )
        )

        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True)),
            height=450,
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    st.divider()

    comparison = pd.DataFrame({

        "Indicator":[
            "Population",
            "Literacy Rate",
            "Hospitals",
            "Beds",
            "Schools",
            "Education Index",
            "Health Index",
            "Infrastructure Index",
            "Development Score"
        ],

        district_a:[
            data_a["Population"],
            data_a["LiteracyRate"],
            data_a["Hospitals"],
            data_a["Beds"],
            data_a["TotalSchools"],
            data_a["EducationIndex"],
            data_a["HealthIndex"],
            data_a["InfrastructureIndex"],
            data_a["DevelopmentScore"]
        ],

        district_b:[
            data_b["Population"],
            data_b["LiteracyRate"],
            data_b["Hospitals"],
            data_b["Beds"],
            data_b["TotalSchools"],
            data_b["EducationIndex"],
            data_b["HealthIndex"],
            data_b["InfrastructureIndex"],
            data_b["DevelopmentScore"]
        ]

    })

    st.subheader("Detailed Comparison")

    st.dataframe(
        comparison,
        hide_index=True,
        use_container_width=True,
    )

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Key Statistics")

        st.metric(
            "Population Difference",
            f"{abs(int(data_a['Population']-data_b['Population'])):,}"
        )

        st.metric(
            "Literacy Difference",
            f"{abs(data_a['LiteracyRate']-data_b['LiteracyRate']):.2f}%"
        )

        st.metric(
            "Hospital Difference",
            int(abs(data_a["Hospitals"]-data_b["Hospitals"]))
        )

    with right:

        st.subheader("Comparison Summary")

        if data_a["DevelopmentScore"] > data_b["DevelopmentScore"]:

            st.success(
                f"{district_a} performs better overall based on the Development Score."
            )

        elif data_b["DevelopmentScore"] > data_a["DevelopmentScore"]:

            st.success(
                f"{district_b} performs better overall based on the Development Score."
            )

        else:

            st.info(
                "Both districts have the same Development Score."
            )

        st.info(
            "Compare education, healthcare and infrastructure together for better planning decisions."
        )

    st.divider()

    st.download_button(
        "⬇ Download Comparison",
        comparison.to_csv(index=False),
        file_name=f"{district_a}_vs_{district_b}.csv",
        mime="text/csv",
        use_container_width=True,
    )