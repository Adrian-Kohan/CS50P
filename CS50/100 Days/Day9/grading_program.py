student_score = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" :74,
    "Neville" : 62
}

student_grade = {}
for key in student_score:
    if 100 >= student_score[key] >= 91:
        student_grade[key] = "Outstanding"
    elif 90 >= student_score[key] >= 81:
        student_grade[key] = "Exceeds expectation"
    elif 80 >= student_score[key] >= 71:
        student_grade[key] = "Acceptable"
    else:
        student_grade[key] = "Fail"

print(student_grade)