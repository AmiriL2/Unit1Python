"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
x = 1
while x < 10:
    print(x)
    x +=1

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
y = 10
while y > 0:
    print(y)
    y -= 1
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
#ask for a number
num = int(input("Please input a number: "))

#set variable as one
factorial = 1 

#if the number is less then cant be done
if num < 0: 
   print("Sorry, factorial does not exist for negative numbers")

#if the num they enter is = to 0 then the factorial is 1
elif num == 0: 
   print("The factorial of 0 is 1")

#if none of this is correct then we add one and multiply by it
else:
   for i in range(1,num + 1): 
       factorial = factorial*i
   print("The factorial of: ",num,"is",factorial) 

"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
password = ['amiri1234'] #makes password
guesses = 0
#Gives the user 5 chances
while guesses < 5: 
    #Makes foorloop to see if the guess if in password
    for i in password : 
        #Creates the guess input
        guess = input('Please attempt to guess the password: ') 
    if guess in password:
        #if correct then it will print
        print(' Correct! ' + guess + ' is the password: ')
        break #Stops the code
    else:
        # if its wrong this prints
        print('Wrong. ') 
         #adds 1 to the guesses

    guesses += 1

if guess in password:
  print()
else:
  #prints when the tries are done
  print("Sorry you have no more tries") 

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""
#creation of the takeSum() function
def takeSum(n): 
    
    #sets sum to 0
    sum = 0 

    #While n parameter doesnt equal 0 then the following runs
    while (n != 0): 
       
       #sets the sum = to the sum plus the parameter modulus 10
        sum = sum + (n % 10) 
        #floor divides the parameter n by 10 to
        n = n//10 
    #returns the sum when this function is called
    return sum 
   
num = int(input('Please input a whole number: ')) #asks user for an int input
print(takeSum(num), "is the sum of the digits within this number") #calls and prints the function with input of the uses

"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""