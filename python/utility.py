# asf
import os
import pandas

from python.constants import *


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
    golf_history = pandas.DataFrame(columns=["Date", "Course", "Score", "Points"])

    for card, _ in scorecards.iterrows():
        scorecard_data = scorecards.iloc[card]
        date_played = scorecard_data["Date"]
        course = scorecard_data["Course"]
        course_par = course_pars[course_pars["Course"] == course]
        total_score_for_round = 0

        total_to_par_for_round = 0
        total_points_for_round = 0

        for hole in GOLF_HOLES:
            hole_par = course_par[str(hole)]
            hole_score = scorecard_data[str(hole)]
            hole_score_to_par = hole_score - hole_par

            total_score_for_round += hole_score
            total_to_par_for_round += hole_score_to_par

            try:
                hole_score_type = GOLF_SCORES_FOR_POINTS.index(hole_score_to_par[0])
                hole_points = POINTS_PER_SCORE[hole_score_type]
            except ValueError:
                hole_points = 0

            total_points_for_round += hole_points

        round_points = pandas.DataFrame({"Date": [date_played],
                                         "Course": [course],
                                         "Score": [total_score_for_round],
                                         "Points": [total_points_for_round]})

        golf_history = pandas.concat([golf_history, round_points])

    return golf_history
