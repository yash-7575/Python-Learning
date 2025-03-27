a=str(input("Enter your name: "))
print(len(a))
print(a)

a1=a.strip()
print(len(a1))
print(a1)

a2=a.rstrip()
print(len(a2))
print(a2)

a3=a.lstrip()
print(len(a3))
print(a3)

a4 = " ".join(a.split())
print(len(a4))
print(a4)