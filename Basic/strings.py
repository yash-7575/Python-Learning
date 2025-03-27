# 1. Print everything except the first two characters.
# 2. Print everything except the last two characters.
# 3. Extract "piece" from "masterpiece".
# 4. Extract "master" from "masterpiece" without using negative indexing.
# 5. Print every alternate character of "masterpiece".

s = "masterpiece"
print(s[2:])
print(s[0:-2])
print(s.index("p"))
print(s[6:]) # [(s.index(p)):] also valid
print(s[0:6])
print(s[0:len(s):2])
s1=s[::-1]
print(s1[::2])

for char in s:
    if char in 'aeiouAEIOU':
        print(char)
    else:
        continue
s_l=[char for char in s if char in 'aeiouAEIOU']
print(s_l)
s2=str(s_l) # wrong it gives "['a', 'e', 'i', 'e', 'e']" full as a str
s2="".join(s_l)
print(s2)

# s_l= ['a', 'e', 'i', 'e', 'e']
s3=''
for i in s_l:
    s3=s3+i
print(s3)
print("fun "*5)

# Given: s = "programming is fun"
# 1. Convert the string to uppercase.
# 2. Replace 'fun' with 'awesome'.
# 3. Find the index of 'is'.

s = "programming is fun"
print(s.upper())
print(s.replace('fun','awesome'))
print(s.find('is'))

# Given: s = "hello world python"
# 1. Split the string into words.
# 2. Join the words back using "-" instead of spaces.

l=s.split(' ')
print(l)
s= "-".join(l)
print(s)

# 1. Print a sentence that contains a new line.
# 2. Print a sentence that contains a tab space.
# 3. Print a sentence with both single and double quotes.
print("Hello\nWorld")
print("Hey\tThere!!!")
print("Hey there I'm \"Yash\"")
s="Hey!!!!!"
print(s.strip("!"))
s4="".join(reversed(s))
print(s4)

# 1. Reverse the string: "Python is powerful"
# 2. Reverse only the words in the string: "I love programming"
s="Python is powerful"
print(s[::-1])
s="I love programming"
l=s.split(" ")
print(l)
s5=''
for i in l: # data type of i is str so we can perform any string methods/operations
    s5=s5+i[::-1]+" "
print(s5)

# Given: s = "Python Programming is Fun!"
# 1. Convert to lowercase.
# 2. Replace "Fun" with "Awesome".
# 3. Find the index of "Programming".
# 4. Extract the word "Python" using slicing.
# 5. Reverse the entire string.

s = "Python Programming is Fun!"
s1=s.lower()
s2=s.replace("Fun","Awesome")
i=s2.find("Programming")
s3=s[:s.find(" ")]
s4=s2[::-1]
print(s)
print(s1)
print(s2)
print(i)
print(s3)
print(s4)