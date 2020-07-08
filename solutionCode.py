#calendar
"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
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

# fetch command line arguments for this program 
num_args = len(sys.argv)

# user didn't pass in any arguments
if num_args == 1:
    # get the current month and year 
    month = datetime.now().month
    year = datetime.now().year
    # render the cal for that 

# user passed in one argument
elif num_args == 2:
    # assume the arg is the specified month 
    # render the cal for that month of the current year 
    year = datetime.now().year
    month = int(sys.argv[1])

# user passed in two arguments 
elif num_args == 3:
    # render the cal for the specified month and specified year 
    month = int(sys.argv[1])
    year = int(sys.argv[2])

# user passed in some other number of arguments 
else:
    # print a usage statement 
    print("usage: 14_cal.py [month] [year]")
    # exit the program 
    sys.exit(1)

cal = calendar.TextCalendar()
cal.prmonth(year, month)
#===================================================================================
#classes
"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
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

# fetch command line arguments for this program 
num_args = len(sys.argv)

# user didn't pass in any arguments
if num_args == 1:
    # get the current month and year 
    month = datetime.now().month
    year = datetime.now().year
    # render the cal for that 

# user passed in one argument
elif num_args == 2:
    # assume the arg is the specified month 
    # render the cal for that month of the current year 
    year = datetime.now().year
    month = int(sys.argv[1])

# user passed in two arguments 
elif num_args == 3:
    # render the cal for the specified month and specified year 
    month = int(sys.argv[1])
    year = int(sys.argv[2])

# user passed in some other number of arguments 
else:
    # print a usage statement 
    print("usage: 14_cal.py [month] [year]")
    # exit the program 
    sys.exit(1)

cal = calendar.TextCalendar()
cal.prmonth(year, month)
#====================================================================
#store
class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def print_welcome(self):
        print(f"Welcome to {self.name}! Which department would you like to visit?")

        for d in self.departments:
            print(d)


# should Department inherit from Store? 
class Department:
    def __init__(self, id, name, products):
        self.id = id
        self.name = name
        self.products = products

    def __str__(self):
        return f"{self.id}: {self.name}"


store = Store("The Dugout", [
    Department(1, "Baseball", []),
    Department(2, "Basketball", []),
    Department(3, "Football", []),
    Department(4, "Golf", []),
])

# loop forever while the user is browsing through departments 
# use the `input` function to prompt the user to select a department to browse 
while True:
    # print a welcome message for the Store
    store.print_welcome()

    # get the department number the user wants to visit:
    selection = input("Which department would you like to visit? ")

    # if the user types "quit", exit the program 
    if selection == "quit":
        break

    chosen_department = store.departments[int(selection)-1]

    print(f"You picked the {chosen_department.name} department.\n")
