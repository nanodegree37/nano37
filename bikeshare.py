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

    while True: 
             
        city = str(input("\nPick a city (chicago, new york city, washington): ").strip().lower())

        if city not in ("chicago", "new york city", "washington"):
            print("\nInvalid Response. Please try again")
            continue
        else:
            print("\nIt looks like you want to see data for: '{}' ".format(city.title()))
            validity_check()
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        month = str(input("\nType in name of month to filter by (i.e. January): ").strip().lower())

        if month not in ("January", "February", "March", "April", "May", "June", "all"):
            print("\nPlease type in month name (or \"all\" to select every month)")
            continue
        else:
            print("\nNice choice! It seems that you want to filter by: '{}' ".format(month.title()))
            validity_check()
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input("\nType in name of day to filter by (i.e. Monday): ").strip().lower())

        if day not in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" , "Sunday", "all"):
            print("Invalid. Please type in valid day (or \"all\" to select every day)")
            continue
        else:
            print("\nOk, you want to filter by: '{}' ".format(day.title()))
            validity_check()
            break
    print("\nYou selected '{}' as city, '{}' as month, and '{}' as day. \nFiltering by your parameters....".format(city.title(), month.title(), day.title()))
    print()
    print('-'*40)
    return city, month, day
    
def validity_check(): 
    
    while True: 
        validity = str(input("Is your input correct? Type 'y' to continue and 'n' to restart: \n").strip().lower())
        if validity not in ("y", "n"):
            print("\nPlease try again")
            continue
        elif validity == 'y':
            break
        else: 
            get_filters()

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime type
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # get month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day_of_Week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour

    # filter by month if applicable

    if month != 'all':
       # use index of the month list 
        months = ['january', 'february', 'march', 'april', 'may', 'june']
       
        month = months.index(month) + 1
        # month column is in type(integer)
        df = df[df['Month'] == month]

  
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
               
        # filter by day of week to create the new dataframe
        df = df[df['Day_of_Week'] == day.title()]
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    #pickup dictionary
    look_up = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May',
        '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}


    return df

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most common Month'.ljust(40, '.'), popular_month)


    # TO DO: display the most common day of week
    
    popular_day = df['Day_of_Week'].mode()[0]
    print("2. The most common day of the week was: {}".format(popular_day))

    # TO DO: display the most common start hour
    
    popular_hour = df['Hour'].mode()[0]
    print('3. The most common start hour was:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    most_common_start_station = str(df['Start Station'].mode()[0])
    print("For the selected filters, the most common start station is: " +
          most_common_start_station)

    # TO DO: display most commonly used end station
    
    most_common_end_station = str(df['End Station'].mode()[0])
    print("For the selected filters, the most common start end is: " +
          most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    df['Start-End Combination'] = (df['Start Station'] + ' - ' +
                                   df['End Station'])
    most_common_start_end_combination = str(df['Start-End Combination']
                                            .mode()[0])
    print("For the selected filters, the most common start-end combination "
          "of stations is: " + most_common_start_end_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = (str(int(total_travel_time//86400)) +
                         'd ' +
                         str(int((total_travel_time % 86400)//3600)) +
                         'h ' +
                         str(int(((total_travel_time % 86400) % 3600)//60)) +
                         'm ' +
                         str(int(((total_travel_time % 86400) % 3600) % 60)) +
                         's')
    print('For the selected filters, the total travel time is : ' +
          total_travel_time + '.')

    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time = (str(int(mean_travel_time//60)) + 'm ' +
                        str(int(mean_travel_time % 60)) + 's')
    print("For the selected filters, the mean travel time is : " +
          mean_travel_time + ".")

    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    ## TO DO: Display counts of user types
    
    if 'User Type' in df.columns:
        print(' User type stats '.center(78, '-'))
        print(df['User Type'].value_counts())
        # print()

    # TO DO: Display counts of gender

    if 'Gender' in df.columns:
        print(' Gender stats '.center(78, '-'))
        df['Gender'].replace(np.nan, 'not disclosed', inplace=True)
        print(df['Gender'].value_counts(dropna=False))
        # print()

    # TO DO: Display earliest, most recent, and most common year of birth
    
    if 'Birth Year' in df.columns:
        print(' Age stats '.center(78, '-'))
        print('Earliest Birth '
              'Year '.ljust(40, '.'), int(df['Birth Year'].min()))
        print('Most recent Birth '
              'Year '.ljust(40, '.'), int(df['Birth Year'].max()))
        print('Most common Birth '
              'Year '.ljust(40, '.'), int(df['Birth Year'].mode()[0]))

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
  
  
