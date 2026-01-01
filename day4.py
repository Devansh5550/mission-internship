i = 1
while i <= 5:
    print(i)
    i += 1


for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)    

for i in range(1,5):
    print('*'*i)

for i in range(4,0,-1):       #range(start, stop, step) step= decides how the value changes each time
    print("*"*i)


for i in range(1,5):
    for j in range(1,i+1):
        print(j, end="")     #Don’t go to a new line after printing, stay on the same line.” by deafult print() adds a new line after printing because by default end="\n"
    print()

num = int(input("ENTER THE NUMBER ="))

for i in range(1,11):
    print(num,"x",i,"=",num*i)