# Plotting functions
import datetime
import matplotlib.pyplot as plt


DOT_SIZE = 150
GRID_ALPHA = 0.4


def plot_golf_statistics(golf_data):
    """

    :param golf_data:
    :return:
    """
    # Calculate axes limits
    date_delta_for_plotting = datetime.timedelta(days=14)
    date_of_first_round = min(golf_data["Date"])
    date_of_last_round = max(golf_data["Date"])

    x_limit = [date_of_first_round - date_delta_for_plotting,
               date_of_last_round + date_delta_for_plotting]

    fig = plt.figure(figsize=(18, 9))
    fig.suptitle("Luke's Golf Statistics")

    # Plot score
    fig = create_subplot(figure=fig, subplot_num=221, xdata=golf_data["Date"], ydata=golf_data["Score"],
                         label="Score", marker_color="C0", x_lim=x_limit, y_lim=[80, 120], x_ticks_on=False,
                         grid_alpha=GRID_ALPHA)

    # Plot points
    fig = create_subplot(figure=fig, subplot_num=222, xdata=golf_data["Date"], ydata=golf_data["Points"],
                         label="Points", marker_color="red", x_lim=x_limit, y_lim=[0, 25], x_ticks_on=False,
                         grid_alpha=GRID_ALPHA)

    # Plot fairways hit and greens in regulation
    fig = create_subplot(figure=fig, subplot_num=223, xdata=golf_data["Date"], ydata=golf_data["Fairways"],
                         label="Fairways hit", marker_color="purple", x_lim=x_limit, y_lim=[0, 8], x_ticks_on=True,
                         grid_alpha=GRID_ALPHA)

    fig = create_subplot(figure=fig, subplot_num=223, xdata=golf_data["Date"], ydata=golf_data["GIR"],
                         label="Greens in regulation", marker_color="orange", x_lim=x_limit, y_lim=[0, 8],
                         x_ticks_on=True, grid_alpha=GRID_ALPHA)

    # Plot putts
    fig = create_subplot(figure=fig, subplot_num=224, xdata=golf_data["Date"], ydata=golf_data["Putts"],
                         label="Number of putts",  marker_color="green", x_lim=x_limit, y_lim=[20, 50], x_ticks_on=True,
                         grid_alpha=GRID_ALPHA)

    plt.show()


def create_subplot(figure, subplot_num, xdata, ydata, label, marker_color, x_lim, y_lim, x_ticks_on, grid_alpha):
    """

    :param figure:
    :param subplot_num:
    :param xdata:
    :param ydata:
    :param label:
    :param marker_color:
    :param x_lim:
    :param y_lim:
    :param x_ticks_on:
    :param grid_alpha:
    :return:
    """
    # Plot overall score
    plt.subplot(subplot_num)
    plt.scatter(xdata, ydata, label=label, s=DOT_SIZE, facecolor=marker_color, edgecolor='k')

    # Set axis limits
    plt.xlim(x_lim)
    plt.ylim(y_lim)

    # Remove tick params
    if not x_ticks_on:
        plt.tick_params(
            axis='x',  # changes apply to the x-axis
            which='both',  # both major and minor ticks are affected
            bottom=False,  # ticks along the bottom edge are off
            top=False,  # ticks along the top edge are off
            labelbottom=False)  # labels along the bottom edge are off
    else:
        plt.xticks(rotation=45)

    # Add a grid and tighten the layout
    plt.grid(alpha=grid_alpha)
    plt.legend()
    plt.tight_layout()

    return figure
