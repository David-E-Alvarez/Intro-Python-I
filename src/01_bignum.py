# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE

#this may be one way. this way doesn't work for the power of 65536
#import math# don't like i have to use math module
#print(math.pow(2,65536))#OverflowError: math range error

print(2**65536)#this way works
