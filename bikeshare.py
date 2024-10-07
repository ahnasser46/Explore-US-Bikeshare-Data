import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Kindly specify which city: chicago, new york city, or washington:\n')
    while city.lower() not in ['chicago', 'new york city', 'washington']:
        print('Choose among the available options')
        city = input('Kindly specify which city: chicago, new york city, or washington:\n')

    # get user input for month (all, january, february, ... , june)
    month = input('Kindly specify which month january, ... ,june or all:\n')
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        print('Choose among the available options')
        month = input('Kindly specify which month january, ... ,june :\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Kindly specify which day or all:\n')
    while day not in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
        print('Recheck your input')
        day = input('Kindly specify which day:\n')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA.get(city))


    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.strftime("%I %p")

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        days = ['saturday','sunday', 'monday', 'tuesday', 'wednesday', 'thurday', 'friday']
        day = days.index(day) + 1
        df = df[df['day'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print("Most common month is {}".format(common_month))

    # display the most common day of week
    common_day = df['day'].mode()[0]
    print("Most common day of week is {}".format(common_day))

    # display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("Most common start hour is {}".format(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    pop_start = df['Start Station'].mode().to_string(index = False)
    print('The most popular start station is {}.'.format(pop_start))

    # display most commonly used end station
    pop_end = df['End Station'].mode().to_string(index = False)
    print('The most popular end station is {}.'.format(pop_end))


    # display most frequent combination of start station and end station trip
    df['journey'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    most_pop_trip = df['journey'].mode().to_string(index = False)
    print('The most popular trip is {}.'.format(most_pop_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time in hours
    total_duration = (df['Trip Duration'].sum())//60.00
    print('The total trip duration is nearly {} hours'.format(total_duration))

    # display mean travel time in hours
    average_duration = (df['Trip Duration'].mean())//60.00
    print('The average trip duration is nearly {} hours'.format(average_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    custs = df['User Type'].value_counts()['Customer']
    subs = df['User Type'].value_counts()['Subscriber']
    print('There are {} Subscribers and {} Customers.'.format(subs, custs))

    try:
    # Display counts of gender
       male_count = df['Gender'].value_counts()['Male']
       female_count = df['Gender'].value_counts()['Female']
       print('There are {} male users and {} female users.'.format(male_count, female_count))
    # Display earliest, most recent, and most common year of birth
       earliest = int(df['Birth Year'].min())
       latest = int(df['Birth Year'].max())
       mode = int(df['Birth Year'].mode())
       print('The oldest users are born in {}.\nThe youngest users are born in {}.'
       '\nThe most popular birth year is {}.'.format(earliest, latest, mode))

    except:
        print('There is no Gender & Birth Year data for washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        start_loc = 0
        end_loc = 5
        while view_data.lower() == 'yes':
           print(df.iloc[start_loc:end_loc])
           view_display = input("Do you wish to continue?: ").lower()
           if view_display == 'yes':
              start_loc += 5
              end_loc += 5
           elif view_display.lower() == 'no':
               break
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()