#Problem 16 : Program to delete characters at indices divisible by 3

# Input a string from the user
text = input("Enter a string: ")

# Create a new string excluding characters at indices divisible by 3
new_text = ""
for index in range(len(text)):
    if index % 3 != 0:  # Keep characters whose indices are not divisible by 3
        new_text += text[index]

# Output the modified string
print("Modified string:", new_text)

# Case 1 : chocolate
''' Step-by-Step:
Positions:
c = 0 (remove), h = 1 (keep), o = 2 (keep), c = 3 (remove), o = 4 (keep), l = 5 (keep), a = 6 (remove), t = 7 (keep), e = 8 (keep).
Result:
"New string: hoolete"
'''
# Case 2 : pineapple
''' Step-by-Step:
Positions:
p = 0 (remove), i = 1 (keep), n = 2 (keep), e = 3 (remove), a = 4 (keep), p = 5 (keep), p = 6 (remove), l = 7 (keep), e = 8 (keep).
Result:
"New string: inaple"
'''
word=str(input("Enter a Word: "))
newstr=""
a=len(word)
# print(a)
for i in range(a):
    if(i%3!=0):
        newstr=newstr+word[i]
print(newstr)