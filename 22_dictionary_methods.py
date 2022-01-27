mydict = {
    "sentences": "in a quick manner",
    "numbers": [3,4,2],
    "anotherdictionary": {'jerry', 'booyah', 'verdict'},
    "anotherdict": {'harry': 'coder', "shinchan": "nobita"},
    1:2
}

print(mydict)

#a.items()--------retuns a lst of (keys,values) tuples ke form me
print(mydict.items())

#a.keys()----------retursn a list of containing dictionary keys
print(mydict.keys())

#a.values()----------returns a list of values of the dictionasry
print(mydict.values())

#a.update({"friends":"sam"})--------updates dictionary with given key value pairs
mydict.update({"numbers":"ab ye no. nahi rha"}) #----changed the previous keyvalue pair
mydict.update({"legend":"fia"})                 #-----updated a new keyvalue pair
print(mydict)

#list(a.keys)
print(list(mydict.keys()))

#a.get("name")------------------returns value of specified keys and value is returned eg. "Harry" is returned here
print(mydict.get("sentences"))    #looks similar as print(mydict["sentences"]) BUT it has a differencce!!!!!!!!!!!!!!
print(mydict["sentences"])
#difference between .get and [syntax in dictionary]
print(mydict.get("kuchbhi"))  #----Returns NONE as kuchbhi is not present in the dictionary
print(mydict["kuchbhi"])       #----Throws ERROR as kuchbhi is not present in the dictionary
'''hence this was the major difference between a.get for values and a[] for values ::::::::this is an interview favourite question'''


#for more methods of the dictionary search python methods for dictionary on docs.python.org


