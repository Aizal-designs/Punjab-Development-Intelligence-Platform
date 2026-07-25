import streamlit as st


def show_about():

    st.markdown(
        """
        <div class="hero">

        <h1>
        ℹ About PDIP
        </h1>

        <p style="color:#64748B;font-size:17px;">
        Punjab Development Intelligence Platform,
        a data science based solution for district level
        development analysis and evidence based planning.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("")


    st.subheader("🎯 Platform Overview")


    st.write(
        """
        Punjab Development Intelligence Platform (PDIP) is an
        interactive analytics dashboard designed to explore,
        compare and analyze development indicators of Punjab districts.

        The platform combines demographic, education, healthcare
        and infrastructure data to generate meaningful insights
        for researchers, students and policy analysts.
        """
    )


    st.divider()


    col1,col2,col3 = st.columns(3)


    with col1:

        st.metric(
            "Purpose",
            "Development Analysis"
        )


    with col2:

        st.metric(
            "Coverage",
            "Punjab Districts"
        )


    with col3:

        st.metric(
            "Version",
            "2.0"
        )


    st.divider()


    st.subheader("🚀 Objectives")


    objectives = [

        "Support evidence based decision making",

        "Analyze district development performance",

        "Identify regional strengths and weaknesses",

        "Provide data driven recommendations",

        "Support academic research and analysis"

    ]


    for item in objectives:

        st.success(item)


    st.divider()


    st.subheader("📊 Available Modules")


    modules = [

        "District Explorer",

        "Punjab Overview",

        "Education Analysis",

        "Healthcare Analysis",

        "Population Analysis",

        "Infrastructure Analysis",

        "Development Index",

        "Statistical Analytics",

        "District Comparison",

        "AI Insights",

        "Research Mode",

        "Reports"

    ]


    st.dataframe(

        {

            "Module": modules,

            "Status": [
                "Available"
                for _ in modules
            ]

        },

        hide_index=True,

        use_container_width=True

    )


    st.divider()


    st.subheader("🛠 Technology Stack")


    tech1,tech2 = st.columns(2)


    with tech1:

        st.write(
            """
            🐍 Python

            🐼 Pandas

            🔢 NumPy

            🎨 Streamlit

            📊 Plotly

            """
        )


    with tech2:

        st.write(
            """
            📈 Data Analytics

            📉 Visualization

            🔧 Git & GitHub

            🧠 Data Science

            📁 CSV Data Processing

            """
        )


    st.divider()


    st.subheader("📌 Project Information")


    st.info(
        """
        Punjab Development Intelligence Platform (PDIP)

        Version: 2.0

        Built as a Data Science Portfolio Project.

        Focus:
        District analytics, development indicators,
        visualization and evidence based insights.
        """
    )