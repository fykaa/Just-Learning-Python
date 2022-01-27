'''Functions with arguments'''
# A function can accept some values it can work with.
# We can put these values in the parenthesis.
# A function can also return values as shown below:

def greet(name):
	gr = "Hello" + name
	return gr
a = greet("Harry")          #“Harry” is passed to greet in name     # a will now contain "Hello Harry"


# similarly,
def mysum(num1,num2):
    return (num1 + num2)
s= mysum(231,12)
print(s)

def multiply(num1, num2):
	return (num1*num2)
m = multiply(1,14)
print(m)




