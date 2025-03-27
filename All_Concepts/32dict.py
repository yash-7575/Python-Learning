info={"name":"yash", "age":18, "eligible":True}
print(info.keys())
print(info.values())

for i in info.keys():
    print(i)
    print(f"Value of {i} is {info[i]}")

print(type(info.items()))
print(info.items())

for i,j in info.items():
    print(i,j)