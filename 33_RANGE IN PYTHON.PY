
'''Range function in Python'''
# The range function in python is used to generate a sequence of numbers.
'''example'''
for i in range(0,7):		#range(7) can also be used THIS IS range(start, stop)
	print(i)		        #prints 0 to 6


# We can also specify the start, stop, and step-size as follows:
# range(start, stop, step_size)

'''EXAMPLE'''
for n in range(0, 7, 2):		#WILL LEAVE STEP SIZE 1 AFTER  EVERY 
	print(n)

# step size is usually not used with range()
# An example demonstrating range() function










'''For loop with else'''
# An optional else can be used with a for loop if the code is to be executed when the loop exhausts.
'''Example:'''

l = [1, 7, 8]
for item in l:
	print(item)
else:
	print("this is inside else of for ")	#This is printed when the loop exhausts!

