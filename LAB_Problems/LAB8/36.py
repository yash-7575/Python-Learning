# 36. Program to Find all Numbers in a Range which are Perfect Squares and Sum of all Digits in # the Number is Less than 10
import math
range_start, range_end = 1, 100
result = []
for num in range(range_start, range_end + 1):
    if math.isqrt(num) ** 2 == num:  # Check if number is a perfect square
        if sum(int(digit) for digit in str(num)) < 10:  # Check if sum of digits is less than 10
            result.append(num)
print("Perfect squares with sum of digits < 10:", result)


# import math
s=1
end=100
l=[]
for i in range(s,end+1):
    if math.isqrt(i)**2==i:
        l.append(i)
print(l)
