#fib => 0,1,1,2,3,5,8,13,21,34,55
#fib => fn = fn-1 + fn-2
def fib(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2) # sarri fib(i) values backend me store hogi and jab hume chahiye usko bula lenge
print(fib(10))

def fibseq(n):
    for i in range(n):
        print (fib(i), end=" ")
fibseq(10)


