
# Generator
import plotly.graph_objects as go


def generate_round_analysis_radar():
    categories = ['Speed', 'Agility', 'Strength', 'Stamina', 'Skill']
    values = [90, 70, 85, 95, 80]
    reference_levels = [20, 40, 60, 80, 100]  # Radius values to label

    values.append(values[0])  # Repeat the first value at the end
    categories.append(categories[0])

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
        for level in reference_levels:
            if level < values[idx]:  # Ensure we don't label values beyond the actual data point
                fig.add_trace(go.Scatterpolar(
                    r=[level],
                    theta=[category],
                    mode='text',
                    textfont=dict(size=20),
                    text=[str(level)],  # Show only the numerical value
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
