"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""

import tui
import process
import visual

DATA_FILE = "data/disneyland_reviews.csv"

def handle_view_data(data, parks):
    tui.display_view_data_menu()
    choice = tui.get_menu_choice()
    tui.display_selected_choice(choice)

    if choice == "A":
        park = tui.get_park_choice(parks)
        reviews = process.get_reviews_by_park(data, park)
        tui.display_reviews(reviews, park)
    elif choice == "B":
        park = tui.get_park_choice(parks)
        location = tui.get_location_choice(data)
        count = process.get_reviews_count_by_park_and_location(data, park, location)
        tui.display_review_count(park, location, count)
    elif choice == "C":
        print("\nAverage Score per year by Park - coming soon\n")
    elif choice == "D":
        print("\nAverage Score per Park by Reviewer Location - coming soon\n")
    else:
        tui.display_invalid_choice()

def handle_visualise_data(data, parks):
    tui.display_visualise_menu()
    choice = tui.get_menu_choice()
    tui.display_selected_choice(choice)

    if choice == "A":
        print("\nMost reviewed Parks - coming soon\n")
    elif choice == "B":
        print("\nPark Ranking by Nationality - coming soon\n")
    elif choice == "C":
        print("\nMost Popular Month by Park \n")
    else:
        tui.display_invalid_choice()

def main():
    tui.display_title()
    data = process.load_data(DATA_FILE)
    parks = process.get_unique_parks(data)
    tui.display_loading_message(len(data))

    while True:
        tui.display_main_menu()
        choice = tui.get_menu_choice()

        tui.display_selected_choice(choice)

        if choice == "A":
            handle_view_data(data, parks)
        elif choice == "B":
            handle_visualise_data(data, parks)
        elif choice == "X":
            print("\nGoodbye!\n")
            break
        else:
            tui.display_invalid_choice()

if __name__ == "__main__":
    main()