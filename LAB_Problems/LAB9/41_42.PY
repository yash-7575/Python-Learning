# Program to Print Keys of Dictionary

rating={"aptitude":8,"technical":9,"personality":10,"communication_skills":9.5}
for skills in rating.keys():
    print(skills, end=" ")
print()
# Program to Print Values of Dictionary

for score in rating.values():
    print(score, end=" ")
print()

d1={"y":100,"s":101}
for keys in d1.keys():
    print(keys)
for values in d1.values():
    print(values)
print(d1)
print(d1["y"])
l=[2,3,4,5]
print(l[0])