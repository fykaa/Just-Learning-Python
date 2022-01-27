 
'''Relational Operators'''
# Relational operators are used to evaluate conditions inside if statements. Some examples of relational operators are:
# = = -> equals

# >=  -> greater than/equal to

# <=, etc.


''' example'''

# age= int(input("enter your age: "))
# if(age>18):
#     print("yes greator than 18")
# elif(age==18):
#     print("yes age is 18")
# else:
#     print("No age is less than 18")










'''Logical Operators'''
# In python, logical operators operate on conditional statements. Example:
# and -> true if both operands are true -----------------else false ---------------matlab if tab hi print karega jab and ke saat ke dono poernds true hai

# or -> true if at least one operand is true-------------else false ----------------malab if tab hi print karega jab or ke saath ke koi bhi ek operand true hai

# not -> inverts true TO false --------------------------and false TO true --------- matlab if taab print karega jab diya gaya operand true nahi hai

'''example 1'''
# number= int(input("Enter a number to find its range: "))
# if( number>1 or number<-1):
#     print("This is range of cosec")
# elif(number<1 or number>-1):
#     print("this is the range of sin or cos")
# else:
#     print("no")
'''example 2'''
# number= int(input("Enter a number: "))
# if( number>180 and not number>360):
#     print("WOW 180 HUH, dont cross 360")
# elif(not number>180):
#     print("sheh so small")
# else:
#     print("idk")









'''elif clause'''
# elif in python means [else if]. If statement can be chained together with a lot of these elif statements followed by an else statement:
# '''
# if (condition1):
#     #code
# elif (condition 2):
#     #code
# elif (condition 2):
#     #code
# ….
# else:
#     #code    '''
'''The above ladder will stop once a condition in an if or elif is met'''



# Important Notes:

# There can be any number of elif statements.
# Last else is executed only if all the conditions inside elifs fail.
# 'if' is always execceuted when prooved true, whereas 'elif' is executed only when above operands are fals


# text = input("Enter the text")

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

