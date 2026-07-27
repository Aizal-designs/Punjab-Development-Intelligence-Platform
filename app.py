import streamlit as st

from config import *



from components.sidebar import create_sidebar

from pages.home import show_home
from pages.district_explorer import show_district_explorer
from pages.overview import show_overview
from pages.education import show_education
from pages.healthcare import show_healthcare
from pages.population import show_population
from pages.infrastructure import show_infrastructure
from pages.development_index import show_development_index
from pages.analytics import show_analytics
from pages.comparison import show_comparison
from pages.ai_insights import show_ai_insights
from pages.research_mode import show_research_mode
from pages.reports import show_reports
from pages.about import show_about


# ======================================
# Page Configuration
# ======================================

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
    initial_sidebar_state=SIDEBAR_STATE
)




# ======================================
# Sidebar Navigation
# ======================================

selected_page = create_sidebar()


# ======================================
# Page Routing
# ======================================

PAGES = {

    "🏠 Home": show_home,

    "📍 District Explorer": show_district_explorer,

    "📊 Overview": show_overview,

    "🎓 Education": show_education,

    "🏥 Healthcare": show_healthcare,

    "👥 Population": show_population,

    "🛣 Infrastructure": show_infrastructure,

    "📈 Development Index": show_development_index,

    "📉 Analytics": show_analytics,

    "⚖ Comparison": show_comparison,

    "🤖 AI Insights": show_ai_insights,

    "🔬 Research Mode": show_research_mode,

    "📄 Reports": show_reports,

    "ℹ About": show_about

}


# ======================================
# Display Selected Page
# ======================================

if selected_page in PAGES:

    PAGES[selected_page]()

else:

    st.error("Page not found.")