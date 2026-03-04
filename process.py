"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""
import csv

def load_data(filepath):
    data = []
    with open(filepath, encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["Rating"] = int(row["Rating"])
            data.append(row)
    return data

def get_unique_parks(data):

    return sorted(set(row["Branch"] for row in data))

def get_reviews_by_park(data, park):

    return [row for row in data if row["Branch"] == park]

def get_reviews_count_by_park_and_location(data, park, location):

    return sum(
        1 for row in data
        if row["Branch"] == park
        and row["Reviewer_Location"] == location
    )