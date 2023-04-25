#1) wap to calculate number of spaces in files using function

def readFileData():
    f=open(input('enter file name')+'.txt','r')
    data = f.read()
    f.close()
    return data
def calculateSpace():
    sp=0
    fdata=readFileData()
    for char in fdata:
        if char.isspace():
            sp+=1
    return sp
numberofspaces  = calculateSpace()
print('Number of Spaces = ' ,numberofspace)

    
#2)wap to copy data from one file to another file using function

def copycode():
    originalfile = input('enter original file name:')
    copyfile = input('enter copy file name:')
    forg = open(originalfile+'.py','r')
    fcopy = open(copyfile+'.txt','w')
    data = forg.read()
    fcopy.flush()
    fcopy.close()
    forg.close()
    
copycode()

#3)wap to calculate number of words in a file
number_of_words = 0
 
with open(r'SampleFile.txt','r') as file:
    data = file.read()
    lines = data.split()
    number_of_words += len(lines)
print(number_of_words)



#4)wap to create a directory and create a file inside the directory
import os

dir_name = input("Enter directory name: ")
file_name = input("Enter file name: ")

if not os.path.exists(dir_name):
    os.makedirs(dir_name)
    print(f"Directory '{dir_name}' created successfully")

file_path = os.path.join(dir_name, file_name)

with open(file_path, 'w') as file:
    file.write("This is a sample file created using Python")
    print(f"File '{file_name}' created successfully inside '{dir_name}' directory")

