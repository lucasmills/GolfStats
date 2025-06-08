
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
                  "   BSOB   ",
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

    bsob_axes = np.linspace(data["BetterSideOfBogey"].min(),
                            data["BetterSideOfBogey"].max(),
                            num=5)

    category_axes = {
        "   Score   ": score_axes,
        "   Fairways   ": fairways_axes,
        "   GIR   ": gir_axes,
        "   Putts   ": putts_axes,
        "   BSOB   ": bsob_axes
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

    scaled_mean_bsob = scale_value(value=data["BetterSideOfBogey"].mean(),
                                   orig_min=data["BetterSideOfBogey"].min(),
                                   orig_max=data["BetterSideOfBogey"].max(),
                                   new_min=20,
                                   new_max=100)

    average_values = [scaled_mean_fairways,
                      scaled_mean_score,
                      scaled_mean_gir,
                      scaled_mean_putts,
                      scaled_mean_bsob,
                      scaled_mean_fairways]

    # BEST ROUND
    min_value = data["Score"].min()
    data_for_best_score = data[data["Score"] == min_value]

    scaled_best_score = scale_value(value=data_for_best_score["Score"][0],
                                    orig_min=data["Score"].min(),
                                    orig_max=data["Score"].max(),
                                    new_min=100,
                                    new_max=20)

    scaled_best_fairways = scale_value(value=data_for_best_score["Fairways"][0],
                                       orig_min=data["Fairways"].min(),
                                       orig_max=data["Fairways"].max(),
                                       new_min=20,
                                       new_max=100)

    scaled_best_gir = scale_value(value=data_for_best_score["GIR"][0],
                                  orig_min=data["GIR"].min(),
                                  orig_max=data["GIR"].max(),
                                  new_min=20,
                                  new_max=100)

    scaled_best_putts = scale_value(value=data_for_best_score["Putts"][0],
                                    orig_min=data["Putts"].min(),
                                    orig_max=data["Putts"].max(),
                                    new_min=100,
                                    new_max=20)

    scaled_best_bsob = scale_value(value=data_for_best_score["BetterSideOfBogey"][0],
                                   orig_min=data["BetterSideOfBogey"].min(),
                                   orig_max=data["BetterSideOfBogey"].max(),
                                   new_min=20,
                                   new_max=100)

    best_data = [scaled_best_fairways,
                 scaled_best_score,
                 scaled_best_gir,
                 scaled_best_putts,
                 scaled_best_bsob,
                 scaled_best_fairways]

    best_date = data_for_best_score["Date"][0]
    best_date_string = best_date.strftime("%Y-%B-%d")

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

    scaled_latest_bsob = scale_value(value=data["BetterSideOfBogey"].iloc[-1],
                                     orig_min=data["BetterSideOfBogey"].min(),
                                     orig_max=data["BetterSideOfBogey"].max(),
                                     new_min=20,
                                     new_max=100)

    latest_data = [scaled_latest_fairways,
                   scaled_latest_score,
                   scaled_latest_gir,
                   scaled_latest_putts,
                   scaled_latest_bsob,
                   scaled_latest_fairways]

    latest_date = data["Date"].iloc[-1]
    latest_date_string = latest_date.strftime("%Y-%B-%d")

    # Create the figure
    fig = go.Figure()

    # Plot the latest round
    fig.add_trace(go.Scatterpolar(
        r=latest_data,
        theta=categories,
        fill="toself",
        line=dict(color='darkblue', width=2),  # Change line color and width
        marker=dict(color='blue', size=8),  # Change marker color
        name="Latest (" + latest_date_string + ")",
        fillcolor="rgba(173, 216, 230, 0.25)"
    ))

    # Plot the averages
    fig.add_trace(go.Scatterpolar(
        r=average_values,
        theta=categories,
        fill="toself",
        line=dict(color='black', width=2),  # Change line color and width
        marker=dict(color='black', size=8),  # Change marker color
        name="Average",
        fillcolor="rgba(128, 128, 128, 0.175)"
    ))

    # Plot the best round
    fig.add_trace(go.Scatterpolar(
        r=best_data,
        theta=categories,
        fill="toself",
        line=dict(color='darkgreen', width=2),  # Change line color and width
        marker=dict(color='green', size=8),  # Change marker color
        name="Best (" + best_date_string + ")",
        fillcolor="rgba(144, 238, 144, 0.25)",
        visible="legendonly"
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
