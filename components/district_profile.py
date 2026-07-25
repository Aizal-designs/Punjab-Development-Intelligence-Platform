import streamlit as st


def show_profile(data):

    st.subheader("District Profile")


    col1, col2, col3, col4 = st.columns(4)


    with col1:
        st.metric(
            "Population",
            f"{int(data['Population']):,}"
        )


    with col2:
        st.metric(
            "Literacy Rate",
            f"{data['LiteracyRate']}%"
        )


    with col3:
        st.metric(
            "Hospitals",
            int(data["Hospitals"])
        )


    with col4:
        st.metric(
            "Schools",
            int(data["TotalSchools"])
        )