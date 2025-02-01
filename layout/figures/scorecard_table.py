#
import pandas
from plotly import graph_objects as go


# Generator
def generate_scorecard_table(all_data, margins):
    all_data["Date"] = all_data["Date"].astype(str)
    all_data = all_data.iloc[:, : 20]
    fig = go.Figure(
        data=[go.Table(
            columnwidth=[20, 20,
                         10, 10, 10, 10, 10, 10, 10, 10, 10,
                         10, 10, 10, 10, 10, 10, 10, 10, 10],
            header=dict(values=["Course", "Date",
                                "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17",
                                "18"]),
            cells=dict(values=all_data.transpose()))
        ])

    fig.update_layout(
        autosize=True,
        margin=margins
    )

    return fig
