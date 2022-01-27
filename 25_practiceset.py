# #############
# mydict = {
#     "teri":"your",
#     "meri":"mine",
#     "uski":"theirs",
#     "sabki":"everyones",
# }
# print("Options are",mydict.keys())
# print(mydict.get(input("Enter the hindi word\n")))
# #another
# dictionary = {
#     "int":34,
#     "tu":"you",
#     "hmm":"floater",
#     "string":2
# }

# print("THE OPTIONS ARE",dictionary.keys())
# print("THE ANSWERS ARE", dictionary.values())
# print(dictionary.get(input("search in the dictionary\n")))


# # #############
# a=input("enter number 1: \n" )
# b=input("enter number 2: \n" )
# c=input("enter number 3: \n" )
# d=input("enter number 4: \n" )
# e=input("enter number 5: \n" )
# f=input("enter number 6: \n" )
# g=input("enter number 7: \n" )
# h=input("enter number 8: \n" )
# i = {a,b,c,d,e,f,g,h}
# print(i)


# ##############################
# a = {324,23,"dfsd",324,18,"18","ab","18"}
# print(a)    #Yes a set can have 18 as an integer and string twice


# ##################
# s = set()
# s.add(20)
# s.add(20.0)
# s.add(20.)
# s.add(20.5)
# s.add("20")
# print(s)
# print(len(s))   #CONCLUSION THAT a INTEGER AND A FLOATING POINT NUMBER SUMMED UP TO THE SAME


# ###################

# s={}
# print(type(s))
# # dictionasry



###########

# dictionary = {
#     "harry": input("Harry's favourite language\n"),
#     "Jack" : input("Jack's favourite language\n"),
#     "Jessica" : input("Jessica's favourite language\n"),
#     "Kishan": input("Kishan's favourite language\n")
# }
# print(dictionary)

# #ANOTHER WAY
# favlang = {}
# a =input("enter your favourite language shubham\n")
# b =input("enter your favourite language jack\n")
# c =input("enter your favourite language jacky\n")
# d =input("enter your favourite language kishan\n")
# favlang['shubham'] = a
# favlang['jack'] = b
# favlang['jacky'] = c
# favlang['kishan'] = d
# print(favlang)














# ###########################

# favlang = {}
# a =input("enter your favourite language shubham\n")
# b =input("enter your favourite language jack\n")
# c =input("enter your favourite language jacky\n")
# d =input("enter your favourite language kishan\n")
# favlang['shubham'] = a
# favlang['jack'] = b
# favlang['jack'] = c
# favlang['kishan'] = d
# print(favlang)      #JACK SIRF EK BAAR PRINT HUA 




#################################

# favlang = {}
# a =input("enter your favourite language shubham\n")
# b =input("enter your favourite language jack\n")
# c =input("enter your favourite language jacky\n")
# d =input("enter your favourite language kishan\n")
# favlang['shubham'] = a
# favlang['jack'] = a
# favlang['jacky'] = c
# favlang['kishan'] = d
# print(favlang)   #koi naa kardegi print











###############################3
# s = {8,7,12,"harry",[1,2]}            
#  stuffs under []  is a list
#  list is unhashable (cant be put) in a set toh question is wrong this set will throw an error
# so add a tuple instead
# stuffs under () is a tuple
s = {8,7,12,"harry",(1,2)}
# we cannot change a set as it is UNINDEXED
# answer: list isnt allowed in set AND tuple change nahi ho sakta kyuki vo hashable(unchangable) hota 



