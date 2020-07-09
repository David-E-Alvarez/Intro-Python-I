"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - [x]If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - [x]If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - [x]If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - []Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime


#this program runs in terminal. it takes in two arguments but user doesn't have to enter any. 
# EX. `14_cal.py [month] [year]`
# print('sys.argv[1]: ', sys.argv[1])# would print what user would enter for month
#print(len(sys.argv) - 1)#can use to determine how many arguments user enters

#calendar for a month and year
cal = calendar.TextCalendar()
current_month = datetime.now().month
current_year = datetime.now().year

user_args_length = len(sys.argv)-1 #number of user arguments
#print('--->',user_args_length)

#1.)if user enters nothing output calendar for current month
if user_args_length == 0:
  print(cal.prmonth(current_year,current_month))

#2.) if user enters one argument; assume month is entered
elif user_args_length == 1:
  year = datetime.now().year
  month = int(sys.argv[1])
  print(cal.prmonth(year,month))

#3.) if user enters two arguments output month and year they want
elif user_args_length == 2:
  year = datetime.now().year
  month = int(sys.argv[1])
  print(cal.prmonth(year,month))
else:
  # print a usage statement 
    print("usage: 14_cal.py [month] [year]")
    # exit the program 
    sys.exit(1)
