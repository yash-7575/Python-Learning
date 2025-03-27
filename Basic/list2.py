import random
# m=[2,3,4]
# print(m[1])

n=int(input("Enter a no: "))
a=random.randint(1,n//2)
b=random.randint((n//2)+1,n)
print(a,b)
l=[]
for i in range (a,b+1):
    l.append(i)     
print(l)

l=[i for i in range(a,b+1) if i%2==0]
print(l)

l=[]
for i in range(a,b+1):
    if(i%2==0):
        l.append(i)
print(l)
for i in range(0,n):
    if i in l:
        print(i)

import math

l1=[(i)**0.5 for i in range (0,20)]
print(l1)