#
import pandas
from plotly import graph_objects as go


# Generator
def generate_scorecard_table(all_data, margins):

    # Take this methodology and apply to scorecards based on value?
    # Can do this just need the par in this
    fill_color = []
    # n = len(df)
    # for col in cols_to_show:
    #     if col != 'output':
    #         fill_color.append(['#e6f2fd'] * n)
    #     else:
    #         fill_color.append(df["color"].to_list())


    c1 = "grey"
    c2 = "blue"
    c3 = "red"
    fill_color = [
        [c1, c2, c3, c1, c3],
        [c1, c2, c2, c2, c2],
        [c1, c2, c2, c2, c2],
        [c1, c2, c2, c2, c2],

        [c1, c2, c2, c2, c2],
        [c1, c2, c2, c2, c2],
        [c1, c2, c2, c2, c2],
        [c1, c2, c2, c2, c2],

        [c1, c2, c2, c2, c2],
        [c1, c2, c2, c2, c2],
        [c1, c2, c2, c2, c2],
        [c1, c2, c2, c2, c2],

        [c1, c2, c2, c2, c2],
        [c1, c2, c2, c2, c2],
        [c1, c2, c2, c2, c2],
        [c1, c2, c2, c2, c2],

        [c1, c2, c2, c2, c2],
        [c1, c2, c2, c2, c2],
        [c1, c2, c2, c2, c2],
        [c1, c2, c2, c2, c2],
    ]

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
                                "18"],
                        line_color='darkslategray',
                        fill_color='grey',
                        font=dict(color='white')
                        ),
            cells=dict(values=all_data.transpose(),
                       # fill_color=fill_color
                       )
        )
        ])

    margins = dict(l=10, r=10, b=10, t=10, pad=0)
    fig.update_layout(
        autosize=True,
        margin=margins
    )

    return fig
