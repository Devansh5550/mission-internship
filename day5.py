def greet():
    print("hello")

greet()

def add(a,b):
    return a+b

print(add(2,5))   #output is 7


def even_odd_checker(num):
    if num%2 == 0:
        return "EVEN NUMBER"
    else:                               
        return "ODD NUMBER"

n=int(input("ENTER THE NUMBER = "))

print(even_odd_checker(n))


def calculate_grade(marks):
    if marks >= 90:
        return "GRADE IS A"
    elif marks >= 80:
        return "grade is b"
    elif marks >= 70:
        return "grade is c"
    else:
        return "Fail"


m = int(input("ENTER MARKS : "))

print(calculate_grade(m))