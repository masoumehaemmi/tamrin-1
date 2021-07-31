import math

number_1 = int(input("Enter your the first number: "))
number_2 = int(input("Enter your the second number: "))

operation = input('''
Please type in the math operation you would like to complete:
+ sum
-  subtraction
* multiplication
/ division
** power
sin  sinus
cos  cosinus
tan  tanzhant
rad  sqrt
fac factorial

''')

if operation == '+':
    output_number = number_1 + number_2
    print( "{} + {} = {}" .format(number_1, number_2, output_number))
elif operation == '-':
    output_number = number_1 - number_2
    print( "{} - {} = {}" .format(number_1, number_2, output_number))
elif operation == '*':
    output_number = number_1 * number_2
    print( "{} * {} = {}" .format(number_1, number_2, output_number))
elif operation == '/':
    output_number = number_1 / number_2
    print( "{} / {} = {}" .format(number_1, number_2, output_number))
elif operation == '**':
    output_number = number_1 ** number_2
    print( "{} ** {} = {}" .format(number_1, number_2, output_number))
elif operation == 'sin':
    output_number = math.sin(number_1)
    print( "sin = {}" .format(number_1))
elif operation == 'cos':
    output_number = math.cos(number_1)
    print( "cos = {}" .format(number_1)) 
elif operation == 'tan':
    output_number = math.tan(number_1)
    print( "tan = {}" .format(number_1)) 
elif operation == 'rad':
    output_number = math.sqrt(number_1)
    print( "sqrt = {}" .format(number_1))          
elif  operation ==  'fac':
    output_number = math.factorial(number_1)
    print( " fac  = {}" .format(number_1))   
else:
    print('enter operation! try again.')

