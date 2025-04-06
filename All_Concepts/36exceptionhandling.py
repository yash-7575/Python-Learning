'''Exception Handling in Python'''

try:
    a=int(input("Enter a number: "))
    print(10/a)
except ZeroDivisionError:
    print("Can't Divide by Zero!")
except ValueError:
    print("ValueError : Write Integer Value")
except Exception as e:
    print("Error occured: ",e) 
    ''' Store the exception (error) in e'''
else:
    print("Program Ran Successfully")
finally:
    print("always printed")
print("Heyyy Cutie Pie!! ")
'''this ans aut'''

try:
    l=[1,2,3,4,5]
    print(l[6])
except IndexError:
    print("IndexError: Index out of the limit of ho gaya hai")
finally:
    print("alwars printed")

try:
    print('5'+3)
except Exception as e:
    print('error: ' ,e) #TypeError
'''
ZeroDivisionError	Dividing by 0
ValueError	        Wrong type conversion (int("abc"))
TypeError	        Wrong operation on data types
IndexError	        Accessing invalid list index
KeyError	        Accessing non-existing dict key
FileNotFoundError	Opening a file that doesn’t exist
'''

try:
    print("hello"*"hello")
except Exception as e:
    print("TypeError: ",e)