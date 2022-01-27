a= set()
print(type(a))
print(a)



##Adding values to an empty set
a.add(3)
a.add(4)
a.add(6)
a.add(3345)
a.add(33)
a.add(3345) #----it wont add the same element twice because set is an non repetitive elements
print(a)

    #YOU CANNOT ADD LIST in set
    # a.add([3,234,234])  

    #YOU CANNOT ADD DICTIONARY in set
    # a.add({234,2234,23423,4})

    #YOU CAN ADD TUPLE in set
a.add((23,2,24,64,26))
print(a)




### OPERATIONS ON SETS ###


## a.len() Printing the length of the set
print(len(a))

## a.remove() Removing a value from the set
a.remove(6)
    #a.remove(34) ---------throws an error: a.remove(34) KeyError: 34 because 34 isnot in the set
print(a)    #-removed 6

## a.pop()   Removing any arbitrary element from the set
a.pop()
print(a)    #removed any 1 element of the set


## a.clear()  Empties the set
a.clear()
print(a)

## a.union({a,b})    Returns a new set wuth all items from both sets i.e {ab}{jo claear kiya tha vo}
b = {23423,64,4}
    # b.union({342,234,2341,234})--aise NAHI DAALNA HAI, PRINT FUNCTION MEIN DAAAL
print(b.union({342,234,(324,324,3)}))
#VERSUS
print(b)


## a.intersection({a,b,c})   returns a set which contains only items in both sets i.e. in set a and in set{a,b,c}
d = {42324,234235,2,1,1,4,3,42,3242}
print(d.intersection({32,42,3,23,3242}))
    #so it printed 3242 as it was in both d as well as in {32,42,3,23,3242}
print(b.intersection({64,434,4}))   #printed only elements common in b and 64 434 4