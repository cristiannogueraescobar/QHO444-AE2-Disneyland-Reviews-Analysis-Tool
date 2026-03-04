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
            print("\nView Data - coming soon\n")
        elif choice == "B":
            print("\nVisualise Data - coming soon\n")
        elif choice == "X":
            print("\nGoodbye!\n")
            break
        else:
            tui.display_invalid_choice()

if __name__ == "__main__":
    main()

