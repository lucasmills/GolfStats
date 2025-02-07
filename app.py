# Main script

# Main application file
import dash_bootstrap_components as dbc

from dash import Dash, dcc, html
from layout.dashboard import dashboard
from layout.navbar import navbar


# Create plotly dashboard application
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX],
           meta_tags=[{'name': 'viewport',
                       'content': 'width=device-width, initial-scale=.5'}])

# Application layout
app.layout = html.Div(children=[
    navbar,
    dashboard,
    dcc.Markdown(
        "*Version 1.2; last updated February 2025",
        link_target="_blank",
        id="attribution",
    ),
])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
