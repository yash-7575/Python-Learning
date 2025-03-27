add = lambda x,y: x+y
print(add(5,3))

square= lambda x:x**2
print(square(2))

area_of_triangle= lambda h,b:0.5*b*h
print(area_of_triangle(2,3))

max = lambda a, b: "A is greater" if a > b else "B is greater"
print(max(2, 3))

even_odd= lambda a:"even" if a%2==0 else "Odd"
print(even_odd(123))

str_reverse= lambda word: word[::-1]
print(str_reverse("hello"))

l=[1,2,3,4,5,6]
square1=list(map(lambda x: x**2,l))
print(square1)

even=list(filter(lambda x:x%2==0, l))
print(even)

double=list(map(lambda x:x*2,l))
print(double)

l2=reversed(l)
print(type(reversed(l)))

n=[i*2 for i in range(1,5)]
print(n)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
even = [x if x%2==0 else "odd" for x in numbers]
print(even)

odd = [ x for x in numbers if x%2!=0]
print(odd)
# for i in numbers:
#     if i%2==0:
#         print(i)
#     else:
#         continue

a, b = 10, 20
max1= a if a>b else b
print(max1)

nums = [-2, 5, -8, 10, -3, 7]
updated_nums = [0 if i<=0 else i for i in nums]
print(updated_nums)

names = ["alice", "bob", "charlie"]
uppercase_names = [i.upper() for i in names ]
print(uppercase_names)

words = ["cat", "elephant", "dog", "giraffe", "ant"]
long_words = []  # Fill in the list comprehension
print(long_words)
