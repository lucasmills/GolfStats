#
import pandas
from plotly import graph_objects as go


# Generator
def generate_scorecard_table(all_data, par_data, margins):

    # Take this methodology and apply to scorecards based on value?
    # Can do this just need the par in this
    fill_color = []
    # n = len(df)
    # for col in cols_to_show:
    #     if col != 'output':
    #         fill_color.append(['#e6f2fd'] * n)
    #     else:
    #         fill_color.append(df["color"].to_list())

    num_lists = 20
    per_list = all_data.shape[0]

    # Creating the list of lists
    fill_color = [[f"grey" for i in range(per_list)] for _ in range(num_lists)]

    for i in range(0, len(fill_color)):
        if i < 2:
            continue

        for j in range(0, len(fill_color[i])):
            a = 1
            course = all_data.iloc[j]["Course"]
            score = all_data.iloc[j][str(i-1)]
            fill = par_data["Course"] == course
            course_par = par_data[fill]
            par = course_par[str(i-1)][0]
            to_par = score - par
            if to_par < 0:
                color = "green"
            elif to_par == 0:
                color = "blue"
            elif to_par == 1:
                color = "yellow"
            else:
                color = "red"

            fill_color[i][j] = color
        a = 1

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
                        line_color="darkslategray",
                        fill_color="grey",
                        font=dict(color="white")
                        ),
            cells=dict(values=all_data.transpose(),
                       fill_color=fill_color
                       )
        )
        ])

    margins = dict(l=10, r=10, b=10, t=10, pad=0)
    fig.update_layout(
        autosize=True,
        margin=margins
    )

    return fig
