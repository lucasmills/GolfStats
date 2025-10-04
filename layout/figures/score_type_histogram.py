#

import plotly.graph_objects as go


# Generator
def generate_score_type_histogram(golf_data, margins):
    layout = go.Layout(
        legend=dict(
            orientation="h",
            yanchor="top",
            y=1.1
        ),
        dragmode="pan"
    )

    fig = go.Figure(layout=layout)

    fig.add_trace(go.Histogram(x=golf_data["Birdies"],
                               name="Birdies",
                               visible="legendonly",
                               marker=dict(color="lightgreen")))
    
    fig.add_trace(go.Histogram(x=golf_data["Pars"],
                               name="Pars",
                               marker=dict(color="skyblue")))

    fig.add_trace(go.Histogram(x=golf_data["Bogeys"],
                               name="Bogeys",
                               marker=dict(color="khaki")))

    fig.add_trace(go.Histogram(x=golf_data["Doubles+"],
                               name="Double+",
                               visible="legendonly",
                               marker=dict(color="lightcoral")))

    # Overlay both histograms
    fig.update_layout(barmode="overlay")

    # Reduce opacity to see both histograms
    fig.update_traces(opacity=0.75)

    fig.update_layout(xaxis_title="Average per round", yaxis_title="Frequency")

    fig.update_layout(
        autosize=True,
        margin=margins
    )

    return fig
