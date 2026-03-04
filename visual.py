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