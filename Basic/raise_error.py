try:
    a=input("Enter Value between 5 and 9 ")
    if(a=="quit"):
        print("Good")
    elif a.isalpha():
        raise ValueError("Bhai ek integer value enter kar ya quit type krde")
    elif(int(a)>9 or int(a)<5):
        raise ValueError("Bhai 5 se 9 ke bich value enter kar")
    else:
        print("Koi error nahi hai")
except Exception as e:
    print(e)

a=input("Enter Value between 5 and 9 ")
if(a=="quit"):
        print("Good")
elif a.isalpha():
        raise ValueError("Bhai ek integer value enter kar ya quit type krde")
elif(int(a)>9 or int(a)<5):
        raise ValueError("Bhai 5 se 9 ke bich value enter kar")
else:
        print("Koi error nahi hai")
'''Without try except code likhoge and error aa gayi to program tham jayega (aage ka execute nahi hoga) but with try except likhoge to pata chal jayega error konsi hai and execution stop nahi hoga'''
while(a!="quit"):
    a=input("Enter a value or quit: ")
a="123"
print(a.isnumeric())
b="yash"
print(b.isalpha())
c="123yash"
print(c.isalnum())