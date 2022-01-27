#program to display a user entered name followed by Goof Afternoon usin INput function

from typing import no_type_check_decorator


a="Good Afternoon "
b=input("Please enter your name\n")

c= a+b
print(c)

































#program to fill in a letter template gicsen below eith name and date

letter= '''Dear <|NAME|>,
\tYou are selected!\nWe are extremely happy announcing that you are a member
Date:<|DATE\> 
'''



date=input("Enter Date\n")

letter= letter.replace("<|NAME|>",b)
letter= letter.replace("<|DATE\>", date)

print(letter)

























#write a program to detect double spaces in a string

# story= "Hi I am harry   and i am really   handsome so  do you like me?\n\tOfcourse you might\n\tAfterall i am a coder"


# print(story)
# print(story.find("  ")) 
# #if there is double space it will show a positive number
# # if there is no double space it will show -1











#4) replace double spaces in problem 3 with single 


story= "Hi I am harry   and i am really   handsome so  do you like me?\n\tOfcourse you might\n\tAfterall i am a coder"


print(story)
print(story.find("  ")) 

story= story.replace("  ", " ")

print(story)

print(story.find("   "))

story= story.replace("  ", " ")

print(story)



































#Format the given letter:
# lettre= "Dear Harry, this python course is amazing. Thanks!"

lettre= "Dear Harry,\n\tThis python course is amazing.\n\tI am glad to be a part.\nThanks!"

print(lettre)