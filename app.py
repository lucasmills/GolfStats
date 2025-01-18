# Main script

# Main application file
import dash_bootstrap_components as dbc

from dash import Dash, dcc, html
from layout.dashboard import dashboard
from layout.navbar import navbar


# Create plotly dashboard application
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

# Application layout
app.layout = html.Div(children=[
    navbar,
    dashboard,
    dcc.Markdown(
        "*Version 1.0. Last updated 18 Jan 2025",
        link_target="_blank",
        id="attribution",
    ),
])

if __name__ == '__main__':
    app.run(debug=True)
