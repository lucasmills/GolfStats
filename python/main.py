# asf
import datetime
import matplotlib.pyplot as plt
import os


from python.constants import *
from python.utility import read_golf_data, collect_score_and_calculate_points


current_wd = os.getcwd()
course_handicaps = read_golf_data(current_wd, PATH_TO_DATA, HANDICAPS)
course_par_data = read_golf_data(current_wd, PATH_TO_DATA, COURSE_PAR)
scorecard_history = read_golf_data(current_wd, PATH_TO_DATA, SCORE_CARDS)

scores_and_points = collect_score_and_calculate_points(scorecard_history, course_par_data)

date_delta_for_plotting = datetime.timedelta(days=14)
date_of_first_round = min(scores_and_points["Date"])
date_of_last_round = max(scores_and_points["Date"])


# PLOT POINTS
fig, ax = plt.subplots()
ax.scatter(scores_and_points["Date"], scores_and_points["Points"], label=scores_and_points["Course"])

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


# PLOT SCORE
fig, ax = plt.subplots()
ax.scatter(scores_and_points["Date"], scores_and_points["Score"], label=scores_and_points["Course"])

ax.legend()
ax.grid(True)

ax.set_xlim([date_of_first_round - date_delta_for_plotting,
             date_of_last_round + date_delta_for_plotting])

plt.xticks(rotation=45)

plt.xlabel("Date of Round")
plt.ylabel("Score Earned")
plt.title("Golf Score History")

plt.tight_layout()
plt.show()
