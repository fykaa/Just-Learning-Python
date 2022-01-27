Story= "once upon a time there was a youtuber named Harry who uploaded python course with notes, thanks harry Harry"

#STRING FUNCTIONS

'''Some of the functions used to perform operatioms or manipulate strings are
 
1) Lens() function- This returns the length of the string'''
   
print(len(Story)) #->upar di gayi story mein 87 character hai 
print(len("harry")) #-> harry mein 5 character hai

'''
2) String ends with _____
this function tells us whethr string ends with ___ or not , if yes then it will show true or false'''
 
print(Story.endswith("notes"))
print(Story.endswith("harry"))

'''
3) String Count("c")
counts teh total number of occurence of character'''

print(Story.count("a")) #soit will count no. of a in story
print(Story.count("Harry"))
print(Story.count(" "))

'''
4) String Capitalise
this will capitalise the first word according to grammer'''

print(Story.capitalize()) #so it has capitalized O in once upon a time as per grammer


'''
5)String find (word)
this will find a word and returns the index of "first occurence" of that word in the string'''

print(Story.find("once"))  #--shows 0 as position of once in story is 0
print(Story.find("upon"))  #--shows 5 as position of upon in story is 5 i.e once_ = 01234    and AT 5TH COMES UPON..............also it showed only the first occurance
print(Story.find("hary"))  #--shows -1 as position of hary in story doesnt exists


'''
6)String replace(oldword, newword)
replaces the old word with new'''

print(Story.replace("Harry","Pushpa"))

letter= "hi harry you are pretty"
b= "pushpa"
letter= letter.replace("harry",b )
print(letter)
#so here we replaced all Harry with Pushpa BUT harry wasnt replaced because python is case sensitive