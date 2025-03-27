import math
print("Enter 2 no.s :")
a=float(input())
b=float(input())
print(f"Addition of 2 no.s is: {a+b}")
print(f"Subtraction of 2 no.s is: {a-b}")
print(f"Multiplication of 2 no.s is: {a*b}")
print(f"Divison of 2 no.s is: {a/b}")
# Floor division(a//b) gives before integer of float value 
print(f"Floor Division of 2 no.s is: {a//b}")
print(f"Exponent of 2 no.s is: {a**b}")
print(f"Remainder when 1st is divided by 2nd is: {a%b}")
c=math.ceil(a/b)
print(f"Ceiling Value is {c}")