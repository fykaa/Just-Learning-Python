
# Code for finding Factorial usin loops
# n = int(input("n:\n")
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print("the factorial of", n, "is", product)

# Code for finding factorial using functions
# def factorial_iter(n):          #intersive factorial
#     product =1 
#     for i in range(n):
#         product = product* (i+1)
#     print(product)              #if you used "return product" then it wont have printed just kept the correct value in its system, fir tujhe har baar factorial ke sath prin(factorial(n)) karna padta, isliye maine function mein hi print daldiya
# factorial_iter(5)

'''RECURSIONS'''

# Now lets do the same factorial formulas using , RECURSION

# first let me tell you a basic law of factorials:
# n! = 1*2*3*4*5*...(n-1)*n
# Also,
# n!= (n-1)!*n                  #but remember if n becomes 1 or 0 it may falsify the formula, isliye make sure to write separate code for 1 and zero in n
# hence,

def factorial_recursive(n):
    if n==1 or n==0:            #base condition which doesnt call the function any further
        return 1
    return n*factorial_recursive(n-1)       #function calling itself

print(factorial_recursive(4))
# in above example of factorial_recursive ,what basically happened was:
'''factorial (4)   #function called
4 x factorial(3)
4 x [3 x factorial(2)]
4 x 3 x  [2 x factorial(1)]
4 x 3x 2 x    [1]          [function returned]
'''




# NOW LETS TAKE DEFINATIONS AND EXPLANATIOns from notess

'''Recursion'''
# Recursion is a function which calls itself.
# It is used to directly use a mathematical formula as a function. 


# For example:

    # n = int(input("numbrr"))
    # product= 1
    # for i in range(n):
    #     product = product * (i+1)
    # print(product)
    # so the above code is for getting factorial of any number. NOW USING FUNCIONS LETS CREATE A CODE JAHA KABHI BHI YOU CAN GET THE CODE FOR FACTORIAL

    # def factorial(n):
    #     product = 1
    #     for i in range(n):
    #         product = product * (i+1)
    #     return product

    # print(factorial(5))



# ANOTHER SIMILAR EXAMPLE AS DONE ABOVE EXPLANATION:

# factorial(n) == n*factorial(n-1)
# This function can be defined as follows:

def factorial(n):
	if i == 0 or i == 1 :                   #Base condition which doesn’t call the function any further
		return i
	else:
		return n*factorial(n-1)             #Function calling itself


# The programmer needs to be extremely careful while working with recursion to ensure that the function doesn’t infinitely keep calling itself.
# jaise ki abhi aapne base condition of i ==0 and 1 returning i nahi likha hota , fir toh function call karta reh jata , with 1-1 0-1 -1-1 -1-2 .... isse stack overflow hoga , memory exhaust hone ke baad , program kill hojayega.
# Recursion is sometimes the most direct way to code an algorithm.

