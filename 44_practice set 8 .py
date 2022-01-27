# '''Write a program using the function to find the greatest of three numbers'''

# def max(num1, num2, num3):
#     if (num1>num2 and num1>num3):
#         print(num1)
#     elif (num2>num1 and num2>num3):
#         print(num2)
#     else:
#         print(num3)

# max(int(input("number1")),234,2)



# '''Write a python program using the function to convert Celsius to Fahrenheit.'''

# def celcius(degree):
#     return(((9/5)*degree)+32)
# d = int(input("Enter value in celcius scale to convert it in Farhenhite"))
# c = celcius(d)
# print("farhenhite is ", c)




# '''How do you prevent a python print() function to print a new line at the end?'''
# print("hello", end = " ")
# print("how",end = " wow ")
# print("are",end = " ")
# print("you",end = "")
# print("?")
# # so use ,end = " " to prevent new line addition



# '''Write a recursive function to calculate the sum of first n natural numbers.'''

# def sum(n):
#     if n==0 or n==1:
#         return 1
#     return n+ sum(n-1)

# print(sum(int(input("ENTER NUMBER WHOSE SUM has to be removed\n"))))



# '''Write a python function to print the first n lines of the following pattern'''
# '''
# ***

# **       #For n = 3

# *
# '''

# n= 3
# for i in range(n):
#     print("*"* (n-i))     #so its printing * , (n-i) times, i = (0,1,2) and n = 3, therefore 3-0,3-1,3-2

# '''Write a python function that converts inches to cms'''

# def conversion(inch):
#     print("the value of", inch , "inch in centimeter is " , inch * 2.54, "cm")

# conversion(int(input("ENTER VALUE IN INCHES: ")))




'''Write a python function to remove a given word from a STRING and strip it at the same time.'''
# what is strip?
# this = "    harry is good    "
# print(this)
# print(this.strip())


def remove_and_split(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()

this = "    harry is good boy  "

n=remove_and_split(this,"harry")
print(n)


'''Write a python function to print the multiplication table of a given number.'''

def multiply(n):
    for i in range (11):
        print(n,"x",i ,"=", n*i)
multiply(int(input("Get multiplication table of: \n")))


