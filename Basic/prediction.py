#Hi Hello to Python
import random

l=["Hello","Hi","Namaste","Namskar", "holla"]
random.shuffle(l)
print(l)

name=str(input("Enter your name : "))
print(f"{l[0]}!! {name}")

a=random.randint(0,5)
print(l[a])