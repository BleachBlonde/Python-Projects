def add(x,y):
    return (x+y)
def subtract(x,y):
    return (x-y)
def multiply(x,y):
    return (x*y)
def divide(x,y):
    return (x/y)
print('\t\t\tCALCULATOR version 1.0')
print('Choose one of the following functions:\n')
print('1. Addition')
print('2. Subraction')
print('3. Multiplication')
print('4. Division')

choice= input('\nEnter operation: 1, 2, 3, 4: ')

if choice == '1':
    print("You've chosen addition.")
    num1= int(input('\nEnter first number: '))
    num2= int(input('Enter second number: '))
    print(add(num1,num2))

elif choice == '2':
    print("You've chosen subtraction.")
    num1= int(input('\nEnter first number: '))
    num2= int(input('Enter second number: '))
    print(subtract(num1,num2))

elif choice == '3':
    print("You've chosen multiplication.")
    num1= int(input('\nEnter first number: '))
    num2= int(input('Enter second number: '))
    print(multiply(num1,num2))

elif choice == '4':
    print("You've chosen division.")
    num1= int(input('\nEnter first number: '))
    num2= int(input('Enter second number: '))
    print(divide(num1,num2))
   
else:
    print("\nInvalid input")
