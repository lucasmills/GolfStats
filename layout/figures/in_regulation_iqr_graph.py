#
import plotly.express as px
import plotly.graph_objects as go


# Generator
def generate_in_regulation_iqr(golf_data, margins):
    fig = px.box(golf_data, y=["Fairways", "GIR"])
    fig.update_layout(xaxis_title="Category", yaxis_title="Achieved per round",
                      dragmode="pan")

    fig.update_layout(
        autosize=True,
        margin=margins
    )

    # Get latest round data
    latest_round = golf_data.iloc[-1]
    latest_round_gir = latest_round["GIR"]
    latest_round_fw = latest_round["Fairways"]

    fig.add_trace(go.Scatter(
        x=["GIR"],
        y=[latest_round_gir],
        mode="markers",
        marker=dict(color="red", size=16),
        showlegend=False
    ))

    fig.add_trace(go.Scatter(
        x=["Fairways"],
        y=[latest_round_fw],
        mode="markers",
        marker=dict(color="red", size=16),
        showlegend=False
    ))

    fig.update_layout(
        xaxis_title=None
    )

    return fig
