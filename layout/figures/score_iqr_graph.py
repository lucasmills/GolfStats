#
import plotly.express as px
import plotly.graph_objects as go


# Generator
def generate_score_iqr(golf_data, margins):
    fig = px.box(golf_data, y=["Score"])
    fig.update_layout(xaxis_title="Category", yaxis_title="Score per round",
                      dragmode="pan")

    fig.update_layout(
        autosize=True,
        margin=margins
    )

    # Get latest round data
    latest_round = golf_data.iloc[-1]
    latest_round_score = latest_round["Score"]

    fig.add_trace(go.Scatter(
        x=["Score"],
        y=[latest_round_score],
        mode="markers",
        marker=dict(color="red", size=16),
        showlegend=False
    ))

    fig.update_layout(
        xaxis_title=None
    )

    return fig
