"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
x = 4.0

print(x)
print(int(x))
# make x a float by adding a decimal point and 0 
# after, print floating point to complete first part. 
# last convert using int() and put it inside print() to make an integer
"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
x = int(input("insert a number"))

if x > 0:
    print("positive")
elif x < 0: 
    print("negative")
else:
    print("zero")
# make x an input
#if x is greater than 0 print "positive"
#if x is less than 0 print "negative"
#if x is neither is has to be zero so print "zero"
"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
x = int(input("give me a number"))
y = float(input("give me anothe number"))

print(x + y)
print(x - y)
print(x * y)
print(x/y)

# request a number for x and make sure it only takes an integer
# take a number for y and make sure it is a float
# print x + y
# print x - y
# print x * y
# print x / y

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""


"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""


