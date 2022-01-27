
'''The break statement'''
# ‘break’ is used to come out of the loop when encountered. It instructs the program to – Exit the loop now.

'''Example:'''

for i in range(0, 80):
	print(i)	#This will print 0, 1, 2 and 3
	if i == 3:
		break




# Difference between else and break
for i in range(10):
	print(i)
	if i==5:
		break
else:
	print("this is inside else of for")	#not printed this hence so you see the loop isnt breaking after exhaustion by loop rather from break  used 
