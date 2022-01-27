'''Chapter 7 – Practice Set'''

'''Write a program to print the multiplication table of a given number using for loop.'''
# my way
# num = int(input("enter a number: "))
# # for i in range(1,11):
# #     print(num, "x" , i , "=", i*num)

# # another way
# num = int(input("enter a number: "))
# for i in range(1,11):
#     print(str(num)+ "x" + str(i) + "=" + str(i*num))

# # another way
# num = int(input("enter a number: "))
# for i in range(1,11):
#     print(f"{num}x{i} = {num*i}")                    #this is using f string, so variables ko curly brakcets mein likho, kyuki curly bracks ke andar evaluation allowed hai
'''F string upar bataya'''

# # another way using while loop
# num = int(input("enter: "))
# i = 0
# while i<11:
#     print(num, "x", i , "=", i*num)
#     i = i+1













'''Write a program to greet all the person names stored in a list l1 and which starts with S.'''
# l1 = [“Harry”, “Sohan”, “Sachin”, “Rahul”]
# Attempt problem 1 using a while loop.


# l1 = ["Harry" , "Sohan", "Sachin", "Rahul"]
# for name in l1:
#     if name.startswith("S"):
#         print("hello", name)













'''Write a program to find whether a given number is prime or not'''
# trick here: IN CASE OF PRIME NUMBERS THE REMAINDER AFTER DIVIDING THEM IS NEVER ZERO EXCPET WITH "ITSELF" and "1"

# num = int(input("enter number: "))
# prime = True    #writing this so the program knows prime exists
# for i in range(2, num):
#     if (num%i == 0):
#         prime = False
#         break   #writing this so that ab aage check naa karo ek bhi baar 0 aaya to proof ho chuka h
# if prime:
#     print("PRIME")
# else:
#     print("Not prime")









'''Write a program to find the sum of first n natural numbers using a while loop.'''

#USING WHILE LOOP
# n = int(input("nmbr: "))
# sum = 0
# i = 0
# while i<n+1:
#     sum= sum + i
#     i = i + 1
# print(f"{sum}")         #toh sum =0 tha abb i ki value n (n+1 daalne se) tak badhte rahegi like if n = 4 then i will keep becoming 1+2+3+4 in sum



# USING FOR LOOP
# n = int((input("number")))
# sum = 0
# for i in range(1, n+1):
#     sum = sum +i
# print(f"sum of {n} is {sum}")
# # if i put n = 4 then i = (1, 5) = 1 2 3 4, matlab sum = 0 and with every loop 0+1+2+3+4










'''Write a program to calculate the factorial of a given number using for loop.'''

# factorial matlab of 4 is 4x3x2x1 = 4!


# n = int(input("number: "))
# factor = 1
# for i in range(1, n+1):    #i.e if n=4 then i=(1,)=123	 
#     factor= factor*i
# print(f"factorial of {num} is {factor})









'''Write a program to print the following star pattern.
'''  
# *
# **
# ***              for any number


# number = int(input("number enter kijye: "))
# for i in range(number+1):
#     print("*"*i)









'''Write a program to print the following star pattern:'''
#    *
#   ***
#  *****


# i wasnt able to do mai bass chaapri hu
# n=3
# for i in range(3):                  #i=012
#     print(" "* (n-i-1) ,end="")     #" "x (3-i-1)
#     print("*"* (2*i+1) ,end="")     #" "x (2xi+1)
#     print(" "* (n-i-1))             #" "x (3-i-1)

# you see ALL THESE 3 prints are pasted in the same line!!!!!! oonce for i=0 , i=2 i=3




'''Write a program to print the following star pattern:'''
# * * *
# *   *             #For n=3
# * * * 


# not done by me or taught answer taken from comment section
# side = int(input("Please Enter any Side of a Square  : "))
# print("Hollow Square Star Pattern") 
# for i in range(side):
#     for j in range(side):
#         if(i == 0 or i == side - 1 or j == 0 or j == side - 1):
#             print('*', end = '  ')
#         else:
#             print(' ', end = '  ')
#     print()





'''Write a program to print the multiplication table of n using for loop in reversed order.
'''
num = int(input("enter a number: "))
for i in range(-10,1):
    print(num, "x" , -i , "=", -i*num)

