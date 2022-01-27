'''Write a program to find the greatest of four numbers entered by the user.'''
# a = int(input("ENTER NUMBER 1: "))
# b = int(input("ENTER NUMBER 2: "))
# c = int(input("ENTER NUMBER 3: "))
# d = int(input("ENTER NUMBER 4: "))

# if(a>b and a>c and a>d):
#     print("the greatest no. is", a)
# elif(b>a and b>c and b>d):
#     print("the greatest no. is", b)
# elif(c>a and c>b and c>d):
#     print("the greatest no. is", c)
# else:
#     print("the greatest no. is", d)
    
















'''Write a program to find out whether a student is pass or fail if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user'''

# science = int(input("percentage in science: "))
# hindi = int(input("percentage in hindi: "))
# maths = int(input("percentage in maths: "))


# if(science>33 and hindi>33 and maths>33 and science/100+maths/100+hindi/100>=0.4):
#     print("Congratulations you are passed!")
# else:
#     print("Failed")


# # another way
# if(science<33 or maths<33 or hindi<33):
#     print("failed")
# elif((science+maths+hindi)/3 <40):
#     print("faild cause less than 40%")
# else:
#     print("pass")


'''A spam comment is defined as a text containing the following keywords:
“make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.'''

# text = input("Enter the text: \n")

# if("make money fast" in text):
#     spam = True
# elif("buy now" in text):
#     spam = True
# elif("subscribe this" in text):
#     spam = True
# elif("click this" in text):
#     spam = True
# else:
#     spam = False

# if(spam):
#     print("This is Spam tetx")
# else:
#     print("This isnt spam ")




'''Write a program to find whether a given username contains less than 10 characters or not.'''
# text = input("Enter Username:\n")

# if(len(text) < 10):
#     print("Username not valid as less than 10 numbers")
# else:
#     print("WOW! Nice Username")




'''Write a program that finds out whether a given name is present in a list or not.'''

# names = ["harry", "potter", "sert", "wow", "fake", "path"]
# name = input("ENTER A NAME: \n")

# if name in names:
#     print("congrats youre a part")
# else:
#     print("fack off")














'''Write a program to calculate the grade of a student from his marks from the following scheme:'''
# 90-10 Ex
# 80-90	A
# 70-80	B
# 60-70	C
# 50-60	D
# <50	F

# grade = int(input("Enter your Marks"))
# if(grade>90):
#     print("Ex")
# elif(grade>80):
#     print("A")
# elif(grade>70):
#     print("B")  
# elif(grade>60):
#     print("C")  
# elif(grade>50):
#     print("D")  
# else:
#     print("Fail")





'''Write a program to find out whether a given post is talking about “Harry” or not.'''


p = input("enter post\n")

if ("harry" in p):
    print("yea")
else:
    print("no")
