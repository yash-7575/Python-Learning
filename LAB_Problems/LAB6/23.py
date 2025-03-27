# is prime or not
n=int(input("Enter a number greater than 1: "))
isprime=True
for i in range(2,n):
    if (n%i==0):
        isprime=False
        print("It's not a prime number")
        break
    else:
        continue
if(isprime==True):
    print("It's a prime number")


        