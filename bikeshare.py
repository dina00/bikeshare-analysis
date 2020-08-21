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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities=['chicago', 'new york city', 'washington']
    months=['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days= ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'all']
    city= input('Enter the city you want to explore chicago, new york city, washington:\n')
    city=city.lower()
    while True:
        if city in cities:
            break
        else:
            city= input('Enter a valid city:')
            continue
        break
    # TO DO: get user input for month (all, january, february, ... , june)
    month=input('Enter the month january, feburary...june or all:\n')
    month=month.lower()
    while True:
        if month in months:
            break
        else:
            month= input('Enter a valid month or all:')
            continue
        break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Enter the day of the week monday,...,sunday or all:\n')
    day=day.lower()
    while True:
        if day in days:
            break
        else:
            day= input('Enter a valid week day:')
            continue
        break
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

   # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('\nMost common month: ',df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('\nMost common day of week: ',df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    print('\nMost common start hour: ',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nMost common start station: ',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('\nMost common end station: ',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('\nMost common ombination of start station and end station trip: ',(df['Start Station']+' - '+df['End Station']).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nTotal travel time:', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('\nMean travel time:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    print('\nCount of users and subscribers:\n',df['User Type'].value_counts())
    # TO DO: Display counts of gender
    if city != 'washington':
        print('\nCount of each gender:\n',df['Gender'].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
        print('\nEarliest year of birth:', df['Birth Year'].min())
        print('\nMost recent year of birth:', df['Birth Year'].max())
        print('\nMost common year of birth:', df['Birth Year'].mode()[0])
    # washington doesn't have birth year and gender data
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    while True:
        ans=input('\nWould like to see some raw data? ')
        if ans.lower() != 'yes':
            print('bye!')
            break
        
        raw=pd.read_csv(CITY_DATA[city])
        print(raw.head(5))
    
        
            


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
