# Problem 18: Program to determine which pins remain standing

# Step 1: Input the total number of pins (N) and the number of balls rolled (K)
N = int(input("Enter the total number of pins: "))
K = int(input("Enter the number of balls rolled: "))

# Step 2: Create a list to represent the pins (1 = standing, 0 = knocked down)
pins = [1] * N

# Step 3: Process each ball's impact
for i in range(K):
    print(f"\nBall {i + 1}:")
    
    # Input the range of pins knocked down by this ball
    start = int(input("Enter the starting position: ")) - 1
    end = int(input("Enter the ending position: ")) - 1
    
    # Knock down the pins in the given range
    for j in range(start, end + 1):
        pins[j] = 0  # Mark pins as knocked down

# Step 4: Generate the final representation of pins
result = ""
for pin in pins:
    if pin == 1:
        result += "I"  # 'I' represents a standing pin
    else:
        result += "."  # '.' represents a knocked-down pin

# Step 5: Output the final state of the pins
print("\nFinal state of the pins:", result)
