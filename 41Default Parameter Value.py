'''Default Parameter Value'''

# We can have a value as the default argument in a function.
# If we specify name = “stranger” in the line containing def, this value is used WHEN NO ARGUMENT WILL BE PASSED.
# For Example:

def greet(name= "stranger"):
	print("good day, ", name)

greet("Harry")        #Name will be “Harry” in function body(passed)
greet()                 #Name will be ‘stranger’ in function body(default)

def age(ifnoage = "not entered"):
	print ("your age is ", ifnoage)

age(input("your age please"))
age()