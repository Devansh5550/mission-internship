a = int(input("ENTER THE NUMBER:"))
if a % 2 == 0 :
    print("number is even")
else:

    print("number is odd")


a=int(input("enter first number"))
b=int(input("enter second  number"))
c=int(input("enter third number"))

if a>b and a>c:
    print("a is the largest number")
elif  b>c:
        print("b is the largest number")
else:
    print("c is the largest number")



    
year = int(input("years of experience ="))
skills = input("do you have skils?(yes/no) : ")
if year >= 1 and skills=="yes":
                                print("start applying for internships")
else:
        print("build skills first")