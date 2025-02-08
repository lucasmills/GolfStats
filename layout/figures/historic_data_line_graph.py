#

import numpy
import plotly.graph_objects as go


# Generator
def generate_historical_line_graph(golf_data, margins):
    line_width = 4
    # Plot score
    layout = go.Layout(
                legend=dict(
                    orientation="h",
                    yanchor="top",
                    y=1.1
                )
    )
    fig = go.Figure(layout=layout)

    # Score
    marker_color = ["grey", "grey"]
    marker_line_color = ["black", "black"]
    marker_symbol = ["hash-dot", "hash-dot"]
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
            line_color="black",
            line_dash="dash",
            line_width=1,
            marker_color=marker_color,
            marker_line_color=marker_line_color,
            marker_line_width=2,
            marker_size=15,
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

    fig.update_layout(
        autosize=True,
        margin=margins,
        updatemenus=[{
            'buttons': [{
                'args': ['mode', 'pan'],
                'label': 'Pan',
                'method': 'relayout'
            }]
        }]
    )

    return fig
