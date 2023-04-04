
#1) find the square of every item in a list and store them in another list name sqlist

my_list = []  
sqlist = []
n = int(input("Enter the number of elements you want to add to the list: "))

for i in range(n):
    element = int(input("Enter element: "))  
    my_list.append(element)  

print("User-defined list: ", my_list)  

for num in my_list:
    sq = (num ** 2)
    sqlist.append(sq)
    
print("Original list:", my_list)
print("Square list:", sqlist)

#2) wap to print sum of all elements of list without using predefined function
my_list = [10, 20, 30, 40, 50]
sum = 0
for i in my_list:
    sum += i
print("The sum of all elements in the list is:", sum)

#3)find the element is present in a list or not  without using predefined function
#   ii) if element is found find its number of occurance without using predefined function
#   iii) print all position where element is found without using predefined function

my_list = [4, 3, 7, 2, 8, 2, 9, 2]
element = int(input("Enter the element you want to search in the list: "))
count = 0
positions = []
found = False
for i in range(len(my_list)):
    if my_list[i] == element:
        found = True
        count += 1
        positions.append(i)
        
if found:
    print(f"{element} is present in the list")
    print(f"Number of occurrences: {count}")
    print(f"Positions where element is found: {positions}")
else:
    print(f"{element} is not present in the list")


#4) wap to calculate avg of players
# ii) show player details on basis of its name
#  pname =['p1','p2','p3']
#  prun =[1000,2000,3000]
#  pmatch =[20,50,60]
#  pavg =[50,40,30]

pname = ['p1', 'p2', 'p3']
prun = [1000, 2000, 3000]
pmatch = [20, 50, 60]
pavg = [50, 40, 30]

total_runs = 0
total_matches = 0
for i in range(len(pname)):
    total_runs += prun[i]
    total_matches += pmatch[i]

avg_runs = total_runs / len(pname)
avg_matches = total_matches / len(pname)

print('Average Runs:', avg_runs)
print('Average Matches:', avg_matches)

name = input('Enter player name: ')
index = pname.index(name)

print('Runs:', prun[index])
print('Matches:', pmatch[index])
print('Average:', pavg[index])

#5)
l1 = [10, 20, 30, 40]
l2 = [1, 2, 3, 2]
result = []

for i in range(len(l1)):
    result.extend([l1[i]] * l2[i])

print(result)

#6) wap to remove all the occurance of given element from list
my_list = [10, 20, 30, 20, 40, 20]
element_to_remove = int(input('Enter the repeated element you want to remove from list: '))

while element_to_remove in my_list:
    my_list.remove(element_to_remove)

print(my_list)




