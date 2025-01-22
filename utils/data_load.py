# Function to load in data

import pandas


def load_data_util(path):
    try:
        with open(path, "rb") as f:
            golf_data = pandas.read_pickle(f)
    except FileNotFoundError:
        web_path = "/home/millsgolfstats/GolfStats/" + path
        with open(web_path, "rb") as f:
            golf_data = pandas.read_pickle(f)

    return golf_data

