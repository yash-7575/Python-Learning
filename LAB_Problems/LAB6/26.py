# Program to display first n Fibonacci numbers
n=int(input("Enter a number : "))
a=0
b=1
print(a,b, end=" ") # end=" " adds a space instead of new line 
for i in range(3,n+1):
    c=a+b
    a=b
    b=c
    print(c, end=" ")
print()

n=int(input("no. "))
a=0
b=1
print(f"{a},{b}", end="")
for i in range(3,n+1):
    c=a+b
    a=b
    b=c
    print(f",{c}",end="")