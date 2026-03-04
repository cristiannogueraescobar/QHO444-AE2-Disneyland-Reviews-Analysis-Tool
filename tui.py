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
    print("          MENU          ")
    print("-" * 50)
    print("\nPlease select an option from the menu.\n")
    print("[A] View Data\n")
    print("[B] Visualise Data\n")
    print("[X] Exit\n")

def get_menu_choice():
    return input("\nEnter your choice: .\n").strip().upper()

def display_selected_choice(choice):
    print("-" * 50)
    print(f"\nYou selected {choice}\n")

def display_invalid_choice():
    print("\nInvalid choice. Please try again.\n")

def display_view_data_menu():
    print("\nPlease select an option from the menu.\n")
    print("[A] View Reviews by Park\n")
    print("[B] Number of Reviews by Park and Location\n")
    print("[C] Average Rating by Park and Year\n")
    print("[D] Average Score per Park by Reviewer Location\n")

def display_visualise_menu():
    print("\nPlease select an option from the menu.\n")
    print("[A] Most Reviewed Parks\n")
    print("[B] Park Ranking by Nationality\n")
    print("[C] Most Popular Month by Park\n")

def get_park_choice(parks):
    print("\nAvailable parks: .\n")
    for i, park in enumerate(parks, 1):
        print(f"   {i}. {park}")
    while True:
        choice = input("\nEnter your choice: .\n").strip()
        if choice in parks:
            return choice
        print("\nInvalid choice. Please try again.\n")

def display_reviews(reviews, park):
    print(f"\n---Park Reviews for {park} ({len(reviews)} total)---.\n")
    if not reviews:
        print("\nNo Reviews Available.\n")
        return
    for review in reviews:
        print(
            f" Rating: {review['Rating']} " 
            f" Date: {review['Year_Month']} "
            f" Location: {review['Reviewer_Location']} "
        )


def get_location_choice(data):
    locations = sorted(set(
        row['Reviewer_Location'] for row in data
        if row['Reviewer_Location']

    ))

    print("\nAvailable locations:\n")
    for loc in locations:
        print(f" - {loc}")
    print()
    return input("\nEnter reviewer location: .").strip()

def display_review_count(park, location, count):
    print(f"\nReviews for {park} from {location}: {count}\n")


