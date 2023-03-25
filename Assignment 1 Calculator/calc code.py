print('To Choose your desired operation,Press:')
print('1. For Addition')
print('2. For Subtraction')
print('3. For Multiplication')
print('4. For Division')

operation = input()
if operation == '1':
    num1 =input('Enter first number: ')
    num2 = input('Enter second number: ')
    print('The sum is ' + str(int(num1)+ int(num2)))
elif operation == '2':
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')
    print('The difference is ' + str(int(num1)-int(num2)))
elif operation == '3':
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')
    print('The result is ' + str(int(num1)* int(num2)))
elif operation == '4':
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')
    print('The result is ' + str(int(num1)/int(num2)))
else:
    print('Invalid choice. Please select a valid operation.')
input()

