import csv
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "Fail"

def get_students():
        print("\n STUDENT", i+1)
        name=input("ENTER NAME OF STUDENT:")
        roll=input("ENTER THE ROLL NO:")
        try:
            marks=int(input("ENTER THE MARKS SCORED BY THE STUDENT:"))
        except:
            marks=int(input("Please enter marks in integer:"))

    

        student = {
            "name":name,
            "roll" :roll,
            "marks" :marks,
            "grade" :calculate_grade(marks)
        }

        students.append(student)

def show_data():
    
    print("\n------STUDENT RESULTS------")

    for s in students:
        print("Name:", s["name"])
        print("Roll:", s["roll"])
        print("Marks:", s["marks"])
        print("Grades:", s["grade"])
        print("-"*20)

def store_data():
    with open("students.csv", "a",newline="") as f:
        writer = csv.writer(f)
        for s in students:
            writer.writerow([s["name"],s["roll"],s["marks"]])
    with open("students.txt", "a") as f:
        for s in students:
            f.write(f"{s["name"]}\t{s["roll"]}\t{s["marks"]}\t{s["grade"]}\n")

students = []
n = int(input("ENTER THE NUMBER OF STUDENTS:"))
for i in range(n):
    get_students()


show_data()
store_data()