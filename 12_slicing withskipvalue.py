#Slicing with Skip Value
# in [a:b:c] here a is starter b is ender but c is the value after wich intervals characters will be skipped

a= "harryji"
print(a[0::1]) #har pehle character ko print karo/ skip 0 after each character
print(a[0::2]) #har dusre character ko print karo/ skip 1 after each character
print(a[0::3]) #har tisre character ko print karo/ skip 2 after each character
print(a[0::4]) #har fourt character ko print karo/ skip 3 after each character


b= "amazing" #---0123456
print(b[1:6:2]) #mazin so MaZiN i.e mzn is answer   so here 12345 index will be taken i.e mazin , then 1 character will be skipped after each i.e mzn
print(b[1:7:2]) #mazing so MaZiNg i.e mzn is answer
