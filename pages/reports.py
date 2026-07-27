import streamlit as st
import pandas as pd
import io

from utils.data_loader import load_data

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_CENTER


def create_pdf(district_name, data):

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER


    heading_style = styles["Heading2"]


    normal_style = styles["BodyText"]


    story = []


    story.append(
        Paragraph(
            "Punjab Development Intelligence Platform (PDIP)",
            title_style
        )
    )

    story.append(
        Spacer(1,20)
    )


    story.append(
        Paragraph(
            f"{district_name} District Development Report",
            heading_style
        )
    )

    story.append(
        Spacer(1,15)
    )


    summary = (
        "This report presents district level development indicators "
        "including population, education, healthcare, infrastructure "
        "and overall development performance."
    )


    story.append(
        Paragraph(
            summary,
            normal_style
        )
    )


    story.append(
        Spacer(1,20)
    )


    table_data = [

        ["Indicator","Value"],

        [
            "Population",
            f"{int(data['Population']):,}"
        ],

        [
            "Literacy Rate",
            f"{data['LiteracyRate']:.2f}%"
        ],

        [
            "Hospitals",
            str(int(data["Hospitals"]))
        ],

        [
            "Total Schools",
            str(int(data["TotalSchools"]))
        ],

        [
            "Education Index",
            f"{data['EducationIndex']:.2f}"
        ],

        [
            "Health Index",
            f"{data['HealthIndex']:.2f}"
        ],

        [
            "Infrastructure Index",
            f"{data['InfrastructureIndex']:.2f}"
        ],

        [
            "Development Score",
            f"{data['DevelopmentScore']:.2f}"
        ],

        [
            "District Rank",
            str(int(data["Rank"]))
        ]

    ]


    table = Table(
        table_data,
        colWidths=[200,150]
    )


    table.setStyle(

        TableStyle([

            ("GRID",(0,0),(-1,-1),0.5,None),

            ("BACKGROUND",
             (0,0),
             (-1,0),
             None),

            ("ALIGN",
             (0,0),
             (-1,-1),
             "CENTER"),

            ("VALIGN",
             (0,0),
             (-1,-1),
             "MIDDLE")

        ])

    )


    story.append(table)


    story.append(
        Spacer(1,25)
    )


    story.append(
        Paragraph(
            "Development Recommendation",
            heading_style
        )
    )


    if data["DevelopmentScore"] >= 70:

        recommendation = (
            "District performance is strong. "
            "Focus on sustainable growth and maintaining quality services."
        )

    elif data["DevelopmentScore"] >= 40:

        recommendation = (
            "District shows moderate development. "
            "Further improvement is required in key sectors."
        )

    else:

        recommendation = (
            "District requires priority investment in education, "
            "healthcare and infrastructure."
        )


    story.append(
        Paragraph(
            recommendation,
            normal_style
        )
    )


    doc.build(story)


    buffer.seek(0)

    return buffer



def show_reports():

    df = load_data()


    st.title("📄 Development Reports")


    st.write(
        "Generate professional district development reports."
    )


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
        f"{selected} Development Profile"
    )


    preview = pd.DataFrame(

        {

            "Indicator":[

                "Population",
                "Literacy Rate",
                "Hospitals",
                "Schools",
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
        preview,
        hide_index=True,
        use_container_width=True
    )


    pdf = create_pdf(
        selected,
        data
    )


    st.download_button(

        label="📥 Download Professional PDF Report",

        data=pdf,

        file_name=f"{selected}_PDIP_Report.pdf",

        mime="application/pdf"

    )