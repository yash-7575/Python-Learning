import random
import time

def display_pins(pins):
    """Displays the current state of the pins."""
    print(" ".join(pins))

def throw_ball(pins):
    """Simulates a ball throw and removes random pins."""
    hit_count = random.randint(1, len(pins) // 2)  # Randomly decide how many pins to knock
    hit_indices = random.sample([i for i, pin in enumerate(pins) if pin == "I"], min(hit_count, pins.count("I")))

    for idx in hit_indices:
        pins[idx] = "."  # Replace knocked-down pins with dots

    return pins

# User input
n = int(input("Enter number of pins: "))
k = int(input("Enter number of balls: "))

# Initial pins setup
pins = ["I"] * n
display_pins(pins)

# Game loop
for ball in range(1, k+1):
    input(f"\nThrow ball {ball}/{k} (Press Enter)")
    
    pins = throw_ball(pins)  # Simulate throw
    display_pins(pins)  # Display updated pins
    time.sleep(1)  # Just for effect
    
    if "I" not in pins:  # Check if all pins are knocked down
        print("\n🎉 You won! All pins are knocked down! 🎉")
        break
else:
    print("\nTry again! Some pins are still standing.")


# Sir's Code
# #Problem 18 :  Program to determine which pins remain standing

# # Input the number of pins (N) and the number of balls (K)
# N = int(input("Enter the total number of pins: "))
# K = int(input("Enter the number of balls rolled: "))

# # Create a list of pins (1 = standing, 0 = knocked down)
# pins = [1] * N

# # Process each ball
# for i in range(K):
#     print(f"Ball {i + 1}:")
#     start = int(input("Enter the starting position: ")) - 1
#     end = int(input("Enter the ending position: ")) - 1
#     for j in range(start, end + 1):
#         pins[j] = 0  # Mark pins as knocked down

# # Output the final state of the pins
# result = "".join(["I" if pin == 1 else "." for pin in pins])
# print("Final state of the pins:", result)




# # III...II store this result in a string and try to find the position of first dot(.) and apply fns to rest of the Is
# import random
# n=int(input("Enter no of pins: "))
# k=int(input("Enter no of balls: "))
# for i in range (1,n+1):
#     print("I", end="")

# print(" ")
# a=random.randint(0,n//2)
# b=random.randint((n//2)+1,n)
# print(f"{(a,b)}")
# l=[]
# for i in range (a,b+1):
#     l.append(i)

# l1=[]
# for i in range(1,n+1):
#     if i in l:
#         print(".", end="")
#         l1.append(".")
#     else :
#         print("I", end="")
#         l1.append("I")
# print()
# print(l1)

# for i in l1:
#     if(i=="I"):
#         print(".", end="")
#     else:
#         print(".", end="")        
