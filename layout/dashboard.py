# Navigation bar
import dash_bootstrap_components as dbc
import pandas
import numpy

from dash import dcc, html
from dash_bootstrap_templates import load_figure_template
from layout.figures.historic_data_line_graph import \
    generate_historical_line_graph
from layout.figures.in_regulation_iqr_graph import generate_in_regulation_iqr
from layout.figures.round_analysis_radar import generate_round_analysis_radar
from layout.figures.score_iqr_graph import generate_score_iqr
from layout.figures.score_type_histogram import generate_score_type_histogram
from layout.figures.scorecard_table import generate_scorecard_table
from utils.calculate_handicap import calculate_handicap
from utils.data_load import load_data_util
from utils.generate_stats_card import generate_stats_card

# Load golf data
golf_data = load_data_util("data/golf_data.pkl")
all_data = pandas.read_excel(open("data/GolfData.xlsx", "rb"),
                             sheet_name="Score Cards")
par_data = pandas.read_excel(open("data/GolfData.xlsx", "rb"),
                             sheet_name="Course Pars")


# Get key stats for call out boxes
num_rounds = golf_data.shape[0]
avg_score = round(numpy.mean(golf_data["Score"]), 1)
avg_score_to_par = round(numpy.mean(golf_data["Score to par"]), 1)
lowest_score = numpy.min(golf_data["Score"])
courses_played = golf_data["Course"].nunique()
handicap = calculate_handicap(golf_data, par_data)


margins = dict(l=60, r=60, b=60, t=25, pad=0)
# Set the template for all dashboard plots
load_figure_template(["lux"])


# Generate figures
historical_line_graph = generate_historical_line_graph(golf_data, margins)
in_regulation_graph = generate_in_regulation_iqr(golf_data, margins)
score_iqr_graph = generate_score_iqr(golf_data, margins)
round_analysis_radar = generate_round_analysis_radar(golf_data)
score_type_histogram = generate_score_type_histogram(golf_data, margins)
scorecards_table = generate_scorecard_table(all_data, par_data, margins)


dashboard = dbc.Row(
    dbc.Col([
        dbc.Row([
            # Number of rounds played
            dbc.Col(generate_stats_card("Rounds played ", num_rounds)),

            # Average strokes
            dbc.Col(generate_stats_card("Average strokes ", avg_score)),

            # Average score to par
            dbc.Col(generate_stats_card("Handicap ",
                                        handicap)),

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

        # # Round analysis
        # dbc.Row([
        #     dbc.Col(
        #         dbc.Card(
        #             [
        #                 dbc.CardHeader(html.H4("Round Analysis")),
        #                 dbc.CardBody(
        #                     [
        #                         dcc.Graph(
        #                             id='example-graph99',
        #                             figure=round_analysis_radar,
        #                             config={'displayModeBar': False},
        #                             style={"height": "700px", "width": "100%", "flex": "1", "display": "flex"}
        #                         ),
        #
        #                         html.Div(style={"flex-grow": 1}),
        #
        #                         # Small text at the bottom
        #                         html.P("BSOB (Better side of Bogey) = ratio of holes better than to worse than bogey",
        #                                className="card-text",
        #                                style={"font-size": "12px", "color": "gray", "text-align": "left"})
        #                     ],
        #                 ),
        #             ],
        #         ),
        #         sm=12,
        #         md=12,
        #         style={'padding-right': "5px"}
        #     ),
        # ],
        #     className="dashboard-row"
        # ),

        # Round analysis 2
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(html.H4("Round Analysis")),
                        dbc.CardBody(
                            [
                                html.Div([

                                    html.Div([
                                        dcc.Graph(figure=in_regulation_graph)
                                    ], style={'width': '60%', 'display': 'inline-block'}),

                                    html.Div([
                                        dcc.Graph(figure=score_iqr_graph)
                                    ], style={'width': '40%', 'display': 'inline-block'}),

                                ]),

                                # Small text at the bottom
                                html.P("Red dot indicates the most recent round.",
                                       className="card-text",
                                       style={"font-size": "12px", "color": "gray", "text-align": "left"})
                            ],
                        ),
                    ],
                ),
                sm=6,
                md=12,
                style={'padding-right': "5px"}
            ),
        ],
            className="dashboard-row"
        ),

        dbc.Row([
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(html.H4("Scorecards")),
                        dbc.CardBody(
                            [
                                dcc.Graph(
                                    id='example-graph4',
                                    figure=scorecards_table
                                )
                            ]),
                    ],
                ),
            ),
        ],
            className="dashboard-row"),

    ],
        sm=12,
        md=12
    ),
    id="dashboard"
)
