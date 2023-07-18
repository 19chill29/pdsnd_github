import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
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
    city_tour = input('Please select Chicago, New York City, or Washington to explore: ').lower()
    while city_tour not in CITY_DATA:
        print('Invalid seletion')
        city_tour = input('Please select Chicago, New York City, or Washington to explore:' ).lower()

             # TO DO: get user input for month (all, january, february, ... , june)
    print('Choose a month')
    month = input('January, February, March, April, May, June, July, August, September, October, Novemeber, December, or all: ').lower()
    #added while loop to check if month input is valid
    while month not in MONTHS:
        print("Invalid Selection")
        month = input('January, February, March, April, May, June, July, August, September, October, Novemeber, December, or all: ').lower
             
    print('Choose a day')
    day = input('Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all: ').lower()
    #added while loop to check if day input was valid
    while day not in DAYS:
        print("Invalid Selection")
        day = input('Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all: ').lower()
 

    print('-'*40)
    return city_tour, month, day


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
    #read in data file from city name stored in CITY_DATA datastructure
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #set the month
    df['Month'] = df['Start Time'].dt.month
    #set the day
    df['Day'] = df['Start Time'].dt.weekday_name

    #filter by month
    if month != 'all':
        #filters by matching the month from the user with month stored in csv file
        month = MONTHS.index(month) + 1
        df = df[df['Month']== month]
    #filter by day
    if day != 'all':
        #filters by matching the month from the user with month stored in csv file
        df = df[df['Day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #get the month
    Month = df['Month'].mode()[0]
    print("The most common month: ",Month)

    # TO DO: display the most common day of week
    #get the day 
    Day = df['Day'].mode()[0]
    print(" the most common day: ",Day)

    # TO DO: display the most common start hour
    #get hours
    df['hour'] = df['Start Time'].dt.hour
    Hour = df['hour'].mode()[0]
    print("the most common start hour: ",Hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most common Start Station: ", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(" The most Common End Station: ", common_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    df['Start to End'] = df['Start Station'].str.cat9df['End Station'], sep=' to ')
    combination = df['Start to End'].mode()[0]

    print("The most common start and end stations", combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time: ", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time: ", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User Type Counts: " )
    print(df['User Type'].value_counts())
    # TO DO: Display counts of gender
    print("Gender Count")
    print(df['Gender'].value_counts())
    
    # TO DO: Display earliest, most recent, and most common year of birth
    print("Earliest Birth Year: ", df['Birth Year'].min()) #earliest
    print("Most Recent Birth Year: ", df['Birth Year'].max()) #most recent
    print("Most Common Birth Year: ", df['Birth Year'].mode()) #most common
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_data(df):

    start, end = 0
    answer = ''
    #get user input
    while answer != 'yes' or answer != 'no':
        answer = input("Would you like to display 5 rows of data: yes or no").lower()
        if answer == 'yes':
            #get first row
            end += 5
            data = df.iloc[start:end, :9]
            print(data)
        elif: answer == 'no':
            print("No data displayed")
            break
        else:
            print("Invalid response")
            answer = input("Please select yes or no").lower()
      #check if user wants to see more data and loop until the condition is broken     
    while answer == 'yes':
        print("would you like to see more data")
        #set display counter to 5
        start += 5
        end += 5
        answer = input("yes or no").lower
        if answer == 'yes' or answer == 'no':
            if answer =='yes':
                #return next 5 rows
                data = df.iloc[start:end, :9]
                print(data)
            elif: answer == 'no':
                print("No data displayed")
                break
            else:
                break
        else:
            print("Invalid response")
            answer = input("Please select yes or no").lower()
            
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
