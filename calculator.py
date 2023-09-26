import math

uno = float(input('Insert First Number'))
dos = float(input('Insert Second Number'))
#allow the user to insert number
print('''
add = Addition
Sub = Subtraction
multi = Multiplication
div = Division
flordiv = Floor Division
expo = Exponents
remain = Remainder
''') #give out the certain options that the user can choose from

input = input('Pick: ') #tell user to pick which operation to use

if input == 'add':
    print(uno + dos)
elif input == 'sub':
    print(uno - dos)
elif input == 'multi':
    print(uno *  dos)
elif input == 'div':
    if dos == 0:
        print('this equation cant be done')
    else:
        print(uno / dos)
elif input == 'flordiv':
    if dos == 0:
        print('this equation cant be done')
    else:
        print(uno // dos)
elif input == 'expo':
    print(uno ** dos)
elif input == 'remainder':
    print(uno % dos)
    #if the user chooses of the options then this is the code that will go through to find out
    # which one was chosen and how to find the answer to the equation
else: 
    print("Invalid Input")# if the user inserts something that was not given as an option, print out that the input is invalid