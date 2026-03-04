"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""

import matplotlib.pyplot as plt

def show_pie_chart_reviews_per_park(park_counts):

    labels = list(park_counts.keys())
    sizes = list(park_counts.values())

    fig, ax = plt.subplots(figsize=(9,6))

    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)

    ax.set_title("Number of reviews per Disneyland park",
                 fontsize=14, fontweight="bold")

    plt.tight_layout()
    plt.show()

def show_bar_chart_top_locations(top_locations, park):

    locations = [item[0] for item in top_locations]
    averages = [item[1] for item in top_locations]
    counts = [item[2] for item in top_locations]

    fig, ax = plt.subplots(figsize=(12,6))

    bars = ax.bar(locations, averages, color="steelblue", edgecolor="black")
    ax.set_title("Top 10 locations by Rating of Disneyland park",
                 fontsize=14, fontweight="bold")
    ax.set_xlabel("Reviewer Locations", fontsize=12)
    ax.set_ylabel("Average Rating (out of 5)", fontsize=12)
    ax.tick_params(axis="x", rotation=45)

    for bar, avg, count in zip(bars, averages, counts):
        ax.text(bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.05,
        f"{avg:.2f}", ha="center", va="bottom", fontsize=9)
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() / 2,
                f"n={count}", ha="center", va="bottom", fontsize=8, color="white")

    plt.tight_layout()
    plt.show()