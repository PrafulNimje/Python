## Assignment - Calculator
x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))
print('1. Addition')
print('2. Substraction')
print('3. Division')
print('4. Multiplication')
choice = int(input('Enter your choice to perform calculation: '))
if choice ==1:
    z = x + y
    print(f'Addition of {x} and {y} is ',z)
elif choice ==2:
    z = x - y
    print(f'Substraction of {x} and {y} is ',z)
elif choice ==3:
    z = x / y
    print(f'Division of {x} and {y} is ',z)
elif choice ==4:
    z = x * y
    print(f'Multiplication of {x} and {y} is',z) 
else:
    print('Invalid choice')
