def isanagram(word,anagram):
    '''This fn helps to check anagram of any word 
    example- listen : silent '''
    l=[]
    for char in word:
        l.append(char)
    l1=[]
    for i in range(0,len(l)):
        for char in anagram:
            if char==l[i]:
                l1.append(char)
    if len(l)==len(l1):
        return True
    else:
        return False

print(isanagram("hello","holle"))
print(isanagram("listen","silent"))

'''Great logic but its just a one line answer'''

def isanagram2(word,anagram):
    return sorted(word)==sorted(anagram)

print(isanagram2("listen","silent"))
print(isanagram2("hello","holle"))