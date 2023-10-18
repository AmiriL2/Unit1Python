#if using try, when the user inputs a string it gives an error
try:
    age = int(input('Enter your age: '))
    #runs even when error occurs
except:
    print("Invalid Number, please try again.")

#asking user for their favorite number
faveNum = int(input('What is your favorite number: '))

#if statement for when age is less than or equal to 21
if age <= 21:
 
 #print they are too young
 print('You are not allowed to enter, you are too young.')

#when if statment is false then this will run
else:
 print('Welcome, you are old enough.')

#use try because when user inputs 0  fro fav number it will cause an error
try:
    print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)

#if the error runs then this happen
except:
   print("This numbver cannot be divided by 0, pleae select a different number")