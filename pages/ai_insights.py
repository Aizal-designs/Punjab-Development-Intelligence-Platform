import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data


def show_ai_insights():

    df = load_data()

    st.markdown(
        """
        <div class="hero">

        <h1>
        🤖 AI Development Insights
        </h1>

        <p style="color:#64748B;font-size:17px;">
        AI based analysis to identify district strengths,
        development gaps and recommended priority actions.
        </p>

        </div>
        """,
        unsafe_allow_html=True,
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


    c1, c2, c3, c4 = st.columns(4)


    with c1:

        st.metric(
            "Development Score",
            f"{data['DevelopmentScore']:.2f}"
        )


    with c2:

        st.metric(
            "Literacy",
            f"{data['LiteracyRate']:.2f}%"
        )


    with c3:

        st.metric(
            "Health Index",
            f"{data['HealthIndex']:.2f}"
        )


    with c4:

        st.metric(
            "Infrastructure",
            f"{data['InfrastructureIndex']:.2f}"
        )


    st.divider()


    strengths = []
    weaknesses = []
    priorities = []


    if data["LiteracyRate"] >= df["LiteracyRate"].mean():

        strengths.append(
            "Literacy performance is above Punjab average."
        )

    else:

        weaknesses.append(
            "Literacy rate is below Punjab average."
        )

        priorities.append(
            "Increase educational access and quality programs."
        )


    if data["HealthIndex"] >= df["HealthIndex"].mean():

        strengths.append(
            "Healthcare indicators are performing well."
        )

    else:

        weaknesses.append(
            "Healthcare infrastructure needs improvement."
        )

        priorities.append(
            "Expand hospitals, beds and medical facilities."
        )


    if data["InfrastructureIndex"] >= df["InfrastructureIndex"].mean():

        strengths.append(
            "Infrastructure development is strong."
        )

    else:

        weaknesses.append(
            "Infrastructure development gap detected."
        )

        priorities.append(
            "Improve roads, facilities and public services."
        )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.subheader(
            "✅ Strengths"
        )

        for item in strengths:

            st.success(item)



    with col2:

        st.subheader(
            "⚠ Development Gaps"
        )

        for item in weaknesses:

            st.warning(item)



    with col3:

        st.subheader(
            "🎯 Priority Actions"
        )

        for item in priorities:

            st.info(item)



    st.divider()


    st.subheader(
        "📊 District vs Punjab Average"
    )


    comparison = pd.DataFrame(

        {

            "Indicator":[
                "Literacy",
                "Health",
                "Infrastructure",
                "Development"
            ],

            selected:[
                data["LiteracyRate"],
                data["HealthIndex"],
                data["InfrastructureIndex"],
                data["DevelopmentScore"]
            ],

            "Punjab Average":[
                df["LiteracyRate"].mean(),
                df["HealthIndex"].mean(),
                df["InfrastructureIndex"].mean(),
                df["DevelopmentScore"].mean()
            ]

        }

    )


    fig = px.bar(

        comparison,

        x="Indicator",

        y=[
            selected,
            "Punjab Average"
        ],

        barmode="group",

        title="Performance Comparison"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )


    st.divider()


    st.subheader(
        "🧠 AI Development Assessment"
    )


    score = data["DevelopmentScore"]


    if score >= 70:

        st.success(
            f"{selected} is a high performing district. "
            "Focus on maintaining growth and improving sustainability."
        )


    elif score >= 40:

        st.info(
            f"{selected} shows moderate development performance. "
            "Targeted investment can improve key sectors."
        )


    else:

        st.warning(
            f"{selected} requires priority development intervention "
            "in education, healthcare and infrastructure."
        )


    st.divider()


    st.subheader(
        "💡 Recommended Planning Strategy"
    )


    recommendation = []


    if data["EducationIndex"] < df["EducationIndex"].mean():

        recommendation.append(
            "Increase education investment and school quality."
        )


    if data["HealthIndex"] < df["HealthIndex"].mean():

        recommendation.append(
            "Strengthen healthcare facilities and medical services."
        )


    if data["InfrastructureIndex"] < df["InfrastructureIndex"].mean():

        recommendation.append(
            "Improve infrastructure development projects."
        )


    if not recommendation:

        recommendation.append(
            "Maintain current performance and focus on sustainable development."
        )


    for r in recommendation:

        st.write(
            "• " + r
        )


    st.divider()


    report = pd.DataFrame(

        {

            "District":[selected],

            "Development Score":[data["DevelopmentScore"]],

            "Literacy Rate":[data["LiteracyRate"]],

            "Health Index":[data["HealthIndex"]],

            "Infrastructure Index":[data["InfrastructureIndex"]]

        }

    )


    st.download_button(

        "⬇ Download AI Report",

        report.to_csv(index=False),

        file_name=f"{selected}_AI_Development_Report.csv",

        mime="text/csv",

        use_container_width=True

    )