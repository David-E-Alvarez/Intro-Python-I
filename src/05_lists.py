# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
print(x)
#x.append(y) i don't like the output of this on repl.it but don't know if i can do print(x + y)
print(x + y)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
print(x + y[1:])
#or x.append(y[1:]) to use print(x)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
#for this one the first thing i do is add the 99 like so:
y.insert(2,99)
#i then can append y to x and "splice" the 8 out like so:
x.append(y[1:])
#if i do the line above i can use print(x) but if i can also do this:
print(x + y[1:])#and not do the appending of y to x
# YOUR CODE HERE
print(x)

# Print the length of list x
# YOUR CODE HERE
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for elem in x:
  print(elem * 1000)
