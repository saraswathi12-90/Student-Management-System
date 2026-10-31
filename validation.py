
while True:
    marks = int(input("Enter marks: "))

    if marks >= 0 and marks <= 100:
        break

    print("Invalid marks! Try again.")

print("Your marks are:", marks)
