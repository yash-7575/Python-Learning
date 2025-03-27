#to print index and value of a list, tuple and dictionary
a=["Tiger","Lion","Elephant","Deer"]
for index, value in enumerate(a):
    print(index,value)
#enumerate is powerful function used to print both index and value of a list, tuple or dictionary
b=("chips","cold drink","coffee")
for index, value in enumerate(b):
    print(index,value)
c={"Yash":100,"Aditya":99}
for index, key in enumerate(c):
    print(index,key)