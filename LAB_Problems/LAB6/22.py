#pgm to reverse a number 
n=int(input("Enter a number : "))
#lets say n=1234
#create a variable where we store the reveresed number

result=0 #initialize it with zero
n1=n #store value of n in n1 to check whether its palindrone or not

while(n!=0): #jab tak n zero na ho jaye loop chala, no need of for loop
    last_digit=n%10 #here we store the last digit of our no. example 1234%10=4
    result=result*10+last_digit #here we upgrade our new result, result=0*10+4=4
    n=n//10 #last me n ko 10 se divide krke uska integer part lelo for further part of loop, 1234//10=123
print(result)
#if reversed number == initial number then these numbers are called palindrone number
if(n1==result):
    print("It's a palindrone number")
else:
    print("It's not a palindrone number")


#pgm to display numbers in reverse order 
m=int(input("Enter a number : "))
for i in range(m,0,-1):
    print(i)

for i in range(10,0,-1):
    print(i)