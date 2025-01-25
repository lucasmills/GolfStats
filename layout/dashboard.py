# Navigation bar
import dash_bootstrap_components as dbc
import numpy
import pandas
import plotly.express as px
import plotly.graph_objects as go

from dash import dcc, html
from dash_bootstrap_templates import load_figure_template
from layout.figures.historic_data_line_graph import generate_historical_line_graph
from utils.data_load import load_data_util
from utils.generate_stats_card import generate_stats_card

# Load golf data
golf_data = load_data_util("data/golf_data.pkl")

# Get key stats for call out boxes
num_rounds = golf_data.shape[0]
avg_score = numpy.mean(golf_data["Score"])
avg_score_to_par = numpy.mean(golf_data["Score to par"])
lowest_score = numpy.min(golf_data["Score"])
courses_played = golf_data["Course"].nunique()

LINE_WIDTH = 4

# Set the template for all dashboard plots
load_figure_template(["lux"])

historical_line_graph = generate_historical_line_graph(golf_data, LINE_WIDTH)

fig2 = px.box(golf_data, y=["Fairways", "GIR"])
fig2.update_layout(xaxis_title="Category", yaxis_title="Achieved per round")


fig3 = go.Figure()
fig3.add_trace(go.Histogram(x=golf_data["Birdies"], name="Birdies"))
fig3.add_trace(go.Histogram(x=golf_data["Pars"], name="Pars"))
fig3.add_trace(go.Histogram(x=golf_data["Bogeys"], name="Bogeys"))
fig3.add_trace(go.Histogram(x=golf_data["Doubles+"], name="Double+"))

# Overlay both histograms
fig3.update_layout(barmode="overlay")
# Reduce opacity to see both histograms
fig3.update_traces(opacity=0.75)

fig3.update_layout(xaxis_title="Average per round", yaxis_title="Frequency")


dashboard = dbc.Row(
    dbc.Col([
        dbc.Row([
            # Number of rounds played
            dbc.Col(generate_stats_card("Rounds played ", num_rounds)),

            # Average strokes
            dbc.Col(generate_stats_card("Average strokes ", avg_score)),

            # Average score to par
            dbc.Col(generate_stats_card("Average handicap ",
                                        avg_score_to_par)),

            # Lowest score
            dbc.Col(generate_stats_card("Lowest score ", lowest_score)),
        ],
            className="dashboard-row",
            style={'marginBlock': '10px'}
        ),

        dbc.Row(
            dbc.Card(
                [
                    dbc.CardHeader(html.H4("Rounds")),
                    dbc.CardBody(
                        [
                            dcc.Graph(
                                id='example-graph1',
                                figure=historical_line_graph
                            )
                        ]),
                ],
            ),
            className="dashboard-row"
        ),

        dbc.Row([
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(html.H4("In regulation")),
                        dbc.CardBody(
                            [
                                dcc.Graph(
                                    id='example-graph2',
                                    figure=fig2
                                )
                            ]),
                    ],
                ),
                sm=12,
                md=6,
                style={'padding-right': "5px"}
            ),

            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(html.H4("Scores per round")),
                        dbc.CardBody(
                            [
                                dcc.Graph(
                                    id='example-graph3',
                                    figure=fig3
                                )
                            ]),
                    ],
                ),
                sm=12,
                md=6,
                style={'padding-left': "5px"}
            ),
        ],
            className="dashboard-row"),

    ],
        sm=12,
        md=12
    ),
    id="dashboard"
)
