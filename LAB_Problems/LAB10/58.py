# Program 58 : Function to calculate factorial
# M1 if youre using python features
def fact(n):
    if n==0 or n==1 :
        return 1
    return n*fact(n-1)
print(fact(6))
#M2 applicable for all programming languages
def fact1(n):
    f=1 #initializing a variable f where we gonna store the result
    for i in range(1,n+1):
        f=f*i
    return f
print(fact1(0))