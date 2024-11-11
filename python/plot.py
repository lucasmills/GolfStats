# Plotting functions
import datetime
import matplotlib.pyplot as plt

DOT_SIZE = 150


def plot_golf_statistics(golf_data):
    # Calculate axes limits
    date_delta_for_plotting = datetime.timedelta(days=14)
    date_of_first_round = min(golf_data["Date"])
    date_of_last_round = max(golf_data["Date"])

    fig = plt.figure(figsize=(18, 9))
    fig.suptitle("Luke's Golf Statistics")

    # Plot overall score
    plt.subplot(221)
    plt.scatter(golf_data["Date"], golf_data["Score"], label="Score",
                s=DOT_SIZE, facecolor='C0', edgecolor='k')

    # Set axis limits
    plt.xlim([date_of_first_round - date_delta_for_plotting,
              date_of_last_round + date_delta_for_plotting])
    plt.ylim([80, 120])

    # Remove tick params
    plt.tick_params(
        axis='x',           # changes apply to the x-axis
        which='both',       # both major and minor ticks are affected
        bottom=False,       # ticks along the bottom edge are off
        top=False,          # ticks along the top edge are off
        labelbottom=False)  # labels along the bottom edge are off

    # Set axis labels
    plt.title("Golf Score History")

    # Add a grid and tighten the layout
    plt.grid(alpha=0.4)
    plt.legend()
    plt.tight_layout()

    # Plot "points"
    plt.subplot(222)
    plt.scatter(golf_data["Date"], golf_data["Points"], label="Points",
                s=DOT_SIZE, facecolor='red', edgecolor='k')

    # Set axis limits
    plt.xlim([date_of_first_round - date_delta_for_plotting,
              date_of_last_round + date_delta_for_plotting])
    plt.ylim([0, 25])

    plt.legend()

    # Remove X tick params
    plt.tick_params(
        axis='x',           # changes apply to the x-axis
        which='both',       # both major and minor ticks are affected
        bottom=False,       # ticks along the bottom edge are off
        top=False,          # ticks along the top edge are off
        labelbottom=False)  # labels along the bottom edge are off

    plt.grid(alpha=0.4)

    # Set labels and title

    plt.tight_layout()

    # PLOT SCORE
    plt.subplot(223)
    plt.scatter(golf_data["Date"], golf_data["Fairways"], label="Fairways hit",
                s=DOT_SIZE, facecolor='purple', edgecolor='k')
    plt.scatter(golf_data["Date"], golf_data["GIR"], label="Greens in regulation",
                s=DOT_SIZE, facecolor='orange', edgecolor='k')

    # Set axis limits
    plt.xlim([date_of_first_round - date_delta_for_plotting,
              date_of_last_round + date_delta_for_plotting])
    plt.ylim([0, 8])

    plt.xticks(rotation=45)
    plt.legend()

    # Set labels and title
    plt.xlabel("Date of Round")

    plt.grid(alpha=0.4)
    plt.tight_layout()

    # Plot number of putts
    plt.subplot(224)
    plt.scatter(golf_data["Date"], golf_data["Putts"], label="Number of putts",
                s=DOT_SIZE, facecolor='green', edgecolor='k')

    # Set axis limits
    plt.xlim([date_of_first_round - date_delta_for_plotting,
              date_of_last_round + date_delta_for_plotting])
    plt.ylim([20, 50])

    plt.xticks(rotation=45)
    plt.grid(alpha=0.4)

    # Set labels and title
    plt.xlabel("Date of Round")

    plt.legend()
    plt.tight_layout()

    plt.show()
