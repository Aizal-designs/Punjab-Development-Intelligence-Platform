import plotly.express as px


GREEN = "#0B5D3A"

LIGHT_GREEN = "#1E7D4F"

GOLD = "#D4A017"


def bar_chart(df, x, y, title):

    fig = px.bar(

        df,

        x=x,

        y=y,

        title=title,

        color_discrete_sequence=[GREEN]

    )

    fig.update_layout(

        template="plotly_white",

        height=430,

        title_x=0.5,

        paper_bgcolor="white",

        plot_bgcolor="white",

        margin=dict(

            l=20,

            r=20,

            t=55,

            b=20

        )

    )

    return fig


def line_chart(df, x, y, title):

    fig = px.line(

        df,

        x=x,

        y=y,

        markers=True,

        title=title

    )

    fig.update_traces(

        line=dict(

            color=GREEN,

            width=4

        ),

        marker=dict(

            size=8,

            color=GOLD

        )

    )

    fig.update_layout(

        template="plotly_white",

        height=430,

        title_x=0.5,

        paper_bgcolor="white",

        plot_bgcolor="white"

    )

    return fig


def pie_chart(df, names, values, title):

    fig = px.pie(

        df,

        names=names,

        values=values,

        hole=0.55,

        title=title,

        color_discrete_sequence=[

            GREEN,

            LIGHT_GREEN,

            GOLD,

            "#7CB342",

            "#A5D6A7"

        ]

    )

    fig.update_layout(

        template="plotly_white",

        height=430,

        title_x=0.5,

        paper_bgcolor="white"

    )

    return fig