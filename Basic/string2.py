a="!!!!!Ramesh Sharma Ramesh!!!!!!"
print(a.upper())
print(a.lower())
print(a.rstrip("!")) #removes the railing charcters after the main string
print(a.replace("Ramesh", "Rahul"))
b=a.split(" ") #split fn is used to create lists of substrings sepereted by commas
print(b)
print(b[0])
print(b[2])
c="introdUctiOn to HTML"
d=c.capitalize() #capatilize the first word
print(d) 
print(len(d))
print(d.center(40))
print(len(d.center(40)))
print(len(d.center(50)))
print(a.count("Ramesh"))
print(d.count("o"))
print(a.endswith("!"))
print(a.endswith("!!!!"))
print(a.endswith("*"))
print(a.startswith("!"))
print(d.endswith("n",0,11))
print(d.endswith("n",0,12))
print(d.startswith("t",2,13))
e="My Name is Yash"
print(e.find("is")) #gives the index of substring
print(e.find("isyh")) #returs -1 if substring not found
#print(e.index("ishh")) # same as find but it gives error if substring not found
f="!Yash1234"
print(f.isalnum())
f1="yash"
print(f1.isalpha())
f2="123"
print(f2.isnumeric())
print(f1.islower())
f3="welcome to my home\n"
print(f3.title()) #capitilize first letter of all words
print(f3.istitle())
print(f3.isprintable()) # returns false when any of the character is not printable '\n'
f4="        "
print(f4.isspace()) # true only when there are blank spaces
f5="Introduction to Python"
print(f5.swapcase()) #upper to lower and lower to upper 

