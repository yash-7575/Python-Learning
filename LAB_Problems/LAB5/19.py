# Problem 19 : Program to calculate the time difference in seconds

# Input the first timestamp
h1 = int(input("Enter hours of the first timestamp: "))
m1 = int(input("Enter minutes of the first timestamp: "))
s1 = int(input("Enter seconds of the first timestamp: "))

# Input the second timestamp
h2 = int(input("Enter hours of the second timestamp: "))
m2 = int(input("Enter minutes of the second timestamp: "))
s2 = int(input("Enter seconds of the second timestamp: "))

# Calculate the total seconds for each timestamp
time1 = h1 * 3600 + m1 * 60 + s1
time2 = h2 * 3600 + m2 * 60 + s2

# Calculate the difference in seconds
difference = time2 - time1

# Output the result
print("The difference in seconds is:",difference)