"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
file = open('/home/david/CS_hw/python/Intro-Python-I/src/foo.txt', 'r')#opens file
file_data = file.read()#"reads" file data and initializes variable with contents of file
#print(file_data)#prints contents of file
file.close()#closes file

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
file2 = open('/home/david/CS_hw/python/Intro-Python-I/src/bar.txt', 'r+')#opens file
file2.write('the day is here, so be queer, cuz the end is near')
file2_data = file2.readline()
print(file2_data)
file2.close()
