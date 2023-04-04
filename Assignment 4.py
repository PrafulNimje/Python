#1)1 
#  1 2 
#  1 2 3 
#  1 2 3 4


for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

#2) 1
#   2 3
#   4 5 6
#   7 8 9 10

num = 1
for i in range(1, 5):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()

#3)A
#  A  B
#  A  B  C
#  A  B  C D

for i in range(65, 69):
    for j in range(65, i+1):
        print(chr(j), end=" ")
    print()
#4)
#a 
#b   c
#d   e  f
#g   h  i  j






#5)
#      *
#   *    *
#*    *    *


for i in range(3):
    for j in range(3-i):
        print(" ", end="")
    for k in range(i+1):
        print("*", end=" ")
    print()

#6)

#         *
#     *   *
#  *  *   *
#* *  *   *

for i in range(1,5):
    for j in range(1,5):
        if(j<=4-i):
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()

#7)
 # *
 #* *
 #* *  *
 #* *
 #*

N = int(input('Enter number of steps: '))
for i in range(N):  
    for j in range(0, i + 1):
            print("*", end = "")
    print()
for i in range(1, N):
  
    for j in range(i, N):
        print("*", end = "")
    print()









