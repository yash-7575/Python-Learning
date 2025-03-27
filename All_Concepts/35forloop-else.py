'''else statement will execute only if for loop completes successfully without break statement'''

for i in range(5):
    print(i)
else:
    print("Loop Completed successfully")

for i in range (6):
    print(i, end="")
    if i==4:
        break
else:
    print("Loop Completed successfully")

'''Above else statement will not execute coz loop breaks in between'''
print()

i=0
while i<6:
    print(i, end="")
    i=i+1
    if i==4:
        break
else:
    print("Loop Completed successfully")

'''Use kaha pe hoga? 
    jab hame confirm krna ho koi loop properly complete ho gaya ya nahi'''