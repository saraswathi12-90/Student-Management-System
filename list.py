students = []

student1 = {
    "name": "Saraswathi",
    "maths": 85,
    "science": 90
}

student2 = {
    "name": "Ravi",
    "maths": 75,
    "science": 80
}

students.append(student1)
students.append(student2)

for student in students:
    print("Student Name:", student["name"])
    print("Maths:", student["maths"])
    print("Science:", student["science"])
    print("--------------------")