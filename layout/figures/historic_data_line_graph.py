#

import numpy
import plotly.graph_objects as go


# Generator
def generate_historical_line_graph(golf_data, line_width):
    # Plot score
    fig = go.Figure()

    # Score
    marker_color = ["grey", "grey"]
    marker_line_color = ["black", "black"]
    marker_symbol = ["diamond", "diamond"]
    rolling_avg = golf_data["Score"].rolling(window=2).mean().values
    num_rows = rolling_avg.size

    for i in range(2, num_rows):
        marker_line_color.append("black")
        if rolling_avg[i] == rolling_avg[i - 1]:
            marker_color.append("black")
            marker_symbol.append("diamond")
        elif rolling_avg[i] > rolling_avg[i - 1]:
            marker_color.append("red")
            marker_symbol.append("arrow-bar-up")
        else:
            marker_color.append("green")
            marker_symbol.append("arrow-bar-down")

    fig.add_trace(
        go.Scatter(
            x=golf_data["Date"],
            y=golf_data["Score"],
            line_width=line_width,
            customdata=["Course"],
            name="Score",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=golf_data["Date"],
            y=rolling_avg,
            customdata=["Course"],
            name="Trend",
            visible="legendonly",
            line_color="darkblue",
            line_dash="dash",
            line_width=line_width,
            marker_color=marker_color,
            marker_line_color=marker_line_color,
            marker_line_width=2,
            marker_size=20,
            marker_symbol=marker_symbol
        )
    )

    # Fairways
    fig.add_trace(
        go.Scatter(
            x=golf_data["Date"],
            y=golf_data["Fairways"],
            name="Fairways",
            visible="legendonly"
        )
    )

    # Greens in regulation
    fig.add_trace(
        go.Scatter(
            x=golf_data["Date"],
            y=golf_data["GIR"],
            line_width=line_width,
            name="Greens",
            visible="legendonly"
        )
    )

    # Putts
    fig.add_trace(
        go.Scatter(
            x=golf_data["Date"],
            y=golf_data["Putts"],
            line_width=line_width,
            name="Putts",
            visible="legendonly"
        )
    )

    return fig
