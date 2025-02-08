#
import plotly.express as px


# Generator
def generate_in_regulation_iqr(golf_data, margins):
    fig = px.box(golf_data, y=["Fairways", "GIR"])
    fig.update_layout(xaxis_title="Category", yaxis_title="Achieved per round",
                      dragmode="pan")

    fig.update_layout(
        autosize=True,
        margin=margins
    )

    return fig
