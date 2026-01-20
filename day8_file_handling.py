name = input("ENTER NAME:")
roll = input("ENTER ROLL:")
marks = int(input("ENTER MARKS SCORED:"))

with open("students.txt", "a") as f:
    f.write(f"{name},{roll},{marks}\n")


print("Record saved successfully")

with open("students.txt", "r") as f:
    for line in f:
        print(line)