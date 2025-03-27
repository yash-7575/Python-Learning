# # Program 62 : Function to print a sequence in reverse order
# def reverse_sequence():
#     n = int(input("Enter a number: "))
#     if n == 0:
#         return None
#     reverse_sequence()
#     print(n)

# reverse_sequence()
def reverse_sequence():
    # Take user input
    number = int(input("Enter a number: "))

    # Base case: Stop recursion if the number is 0
    if number == 0:
        return  
    else:
        # Recursive call
        reverse_sequence()
        
        # Print the number after returning from recursion
        print(number)

# Call the function
reverse_sequence()
