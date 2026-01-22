import csv

with open("students.csv", "a",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["Name","Roll","Marks"])
