import streamlit as st
import pandas as pd

from utils.data_loader import load_data


def show_reports():

    df = load_data()


    st.markdown(
        """
        <div class="hero">

        <h1>
        📄 Development Reports
        </h1>

        <p style="color:#64748B;font-size:17px;">
        Generate professional district development reports
        using Punjab development indicators.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("")


    districts = sorted(
        df["District"].unique()
    )


    selected = st.selectbox(
        "Select District",
        districts
    )


    data = df[
        df["District"] == selected
    ].iloc[0]


    st.divider()


    st.subheader(
        f"📍 {selected} Development Profile"
    )


    col1,col2,col3,col4 = st.columns(4)


    with col1:

        st.metric(
            "Population",
            f"{int(data['Population']):,}"
        )


    with col2:

        st.metric(
            "Development Score",
            f"{data['DevelopmentScore']:.2f}"
        )


    with col3:

        st.metric(
            "District Rank",
            int(data["Rank"])
        )


    with col4:

        st.metric(
            "Literacy Rate",
            f"{data['LiteracyRate']:.2f}%"
        )


    st.divider()


    st.subheader(
        "📊 Executive Summary"
    )


    if data["DevelopmentScore"] >= df["DevelopmentScore"].mean():

        summary = (
            f"{selected} shows above average development performance "
            "compared with other Punjab districts."
        )

    else:

        summary = (
            f"{selected} requires targeted development attention "
            "in education, healthcare and infrastructure sectors."
        )


    st.info(summary)


    st.divider()


    st.subheader(
        "📋 Key Development Indicators"
    )


    indicators = pd.DataFrame(

        {

            "Indicator":[

                "Population",
                "Literacy Rate",
                "Hospitals",
                "Beds",
                "Total Schools",
                "Education Index",
                "Health Index",
                "Infrastructure Index",
                "Development Score",
                "Rank"

            ],


            "Value":[

                f"{int(data['Population']):,}",
                f"{data['LiteracyRate']:.2f}%",
                int(data["Hospitals"]),
                int(data["Beds"]),
                int(data["TotalSchools"]),
                f"{data['EducationIndex']:.2f}",
                f"{data['HealthIndex']:.2f}",
                f"{data['InfrastructureIndex']:.2f}",
                f"{data['DevelopmentScore']:.2f}",
                int(data["Rank"])

            ]

        }

    )


    st.dataframe(

        indicators,

        hide_index=True,

        use_container_width=True

    )


    st.divider()


    st.subheader(
        "🏥 Sector Performance"
    )


    col1,col2,col3 = st.columns(3)


    with col1:

        st.metric(
            "Education",
            f"{data['EducationIndex']:.2f}"
        )


    with col2:

        st.metric(
            "Healthcare",
            f"{data['HealthIndex']:.2f}"
        )


    with col3:

        st.metric(
            "Infrastructure",
            f"{data['InfrastructureIndex']:.2f}"
        )


    st.divider()


    st.subheader(
        "✅ Strength Analysis"
    )


    strengths = []


    if data["EducationIndex"] >= df["EducationIndex"].mean():

        strengths.append(
            "Education performance is above Punjab average."
        )


    if data["HealthIndex"] >= df["HealthIndex"].mean():

        strengths.append(
            "Healthcare indicators show strong performance."
        )


    if data["InfrastructureIndex"] >= df["InfrastructureIndex"].mean():

        strengths.append(
            "Infrastructure development is comparatively strong."
        )


    if not strengths:

        strengths.append(
            "District requires balanced improvement across sectors."
        )


    for item in strengths:

        st.write(
            "✔ " + item
        )


    st.divider()


    st.subheader(
        "🎯 Recommended Development Priorities"
    )


    recommendations = []


    if data["EducationIndex"] < df["EducationIndex"].mean():

        recommendations.append(
            "Increase education facilities and literacy programs."
        )


    if data["HealthIndex"] < df["HealthIndex"].mean():

        recommendations.append(
            "Improve healthcare facilities and medical infrastructure."
        )


    if data["InfrastructureIndex"] < df["InfrastructureIndex"].mean():

        recommendations.append(
            "Focus on infrastructure expansion and public services."
        )


    if not recommendations:

        recommendations.append(
            "Maintain current development progress and improve sustainability."
        )


    for item in recommendations:

        st.write(
            "• " + item
        )


    st.divider()


    st.subheader(
        "📥 Download Report"
    )


    report = f"""
Punjab Development Intelligence Platform

District Development Report

District:
{selected}


Population:
{int(data['Population']):,}


Literacy Rate:
{data['LiteracyRate']:.2f}%


Hospitals:
{int(data['Hospitals'])}


Schools:
{int(data['TotalSchools'])}


Education Index:
{data['EducationIndex']:.2f}


Health Index:
{data['HealthIndex']:.2f}


Infrastructure Index:
{data['InfrastructureIndex']:.2f}


Development Score:
{data['DevelopmentScore']:.2f}


District Rank:
{int(data['Rank'])}


Development Recommendation:

{chr(10).join(recommendations)}
"""


    st.download_button(

        "📄 Download Development Report",

        report,

        file_name=f"{selected}_Development_Report.txt",

        mime="text/plain"

    )