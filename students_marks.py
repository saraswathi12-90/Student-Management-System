
print("===== Student Marks Calculator =====")

name = input("Enter your name: ")

while True:
    maths = int(input("Enter Maths marks: "))

    if maths >= 0 and maths <= 100:
        break

    print("Invalid marks! Enter marks between 0 and 100.")

while True:
    science = int(input("Enter Science marks: "))

    if science >= 0 and science <= 100:
        break

    print("Invalid marks! Enter marks between 0 and 100.")

while True:
    english = int(input("Enter English marks: "))

    if english >= 0 and english <= 100:
        break

    print("Invalid marks! Enter marks between 0 and 100.")

while True:
    social = int(input("Enter Social marks: "))

    if social >= 0 and social <= 100:
        break

    print("Invalid marks! Enter marks between 0 and 100.")

while True:
    computer = int(input("Enter Computer marks: "))

    if computer >= 0 and computer <= 100:
        break

    print("Invalid marks! Enter marks between 0 and 100.")

total = maths + science + english + social + computer

percentage = (total / 500) * 100

# Pass or Fail calculation
if maths >= 35 and science >= 35 and english >= 35 and social >= 35 and computer >= 35:
    result = "Pass"
else:
    result = "Fail"

# Grade calculation
if result == "Fail":
    grade = "F"
elif percentage >= 90:
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

print("\n===== Student Report =====")

print("Student Name:", name)
print("Maths:", maths)
print("Science:", science)
print("English:", english)
print("Social:", social)
print("Computer:", computer)

print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Result:", result)
print("Grade:", grade)
