n=int(input("Enter a number : "))
counter=1
for i in range(2,n):
    counter=counter+1
    if (n%i==0):
        print("It's not a prime number")
    else:
        continue
print(counter)
print(n)
if(counter==n-1):
    print("It's a prime number")


        