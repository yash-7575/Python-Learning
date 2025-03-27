a="0123456789"
print(a[0])
print(a[3])
'''print(a[1.6]) # for type error
print(a[10]) # for index error '''
print(a[2:7])
print(a[2:7]+a[1:5])
print(len(a))
print(a.upper())
print(a.lower().isdigit())
print(a.lower().capitalize().title().split(" "))
b="Iron Man"
c="Captain America"
d=b.replace("Iron","Fire")
print(d)
e=d.replace("Fire",'')
print(e)
print(e*5)