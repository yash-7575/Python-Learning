def f1():
    ''' Finally keyword always executed even if the function returns the value'''
    try:
        a=int(input())
        # a=10/0
        return a
    except ValueError:
        print("Enter integer value")
    except ZeroDivisionError:
        print("Can't divide by zero")
    finally:
        print("Always Executed")
print(f1())
''' It is used in the functions coz after returning the value nothing is executed but the finally is the exception it used to do some tasks even if the fn returns any value'''
try:
    l=[1,2,3,4]
    a=int(input())
    print(l[a])
except IndexError:
    print("Index is out of limit")
finally:
    print("Always Executed")