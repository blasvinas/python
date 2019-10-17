#Shows how to work with dates and time
import calendar
print(calendar.isleap(2020))

from datetime import date
halloween = date(2019,10,31)
print(f"Date: {halloween}.  Year: {halloween.year}.  Month: {halloween.month}.  Day: {halloween.day}")
now = date.today()
print(now)

from datetime import timedelta
today = date.today()
tomorrow = today + timedelta(days=1)
print(f"Today: {today}.  Tommorrow: {tomorrow}")

from datetime import time, datetime
noon = time(12,0,0)
print(noon)
now = datetime.now()
print(f"Now: {now}. Hour: {now.hour}.  Minute: {now.minute}.  Second: {now.second}")

import time
now = time.time()
print(f"EPOC: {now}.  Date: {time.ctime(now)}")
current_time = time.localtime()
print(current_time)
fmt = "It is %A, %B %d, %Y, local time: %I:%M:%S%p"
print(time.strftime(fmt,current_time))

#Converting from string to date
fmt = "%Y-%m-%d"
my_date = time.strptime("2019-10-16",fmt)
print(my_date)
