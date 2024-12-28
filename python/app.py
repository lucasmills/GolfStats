# Main script
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import pickle

app = Dash()

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

with open("data\\golf_data.pkl", "rb") as f:
    data = pickle.load(f)

# Plot score
fig = px.line(data, x=data["Date"], y=data["Score"], markers=True)

# Application layout
app.layout = html.Div(children=[
    html.H1(children="Lucas' Golf Statistics"),

    html.Div(children='''
        Score plots and stuff.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
