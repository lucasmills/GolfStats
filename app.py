# Main script

import dash_bootstrap_components as dbc

from dash import Dash, dcc, html
from layout.dashboard import dashboard
from layout.navbar import navbar


# Create plotly dashboard application
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX],
           meta_tags=[{'name': 'viewport',
                       'content': 'width=device-width, initial-scale=.5'}])

# Application title and icon for browser
app.title = "Mills Golf Stats"
app._favicon = "golf_ball.ico"

# Application layout
app.layout = html.Div(children=[
    navbar,
    dashboard,
    dcc.Markdown(
        "*Version 1.5.6; last updated 04 October 2025. Acknowledgements: Adrian WG, Adam H",
        link_target="_blank",
        id="attribution",
    ),
])

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
