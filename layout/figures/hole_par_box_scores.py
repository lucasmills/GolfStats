#
import dash_bootstrap_components as dbc
from dash import html


# Generator
def generate_hole_par_box_scores(golf_data, margins):
    # Column headers
    headers = ["Par", "All", "Last"]

    # Calculate means
    p3_avg = round(golf_data["Par3Average"].mean(), 1)
    p4_avg = round(golf_data["Par4Average"].mean(), 1)
    p5_avg = round(golf_data["Par5Average"].mean(), 1)

    # Most recent round
    last_round = golf_data.iloc[-1]
    p3_last = round(last_round["Par3Average"], 1)
    p4_last = round(last_round["Par4Average"], 1)
    p5_last = round(last_round["Par5Average"], 1)

    # Comment
    numbers = [
        # PAR AVG LAST
        3, p3_avg, p3_last,
        4, p4_avg, p4_last,
        5, p5_avg, p5_last
    ]

    # Header row
    header_row = dbc.Row([
        dbc.Col(html.Div(header, style={
            'fontWeight': 'bold', 'textAlign': 'center'   #'fontWeight': 'bold', 'fontSize': '24px', 'textAlign': 'center'
        }), width=4) for header in headers
    ], className="mb-4")

    # Number grid rows
    grid_rows = []
    for i in range(0, 9, 3):
        row = dbc.Row([
            dbc.Col(html.Div(str(numbers[i + j]),
                             style={'textAlign': 'center'}   # style={'fontSize': '48px', 'textAlign': 'center'}
                             ), width=4) for j in range(3)
        ], className="mb-3")
        grid_rows.append(row)

    return header_row, grid_rows
