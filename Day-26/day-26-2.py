with open('file1.txt','r') as file:
    file1=file.readlines()

with open('file2.txt','r') as file:
    file2=file.readlines()

common_num=[int(num) for num in file1 if num in file2]
print(common_num)