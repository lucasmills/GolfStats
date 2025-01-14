# Script to house utility function for dash application
import dash_bootstrap_components as dbc

from dash import html


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
                   # "backgroundColor": '#363636',
                   'border': 'none',
                   'borderRadius': '10px'}
        )
    )
