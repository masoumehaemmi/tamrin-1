import math

a = int(input("please Enter side1: "))
b = int(input("please Enter side2: "))
c = int(input("please Enter side3: "))

if a*a == b*b + c*c or b*b == c*c + a*a or c*c == a*a + b*b:
    print("Yes")

else:
    print("No")