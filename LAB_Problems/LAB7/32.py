#program to check whether the list is empty or not

# simple code
# empty_list=[]
# if empty_list:
#     print("It's not a empty list")
# else:
#     print("It's a empty list")
# l1=[2,3]
# if l1:
#     print("not empty")
# else:
#     print("empty")

a=[]
n=int(input("Enter the no. of elemets: "))
for i in range(0,n):
    b=int(input("Enter the elements: "))
    a.append(b)
print(a)
if len(a)==0:
    print("List is empty")
else:
    print("List isn't empty")
    print(len(a))
