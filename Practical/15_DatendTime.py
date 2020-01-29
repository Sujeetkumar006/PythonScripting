# tick: Time intervals are floating-point numbers in units of seconds. Particular instants in time are expressed in seconds since 12:00am, January 1, 1970(epoch).

#There is a popular time module available in Python which provides functions for working with times, and for converting between representations. The function time.time() returns the current system time in ticks since 12:00am, January 1, 1970(epoch).

# theer are three modules to handle time: date, datetime and time. Calender is module to handle calender.in Python, date, time and datetime classes provides a number of function to deal with dates, times and time intervals. Date and datetime are an object in Python, so when you manipulate them, you are actually manipulating objects and not string or timestamps. Whenever you manipulate dates or time, you need to import datetime function.

#date – Manipulate just date ( Month, day, year)
#time – Time independent of the day (Hour, minute, second, microsecond)
#datetime – Combination of time and date (Month, day, year, hour, second, microsecond)
#timedelta— A duration of time used for manipulating dates
#tzinfo— An abstract class for dealing with time zones

#
from datetime import date
from datetime import time
from datetime import datetime
#### Time module
import time
ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks

#Getting current time
localtime = time.localtime(time.time())
print "Local current time :", localtime

#Getting formatted time
localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime


### Calender Module
#Getting calendar for a month
import calendar
cal = calendar.month(2008, 1)
print "Here is the calendar:"
print cal


## datetime module
import datetime  # This is required to include time module.
datetime_object = datetime.datetime.now() # current date and time
print(datetime_object)

date_object = datetime.date.today() # today date
print(date_object)

d = datetime.date(2019, 4, 13) # date creation.
print(d)

from datetime import date
timestamp = date.fromtimestamp(1326244364) ## date creation from time epoch
print("Date =", timestamp)


today = date.today() 
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

#datetime(year, month, day)
a = datetime(2018, 11, 28)
print(a)
# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)

##Difference between two dates and times
from datetime import datetime, date
t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print("t3 =", t3)
t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)
print("type of t3 =", type(t3)) 
print("type of t6 =", type(t6))
 
####datetime.timedelta: A timedelta object represents the difference between two dates or times.
from datetime import timedelta
t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2
print("t3 =", t3)


# Date formating: Python format datetime: Python has strftime() and strptime() methods to handle this.
#Each control code resembles different parameters like year,month, weekday and date [(%y/%Y – Year), (%a/%A- weekday), (%b/%B- month), (%d - day of month)]
 
print "Time in seconds since the epoch: %s" %time.time()
print "Current date and time: " , datetime.datetime.now()
print "Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M")

print "Current year: ", datetime.date.today().strftime("%Y")
print "Month of year: ", datetime.date.today().strftime("%B")
print "Week number of the year: ", datetime.date.today().strftime("%W")
print "Weekday of the week: ", datetime.date.today().strftime("%w")
print "Day of year: ", datetime.date.today().strftime("%j")
print "Day of the month : ", datetime.date.today().strftime("%d")
print "Day of week: ", datetime.date.today().strftime("%A")


#Python strptime() - string to datetime
The strptime() method creates a datetime object from a given string (representing date and time).
from datetime import datetime
date_string = "21 June, 2018"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y") #%d, %B and %Y format codes are used for day, month(full name) and year respectively.
print("date_object =", date_object)


#Handling timezone in Python
from datetime import datetime
import pytz
local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))
tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))
tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

### Different time format:

from datetime import date
today = date.today()
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)
# Textual month, day and year	
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)
# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)
# Month abbreviation, day and year	
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)

https://www.tutorialspoint.com/python/python_date_time.htm
https://www.programiz.com/python-programming/datetime
https://www.programiz.com/python-programming/datetime/current-datetime
https://www.guru99.com/date-time-and-datetime-classes-in-python.html
https://www.pythonforbeginners.com/basics/python-datetime-time-examples
