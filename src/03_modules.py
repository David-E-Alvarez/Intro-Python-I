"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
#1.)print("sys.argv: ", sys.argv)#prints "sys.argv:  ['03_modules.py']"
#2.)print("sys.argv[1]: ", sys.argv[1])#prints "sys.argv[1]:  LambdaRules!" if "python3 03_modules.py LambdaRules!" in terminal
#3.)print("2 + 2: ", int(sys.argv[1]) + int(sys.argv[2]))# "python3 03_modules.py 2 2"

# Print out the OS platform you're using:
# YOUR CODE HERE
#print(sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
#print(sys.version)

import os, pwd
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
# Print the current process ID
# YOUR CODE HERE
#print("current process id: ", os.getgid())

# Print the current working directory (cwd):
# YOUR CODE HERE
#print("current working directory: ", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
#print(pwd.getpwuid(os.getuid())[0])