# Bikeshare Data Analysis

This project is part of the Professional Data Analysis Nanodegree by Udacity. This project analyzes bikeshare data for three major US cities: Chicago, New York City, and Washington. The script allows users to filter the data by city, month, and day to compute various statistics.

## Table of Contents
- Introduction
- Files
- Usage
- Functions
- How to Run
- License

## Introduction
The script provides insights into bikeshare usage patterns by calculating statistics on the most frequent times of travel, popular stations, trip durations, and user demographics.

## Files
- `bikeshare.py`: The main script for analyzing bikeshare data.
- `chicago.csv`, `new_york_city.csv`, `washington.csv`: Datasets for the respective cities.

## Usage
1. **get_filters()**: Prompts the user to specify a city, month, and day to analyze.
2. **load_data(city, month, day)**: Loads and filters the data based on user input.
3. **time_stats(df)**: Displays statistics on the most frequent times of travel.
4. **station_stats(df)**: Displays statistics on the most popular stations and trips.
5. **trip_duration_stats(df)**: Displays statistics on trip durations.
6. **user_stats(df)**: Displays statistics on bikeshare users.

## Functions
- **get_filters()**: Asks the user to specify a city, month, and day to analyze.
- **load_data(city, month, day)**: Loads data for the specified city and filters by month and day if applicable.
- **time_stats(df)**: Displays statistics on the most frequent times of travel.
- **station_stats(df)**: Displays statistics on the most popular stations and trip.
- **trip_duration_stats(df)**: Displays statistics on the total and average trip duration.
- **user_stats(df)**: Displays statistics on bikeshare users.

## How to Run
1. Ensure you have the necessary CSV files (`chicago.csv`, `new_york_city.csv`, `washington.csv`) in the same directory as `bikeshare.py`.
2. Run the script using Python:
    ```sh
    python bikeshare.py
    ```
3. Follow the prompts to filter the data and view statistics.

## License
This project is licensed under the MIT License.
