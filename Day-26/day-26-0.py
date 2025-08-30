""" List Comprehension """
numbers=[1,2,3]
new_list=[num+1 for num in numbers]
print(new_list)

name='Usman'
new_list=[letter for letter in name]
print(new_list)


new_list=[num*2 for num in range(1,5)]
print(new_list)

names=['Usman','Ali','Hadi','Umer','Abbas','Abdullah']
short_names=[name for name in names if len(name)<5]
print(short_names)

upper_case_name=[name.upper() for name in names if len(name)>5]
print(upper_case_name)
