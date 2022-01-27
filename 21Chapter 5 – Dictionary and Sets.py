#DICTIONARY
#  wrote using {}
# example:

mydict = {
    "sentences": "in a quick manner",
    "numbers": [3,4,2],
    "anotherdictionary": {'jerry', 'booyah', 'verdict'},
    "anotherdict": {'harry': 'coder', "shinchan": "nobita"},
    1:2
}

print(mydict['sentences'])  #-printted the complete sentences

print(mydict['numbers'])    #-printed all the numbers

print(mydict['numbers'][2])    #-printed ONLY the number with index 2--------Hence prooved that Dictionaries are Indexed

print(mydict['anotherdictionary']) #-printed complete dictionary BUT IN ANY ORDER-----------hence prooved dictionary is unordered

print(mydict['anotherdict']['harry']) #-prtinted ONLY harry's meaning in the dictionary

mydict['numbers']= [2,323,2]
print(mydict['numbers'])   #- Hence prooved that dictionaries are Mutable

mydict['sentences'] = 'not in quick manner alright'
print(mydict["sentences"])  #------again prooved that dictionary is mutable


'''PROPERTIES OF PYTHON DICTIONARY:
It's unordered 
It's Mutable
It's indexed
Cannot contain duplicate keys
'''


#To print all the keys of dictionary
print(mydict.keys())      
print(list(mydict.keys())) #-Prints the Keys of the dictionary same as print(mydict.keys())

#To print all the values of the dictionary
print(mydict.values()) 
print(mydict['anotherdict']['harry'])

# Type of this keys
print(type(mydict.keys()))   #-shows class as dictionary keys NOT strings or integers


