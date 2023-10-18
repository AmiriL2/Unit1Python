import math
"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
#define square root as a
def square(a):

    #return the square of a number
    return a**2

#if the function = 256, the assert will not return anything/ function will fun normally
assert square(16) == 256

#print the result
print(square(16))

#16 squared is not 256 so assertionerror will return
assert square(16) == 265


"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""
#define the variables
def area(l,w):

    #return the length times the width
    return l * w

#if function = 30, function will not return an error and proceed normally
assert area(5,6) == 30

#5 * 6 does not equal 27 so assertion error will return
assert area(5,6) == 27

#print the result
print(area(5,6))

"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def conversion(C):
    return (C * 1.8) + 32

#function is equal to 50, so functuon will continue as normal
assert conversion(10) == 50

print("The current temperature is:", conversion(10),"°" )

#10 degrees C is not 49 degrees F so assertion error will return
assert conversion(10) == 49

"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""
#define
def average(A):

    #average function will return 44 so no error will occur and will proceed as normal
    assert average([30, 66,36]) == 44
    
    #return total over nuber of items in list
    return sum(average([30, 66,36])) / len(A)

#average of 30, 66, and 36 is not 45, so assertion error will return
assert average([30, 66,36]) == 45

