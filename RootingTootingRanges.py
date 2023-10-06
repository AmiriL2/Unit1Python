"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
# for all the items in the range
for x in range(1, 11):

    #print all the numbers in the range
    print(x)

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
# for all of the numbers in the range ( third in the parenthesis are how much the numbers will be going up by)
for y in range(900, 1001, 10):

    #print in increments of 10 till 1000 from 900 
    print(y)
"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
#for all of the numbers in the range (going up in increments of 9)
for t in range(0, 100, 9):

    #print from 0-100 in increments of 9
    print(t)

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
#this is so that the original sum is set to zero
total = 0

#for all the items in the range
for u in range(1, 11):
   
   #add the total plus the numbers in the range
   total += u

   #print all of the totals
   print(total)
"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?"""
#The output of the code is 15 individual rows of stars
"""
- Explain the iterative process that this code executes to get that output
"""
#the value of rows is 5
rows = 5

# for the amount of rows in the range (1,2,3,4,5)
for i in range(rows):

    #add one to the amount in each line for each row(5 rows)
    for j in range(i + 1):

        #print a star and add one after one row until 5
        print('*', end=' ')
        
        #print out 
    print()