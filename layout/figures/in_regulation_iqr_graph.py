#
import plotly.express as px


# Generator
def generate_in_regulation_iqr(golf_data):
    fig = px.box(golf_data, y=["Fairways", "GIR"])
    fig.update_layout(xaxis_title="Category", yaxis_title="Achieved per round")

    return fig
