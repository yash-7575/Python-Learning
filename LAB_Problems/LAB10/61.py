# Program 61 : Function to greet the user
def greet_user(name):
    if name[len(name)-1]=="a" or name[len(name)-1]=="i" or name[len(name)-1]=="A" or name[len(name)-1]=="I":
        return f"Good Evening Mrs. {name} !! Welcome to our mall"
    else:
        return f"Good Evening Mr. {name} !! Welcome to our mall" 
n=str(input("Enter your name : "))
print(greet_user(n))
# a="Yash"
# print(a[len(a)-1])

# M2
def greet_user1(name):
    if name[len(name)-1] in ("a","i","A","I"):
        return f"Good Evening Mrs. {name} Welcome to our mall"
    else:
        return f"Good Evening Mr. {name} Welcome to our mall"
n1=str(input("Enter your name : "))
print(greet_user1(n1))

a="Yash"
print(a[len(a)-1])

def greet(name):
    last_letter=name[len(name)-1]
    if last_letter =="a" or last_letter=="i":
        print(f"GM, Mrs {name}")
    else:
        print(f"Namaskar Mr {name} ji")
n1=str(input("Enter your name : "))
greet(n1)