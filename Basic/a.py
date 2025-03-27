print("hello \"Yash\" \nYou're Welcome")
print("Yash", 5, 89, sep="~", end="-445\n")
a=1
b="Yash"
c=True
d=None
e=complex(8,2) #for storing complex numbers
print(a,type(a),"\n",b,type(b),"\n", c,type(c),"\n", d,type(d), "\n", e,type(e) )

# Lists and Tuples are ordered collection of data 
# lists are mutable can be changed
# Tuples are immutable cant be changed 

list1=[1,2.3,["Yash","Bhagyawant"],[2.3,3.1]] 
print(list1)
print(list1[2])
tuple1=(2,3.4,[5,6],"Yash")
print(tuple1[1])

# Dictionaries are mapped collection of data 
dict1={"Name": str(input("Enter Your Name: ")),"Age":int(input("Enter Your Age: ")),"CanVote":True}
print("Name of The Person is :", dict1["Name"])
print("Age of The Person is :", dict1["Age"])

a=dict1["Age"]
if (a>=18):
    print("He can vote")
else :
    print("He cant vote")

#Calculator
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