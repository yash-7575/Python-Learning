# 35. Program to Put Even and Odd elements in a List into Two Different Lists
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
