students_height=input('Enter the heights of the students\t').split()
for n in range(0,len(students_height)):
    students_height[n]=int(students_height[n])
# print(students_height)
total_heights=0
for heights in students_height:
    total_heights+=heights
# print(total_heights)
no_of_students=0
for student in students_height:
    no_of_students+=1
# print(no_of_students)
avg=round(total_heights/no_of_students)
print(avg)