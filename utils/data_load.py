# Function to load in data

import pandas


def load_data_util(path, web=True):
    if web:
        path = "/home/millsgolfstats/GolfStats/" + path
    # Load golf data
    with open(path, "rb") as f:
        golf_data = pandas.read_pickle(f)

    return golf_data

