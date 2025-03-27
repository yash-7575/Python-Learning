d1 = {"name": "John", "age": 21, "GPA": 3.8}
d2 = {"course": "Python", "credits": 4, "instructor": "Smith"}
d1.update(d2)
print(d1)
print(d2)

d1 = {"name": "John", "age": 21, "GPA": 3.8}
d1.clear()
print(d1)

# del d1
# print(d1)

d1 = {"name": "John", "age": 21, "GPA": 3.8}
value=d1.pop("age") # d.pop("key") removes the key and store the value in a variable
print(value)
print(d1)

d1 = {"name": "John", "age": 21, "GPA": 3.8}
del d1["name"]
print(d1)

d1 = {"name": "John", "age": 21, "GPA": 3.8}
b = d1.popitem() # d.popitem() removes the last item and store it in a variable
print(b, d1)
print(type(b))  # Tuple

d1 = {"name": "John", "age": 21, "GPA": 3.8}
saved_item = {"age": d1["age"]}
print(saved_item)
