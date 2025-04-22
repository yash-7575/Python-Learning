# ValueError
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print("Error:", e)

# TypeError
try:
    x = "hello"
    if not isinstance(x, int):
        raise TypeError("Expected an integer")
except TypeError as e:
    print("Error:", e)

# KeyError
try:
    my_dict = {"name": "Yash"}
    if "age" not in my_dict:
        raise KeyError("Key 'age' not found in dictionary")
except KeyError as e:
    print("Error:", e)

# IndexError
try:
    my_list = [1, 2, 3]
    if len(my_list) < 5:
        raise IndexError("List index out of range")
except IndexError as e:
    print("Error:", e)

# ZeroDivisionError
try:
    num = 10
    denom = 0
    if denom == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
except ZeroDivisionError as e:
    print("Error:", e)

# FileNotFoundError
try:
    file_name = "non_existent_file.txt"
    raise FileNotFoundError(f"File '{file_name}' not found")
except FileNotFoundError as e:
    print("Error:", e)

# Custom Exception
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print("Error:", e)

a=int(input("Enter Value between 5 and 9 "))
if(a>9 or a<5):
    raise ValueError("Value should be 5 to 9")
else:
    print("Good")

try:
    l=[1,2,3,4]
    a=int(input("Enter index "))
    if a>3 or a<0:
        raise IndexError("Enter index from 0 to 3")
    else:
        print(l[a])
    
except Exception as e:
    ''' Jo bhi error generate huyi usko e me store kro and print krdo '''
    print("Error:", e)
finally:
    print("Always Executed")