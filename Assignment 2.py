#1) wap to reverse a 4 digit number without using loop
#1234  , 4321

n = int(input("Enter number:  "))
r1 = n%10
q1 = n//10
r2 = q1%10
q2 = q1//10
r3 = q2%10
q3 = q2//10
print(r1,r2,r3,q3)

#2) wap to calculate total bill
#noitem, price of item ,gst ,totalbill =?

no_of_items = int(input("Enter number of items: "))
price_of_items = float(input("Enter price of items: "))
gst = float(input("Enter GST: "))
totalbill = (no_of_items * price_of_items) + (no_of_items * price_of_items * gst)/100
print("Number of items: ",no_of_items)
print("Price of items: ",price_of_items)
print("GST% is = ",gst)
print("Amount: ",(no_of_items * price_of_items))
print("GST amount: ",(no_of_items * price_of_items * gst)/100)
print("Total Bill: ",totalbill)

#3)write a python program to calculate number of dot balls and total number of runs 
#total ball faced by batsman = 
#no of 1 
#no of 2
#no of 3
#no of 4
#no of 6
# Input the number of balls faced by batsman
balls_faced = int(input("Enter the total number of balls faced by batsman: "))

# Input the number of 1s, 2s, 3s, 4s, and 6s scored by batsman
num_1s = int(input("Enter the total number of 1s scored: "))
num_2s = int(input("Enter the total number of 2s scored: "))
num_3s = int(input("Enter the total number of 3s scored: "))
num_4s = int(input("Enter the total number of 4s scored: "))
num_6s = int(input("Enter the total number of 6s scored: "))

# Calculate the total number of runs scored
total_runs = (num_1s + (2 * num_2s) + (3 * num_3s) + (4 * num_4s) + (6 * num_6s))

# Calculate the number of dot balls
dot_balls = balls_faced - (num_1s + num_2s + num_3s + num_4s + num_6s)

# Print the results
print("Total runs scored:", total_runs)
print("Number of dot balls:", dot_balls)


#4)wap for deposit of atm, check for given conditions
#dmt=? , dmt%100  , dmt>=100
#show deposited amount as well as update balance amount
#show the time of when amount is deposite

import datetime

balance = float(input("Enter Balance amount: "))
dmt = int(input("Enter the deposit amount: "))
if dmt >= 100 and dmt % 100 == 0:
    balance += dmt  
    print("===== Receipt ====")
    print(f"Deposited amount: {dmt}")
    print(f"Updated balance amount: {balance}")
    print(f"Time of deposit: {datetime.datetime.now()}")
else:
    print("Deposit amount should be greater than or equal to 100 and a multiple of 100.")
)
