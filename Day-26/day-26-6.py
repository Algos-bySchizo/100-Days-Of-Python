import pandas

student_dict={'Students':['Usman', 'Ali', 'Abdullah'],
              'Scores':[56,67,90]}
for key,value in student_dict.items():
    # print(key,value)
    pass

student_data_frames=pandas.DataFrame(student_dict)
# print(student_data_frames)

for key,value in student_data_frames.items():
    # print(value)
    pass

""" Itterrows in Pandas for better looping in Pandas dataframes """

for (index,row) in student_data_frames.iterrows():
    if row.Students == 'Usman':
        print(row.Scores)
        