students_score={
    "Usman":81,
    "Ali":78,
    "Maryam":99,
    "Fizza":74,
    "Nimra":62
}
students_grade={}
for stdnt_score in (students_score):
    if students_score[stdnt_score]>90:
        students_grade[stdnt_score]="Outstanding"
    elif students_score[stdnt_score]>80:
        students_grade[stdnt_score]="Exceeeds Expectation"
    elif students_score[stdnt_score]>70:
        students_grade[stdnt_score]="Acceptable"
    elif students_score[stdnt_score]<=70:
        students_grade[stdnt_score]="Fail"
print(students_grade)