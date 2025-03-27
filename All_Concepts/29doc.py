# docstrings (fn.__doc__) is used to print description of any fn written just below the declaration of fn if it is used after somelines of declaration then it doesnt work
def square(n):
    '''It's function that returns square of any number'''
    return n*n
print(square.__doc__)
print(square(5))

def sum(a):
    print(a)
    '''It's fn that returns sum of numbers'''
    return a+a
print(sum.__doc__) #returns None coz doc string must be just below after declaration of function
print(sum(8))