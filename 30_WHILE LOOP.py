'''While loop'''
# The syntax of a while loop looks like this:
# ''' while condition:
    #Body of the loop '''

# The block keeps executing until the condition is true/false
# In while loops, the condition is checked first. If it evaluates to true, the body of the loop is executed, otherwise not!
# If the loop is entered, the process of condition check and execution is continued until the condition becomes false.

'''exmaple'''
i = 0
while i<5:
    print("Harry",str(i))
    i = i+1   #this kept increasing i every time in the loop so that i=1 i=2 i=3 i=4 aate rahe varna ye loop kabhi khatam nahi hota
print("done")
# (Above program will print Harry 5 times)
# Note: if the condition i<5 never becomes false, the loop keeps getting executed!

#again
# i = 0
# while i<5:
#     print("Harry",str(i))
#     i = i+1   #this kept increasing i every time in the loop so that i=1 i=2 i=3 i=4 aate rahe varna ye loop kabhi khatam nahi hota
#     print("done")
#ye jo code hai isme print(done) loop ke andar aaraha hai 

'''Quick Quiz: Write a program to print 1 to 50 using a while loop'''
# i=1
# while i<=50:
#     print(i)
#     i=i+1


# wE Generally use 'False while' jaha condition ek point pr false ho jati hai
# sometimes 'true while' is used jahaa condition kabhi false nahi hoti isliye infinite print hote rehta hai.


'''example'''
# write a program to print the content of a list using while loop
from types import FrameType


# i= 0
# fruit = ["apple" ,"anana" ,"chappal" ,"hi"]
# while i<len(fruit):
#     print(fruit[i])
#     i= i+1


i=0
list = ["grapes", "banana", "chiku", "samosa"]
while i<len(list):
    print(list[i],str(i))
    i= i+1

