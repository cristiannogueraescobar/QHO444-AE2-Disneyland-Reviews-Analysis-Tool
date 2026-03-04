"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""
def display_title():
    print("-" * 50)
    print("          DISNEYLAND REVIEWS ANALYSIS TOOL          ")
    print("-" * 50)

def display_loading_message(row_count):
    print(f"\nLoading Data...\n")
    print(f"{row_count} reviews found.\n")

def display_main_menu():
    print("-" * 50)
    print("\n          MENU          \n")
    print("-" * 50)
    print("\nPlease select an option from the menu.\n")
    print("[A] View Data\n")
    print("[B] Visualise Data\n")
    print("[C] Exit\n")

def get_menu_choice():
    return input("\nEnter your choice: .\n").strip().upper()

def display_selected_choice(choice):
    print("-" * 50)
    print(f"\nYou selected {choice}\n")

def display_invalid_choice():
    print("\nInvalid choice. Please try again.\n")

