
# QHO444-AE2 – Disneyland Reviews Analysis Tool

## What is this project?

This project is a Python application that analyses a dataset of Disneyland 
reviews from parks around the world. It was developed as part of the 
QHO444 Problem Solving Through Programming module at Solent University London.

The program reads a CSV file containing over 42,000 reviews and allows 
the user to explore the data through a text-based menu system.

## What can the program do?

The program is divided into three main sections:

**View Data**
- See all reviews for a specific park
- Find out how many reviews a park received from a specific country
- Check the average rating a park received in a specific year
- View the average score each park received from every reviewer location

**Visualise Data**
- A pie chart showing how many reviews each park received
- A bar chart showing the top 10 countries by number of reviews and their average rating
- A bar chart showing the average rating per month for a specific park

**Export Data**
- Export a summary of park statistics to TXT, CSV or JSON format

## How to run the program

1. Make sure Python is installed on your machine
2. Install the only required library by running:
```
pip install matplotlib
```
3. Run the program from the terminal:
```
python main.py
```

## Project structure
```
QHO444-AE2/
├── main.py        # Controls the program flow
├── tui.py         # Handles all user input and output
├── process.py     # Handles all data processing
├── visual.py      # Handles all charts and visualisations
├── exporter.py    # OOP export feature (TXT, CSV, JSON)
└── data/
    └── disneyland_reviews.csv
```

## Technologies used

- Python 3
- Matplotlib (for charts)
- CSV and JSON (built-in Python libraries)

## Notes

- The GitHub repository for this project is set to private as required 
  by the assessment brief
- All code follows PEP 8 style guidelines
- The program must be run from main.py