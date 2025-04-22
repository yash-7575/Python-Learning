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
