'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''
task1 = int(input("please insert a number"))#allow the user input for the number
if task1 > 10 and task1 %2 == 0: #if the number is divisible by 2 and greater than 10 then print 2. 
                                #if both conditions are false or only one is true print false
    print("True")
else:
    print("False")
'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
age = int(input("please enter age"))#allow the user input for age
status = input("are you a student")#allow the user input for student status
if age < 18 or status == "yes":
    print("Ticket Cost: $10")#print result based on age or student status being true
else: 
    print("Ticket Cost: $20")

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
fruit = input("Please enter a fruit name")#allow the user input for fruit
FruitList = ["strawberries", "raspberries", "blueberries", "kiwi", "passionfruit"]#fruits on the list
if fruit in FruitList:
    print("Yes, that fruit is in the list.") #print result based on if fruit is in list or not
else: 
    print("No, that fruit is not in the list.")

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''
year = int(input("please enter a year"))#allow the user input for year
if year %100 == 0 and year %4 == 0: # if the year is divisible by 100 then it is a cenury year and 
                                    #if it is a leap year it is devidivle by 4
    print("This is a leap year and century year")# print result based on if both conditions are true. 
                                                #if only one is true then print the else statemnt
else:
    print("This is not a leap year or century year")
'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
weight = int(input("please insert weight of package"))#weight of package
zone = input("please insert which zone you are shipping to") #destination zone of package
if zone == "Zone B":
    print (weight * 7)# print the weight times 7 if zone is zone b
elif zone == "Zone A":
    print(weight * 5)#print the weight times 5 if zone is zone a
elif weight == 0:
    print("Invalid Weight")# if weight = 0 then an error message should pop up
'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''

a = int(input("please input a number"))
b = int(input("please input a number"))
c = int(input("please input a number"))

if a == b and b == c and c == a:
    print("This is an equilateral triangle") # if 2 sides are equal this is an equilateral
elif (a == b) or (a == c) or (c == b) and (a > b or a < b) or (c > a or c < a) or (b > c or b < c):
    print("this is an isosceles triangle") # if 2 sides are equal this is an isosceles
elif a != b and b != c and c != a:
    print("this is a scalene triangle")# if no sides are equal then is it a scalene
else: 
    print("not a triangle")#if none of these are true this is not a triangle

