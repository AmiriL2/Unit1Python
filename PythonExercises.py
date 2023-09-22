import math
'''
TASK 1 Even or Odd
Determine if a number is even or odd.
'''
number = int(input("please insert number"))
if (number %2) == 0: 
    print("this number is even")
else: 
    print("this number is odd")
#if the number is divisible by 2 then it is an even number.
#if not then it is a odd number
'''
TASK 2 Positive, Negative, or Zero:
Determine if a number is positive, negative, or zero.

EXTRA CREDIT: Tell the user if they did not enter a valid number
'''
x = int(input("insert a number"))

if x > 0:
    print("positive")
elif x < 0: 
    print("negative")
else:
    print("zero")

#make x an input
#if x is greater than 0 print "positive"
#if x is less than 0 print "negative"
#if x is neither is has to be zero so print "zero"
'''
TASK 3: Largest of Three
Find and print the largest of three numbers.
'''
y = max(5, 10, 25)
print(y)
 #choose any 3 number
 #the maximum(largest) number is the only number tht would be printed
'''
TASK 4: Leap Year
Determine if a year is a leap year or not.
'''
BirthYear = int(input("please insert you birth year"))
if BirthYear % 4 == 0:
    print("Congratulations, you were born on a leap year")
else: 
    print("Sorry, you were not born on a leap year")
# if your birth year is divible by 4 then print they were born on a leap year
# if not then print it is not a leap year
'''
TASK 5: Vowel or Consonant:
Identify if a character is a vowel or consonant.

EXTRA CREDIT: Tell the user if they did not enter a valid letter
'''

letter = input("pick a letter in the alphabet")

if letter == "a" or letter == "e" or letter == "i" or letter ==  "o" or letter == "u":
    print("That is a vowel")
else:
    print("this is a constant")
#if letter is equal to a,e,i,o or u then it will print that it is a vowel. 
#if it is not any of those then it is a constant
