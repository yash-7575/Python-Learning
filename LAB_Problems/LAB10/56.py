# Program 56 : Function with keyword arguments to cricket player
def about_player(name,type,age):
    print(f"Player's name is {name}, He is a {type}, his age is {age}")
n="Rohit Sharma"
t="Batsman"
a="35"
about_player(n,t,a)

#m2
def about_player1(name,type,age):
    return (f"Player's name is {name}, He is a {type}, his age is {age}")
print(about_player1(name="Virat Kohli",type="Batsman",age="32"))
      