import streamlit as st
import plotly.express as px

from utils.data_loader import load_data


def show_population():

    df = load_data()


    st.markdown(
        """
        <div class="hero">

        <h1>
        👥 Population Analysis
        </h1>

        <p style="color:#64748B;font-size:17px;">
        Explore population distribution, demographic trends,
        density patterns and growth indicators across Punjab districts.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("")


    col1,col2,col3,col4 = st.columns(4)


    with col1:

        st.metric(
            "Total Population",
            f"{df['Population'].sum()/1000000:.1f} M"
        )


    with col2:

        st.metric(
            "Average Density",
            f"{df['Density'].mean():,.1f}"
        )


    with col3:

        st.metric(
            "Urban Coverage",
            f"{df['UrbanPercent'].mean():.1f}%"
        )


    with col4:

        st.metric(
            "Average Growth Rate",
            f"{df['GrowthRate'].mean():.2f}%"
        )


    st.divider()


    st.subheader(
        "👥 Population Distribution"
    )


    population = df.sort_values(
        "Population",
        ascending=False
    )


    fig = px.bar(

        population,

        x="District",

        y="Population",

        color="Population",

        title="Population by District"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )


    st.divider()


    col1,col2 = st.columns(2)


    with col1:

        st.subheader(
            "👨‍👩‍👧 Gender Distribution"
        )


        gender = {

            "Category":[
                "Male",
                "Female",
                "Transgender"
            ],

            "Population":[

                df["Male"].sum(),

                df["Female"].sum(),

                df["Transgender"].sum()

            ]

        }


        import pandas as pd


        gender_df = pd.DataFrame(
            gender
        )


        fig = px.pie(

            gender_df,

            names="Category",

            values="Population",

            title="Punjab Population Composition"

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )


    with col2:

        st.subheader(
            "📍 Population Density"
        )


        density = df.sort_values(

            "Density",

            ascending=False

        ).head(10)


        fig = px.bar(

            density,

            x="District",

            y="Density",

            color="Density",

            title="Top Density Districts"

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )


    st.divider()


    st.subheader(
        "📈 Population Growth Analysis"
    )


    growth = df.sort_values(

        "GrowthRate",

        ascending=False

    ).head(10)


    fig = px.bar(

        growth,

        x="District",

        y="GrowthRate",

        color="GrowthRate",

        title="Highest Population Growth Rate"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )


    st.divider()


    st.subheader(
        "📊 Population Indicators"
    )


    data = df[

        [

            "District",

            "Population",

            "Male",

            "Female",

            "Density",

            "UrbanPercent",

            "GrowthRate"

        ]

    ].sort_values(

        "Population",

        ascending=False

    )


    st.dataframe(

        data,

        hide_index=True,

        use_container_width=True

    )