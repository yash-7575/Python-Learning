import random

l=[11,2,4,5,2,34,54,23,99]
# l.append(83) #adds value at end
# l.sort() #by asending
# l.sort(reverse=True) #desending
# l.reverse() #reverse the list
m=l
m[0]=0 # never do this it changes the actual value in orignal list too
# instead use .copy() fn

n=l.copy()
n[2]=23

print(l.index(23)) #python tu muje ye bata 23 ka index kya hoga list me

p=[23,34,45]
l.extend(p) #add values from list p

print(l.insert(4,899))

# concatanate
k=n+l
print(k)
l1 = ["apple", "banana", "date","cherry", "fig"]
# random.shuffle(l1)
l1.sort() #sort by alphabetic
l1.sort(reverse=True)

print(l)
#python tu muje ye bata 23 kitni baar aaya hai list me
print(f"Yash, dekh (23) {l.count(23)} baar aaya hai list me") 
print(n)
print(l1)