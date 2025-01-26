#

import numpy
import plotly.graph_objects as go


# Generator
def generate_score_type_histogram(golf_data, margins):
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=golf_data["Birdies"], name="Birdies"))
    fig.add_trace(go.Histogram(x=golf_data["Pars"], name="Pars"))
    fig.add_trace(go.Histogram(x=golf_data["Bogeys"], name="Bogeys"))
    fig.add_trace(go.Histogram(x=golf_data["Doubles+"], name="Double+"))

    # Overlay both histograms
    fig.update_layout(barmode="overlay")
    # Reduce opacity to see both histograms
    fig.update_traces(opacity=0.75)

    fig.update_layout(xaxis_title="Average per round", yaxis_title="Frequency")

    fig.update_layout(
        autosize=True,
        margin=margins
    )

    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=1
    ))

    return fig
