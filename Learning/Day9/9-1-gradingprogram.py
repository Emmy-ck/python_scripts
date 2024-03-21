student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}
#---------------------------------------------------------------------------#
# Don't change the code above
# TO DO 1 - Create an empty dictionary called student_grades
# TO DO 2 - Write your code below to add the grades

# Score 91 - 100: Grade = "Outstanding"
# Score 81 - 90: Grade = "Exceeds expectations"
# Score 71 - 80: Grade = "Acceptable"
# Score 70 or lower: Grade = "Fail"
#---------------------------------------------------------------------------#
student_grades = {}
for key in student_scores:
    student_grades[key] = student_scores[key]
for key in student_scores:
    if student_scores[key] in range(91, 101):
        student_grades[key] = "Outstanding"
    elif student_scores[key] in range(81, 91):
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] in range(71, 81):
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

#---------------------------------------------------------------------------#
# Don't change the code below
#---------------------------------------------------------------------------#
print(student_grades)
#---------------------------------------------------------------------------#

# DONE !!! :)))