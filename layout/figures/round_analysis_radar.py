
# Generator
import numpy as np
import plotly.graph_objects as go

from utils.scale_values import scale_value


def generate_round_analysis_radar(data):
    # Categories to plot
    categories = ["   Fairways   ",
                  "   Score   ",
                  "   GIR   ",
                  "   Putts   ",
                  "   Skill   ",
                  "   Fairways   "]

    # Radius values to label
    reference_levels = [20, 40, 60, 80, 100]

    # Get axes tick mark labels
    score_axes = np.linspace(data["Score"].max(),
                             data["Score"].min(),
                             num=5)

    fairways_axes = np.linspace(data["Fairways"].min(),
                                data["Fairways"].max(),
                                num=5)

    gir_axes = np.linspace(data["GIR"].min(),
                           data["GIR"].max(),
                           num=5)

    putts_axes = np.linspace(data["Putts"].max(),
                             data["Putts"].min(),
                             num=5)

    other_axes = np.linspace(0, 100, num=5)

    category_axes = {
        "   Score   ": score_axes,
        "   Fairways   ": fairways_axes,
        "   GIR   ": gir_axes,
        "   Putts   ": putts_axes,
        "   Skill   ": other_axes
    }

    # AVERAGES
    # Values to plot
    scaled_mean_score = scale_value(value=data["Score"].mean(),
                                    orig_min=data["Score"].min(),
                                    orig_max=data["Score"].max(),
                                    new_min=100,
                                    new_max=20)

    scaled_mean_fairways = scale_value(value=data["Fairways"].mean(),
                                       orig_min=data["Fairways"].min(),
                                       orig_max=data["Fairways"].max(),
                                       new_min=20,
                                       new_max=100)

    scaled_mean_gir = scale_value(value=data["GIR"].mean(),
                                  orig_min=data["GIR"].min(),
                                  orig_max=data["GIR"].max(),
                                  new_min=20,
                                  new_max=100)

    scaled_mean_putts = scale_value(value=data["Putts"].mean(),
                                    orig_min=data["Putts"].min(),
                                    orig_max=data["Putts"].max(),
                                    new_min=100,
                                    new_max=20)

    average_values = [scaled_mean_fairways,
                      scaled_mean_score,
                      scaled_mean_gir,
                      scaled_mean_putts,
                      80,
                      scaled_mean_fairways]

    # MOST RECENT ROUND
    # Values to plot
    scaled_latest_score = scale_value(value=data["Score"].iloc[-1],
                                      orig_min=data["Score"].min(),
                                      orig_max=data["Score"].max(),
                                      new_min=100,
                                      new_max=20)

    scaled_latest_fairways = scale_value(value=data["Fairways"].iloc[-1],
                                         orig_min=data["Fairways"].min(),
                                         orig_max=data["Fairways"].max(),
                                         new_min=20,
                                         new_max=100)

    scaled_latest_gir = scale_value(value=data["GIR"].iloc[-1],
                                    orig_min=data["GIR"].min(),
                                    orig_max=data["GIR"].max(),
                                    new_min=20,
                                    new_max=100)

    scaled_latest_putts = scale_value(value=data["Putts"].iloc[-1],
                                      orig_min=data["Putts"].min(),
                                      orig_max=data["Putts"].max(),
                                      new_min=100,
                                      new_max=20)

    latest_data = [scaled_latest_fairways,
                   scaled_latest_score,
                   scaled_latest_gir,
                   scaled_latest_putts,
                   80,
                   scaled_latest_fairways]

    latest_date = data["Date"].iloc[-1]
    latest_date_string = latest_date.strftime("%Y-%B-%d")

    # Create the figure
    fig = go.Figure()

    # Plot the averages
    fig.add_trace(go.Scatterpolar(
        r=average_values,
        theta=categories,
        fill="toself",
        name="Average",
        fillcolor="rgba(173, 216, 230, 0.25)"
    ))

    # Plot the latest round
    fig.add_trace(go.Scatterpolar(
        r=latest_data,
        theta=categories,
        fill="toself",
        line=dict(color='darkgreen', width=2),  # Change line color and width
        marker=dict(color='green', size=8),  # Change marker color
        name=latest_date_string,
        fillcolor="rgba(144, 238, 144, 0.25)"
    ))

    # Ensure each axis has its reference levels **without duplication**
    for idx, category in enumerate(categories):
        reference_level = category_axes[category]
        for i in range(0, len(reference_levels)):
            r = reference_levels[i]
            fig.add_trace(go.Scatterpolar(
                r=[r],
                theta=[category],
                mode='text',
                textfont=dict(size=18),
                text=[str(reference_level[i])],  # Show only the numerical value
                textposition="middle center",
                showlegend=False
            ))

            fig.update_layout(
                polar=dict(
                    angularaxis=dict(
                        tickfont=dict(size=22)
                    ),

                    radialaxis=dict(
                        dict(
                            showticklabels=False
                        ),
                        visible=True,
                        range=[0, 100]
                    )
                ),

                legend=dict(
                    orientation="h",
                    yanchor="top",
                    y=1.1,
                    font=dict(size=18)
                ),
                showlegend=True
            )

    return fig
