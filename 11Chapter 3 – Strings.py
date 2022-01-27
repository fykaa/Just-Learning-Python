# a='harry' #single quoted string
# b="johny" #double quoted string
# c='''jacky''' #triple quoted string
# print(a)
# print(b)
# print(c)





#STRING SLICING
'''A string can be sliced for getting a part of the string
consider the followng strings
Name= "harry" ------------length is 5
       01234  ------------these are representations of each character of the string
    -5-4-3-2-1------------this representation can be used for backward characthers
    
    '''
    # the index in a sstring starts from 0 to (length-1) 
    # another way to write the index is from the end that is negative indices 
    # in order to slice the string we will use following syntax.



greeting = "good morning "
name = "harryji"
# Concatenating two strings
print(greeting  + name)

print(name [0:2]) #-------here the boxes are used for string slicing here it will take 0 and 1
print(name[-5:-2]) #-----here we used negative indices for slicing here it will take -5 -4 and -3
# THE ABOVE IS SAME AS print(name[3:6])

# so as seen [last ka ek index chorrtha hi hai]


print(name[1])     #harry mein 01234 me 1 pr a hai
print(name[-3])       #harry mein -5-4-3-2-1 mein -3 pr r hai

# name[1] = "d" ------>doesnt works!


print("A UNIQUE FEAUTURE OF SLICING")
print(name[:])     #----> will print everything in name, is same as print(name)
print(name[:5])    #----> is same as name[0:5]
print(name[-5:])   #----> here -1 is also printed
print(name[-5:-1]) #----> here -1 will not be printed
print(name[-5:0])  #----> here it wont print anything
print(name[:4])    #----> is same as name[0:4]
print(name[0:])    #----> is same as name[0:7]
print(name[0:7])   #proof




