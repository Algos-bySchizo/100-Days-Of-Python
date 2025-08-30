import random
""" Dictonary Compreension in Python """

# Syntax for Dictonary Comprehension new_dict={new_key:new_value for item in list}
# Syntax for creating a new dict through Comprehension new_dict={new_key:new_value for (key,value) in dict.items()}

names=['Usman','Ali','Hadi','Umer','Abbas','Abdullah']

dict={name:random.randint(1,100) for name in names}
print(dict)

passed_students={student for (student,marks) in dict.items() if marks>90}
print(passed_students)