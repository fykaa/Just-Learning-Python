'''Functions '''
# A function is a group of statements performing a specific task.
# When a program gets bigger in size and its complexity grows, it gets difficult for a programmer to keep track of which piece of code is doing what!
# A function can be reused by the programmer in a given program any number of times.

# Example and Syntax of a function
# The syntax of a function looks as follows:

def func1():
	print("Hello")
    # This function can be called any number of times, anywhere in the program.

# Function call
# Whenever we want to call a function, we put the name of the function followed by parenthesis as follows:
# func1()          #This is called function call

# Function definition
# The part containing the exact set of instructions that are executed during the function call.


# Explantion:
# without functkion call
mark1= [22,23,64,75]
percent1 = ((sum(mark1)/400)*100)
print(percent1)

mark2= [34,57,86,72]
percent2 = ((sum(mark2)/400)*100)
print(percent2)
    # toh in this example you've written each code more than once, like dono ke liye baar bar formula likhna padhra , but if jyou use funtion call then you can literally put a logical equation once, aur fir next time se tujhe sirf values place karne padege , and function khud solve kardega

# with function call

def percent(marks):
    p = ((sum(marks)/400)*100)
    return p

mark1= [22,23,64,75]
percent1 = percent(mark1)   #so now you dont have to enter any huge equation again and again.
print(percent1)

mark2= [34,57,86,72]
percent2 = percent(mark2)
print(percent2)

# so whenever there is a sambhaavna ki you are going to use this particular code in future toh use ek function mein wrap kardo, like yaha maine p nam ke function mein wrap kr




'''Quick Quiz: Write a program to greet a user with “Good day” using functions.'''
def greet(name):
    print("good day", name)
greet ("harry")