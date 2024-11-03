# asf
import datetime
import matplotlib.pyplot as plt
import os
import pandas


# Set path constants
PATH_TO_DATA = "data\\GolfData.xlsx"
SCORE_CARDS = "Score Cards"
HANDICAPS = "Course Handicaps"
COURSE_PAR = "Course Pars"

# Set base golf data
# TODO: This can be an enum
GOLF_HOLES = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)

# Set golf score constants
EAGLE = -2
BIRDIE = -1
PAR = 0
BOGEY = 1
DOUBLE_BOGEY = 2
TRIPLE_BOGEY = 3
QUADRUPLE_BOGEY = 4

GOLF_SCORES_FOR_POINTS = (EAGLE, BIRDIE, PAR, BOGEY)
POINTS_PER_SCORE = (4, 3, 2, 1)


# Function to read in raw golf data
def read_golf_data(current, data_location, sheet):
    path = os.path.join(current, data_location)
    raw_golf_data = pandas.read_excel(path, sheet_name=sheet)
    return raw_golf_data


# Function to calculate "points"
def calculate_points(scorecards, course_pars):
    points_history = pandas.DataFrame(columns=["Date", "Course", "Points"])

    for card, _ in scorecards.iterrows():
        scorecard_data = scorecards.iloc[card]
        date_played = scorecard_data["Date"]
        course = scorecard_data["Course"]
        course_par = course_pars[course_pars["Course"] == course]
        total_score_for_round = 0

        for hole in GOLF_HOLES:
            hole_par = course_par[str(hole)]
            hole_score = scorecard_data[str(hole)]
            hole_score_to_par = hole_score - hole_par

            try:
                hole_score_type = GOLF_SCORES_FOR_POINTS.index(hole_score_to_par[0])
                hole_points = POINTS_PER_SCORE[hole_score_type]
            except ValueError:
                hole_points = 0

            total_score_for_round += hole_points

        round_points = pandas.DataFrame({"Date": [date_played],
                                         "Course": [course],
                                         "Points": [total_score_for_round]})

        points_history = points_history.append(round_points)

    return points_history


current_wd = os.getcwd()
course_handicaps = read_golf_data(current_wd, PATH_TO_DATA, HANDICAPS)
course_par_data = read_golf_data(current_wd, PATH_TO_DATA, COURSE_PAR)
scorecard_history = read_golf_data(current_wd, PATH_TO_DATA, SCORE_CARDS)

points = calculate_points(scorecard_history, course_par_data)

date_delta_for_plotting = datetime.timedelta(days=14)
date_of_first_round = min(points["Date"])
date_of_last_round = max(points["Date"])

fig, ax = plt.subplots()
ax.scatter(points["Date"], points["Points"], label=points["Course"])

ax.legend()
ax.grid(True)

ax.set_xlim([date_of_first_round - date_delta_for_plotting,
             date_of_last_round + date_delta_for_plotting])
ax.set_ylim([0, 25])

plt.xticks(rotation=45)

plt.xlabel("Date of Round")
plt.ylabel("Points Earned")
plt.title("Golf Points History")

plt.tight_layout()
plt.show()
