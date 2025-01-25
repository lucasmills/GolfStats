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
                        dbc.CardHeader(html.H4("Scores per round")),
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

    ],
        sm=12,
        md=12
    ),
    id="dashboard"
)
