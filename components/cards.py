import streamlit as st


def metric_card(title, value, icon="📊"):

    st.markdown(
        f"""
<div class="metric-card">

<div style="display:flex;justify-content:space-between;align-items:center;">

<div>

<div style="color:#64748B;font-size:15px;font-weight:600;">
{title}
</div>

<div style="font-size:34px;font-weight:800;color:#111827;margin-top:8px;">
{value}
</div>

</div>

<div style="
width:58px;
height:58px;
border-radius:16px;
background:#E8F5E9;
display:flex;
justify-content:center;
align-items:center;
font-size:28px;
">
{icon}
</div>

</div>

</div>
""",
unsafe_allow_html=True
)