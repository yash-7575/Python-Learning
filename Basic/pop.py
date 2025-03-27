''' When we want to remove an element from a list and want to store it as new variable we use .pop() function for ex.=> Tossing a coin and catching it'''
# Conventional Method 
l=[1,2,3,4]
a=l[3]
l.remove(4)
print(a,l)
# To much longer for solving the problem instead we will use .pop()
l=[1,2,3,4]
a=l.pop()
print(a,l)

''' .pop() remove and return the value default last value
.pop(0) removes and return 1st value of list we have to give index as a parameter'''
b=l.pop(0)
print(a,b,l)
