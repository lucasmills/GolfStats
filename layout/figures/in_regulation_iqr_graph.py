#
import plotly.express as px


# Generator
def generate_in_regulation_iqr(golf_data, margins):
    fig = px.box(golf_data, y=["Fairways", "GIR"])
    fig.update_layout(xaxis_title="Category", yaxis_title="Achieved per round")

    fig.update_layout(

        margin=dict(
            l=50,
            r=50,
            b=50,
            t=25,
            pad=4
        )


    return fig
