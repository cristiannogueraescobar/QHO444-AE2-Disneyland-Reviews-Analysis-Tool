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
def get_average_rating_by_park_and_year(data, park, year):
    ratings = [
        row["Rating"] for row in data
        if row["Branch"] == park
        and row["Year_Month"].startswith(year)
    ]
    if not ratings:
        return None
    return sum(ratings) / len(ratings)

def get_review_count_by_park(data):
    counts = {}
    for row in data:
        park = row["Branch"]
        counts[park] = counts.get(park, 0) + 1
    return counts

def get_top_locations_by_average_rating(data, park, top_n=10):

    park_data = [row for row in data if row["Branch"] == park]
    location_totals = {}
    location_counts = {}

    for row in park_data:
        loc = row["Reviewer_Location"]
        location_totals[loc] = location_totals.get(loc, 0) + row["Rating"]
        location_counts[loc] = location_counts.get(loc, 0) + 1

    averages = {
        loc : location_totals[loc] / location_counts[loc]
        for loc in location_totals
    }
    sorted_locs = sorted(averages.items(), key=lambda x: x[1], reverse=True)
    top_10_by_count = sorted(
        [(loc, avg, location_counts[loc]) for loc, avg in averages.items()],
        key=lambda x: x[2], reverse=True
    )
    return top_10_by_count[:top_n]
