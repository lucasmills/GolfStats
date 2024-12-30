# Main script

# Core python imports
from dash import Dash, html, dcc
from dash_bootstrap_templates import load_figure_template

import dash_bootstrap_components as dbc
import numpy
import plotly.express as px
import pickle

# Local project imports
from python.dash_utility.utility import generate_stats_card

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
load_figure_template(["cyborg", "darkly"])

# Plot score
fig = px.line(golf_data,
              x="Date",
              y="Score",
              custom_data=["Course"],
              markers=True)

fig.update_traces(hovertemplate="<br>".join([
    "Date: %{x}",
    "Score: %{y}",
    "Course: %{customdata[0]}"]),
    marker=dict(size=15))


# Create plotly dashboard application
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Application layout
app.layout = html.Div(children=[
    html.H1(children="Lucas' Golf Statistics",
            style={"textAlign": "center"}),

    dbc.Row([
        # Number of rounds played
        dbc.Col(generate_stats_card("Rounds played ", num_rounds)),

        # Average strokes
        dbc.Col(generate_stats_card("Average strokes ", avg_score)),

        # Average score to par
        dbc.Col(generate_stats_card("Average score to par ", avg_score_to_par)),

        # Lowest score
        dbc.Col(generate_stats_card("Lowest score ", lowest_score)),

        # Number of unique course played
        dbc.Col(generate_stats_card("Courses played ", courses_played)),
    ],
        style={'marginBlock': '10px'}),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
