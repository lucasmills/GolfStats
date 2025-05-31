
# Generator
import numpy as np
import plotly.graph_objects as go


def generate_round_analysis_radar(data):
    categories = ["Score", "Fairways", "GIR", "Putts", 'Skill']
    values = [90, 70, 85, 95, 80]
    reference_levels = [20, 40, 60, 80, 100]  # Radius values to label

    values.append(values[0])  # Repeat the first value at the end
    categories.append(categories[0])

    # Get axes tick mark labels
    score_axes = np.linspace(data["Score"].min(),
                             data["Score"].max(),
                             num=5)
    fairways_axes = np.linspace(data["Fairways"].min(),
                                data["Fairways"].max(),
                                num=5)

    gir_axes = np.linspace(data["GIR"].min(),
                           data["GIR"].max(),
                           num=5)

    putts_axes = np.linspace(data["Putts"].min(),
                             data["Putts"].max(),
                             num=5)

    other_axes = np.linspace(0, 100, num=5)

    category_axes = {
        "Score": score_axes,
        "Fairways": fairways_axes,
        "GIR": gir_axes,
        "Putts": putts_axes,
        "Skill": other_axes
    }

    fig = go.Figure()

    # Main radar chart
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill="toself",
        name="Player Stats",
        fillcolor="rgba(173, 216, 230, 0.25)"
    ))

    # Ensure each axis has its reference levels **without duplication**
    for idx, category in enumerate(categories):
        reference_level = category_axes[category]
        for i in range(0, len(reference_levels)-1):
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
                    radialaxis=dict(
                        dict(showticklabels=False),
                        visible=True,
                        range=[0, 100]
                    )
                ),
                showlegend=True
            )

    return fig


# import numpy as np
# import plotly.graph_objects as go
# categories = ['Speed', 'Agility', 'Strength', 'Stamina', 'Skill']
# values = [90, 70, 85, 95, 80]
# reference_levels = [20, 40, 60, 80, 100]  # Radius values to label
#
# values.append(values[0])  # Repeat the first value at the end
# categories.append(categories[0])
#
# fig = go.Figure()
#
# # Main radar chart
# fig.add_trace(go.Scatterpolar(
#     r=values,
#     theta=categories,
#     fill="toself",
#     name="Player Stats",
#     fillcolor="rgba(173, 216, 230, 0.25)"
# ))
#
# # Ensure each axis has its reference levels **without duplication**
# for idx, category in enumerate(categories):
#     for level in reference_levels:
#         if level < values[idx]:  # Ensure we don't label values beyond the actual data point
#             fig.add_trace(go.Scatterpolar(
#                 r=[level],
#                 theta=[category],
#                 mode='text',
#                 textfont=dict(size=20),
#                 text=[str(level)],  # Show only the numerical value
#                 textposition="middle center",
#                 showlegend=False
#             ))
#
#     fig.update_layout(
#         polar=dict(
#             radialaxis=dict(
#                 dict(showticklabels=False),
#                 visible=True,
#                 range=[0, 100]
#             )
#         ),
#         showlegend=True
#     )
#
# fig.show()
