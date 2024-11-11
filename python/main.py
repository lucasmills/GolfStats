# Main script
import os

from python.constants import *
from python.plot import plot_golf_statistics
from python.utility import read_golf_data, collect_score_and_calculate_points


current_wd = os.getcwd()
course_handicaps = read_golf_data(current_wd, PATH_TO_DATA, HANDICAPS)
course_par_data = read_golf_data(current_wd, PATH_TO_DATA, COURSE_PAR)
scorecard_history = read_golf_data(current_wd, PATH_TO_DATA, SCORE_CARDS)

scores_and_points = collect_score_and_calculate_points(scorecard_history, course_par_data)
plot_golf_statistics(scores_and_points)
