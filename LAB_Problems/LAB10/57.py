# Program 57 : Function to describe a player with a default type
def about_type_default(name, type="Batsman", age=35):
    return f"Player name is {name}, He is a {type}, his age is {age}"
print(about_type_default(name="Dhoni"))

def about_type_default1(name, type="Batsman", age=35):
    return f"Player name is {name}, He is a {type}, his age is {age}"
print(about_type_default1(name="Virat",age=32))