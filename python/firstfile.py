# asf
import os
import pandas


# Set path constants
PATH_TO_DATA = "..\\data\\GolfData.xlsx"
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


# Function to read in raw golf data
def read_golf_data(current, data_location, sheet):
    path = os.path.join(current, data_location)
    raw_golf_data = pandas.read_excel(path, sheet_name=sheet)
    return raw_golf_data


# Function to calculate "points"
def calculate_points(scorecards, course_pars):
    for card, _ in scorecards.iterrows():
        scorecard_data = scorecards.iloc[card]
        date_played = scorecard_data["Date"]
        course = scorecard_data["Course"]
        course_par = course_pars[course_pars["Course"] == course]

        for hole in GOLF_HOLES:
            hole_par = course_par[str(hole)]
            hole_score = scorecard_data[str(hole)]
            hole_score_to_par = hole_par - hole_score
            hole_points = 0

    total_points_placeholder = 0
    return total_points_placeholder


current_wd = os.getcwd()
course_handicaps = read_golf_data(current_wd, PATH_TO_DATA, HANDICAPS)
course_par_data = read_golf_data(current_wd, PATH_TO_DATA, COURSE_PAR)
scorecard_history = read_golf_data(current_wd, PATH_TO_DATA, SCORE_CARDS)


points = calculate_points(scorecard_history, course_par_data)
