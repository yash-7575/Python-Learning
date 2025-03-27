# Program 59 : Function to calculate the sum of digits
def sumd(n):
    s=0
    while n!=0:
        ld=n%10
        s=s+ld
        n=n//10
    return s
a=int(input("Enter a no. "))
print(sumd(a))