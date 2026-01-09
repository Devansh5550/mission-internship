marks = [85,90,78,92]
print(marks)
print(marks[0])

marks.append(80)
print(marks)
print(len(marks))

marks.remove(78)
print(marks)

for m in marks:
    print(m)

coords = (10,20)
print(coords[0])

student = {
    "name": "Adarsh",
    "roll": 12,
    "cgpa": 8.6
}


print(student["name"])

student["cgpa"] = 8.8

for key,value in student.items():
    print(key, ":", value)

marks = []

for i in range(5):
    m=int(input("ENTER MARKS : "))
    marks.append(m)

avg = sum(marks)/len(marks)
print("Average:",avg)

student = {}
student["name"]=input("Name: ")
student["roll"]=input("Roll: ")
student["marks"]=int(input("Marks: "))

print("\nStudent details")
for k,v in student.items():
    print(k, ":", v)