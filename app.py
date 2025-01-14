# Main script

# Main application file
import dash_bootstrap_components as dbc

from dash import Dash, html
from layout.dashboard import dashboard
from layout.navbar import navbar


# Create plotly dashboard application
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

# Application layout
app.layout = html.Div(children=[
    navbar,
    dashboard
])

if __name__ == '__main__':
    app.run(debug=True)
