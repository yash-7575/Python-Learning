print("enter the coefficients of x^2, x and constant")
a=int(input())
b=int(input())
c=int(input())
d=b**2-(4*a*c)
x1=(-b+((d)**0.5))/(2*a)
x2=(-b-((d)**0.5))/(2*a)
if(d==0) :
    print("roots are real and equal")
elif(d>0) :
    print("roots are real and unequal")
else :
    print("roots are imaginary")
print(x1, x2)
