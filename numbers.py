# Calculate how many seconds are in an hour
seconds_per_minute = 60
minutes_per_hour = 60
seconds_per_hour = minutes_per_hour * seconds_per_minute
print(f'The number of seconds in an hour is {seconds_per_hour}')

# Calculate the numbers of seconds in a day
hours_per_day = 24
seconds_per_day = hours_per_day * seconds_per_hour
print(f'The number of seconds in a day is {seconds_per_day}')

# Calculate the hours in a day using seconds_per_hour and seconds_per_day
print(f'The number of hours in a day are: {seconds_per_day / seconds_per_hour}')