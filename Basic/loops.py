name="Yash"
for i in name:
    print(i)
for i in range(5): #hamesha yaad rakho ye loop deafault zero se hi start hoga and n-1 tak jayega
    print(i+1) 
for i in range(1,5):
    print(i)
for i in range(0,10,2): #(start,stop,step) step is used as incrementor or decrementor, if step is 2 then it adds +2 to starting value and it countisly adds 2 to each new element
    print(i)
for i in range(1,10,3):
    print(i)
for i in range(10,1,-1):
    print(i)
name1="Rahul"
for i in name1:
    print(i)
    if (i=="h") :
        print("THIS IS SPECIAL!!")
x=["Red","Green","Blue"]
for i in x:
    print(i)
    if(i=="Green"):
        print("HI")
    for j in i:
        print(j)
i=0
while(i<=5):
    print(i)
    i=i+1
# j=0
# while(j>-1):
#  print(j)
#  j=j+1
a=int(input("enter a value: "))
while(a<50):
    a=int(input("enter a value: "))
else:
    print("no. is greater than 50")
