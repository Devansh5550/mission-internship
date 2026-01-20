try:
    x=int(input("ENTER A NUMBER:"))
    print("ENTERED NUMBER =", x)
except:
    print("INVALID INPUT PLEASE ENTER A NUMBER :")

try:
    num=int(input("ENTER A NUMBER="))
    result = 10/num
except ValueError:
    print("Please enter a valid integer")

except ZeroDivisionError:                               #ZeroDivisionError is a predifined except block in python 
    print("Number cannot be zero!!")

try:
    x=int(input("Enter an integer:"))
except:
    print("Invalid Input")
else:
    print("Square:",x*x)
finally:
    print("Program is ended")