# Program to find the length of the widest fragment where all elements are equal

# Initialize variables
current_count = 1  # Count of current fragment
max_count = 0  # Maximum count of equal elements

# Input the first number
prev_number = int(input("Enter a number (0 to stop): "))

# Continue until 0 is entered
while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        # Ensure max_count is updated before breaking out
        max_count = max(max_count, current_count)
        break

    if number == prev_number:  # Check if the number matches the previous one
        current_count += 1
    else:
        # Update max_count and reset current_count
        max_count = max(max_count, current_count)
        current_count = 1
    
    prev_number = number

# Print the length of the widest fragment
print("Length of the widest fragment:", max_count)


max_count=0
current_count=1
prev_number=int(input("Enter a no. "))
while True:
    number=int(input("Entere a no. "))
    if number==0:
        max_count=max(max_count,current_count)
        break
    if number==prev_number:
        current_count=current_count+1
    else:
        max_count=max(max_count,current_count)
        current_count=1
    prev_number=number
print(max_count)
