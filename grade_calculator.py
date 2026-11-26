
print("Welcome to Student Grade Calculator!")

name = input("Enter your name: ")

grade1 = float(input("Enter first grade: "))
grade2 = float(input("Enter second grade: "))
grade3 = float(input("Enter third grade: "))

average = (grade1 + grade2 + grade3) / 3

print("\nStudent:", name)
print("Average:", average)

if average >= 50:
    print("Result: Passed!")
else:
    print("Result: Failed!")
