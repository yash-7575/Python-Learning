#To calculate factorial of any number
n=int(input("enter a number: "))
#lets say n=4
f=1 #create a varible where we can store our result
for i in range (1,n+1):
 f=f*i
#f=1*1=1, f=1*2=2,f=2*3=6, f=6*4=24
print("factorial of no. is :", f)
#this pgm works for 0! too

# n=7
# f=1
# for i in range(1,n+1):
#     f=f*i
# print(f)