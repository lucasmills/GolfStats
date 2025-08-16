# Script to house utility function for dash application

import numpy
from heapq import nsmallest


def calculate_handicap(scores, par_data):

    ordered_scores = scores.sort_values("Date", ascending=False)
    differentials = []
    num_rounds = len(ordered_scores)
    i = 1
    while i < 20:
        if i+1 > num_rounds:
            break

        data = ordered_scores.iloc[i, :]
        course = data["Course"]
        course_data = par_data[par_data["Course"] == course]
        rating = course_data["Rating"].iloc[0]
        slope = course_data["Slope"].iloc[0]
        score = data["Score"]

        differential = 113 / slope * (score - rating)
        differentials.append(differential)
        i = i + 1

    if len(differentials) <= 11:
        num_avg = 3
    elif len(differentials) <= 14:
        num_avg = 4
    elif len(differentials) <= 16:
        num_avg = 5
    elif len(differentials) <= 18:
        num_avg = 6
    elif len(differentials) <= 19:
        num_avg = 7
    else:
        num_avg = 8

    handicap = numpy.floor(numpy.mean(nsmallest(3, differentials)))
    return handicap
