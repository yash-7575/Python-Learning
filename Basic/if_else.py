import time
t=time.strftime("%H,%M,%S")
print(t)
# age=int(input("Enter your age "))
# if (age>=18):
#     print("You can drive")
# else :
#     print("You cant drive")
th=int(time.strftime("%H"))
print(th)
if(9<=th<4):
    print("Good Night SIR!!")
elif(4<=th<12):
    print("Good Morning SIR!!")
elif(12<=th<16):
    print("Good Afternoon SIR!!")
else :
    print("Good Evening SIR!!")
