#1) wap to print square of all the number between 50 to 75
for i in range(50, 76):
    print(i * i)

#2) wap to print number in reverse order from 1000 to 850

for i in range(1000, 849, -1):
    print(i)

#3) wap to calculate factorial of a number

n = int(input("Enter a number: "))
fact = 1

for i in range(1, n+1):
    fact *= i

print("Factorial of", n, "is", fact)

#4) wap to check a number is palindrom or not 
num = int(input("Enter a number: "))
num_str = str(num)
num_reverse = int(num_str[::-1])
if num == num_reverse:
    print("The number is palindrome")
else:
    print("The number is not palindrome")

#5) wap to print all the armstrong number in range of 100 to 1000

for num in range(100, 1000):
    num_of_digits = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** num_of_digits
        temp //= 10
    if num == sum:
        print(num)

#6) wap to check a number is a prime number or not
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")

