# Program 60 : Function to count vowels in a string
def count_vowels(word):
    count=0
    vowels="aeiouAEIOU"
    for char in word:
        if char in vowels:
            count=count+1
        else:
            continue
    return f"Total vowels are {count}"
a=str(input("Enter a Word: "))
print(count_vowels(a))

def count_vowels(word):
    vowels="aeiouAEIOU"
    count=0
    for char in word:
        if char in vowels:
            count=count+1
        else:
            continue
    return count
word1=str(input("Enter a Word"))
print(count_vowels(word1))
