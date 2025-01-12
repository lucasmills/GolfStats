# Main script
import os
import pickle

from data_collection.constants import *
from data_collection.data_collection_utility import read_golf_data, \
    collect_score_and_calculate_points


print("Record and shot performance on each of the Par types")
current_wd = os.getcwd()
course_handicaps = read_golf_data(current_wd, PATH_TO_DATA, HANDICAPS)
course_par_data = read_golf_data(current_wd, PATH_TO_DATA, COURSE_PAR)
scorecard_history = read_golf_data(current_wd, PATH_TO_DATA, SCORE_CARDS)

scores_and_points = collect_score_and_calculate_points(scorecard_history,
                                                       course_par_data)

# Pickle the data
db_file = open("data\\golf_data.pkl", 'ab')

# source, destination
pickle.dump(scores_and_points, db_file)
db_file.close()
