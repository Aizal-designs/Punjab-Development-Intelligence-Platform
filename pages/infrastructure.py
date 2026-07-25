import streamlit as st
import plotly.express as px

from utils.data_loader import load_data


def show_infrastructure():

    df = load_data()


    st.markdown(
        """
        <div class="hero">

        <h1>
        🛣 Infrastructure Analysis
        </h1>

        <p style="color:#64748B;font-size:17px;">
        Analyze infrastructure strength, urban development
        and regional facilities across Punjab districts.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("")


    col1,col2,col3,col4 = st.columns(4)


    with col1:

        st.metric(
            "Average Infrastructure Index",
            f"{df['InfrastructureIndex'].mean():.2f}"
        )


    with col2:

        st.metric(
            "Total Schools",
            f"{int(df['TotalSchools'].sum()):,}"
        )


    with col3:

        st.metric(
            "Urban Coverage",
            f"{df['UrbanPercent'].mean():.1f}%"
        )


    with col4:

        st.metric(
            "Average Density",
            f"{df['Density'].mean():,.1f}"
        )


    st.divider()


    st.subheader(
        "🏗 Infrastructure Performance Ranking"
    )


    infra = df.sort_values(
        "InfrastructureIndex",
        ascending=False
    )


    fig = px.bar(

        infra,

        x="District",

        y="InfrastructureIndex",

        color="InfrastructureIndex",

        title="Infrastructure Index by District"

    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    st.divider()


    st.subheader(
        "🏙 Urban Development Analysis"
    )


    col1,col2 = st.columns(2)


    with col1:


        urban = df.sort_values(
            "UrbanPercent",
            ascending=False
        ).head(10)


        fig = px.bar(

            urban,

            x="District",

            y="UrbanPercent",

            color="UrbanPercent",

            title="Top Urbanized Districts"

        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


    with col2:


        fig = px.scatter(

            df,

            x="Density",

            y="InfrastructureIndex",

            size="Population",

            color="UrbanPercent",

            hover_name="District",

            title="Density vs Infrastructure"

        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )


    st.divider()


    st.subheader(
        "📊 Infrastructure Facilities"
    )


    facilities = df[

        [

            "District",

            "TotalSchools",

            "PrimarySchools",

            "MiddleSchools",

            "HighSchools",

            "UrbanPercent",

            "Density"

        ]

    ].sort_values(

        "TotalSchools",

        ascending=False

    )


    st.dataframe(

        facilities,

        hide_index=True,

        use_container_width=True

    )


    st.divider()


    st.subheader(
        "🏆 Top Infrastructure Districts"
    )


    top = df.sort_values(

        "InfrastructureIndex",

        ascending=False

    ).head(10)



    st.dataframe(

        top[

            [

                "District",

                "InfrastructureIndex",

                "UrbanPercent",

                "TotalSchools",

                "Density"

            ]

        ],

        hide_index=True,

        use_container_width=True

    )