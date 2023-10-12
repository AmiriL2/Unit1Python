"""Task 1: Greeting Function
Write a function `greet(name)` that takes a name as a parameter and prints a greeting message like "Hello, [name]!".
"""
#define what greet is
def greet(name):

#print hello and then the name it is given
    print("Hello,",name + "!")

#the name for greet is Amiri
greet("Amiri")

"""Task 2: Sum of Two Numbers
Write a function `sum_numbers(a, b)` that takes two numbers as parameters and returns their sum.
"""
#define what sum_numbers is
def sum_numbers(a, b):

#print the addition of a and b
    print(a + b)

#a = 5 and b = 4
sum_numbers(5, 4)
"""
Task 3: Calculate Factorial
Write a function `factorial(n)` that calculates the factorial of a given number `n`.
"""
#define what factorial is
def factorial(n):
    #factorial is 1
    fact = 1
    # xzero has no factorial
    if n < 0:
       print("Sorry, this factorial does not exist")
       #factor is 0 for 0
    elif n == 0:
        print("The factorial is 0")
    else:
       #print factorial if it is greater than 0
       for i in range(1, n + 1):
           fact = fact * 1
    print("The fatcorial of " ,n, "is", fact)
    #factorial is 6
factorial(5)
"""
Task 4: Check Even or Odd
Write a function `is_even(num)` that takes a number as a parameter and returns `True` if the number is even, and `False` otherwise.
"""
#define what is_even is
def is_even(num):

# if number is divisible by 2 its even therefore print true
    if num%2 == 0: 
        print(True)

# otherwise print false
    else: 
        print(False)

# number equals 12        
is_even(12)
"""
Task 5: Calculate Area of a Rectangle
Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle given its length and width.
"""
#define what calculate_area is
def calculate_area(length, width):

    #print L * W which is area of rectangle
    print(length * width)

# L = 50 and W = 50
calculate_area(50, 50)
