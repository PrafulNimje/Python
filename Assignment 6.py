#1) sort values in a list without using predefined method
my_list = [5, 1, 3, 8, 2]
print("Before sorting")
print(my_list)
for i in range(len(my_list)):
    for j in range(i+1, len(my_list)):
        if my_list[i] > my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]
print("After sorting")
print(my_list)


#2)remove the all the repeation of a number except first in a list

l = [10, 20, 10, 20, 30, 40, 20, 10]
print(l)
e = int(input("Enter number you want to remove from list: "))
flag = False
result = []

for num in l:
    if num == e and not flag:
        result.append(num)
        flag = True
    elif num != e:
        result.append(num)

print(result)


#ATM program

userlist = ["Raj", "Kartik", "Nikhil"] 
amounts = [10000, 20000, 5000]  
upins = [1234, 5678, 9876] 

for i in range(4):  
    name = input("Enter your name: ")
    if name in userlist:
        pin = int(input("Enter your PIN: "))
        index = userlist.index(name)
        if pin == upins[index]:
            print("Welcome,", name)
            while True:
                print("Please select an option:")
                print("1. Withdraw")
                print("2. Deposit")
                print("3. Show balance")
                print("4. Exit")
                choice = int(input("Enter choice (1-4): "))
                if choice == 1:  # Withdraw
                    amount = int(input("Enter amount to withdraw: "))
                    if amount % 100 == 0 and amount <= amounts[index] and amount >= 100:
                        amounts[index] -= amount
                        print("Withdrawn amount:", amount)
                        print("Updated balance:", amounts[index])
                        cont = input("Do you want to continue? (y/n): ")
                        if cont == "n":
                            break
                    else:
                        print("Invalid amount")
                elif choice == 2:  # Deposit
                    amount = int(input("Enter amount to deposit: "))
                    if amount % 100 == 0 and amount >= 100:
                        amounts[index] += amount
                        print("Deposited amount:", amount)
                        print("Updated balance:", amounts[index])
                        cont = input("Do you want to continue? (y/n): ")
                        if cont == "n":
                            break
                    else:
                        print("Invalid amount")
                elif choice == 3:  # Show balance
                    print("Your current balance is:", amounts[index])
                    cont = input("Do you want to continue? (y/n): ")
                    if cont == "n":
                        break
                elif choice == 4:  # Exit
                    break
                else:
                    print("Invalid choice")
        else:
            print("Invalid PIN")
    else:
        print("Invalid user")
print("Maximum tries exceeded")
