#
import pandas
from plotly import graph_objects as go


# Generator
def generate_scorecard_table(all_data, par_data, margins):
    all_data = all_data.sort_values("Date", ascending=False)

    num_lists = 20
    per_list = all_data.shape[0]

    # Creating the list of lists
    fill_color = [[f"lightgrey" for i in range(per_list)] for _ in range(num_lists)]

    for i in range(0, len(fill_color)):
        if i < 2:
            continue

        for j in range(0, len(fill_color[i])):
            course = all_data.iloc[j]["Course"]
            score = all_data.iloc[j][str(i-1)]
            fill = par_data["Course"] == course
            course_par = par_data[fill]
            par = course_par[str(i-1)][0]
            to_par = score - par
            if to_par < 0:
                color = "lightgreen"
            elif to_par == 0:
                color = "skyblue"
            elif to_par == 1:
                color = "khaki"
            else:
                color = "lightcoral"

            fill_color[i][j] = color

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
                       fill_color=fill_color,
                       line_color="darkslategray"
                       )
        )
        ])

    margins = dict(l=10, r=10, b=10, t=10, pad=0)
    fig.update_layout(
        autosize=True,
        margin=margins
    )

    return fig
