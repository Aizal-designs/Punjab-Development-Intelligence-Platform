import streamlit as st

from config import APP_VERSION


def create_sidebar():

    with st.sidebar:

        st.title("PDIP")

        st.caption(
            "Punjab Development Intelligence Platform"
        )


        st.divider()


        st.subheader("Navigation")


        pages = [

            "🏠 Home",

            "📍 District Explorer",

            "📊 Overview",

            "🎓 Education",

            "🏥 Healthcare",

            "👥 Population",

            "🛣 Infrastructure",

            "📈 Development Index",

            "📉 Analytics",

            "⚖ Comparison",

            "🤖 AI Insights",

            "🔬 Research Mode",

            "📄 Reports",

            "ℹ About"

        ]


        page = st.radio(
            "Select Page",
            pages,
            label_visibility="collapsed"
        )


        st.divider()


        st.caption(
            "Data Driven Decision Support System"
        )

        st.caption(
            f"Version {APP_VERSION}"
        )


    return page