# Typecasting: It is conversion of str to int or vice vrsa if possible
# example
from types import FunctionType


a = "4"
print(type(a))

'''here it shows class string'''


# now lets convert a str into int using typecasting
b = "5"
b = int(b)
print(type(b))
'''now we converted a str into int hence type is shown as int'''

# print (a+7) this will show  a error TypeError: can only concatenate str (not "int") to str because a is a string.
print (b+3)


'''
str(31) = "31"       int to str conversion
int("32") = 32       str to int conversion
float(32) = 32.0     int to float conversion

here "31" is string literal and 31 a numeric literal

'''


# Input Function
# this function allows the user to take input from the keyboard as a string