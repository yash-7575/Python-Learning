# recurssive fn is used to iterate fn multiple times until a certain condition reaches

#5!=5.4.3.2.1
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
