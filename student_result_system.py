def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "Fail"

students = []
n = int(input("ENTER THE NUMBER OF STUDENTS:"))
for i in range(n):
    print(f"\n STUDENT {i+1}")
    name=input("ENTER NAME OF STUDENT:")
    roll=input("ENTER THE ROLL NO:")
    marks=int(input("ENTER THE MARKS SCORED BY THE STUDENT:"))

    student = {
        "name": name,
        "roll" : roll,
        "marks" : marks,
        "grade" : calculate_grade(marks)
    }

    students.append(student)

print("\n------STUDENT RESULTS------")

for s in students:
    print("Name:", s["name"])
    print("Roll:", s["roll"])
    print("Marks:", s["marks"])
    print("Grades:", s["grade"])
    print("-"*20)