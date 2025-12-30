import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import requests

# Fetch data
response = requests.get("http://127.0.0.1:8000/students")
df = pd.DataFrame(response.json())

app = dash.Dash(__name__)

# ---------- STYLES ----------
CARD_STYLE = {
    "backgroundColor": "white",
    "padding": "20px",
    "borderRadius": "10px",
    "boxShadow": "0 4px 8px rgba(0,0,0,0.1)",
    "textAlign": "center",
    "flex": "1"
}

# ---------- LAYOUT ----------
app.layout = html.Div(
    style={
        "fontFamily": "Segoe UI",
        "backgroundColor": "#f4f6f9",
        "padding": "20px"
    },
    children=[

        # ===== HEADER =====
        html.H1(
            "Student Performance Dashboard",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "marginBottom": "10px"
            }
        ),
        html.P(
            "Interactive analysis of student marks using MongoDB & FastAPI",
            style={"textAlign": "center", "color": "#7f8c8d"}
        ),

        html.Br(),

        # ===== FILTERS =====
        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "15px",
                "borderRadius": "10px",
                "boxShadow": "0 2px 6px rgba(0,0,0,0.1)",
                "display": "flex",
                "gap": "40px",
                "alignItems": "center"
            },
            children=[
                html.Div([
                    html.Label("Select Subject"),
                    dcc.Dropdown(
                        id="subject_filter",
                        options=[
                            {"label": "All", "value": "All"},
                            {"label": "Maths", "value": "Maths"},
                            {"label": "Physics", "value": "Physics"},
                            {"label": "Chemistry", "value": "Chemistry"},
                        ],
                        value="All",
                        clearable=False
                    )
                ], style={"width": "200px"}),

                html.Div([
                    html.Label("Marks Range"),
                    dcc.RangeSlider(
                        id="marks_filter",
                        min=0,
                        max=100,
                        step=1,
                        value=[0, 100],
                        marks={0: "0", 50: "50", 100: "100"},
                        tooltip={"placement": "bottom"}
                    )
                ], style={"width": "400px"})
            ]
        ),

        html.Br(),

        # ===== KPI CARDS =====
        html.Div(
            style={"display": "flex", "gap": "20px"},
            children=[
                html.Div([
                    html.H3(id="total_students"),
                    html.P("Total Students")
                ], style=CARD_STYLE),

                html.Div([
                    html.H3(id="average_marks"),
                    html.P("Average Marks")
                ], style=CARD_STYLE),

                html.Div([
                    html.H3(id="topper_marks"),
                    html.P("Highest Marks")
                ], style=CARD_STYLE),
            ]
        ),

        html.Br(),

        # ===== GRAPHS =====
        html.Div(
            style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "20px"},
            children=[
                dcc.Graph(id="bar_chart"),
                dcc.Graph(id="pie_chart"),
            ]
        ),

        html.Br(),

        dcc.Graph(id="scatter_chart")
    ]
)

# ---------- CALLBACK ----------
@app.callback(
    Output("bar_chart", "figure"),
    Output("pie_chart", "figure"),
    Output("scatter_chart", "figure"),
    Output("total_students", "children"),
    Output("average_marks", "children"),
    Output("topper_marks", "children"),
    Input("subject_filter", "value"),
    Input("marks_filter", "value")
)
def update_dashboard(subject, marks_range):
    filtered = df.copy()

    if subject != "All":
        filtered = filtered[filtered["subject"] == subject]

    filtered = filtered[
        (filtered["marks"] >= marks_range[0]) &
        (filtered["marks"] <= marks_range[1])
    ]

    bar_fig = px.bar(
        filtered,
        x="name",
        y="marks",
        color="subject",
        title="Marks by Student"
    )

    pie_fig = px.pie(
        filtered,
        names="subject",
        values="marks",
        title="Subject-wise Distribution"
    )

    scatter_fig = px.scatter(
        filtered,
        x="marks",
        y="name",
        color="subject",
        title="Performance Scatter"
    )

    total = len(filtered)
    avg = round(filtered["marks"].mean(), 2) if total > 0 else 0
    top = filtered["marks"].max() if total > 0 else 0

    return bar_fig, pie_fig, scatter_fig, total, avg, top


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8050, debug=True)
