# asf
import os
import pandas


# Set path constants
PATH_TO_DATA = "..\\data\\GolfData.xlsx"
SCORE_CARDS = "Score Cards"
HANDICAPS = "Course Handicaps"
PAR = "Course Pars"


# Function to read in golf data
def read_golf_data(current, data_location, sheet):
    path = os.path.join(current, data_location)
    raw_golf_data = pandas.read_excel(path, sheet_name=sheet)
    return raw_golf_data


current_wd = os.getcwd()
course_handicaps = read_golf_data(current_wd, PATH_TO_DATA, HANDICAPS)
course_pars = read_golf_data(current_wd, PATH_TO_DATA, PAR)
scores = read_golf_data(current_wd, PATH_TO_DATA, SCORE_CARDS)
