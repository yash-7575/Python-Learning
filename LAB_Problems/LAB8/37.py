# 37. Program to Generate Random Numbers from 1 to 20 and Append Them to the List
import random
random_numbers = [random.randint(1, 20) for _ in range(10)]  # Generate 10 random numbers
print("Random numbers:", random_numbers)

# import random
l=[]
for i in range(0,10):
    a=random.randint(0,20)
    l.append(a)
print(l)