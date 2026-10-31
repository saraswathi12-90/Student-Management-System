

import json
import os

students = []
FILE_NAME = "students.json"


def load_students():
    global students

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            students = json.load(file)


def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def get_marks(subject):
    while True:
        try:
            marks = int(input("Enter " + subject + " marks: "))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter numbers only.")


def calculate_result(student):
    total = (
        student["maths"] + student["science"]
        + student["english"] + student["social"]
        + student["computer"]
    )

    percentage = (total / 500) * 100

    if any(student[s] < 35 for s in
           ["maths", "science", "english", "social", "computer"]):
        result = "Fail"
        grade = "F"
    else:
        result = "Pass"

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "E"

    student["total"] = total
    student["percentage"] = percentage
    student["result"] = result
    student["grade"] = grade


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))

    student = {
        "name": name,
        "age": age,
        "maths": get_marks("Maths"),
        "science": get_marks("Science"),
        "english": get_marks("English"),
        "social": get_marks("Social"),
        "computer": get_marks("Computer")
    }

    calculate_result(student)
    students.append(student)
    save_students()

    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found!")
        return

    for student in students:
        print("\nName:", student["name"])
        print("Age:", student["age"])
        print("Total:", student["total"], "/ 500")
        print("Percentage:", student["percentage"], "%")
        print("Result:", student["result"])
        print("Grade:", student["grade"])
        print("------------------------")


def search_student():
    name = input("Enter student name to search: ").lower()

    found = False

    for student in students:
        if student["name"].lower() == name:
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Total:", student["total"], "/ 500")
            print("Percentage:", student["percentage"], "%")
            print("Result:", student["result"])
            print("Grade:", student["grade"])
            found = True

    if not found:
        print("Student not found!")


def update_student():
    name = input("Enter student name to update: ").lower()

    for student in students:
        if student["name"].lower() == name:
            print("Student found. Enter updated details.")

            student["age"] = int(input("Enter new age: "))
            student["maths"] = get_marks("Maths")
            student["science"] = get_marks("Science")
            student["english"] = get_marks("English")
            student["social"] = get_marks("Social")
            student["computer"] = get_marks("Computer")

            calculate_result(student)
            save_students()

            print("Student updated successfully!")
            return

    print("Student not found!")


def delete_student():
    name = input("Enter student name to delete: ").lower()

    for student in students:
        if student["name"].lower() == name:
            students.remove(student)
            save_students()
            print("Student deleted successfully!")
            return

    print("Student not found!")


load_students()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
