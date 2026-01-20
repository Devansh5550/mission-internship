n=int(input("HOW MANY STUDENTS DATA NEEDS TO BE STORED ?"))

for i in range(n):
    name = input("ENTER NAME:")
    roll = input("ENTER ROLL:")
    marks = int(input("ENTER MARKS SCORED:"))


    # Using 'a' (append) mode so that new student records are added
# without deleting the existing data in the file

    with open("students.txt", "a") as f:                                      
        f.write(f"{name}\t{roll}\t{marks}\n")
# 'with open()' is used because it automatically closes the file
# after the block ends, making the code safer and cleaner



print("Record saved successfully")

print("Name\tRoll\tMarks")
print("-"*20)

with open("students.txt", "r") as f:
    for line in f:
        print(line.strip())                  # strip() is used to remove extra newline characters and spaces
                                            # so that each record prints cleanly without blank lines