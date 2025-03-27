# Program 54 : Function to check if a number is even or odd

def even_odd(n):
    if n%2==0:
        print("Even")
    else :
        print("Odd")
n1=int(input("Enter a no. :"))
even_odd(n1)    

#Method 2:
def even_odd2(n):
    if n%2==0:
        return "Even"
    else :
        return "Odd"
n1=int(input("Enter a no. :"))
print(even_odd2(n1))