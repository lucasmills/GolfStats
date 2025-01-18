# Utility functions
import datetime
import os
import pandas

from data_collection.constants import *


# Function to read in raw golf data
def read_golf_data(current, data_location, sheet):
    path = os.path.join(current, data_location)
    raw_golf_data = pandas.read_excel(path, sheet_name=sheet)
    return raw_golf_data


def collect_score_and_calculate_points(scorecards, course_pars):
    """
    Description of function
    :param scorecards:
    :param course_pars:
    :return:
    """

    # Comment
    golf_history = pandas.DataFrame(columns=["Date", "Course", "Score",
                                             "Points", "Fairways", "GIR",
                                             "Putts", "Birdies", "Pars",
                                             "Bogeys", "Doubles+"])

    # Comment
    for card, _ in scorecards.iterrows():
        # Comment
        scorecard_data = scorecards.iloc[card]
        fairways_hit = scorecard_data["Fairways"]
        greens_reached_in_regulation = scorecard_data["GIR"]
        number_of_putts = scorecard_data["Putts"]

        date_played = scorecard_data["Date"]
        course = scorecard_data["Course"]
        course_par = course_pars[course_pars["Course"] == course]

        course_par_score = course_par.sum(axis=1, numeric_only=True)
        # Comment
        total_score_for_round = 0
        total_to_par_for_round = 0
        total_points_for_round = 0

        total_birdies_for_round = 0
        total_pars_for_round = 0
        total_bogeys_for_round = 0
        total_doubles_plus_per_round = 0

        # Comment
        for hole in GOLF_HOLES:
            hole_par = course_par[str(hole)]
            hole_score = scorecard_data[str(hole)]
            hole_score_to_par = hole_score - hole_par

            total_score_for_round += hole_score
            total_to_par_for_round += hole_score_to_par

            # Comment
            try:
                hole_score_type = GOLF_SCORES_FOR_POINTS.index(
                    hole_score_to_par[0])
                hole_points = POINTS_PER_SCORE[hole_score_type]
            except ValueError:
                hole_points = 0

            total_points_for_round += hole_points

            if hole_points == 3:
                total_birdies_for_round += 1
            elif hole_points == 2:
                total_pars_for_round += 1
            elif hole_points == 1:
                total_bogeys_for_round += 1
            elif hole_points == 0:
                total_doubles_plus_per_round += 1

        # Comment
        round_score = \
            pandas.DataFrame({"Date": [date_played],
                              "Course": [course],
                              "Score": [total_score_for_round],
                              "Score to par": [total_to_par_for_round],
                              "Points": [total_points_for_round],
                              "Fairways": [fairways_hit],
                              "GIR": [greens_reached_in_regulation],
                              "Putts": [number_of_putts],
                              "Birdies": [total_birdies_for_round],
                              "Pars": [total_pars_for_round],
                              "Bogeys": [total_bogeys_for_round],
                              "Doubles+": [total_doubles_plus_per_round]})

        # Comment
        golf_history = pandas.concat([golf_history, round_score])

    return golf_history
