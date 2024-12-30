# Main script
from dash import Dash, html, dcc

import plotly.express as px
import pandas as pd
import pickle

from dash_bootstrap_templates import load_figure_template

import dash_bootstrap_components as dbc


def generate_stats_card(title, value):
    return html.Div(
        dbc.Card([
            dbc.CardBody([
                html.P(value,
                       className="card-value",
                       style={'margin': '0px',
                              'fontSize': '22px',
                              'fontWeight': 'bold'}),

                html.H4(title,
                        className="card-title",
                        style={'margin': '0px',
                               'fontSize': '18px',
                               'fontWeight': 'bold'})
            ],
                style={'textAlign': 'center'}),
            ],
            style={'paddingBlock': '10px',
                   "backgroundColor": '#363636',
                   'border': 'none',
                   'borderRadius': '10px'})
    )


load_figure_template(["cyborg", "darkly"])

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Load golf data
with open("data\\golf_data.pkl", "rb") as f:
    data = pickle.load(f)

# Plot score
fig = px.line(data, x=data["Date"], y=data["Score"], markers=True)

# Application layout
app.layout = html.Div(children=[
    html.H1(children="Lucas' Golf Statistics",
            style={'textAlign': 'center'}),

    html.Div(children='''
        Overview statistics from the last 12 months
    '''),

    dbc.Row([
        dbc.Col(generate_stats_card("Number of rounds played ", 12), width=3),
        dbc.Col(generate_stats_card("Average score ", 92), width=3),
        dbc.Col(generate_stats_card("Average score ", 92), width=3),
        dbc.Col(generate_stats_card("Average score ", 92), width=3),
    ],
        style={'marginBlock': '10px'}),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
