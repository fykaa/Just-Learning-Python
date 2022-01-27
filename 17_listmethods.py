'''l1.sort() -------- >  sorts the list'''
# correct way of sorting list
l1 = [1,7,3,8,43,23,11]
print(l1)
l1.sort()
print(l1)
# incorrectway of sorting list
l1_sorted = l1.sort()
print(l1_sorted)


'''l1.reverse() --------- >  reverses the list'''
l1.reverse()
print(l1)

'''l1.append() ---------- > Adds at the end of the list'''
l1.append(45)
l1.append("hello")
print(l1)


'''l1.insert(a,b) -----> Inserts b in l1 such that 'index of b' becomes 'a' '''
l1.insert(4,544)   #so you see now 544 ki index 4 hai
print(l1)



'''l1.pop(a) ------------- >  will delete elemant at "index a" '''
l1.pop(2)
l1.pop(8)
print(l1)   #-----toh dekho 11 fir hello nikal gaya


''' l1.remove(a) -----------> will remove a from l1 '''
l1.remove(3)
print(l1)