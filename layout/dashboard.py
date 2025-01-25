# Navigation bar
import dash_bootstrap_components as dbc
import numpy


from dash import dcc, html
from dash_bootstrap_templates import load_figure_template
from layout.figures.historic_data_line_graph import \
    generate_historical_line_graph
from layout.figures.in_regulation_iqr_graph import generate_in_regulation_iqr
from layout.figures.score_type_histogram import generate_score_type_histogram
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

# Generate figures
historical_line_graph = generate_historical_line_graph(golf_data, LINE_WIDTH)
in_regulation_graph = generate_in_regulation_iqr(golf_data)
score_type_histogram = generate_score_type_histogram(golf_data)

import pandas
from plotly import graph_objects as go
fig = go.Figure(data=[go.Table(header=dict(values=['A Scores', 'B Scores']),
                 cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
                     ])

all_data = pandas.read_excel("data/GolfData.xlsx")
all_data["Date"] = all_data["Date"].astype(str)
all_data = all_data.iloc[:, : 20]
fig = go.Figure(
    data=[go.Table(
        columnwidth=[20, 20,
                     10, 10, 10, 10, 10, 10, 10, 10, 10,
                     10, 10, 10, 10, 10, 10, 10, 10, 10],
        header=dict(values=["Course", "Date",
                            "1", "2", "3", "4", "5", "6", "7" ,"8", "9",
                            "10", "11", "12", "13", "14", "15", "16", "17",
                            "18"]),
        cells=dict(values=all_data.transpose()))
    ])

fig.update_layout(
    autosize=True,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=0
    )
)

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
                                    figure=in_regulation_graph
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
                        dbc.CardHeader(html.H4("Scorecards")),
                        dbc.CardBody(
                            [
                                dcc.Graph(
                                    id='example-graph3',
                                    figure=score_type_histogram
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









        dbc.Row([
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(html.H4("Scores per round")),
                        dbc.CardBody(
                            [
                                dcc.Graph(
                                    id='example-graph4',
                                    figure=fig
                                )
                            ]),
                    ],
                ),
                # sm=12,
                # md=12,
                # style={'padding-left': "5px"}
            ),
        ],
            className="dashboard-row"),












    ],
        sm=12,
        md=12
    ),
    id="dashboard"
)
