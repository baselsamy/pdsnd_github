import time
import pandas as pd
import numpy as np

# Datasets used for analysis 

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Get user input for city (chicago, new york city, washington)
    
    cities_list = ['Chicago','New York City','Washington']
    correct_answer = 0
    while correct_answer != 1:
        print()
        city_input = input("what city do you want to look at? please enter one of the following city's name (chicago, new york city, washington).\n")
        city = city_input.title()
        if city not in cities_list:
            print()
            print("Please enter a valid name or make sure the spelling is correct.")
        else:
            correct_answer += 1
            
    # Get user input for month (all, january, february, ... , june).
    
    months_list = ['All', 'January', 'February', 'March', 'April', 'May', 'June']
    correct_answer = 0
    while correct_answer != 1:
        print()
        month_input = input('what month do you want to filter with? please enter the name of the month or "all" to see all months (From January to June).\n')
        month = month_input.title()
        if month not in months_list:
            print()
            print("Please enter a valid name or make sure the spelling is correct.")
        else:
            correct_answer += 1
    # Get user input for day of week (all, monday, tuesday, ... sunday).
    
    days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']
    correct_answer = 0
    while correct_answer != 1:
        print()
        day_input = input('what day do you want to filter with? please enter the name of the day or "all" to see all days.\n')
        day = day_input.title()
        if day not in days_list:
            print()
            print("Please enter a valid name or make sure the spelling is correct.")
        else:
            correct_answer += 1
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
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'All':
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    input:
        (Panda dataframe) df - Pandas DataFrame containing city data filtered by month and day
    
    Returns:
        - display (print) the most common month
        - display (print) the most common day of week
        - display (print) the most common start hour
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    m_comm =  df['month'].mode()
    popular_month = m_comm[0]
    print()
    print('Most Poular month: ', popular_month)

    # TO DO: display the most common day of week
    d_comm =  df['day_of_week'].mode()
    popular_day = d_comm[0]
    print('Most Poular day: ', popular_day)
    
    # TO DO: display the most common start hour
   
    ## extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    ## find the most popular hour
    h_comm = df['hour'].mode()
    popular_hour = h_comm[0]
    print('Most Poular hour: ', popular_hour)
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    input:
        (Panda dataframe) df - Pandas DataFrame containing city data filtered by month and day
        
    Returns:
        - Display (Print) commonly used start station
        - Display (Print) commonly used end station
        - Display (Print) most frequent combination of start station and end station trip
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    s_st_comm =  df['Start Station'].mode()
    popular_start_station = s_st_comm[0]
    print('Most Poular start station: ', popular_start_station)

    # Display most commonly used end station
    e_st_comm =  df['End Station'].mode()
    popular_end_station = e_st_comm[0]
    print('Most Poular end station: ', popular_end_station)

    # Display most frequent combination of start station and end station trip
    df['combined_stations'] = "Start Station: " + df['Start Station'] + '\n' + "End Station: " + df['End Station']
    T_st_comm = df['combined_stations'].mode()
    popular_combined_stations = T_st_comm[0]
    print('Most Poular line: \n')
    print(popular_combined_stations)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    input:
        (Panda dataframe) df - Pandas DataFrame containing city data filtered by month and day
        
    Returns:
        - Display (Print) total travel time
        - Display (Print) average (mean) travel time
    
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['travel_time'] = df['End Time'] - df['Start Time']
    total_travel_time = df['travel_time'].sum()
    print('Total travel time: ', total_travel_time)
    
    # Display mean travel time
    average_travel_time = df['travel_time'].mean()
    print('Average travel time : ', average_travel_time)
    print()
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 
def user_stats(df):
    """Displays statistics on bikeshare users.
    input:
        (Panda dataframe) df - Pandas DataFrame containing city data filtered by month and day
        
    Returns:
        - Display (Print) counts of user types
        - Display (Print) gender counts. If data is unavailable (as in Washington's case), display a message indicating its absence.
        - Display (Print) earliest, most recent, and most common year of birth. If data is unavailable (as in Washington's case), display a message indicating its absence.
        
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print("User Types: ")
    print()
    print(user_types_count.to_frame())
    print()

    # Display counts of gender
    if 'Gender' in df:
        gender_dist = df['Gender'].value_counts()
        print('Gender Distribution: ')
        print()
        print(gender_dist.to_frame())
        print()
    else:
        print("Gender Distribution: No data about gender exist in the dataset.")
        print()

        
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()
        print('Earliest birth year: ', int(earliest_year))
        print('Most recent birth year: ', int(most_recent_year))
        print('Most common birth year: ', int(most_common_year[0]))
        print()
    else:
        print('Earliest birth year: No data about birth years exist in the dataset.')
        print('Most recent birth year: No data about birth years exist in the dataset.')
        print('Most common birth year: No data about birth years exist in the dataset.')
        print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def main():
    """Start the program when the script is running. 
    
    Input:
        - Asks user to specify a city, month, and day to analyze.
        - Load dataset using the city, month, and day as filters.
        - Ask the user if they wants to display raw data (five rows at a time).
        - At the end of the program, ask the users if they want to restart the program.
    
    Returns:
        - Displays statistics on the most frequent times of travel.
        - Displays statistics on the most popular stations and trip.
        - Displays statistics on the total and average trip duration.
        - Displays statistics on bikeshare users.
        - Display raw data upon user request (five rows at a time).
        - Restart the program when prompted by the user.
    """
    while True:
        # Get the user input for city, month and day filters.
        city, month, day = get_filters()
        # Load the data set using the city, month and day filters.
        df = load_data(city, month, day)
        
        # Display statistics 
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        # Offer to display raw data in five-row increments. Continue prompting and showing the next 5 rows until the user declines.
        
        request = 0
        i = 0
        while True:
            raw_data_request = input('\nWould you like to view raw data from the dataset (five rows at a time)? Enter yes or no.\n').lower()
            if raw_data_request != 'yes':
                break
            elif raw_data_request == 'yes':
                print(df[i : i + 5])
                i = i + 5
                
        # Ask user if they wish to restart the program or end their session. 
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
