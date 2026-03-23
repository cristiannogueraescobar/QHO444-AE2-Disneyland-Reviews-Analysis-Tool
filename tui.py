
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
    print("\nPlease select an option from the menu\n")
    print("[A] View Data\n")
    print("[B] Visualise Data\n")
    print("[C] Export Data\n")
    print("[X] Exit\n")

def get_menu_choice():
    return input("\nEnter your choice: \n").strip().upper()

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
    print("[X] Back to Main Menu\n")

def display_visualise_menu():
    print("\nPlease select an option from the menu.\n")
    print("[A] Most Reviewed Parks\n")
    print("[B] Park Ranking by Nationality\n")
    print("[C] Most Popular Month by Park\n")
    print("[X] Back to Main Menu\n")

def get_park_choice(parks):
    print("\nAvailable parks: \n")
    for i, park in enumerate(parks, 1):
        print(f"   {i}. {park.replace('_', ' ')}")
    while True:
        choice = input("\nEnter your choice (number or name): ").strip()
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(parks):
                return parks[idx - 1]
        if choice.replace(" ", "_") in parks:
            return choice.replace(" ", "_")
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
    return input("\nEnter reviewer location: ").strip()

def display_review_count(park, location, count):
    print(f"\nReviews for {park} from {location}: {count}\n")

def get_year_choice():
    return input("\nEnter a year (e.g. 2019): \n").strip()

def display_average_rating(park, year, average):
    if average is None:
        print(f"\nNo data found for {park} in {year}.\n")
    else:
        print(f"\nAverage Rating for {park} in {year}: {average:.2f}.\n")

def display_average_score_by_location(results):
    for park, location_data in results.items():
        print(f"\n--- {park} ---")
        for location, avg in sorted(location_data.items()):
            print(f" - {location}: {avg:.2f}")

def display_export_menu():
    print("\nPlease select export format.\n")
    print("[A] Export to TXT\n")
    print("[B] Export to CSV\n")
    print("[C] Export to JSON\n")
    print("[X] Back to Main Menu\n")

def display_export_success(filename):
    print(f"\nData Successfully Exported to '{filename}'.\n")