# Navigation bar
import dash_bootstrap_components as dbc
import numpy
import pickle
import plotly.express as px
import plotly.graph_objects as go

from dash import dcc, html
from dash_bootstrap_templates import load_figure_template
from utils.utility import generate_stats_card

# Load golf data
with open("data\\golf_data.pkl", "rb") as f:
    golf_data = pickle.load(f)

# Get key stats for call out boxes
num_rounds = golf_data.shape[0]
avg_score = numpy.mean(golf_data["Score"])
avg_score_to_par = numpy.mean(golf_data["Score to par"])
lowest_score = numpy.min(golf_data["Score"])
courses_played = golf_data["Course"].nunique()

# Set the template for all dashboard plots
load_figure_template(["lux"])

# Plot score
fig = go.Figure()

# Score
fig.add_trace(
    go.Scatter(
        x=golf_data["Date"],
        y=golf_data["Score"],
        customdata=["Course"],
        name="Score"
    )
)

# Fairways
fig.add_trace(
    go.Scatter(
        x=golf_data["Date"],
        y=golf_data["Fairways"],
        name="Fairways",
        visible="legendonly"
    )
)

# Greens in regulation
fig.add_trace(
    go.Scatter(
        x=golf_data["Date"],
        y=golf_data["GIR"],
        name="Greens",
        visible="legendonly"
    )
)

# Putts
fig.add_trace(
    go.Scatter(
        x=golf_data["Date"],
        y=golf_data["Putts"],
        name="Putts",
        visible="legendonly"
    )
)

# fig.update_traces(hovertemplate="<br>".join([
#     "Score: %{y}",
#     "Course: %{customdata}"]),
#     marker=dict(size=10))

fig2 = px.box(golf_data, y=["Fairways", "GIR"])


fig3 = go.Figure()
fig3.add_trace(go.Histogram(x=golf_data["Birdies"], name="Birdies"))
fig3.add_trace(go.Histogram(x=golf_data["Pars"], name="Pars"))
fig3.add_trace(go.Histogram(x=golf_data["Bogeys"], name="Bogeys"))
fig3.add_trace(go.Histogram(x=golf_data["Doubles+"], name="Double+"))

# Overlay both histograms
fig3.update_layout(barmode='overlay')
# Reduce opacity to see both histograms
fig3.update_traces(opacity=0.75)

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
                                figure=fig
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
                md=6
            ),
        ],
            className="dashboard-row"),

    ],
        sm=12,
        md=12
    ),
    id="dashboard"
)
