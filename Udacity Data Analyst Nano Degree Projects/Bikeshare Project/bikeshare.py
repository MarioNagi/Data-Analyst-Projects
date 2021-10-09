import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS_DATA=['january', 'february', 'march', 'april', 'may', 'june','all']
WEEK_DATA=['all', 'monday', 'tuesday','wednesday','thursday','friday','saturday', 'sunday','all']
USER_CHOICE=['yes','no']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city=month=day=''
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in CITY_DATA.keys():
        city=input("Please pick a city: Chicago, New York City, Washington either in lower or upper cases\n").lower().strip()
        if city not in CITY_DATA.keys():
            print("{} is not a valid".format(city))
            print("please enter valid value: Chicago, New York City, Washington either in lower or upper cases")
    # TO DO: get user input for month (all, january, february, ... , june)
    while month not in MONTHS_DATA:
        month=input("Please pick a month to filter by (all, january, february, ... , june) or enter all for no filter\n").lower().strip()
        if month not in MONTHS_DATA:
            print("{} is not a valid".format(month))
            print("please enter valid value: (all, january, february, ... , june)")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in WEEK_DATA:
        day=input("Please pick a day to filter by (all, monday, tuesday, ... sunday) or enter all for no filter\n").lower().strip()
        if day not in WEEK_DATA:
            print("{} is not a valid".format(day))
            print("please enter valid value: (all, monday, tuesday, ... sunday)")
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
    df['Start Time'] = df['Start Time'].astype('datetime64[ns]')

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df["start_hour"]=df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]
    
    return df
    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    top_month=df['month'].mode()[0]
    #can use idxmax to get the same result, tested and working fine
    #max_Month=df['month'].value_counts().idxmax()
    
    print("the most common month is {}".format(top_month))
    #can use idxmax to get the same result, tested and working fine
    #print("the most common month using idxmax is {}".format(max_Month))
    
    # TO DO: display the most common day of week

    top_day_of_week=df['day_of_week'].mode()[0]
    print("the most common day of week is {}".format(top_day_of_week))
    # TO DO: display the most common start hour
    top_hour=df['start_hour'].mode()[0]
    print("the most common hour is {}".format(top_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    top_start_station=df["Start Station"].mode()[0]
    print("the most used Start Station is {}".format(top_start_station))

    # TO DO: display most commonly used end station
    top_end_station=df["End Station"].mode()[0]
    print("the most used End Station is {}".format(top_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    top_combination=df.groupby(["Start Station","End Station"]).size().idxmax()
    print("the most combination station is {}".format(top_combination))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df["Trip Duration"].sum()
    
    """the above number is in seconds, which is equals to =x days*24+y hours*3600+z mins*60+a seconds
    to get the values of x,y,z,a which is days, hours, mins and seconds out of this number, 
    we will use Divmod function which take 2 numbers and return quotient and remainder of their division as a tuple
    will use it first to returns seconds and mins then using it again to return hours and min and finally days"""
    
    total_mins,total_seconds=divmod(total_travel_time, 60)
    total_hours,total_mins=divmod(total_mins, 60)
    total_days,total_hours=divmod(total_hours, 24)

    print("The total travel time took {} days, {} hours, {} mins, {} seconds".format(total_days,total_hours,total_mins,total_seconds))
    # TO DO: display mean travel time
    mean_travel_time=round(df["Trip Duration"].mean())
    print("Avg. travel time is {} seconds".format(mean_travel_time) )
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    counts_of_user_types=df['User Type'].value_counts()
    print("counts of user types are \n{}".format(counts_of_user_types))
    # TO DO: Display counts of gender
    # not every city/sheet has the gender column, so we put this code in try,expect block to avoid throwing errors
    try:
        counts_of_gender = df['Gender'].value_counts()
        print( "\nthe number of our cutsomers sorted by Gender are as seen below:\n{}".format(counts_of_gender))
    except:
        print("The 'Gender' is not specified in this sheet/city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    # the same goes for the birth year column not every city/sheet has it,
    #so we put this code in try,expect block to avoid throwing errors
    try:
        earliest_year = df["Birth Year"].min()
        most_recent_year=df["Birth Year"].max()
        most_common_year=df["Birth Year"].value_counts().idxmax()
        print( "\nour oldest customer was born on {},\nwhile our youngest was born on {}\nand the average birth year of our customers is {}\n".format(earliest_year,most_recent_year,most_common_year))
    except:
        print("The 'birth year' is not specified in this sheet/city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """displaying the top rows in data in increment of 5 based on user input"""
    
    start_time = time.time()
    data_check=''
    counter=5
    print("Do you want to see the top 5 rows of your choice?")
        # TO DO: get user input for month (all, january, february, ... , june)
    while data_check not in USER_CHOICE:
        data_check=input("Please enter Yes to display or No to contiune\n").lower().strip()
        if data_check not in USER_CHOICE:
            print("{} is not a valid".format(data_check))
            print("please enter valid value: Yes or No")
        elif data_check=="yes":
            print("displaying top data")
            print(df.head())
            
            
        while data_check=="yes":
            print("want to view more data?\n Enter Yes or No\n")
            second_check=input().lower()
            if second_check=="yes":
                counter+=5
                print(df.head(counter))
            else:
                break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)               

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
