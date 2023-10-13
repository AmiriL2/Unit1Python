import math
"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
#define square root as a
def square(a):

    #return the square of a number
    return a**2

#set the number equal to something
x = square(16)

#print the result
print(x)

"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
#define the variables
def area(l,w):

    #return the length times the width
    return l * w

#set the value of l and w
y = area(5,6)

#print the result
print(y)

"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def conversion(C):
    return (C * 1.8) + 32
F = conversion(10)
print("The current temperature is:", F,"°" )


"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""
#define
def average(A):

    #add all numbers together
    total = sum(A)
    
    #return total over nuber of items in list
    return total / len(A)

#print list of numbers
print(average([34, 667,35]))


