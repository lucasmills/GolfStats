#
import dash_bootstrap_components as dbc
from dash import html


# Generator
def generate_other_metrics_box_scores(golf_data, margins):
    # Column headers
    headers = ["Type", "All", "Last"]

    # Calculate means
    fairways_avg = round(golf_data["Fairways"].mean(), 1)
    gir_average = round(golf_data["GIR"].mean(), 1)
    putts_average = round(golf_data["Putts"].mean(), 1)

    # Most recent round
    last_round = golf_data.iloc[-1]
    fairways_last = round(last_round["Fairways"], 1)
    gir_last = round(last_round["GIR"], 1)
    putts_last = round(last_round["Putts"], 1)

    # Comment
    numbers = [
        # PAR AVG LAST
        "FIR", fairways_avg, fairways_last,
        "GIR", gir_average, gir_last,
        "Putts", putts_average, putts_last
    ]

    # Header row
    header_row = dbc.Row([
        dbc.Col(html.Div(header, style={
            'fontWeight': 'bold', 'textAlign': 'center'
        }), width=4) for header in headers
    ], className="mb-4")

    # Number grid rows
    grid_rows = []
    for i in range(0, 9, 3):
        row = dbc.Row([
            dbc.Col(html.Div(str(numbers[i + j]),
                             style={'textAlign': 'center'}
                             ), width=4) for j in range(3)
        ], className="mb-3")
        grid_rows.append(row)

    return header_row, grid_rows
