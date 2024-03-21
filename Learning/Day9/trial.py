import os

student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}
for key in student_scores:
    if student_scores[key] in range(90, 101):
        print(student_scores[key])
print(student_scores["Draco"])
os.system("cls")
print("Wow")
print(len(student_scores))
