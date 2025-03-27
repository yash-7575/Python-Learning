#pgm to calculate sum and avg of first n natural numbers
n=int(input("Enter a number : "))
r=0
for i in range (1,n+1):
    r=r+i
print(f"sum {r}")
avg=r/n
print(f"avg {avg}")