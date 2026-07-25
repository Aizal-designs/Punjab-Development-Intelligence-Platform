import streamlit as st
import plotly.express as px
import pandas as pd

from utils.data_loader import load_data


def show_research_mode():

    df = load_data()


    st.markdown(
        """
        <div class="hero">

        <h1>
        🔬 Research Mode
        </h1>

        <p style="color:#64748B;font-size:17px;">
        Advanced analytical workspace for researchers,
        students and data analysts.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("")


    col1,col2,col3,col4 = st.columns(4)


    with col1:

        st.metric(
            "Rows",
            len(df)
        )


    with col2:

        st.metric(
            "Columns",
            len(df.columns)
        )


    with col3:

        st.metric(
            "Numeric Features",
            len(
                df.select_dtypes(
                    include="number"
                ).columns
            )
        )


    with col4:

        st.metric(
            "Districts",
            df["District"].nunique()
        )


    st.divider()


    option = st.selectbox(

        "🧪 Select Research Tool",

        [

            "Dataset Explorer",

            "Statistical Summary",

            "Missing Data Analysis",

            "Correlation Analysis",

            "Feature Analysis"

        ]

    )


    st.divider()


    if option == "Dataset Explorer":


        st.subheader(
            "📄 Dataset Explorer"
        )


        st.write(
            "Complete Punjab district development dataset."
        )


        st.dataframe(

            df,

            hide_index=True,

            use_container_width=True

        )



    elif option == "Statistical Summary":


        st.subheader(
            "📊 Statistical Summary"
        )


        summary = df.describe().T


        st.dataframe(

            summary,

            use_container_width=True

        )



    elif option == "Missing Data Analysis":


        st.subheader(
            "⚠ Missing Values Report"
        )


        missing = pd.DataFrame(

            {

                "Column": df.columns,

                "Missing Values": df.isnull().sum(),

                "Missing Percentage":
                (
                    df.isnull().sum()
                    /
                    len(df)
                    *
                    100
                ).round(2)

            }

        )


        missing = missing.sort_values(

            "Missing Values",

            ascending=False

        )


        st.dataframe(

            missing,

            hide_index=True,

            use_container_width=True

        )


        fig = px.bar(

            missing,

            x="Column",

            y="Missing Percentage",

            title="Missing Data Percentage"

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )



    elif option == "Correlation Analysis":


        st.subheader(
            "🔗 Feature Correlation Matrix"
        )


        numeric = df.select_dtypes(

            include="number"

        )


        correlation = numeric.corr()


        fig = px.imshow(

            correlation,

            text_auto=True,

            title="Correlation Heatmap"

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )


        st.dataframe(

            correlation,

            use_container_width=True

        )



    elif option == "Feature Analysis":


        st.subheader(
            "📈 Feature Relationship Analysis"
        )


        numeric_columns = list(

            df.select_dtypes(

                include="number"

            ).columns

        )


        x_axis = st.selectbox(

            "Select X Feature",

            numeric_columns

        )


        y_axis = st.selectbox(

            "Select Y Feature",

            numeric_columns,

            index=1

        )


        fig = px.scatter(

            df,

            x=x_axis,

            y=y_axis,

            hover_name="District",

            title=f"{x_axis} vs {y_axis}"

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )



    st.divider()


    st.subheader(
        "📥 Export Research Dataset"
    )


    csv = df.to_csv(

        index=False

    )


    st.download_button(

        label="Download Complete CSV Dataset",

        data=csv,

        file_name="Punjab_Development_Dataset.csv",

        mime="text/csv"

    )