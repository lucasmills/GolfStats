# Navigation bar
import dash_bootstrap_components as dbc
import numpy
import pickle
import plotly.express as px

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
fig = px.line(golf_data,
              x="Date",
              y="Score",
              custom_data=["Course"],
              markers=True)

fig.update_traces(hovertemplate="<br>".join([
    "Score: %{y}",
    "Course: %{customdata[0]}"]),
    marker=dict(size=10))


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
            style={'marginBlock': '10px'}),

        dbc.Card(
            [
                dbc.CardHeader(html.H4("Round scores")),
                dbc.CardBody(
                    [
                        dcc.Graph(
                            id='example-graph',
                            figure=fig
                        )
                    ]),
            ],
        )
    ]),
    id="dashboard"
)
