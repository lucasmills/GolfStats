#

import numpy
import plotly.graph_objects as go


# Generator
def generate_score_type_histogram(golf_data):
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
        margin=dict(
            l=50,
            r=50,
            b=50,
            t=25,
            pad=4
        )
    )

    return fig
