"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
cars = ["Audi", "Lexus", "Rolls Royce", "Nissan"]
print(cars)
# first i created a list of 4 cars, then i printed the list

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
cars.append("Mercedes-Benz")
print(cars)
# when you use append it adds something to the list, so you have to append a new element
# in my case it was merceded benz, so after i added it i used print()
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
cars.remove("Audi") 
print(cars)
# when you use .remove it removes an item, so in my case i removed audi
# now when i print the list it removed audi from it
"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
cars[3]= "BMW"
print(cars)
# when you have the index of an element in the list and you equate it to a new 
# element it will change to the new element you give it.

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""

cars.append("Ferrari")
cars.append("Mercedes-Benz")
cars.append("Acura")
print(cars)
# you have to append multiple times to add new elements to a list, so i did that and printed again
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
del cars[4]
print(cars)
#to delete an element from a specific index you use del and then the specific index you want to delete
"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
x = cars[:2] # takes the first items of the list and stires it in x(variabes)
print(x)# print new list
"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""

cars_1 = ['audi','lexus','BMW'] #make one list
cars_2 =['Maserati','Toyota'] # make a second list

CARS = cars_1 + cars_2 # extend the list by joining them