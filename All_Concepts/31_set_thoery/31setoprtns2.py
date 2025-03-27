s={1,2,3,4}
s.add(23)
print(s)

s.update({11,23,12})
print(s)

l1=[22,14,53,64]
s1=set(l1) #list ko set me change kar diya
print(s1)

s.update(s1)
print(s)

s.remove(1) #.remove() shows an error if the item isnt in the set
print(s)

'''s.discard(1) #whereas .discard() doesnt show error even if item isnt present
print(s)'''

#For multiple remove we use difference_update()
s.difference_update({11, 12})
print(s)

s={20,30,40,50,60,70}
s1=s.pop()
print(s1)
print(s)

#del is used to delete entire set
'''s2={2,3,4}
del s2
print(s2)'''

#.clear() is used to remove all the items from set
s2={2,3,4}
s2.clear()
print(s2) 