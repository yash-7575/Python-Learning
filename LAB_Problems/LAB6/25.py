# To display first n multiples of number
n=int(input("Enter a number : "))
n1=int(input("How many multiples do you want: "))
print(f"first {n1} Multiples are : ")
for i in range(1,n1+1):
    print(n*i)

print("Factors are: ")
#lets say n=12, factors=1,2,3,4,6,12
for i in range(1,n+1):
    if(n%i==0):
        print(i)
    else:
        continue