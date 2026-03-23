
import tui
import process
import visual

DATA_FILE = "data/disneyland_reviews.csv"

def handle_view_data(data, parks):
    while True:
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
            park = tui.get_park_choice(parks)
            year = tui.get_year_choice()
            average = process.get_average_rating_by_park_and_year(data, park, year)
            tui.display_average_rating(park, year, average)
        elif choice == "D":
            results = process.get_average_score_per_park_by_location(data)
            tui.display_average_score_by_location(results)
        elif choice == "X":
            break
        else:
            tui.display_invalid_choice()


def handle_visualise_data(data, parks):
    while True:
        tui.display_visualise_menu()
        choice = tui.get_menu_choice()
        tui.display_selected_choice(choice)

        if choice == "A":
            counts = process.get_review_count_by_park(data)
            visual.show_pie_chart_reviews_per_park(counts)
        elif choice == "B":
            park = tui.get_park_choice(parks)
            top = process.get_top_locations_by_average_rating(data, park)
            visual.show_bar_chart_top_locations(top, park)
        elif choice == "C":
            park = tui.get_park_choice(parks)
            monthly_data = process.get_average_rating_by_month(data, park)
            visual.show_bar_chart_monthly_ratings(monthly_data, park)
        elif choice == "X":
            break
        else:
            tui.display_invalid_choice()


def handle_export_data(data):
    from exporter import ParkExporter

    while True:
        tui.display_export_menu()
        choice = tui.get_menu_choice()
        tui.display_selected_choice(choice)

        format_map = {"A": "txt", "B": "csv", "C": "json"}

        if choice == "X":
            break
        elif choice in format_map:
            fmt = format_map[choice]
            exporter = ParkExporter(data)
            filename = exporter.export(fmt)
            tui.display_export_success(filename)
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
        elif choice == "C":
            handle_export_data(data)
        elif choice == "X":
            print("\nGoodbye!\n")
            break
        else:
            tui.display_invalid_choice()

if __name__ == "__main__":
    main()