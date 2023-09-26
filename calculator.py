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
else: 
    print("Invalid Input")