import random

# Your list
l1 = ['I', 'I', 'I', 'I', 'I', '.', '.', 'I', '.', '.']

# Number of 'I's to replace (e.g., half of them)
num_to_replace = len(l1) // 2

# Indices of 'I's in the list
indices = [i for i, x in enumerate(l1) if x == 'I']

# Randomly select indices to replace
random_indices = random.sample(indices, num_to_replace)

# Replace 'I' with '.' at the selected indices
for index in random_indices:
    l1[index] = '.'

print(l1)

l=[1]*5
print(l)