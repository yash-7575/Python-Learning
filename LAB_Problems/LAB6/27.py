# Program to find the sum of digits of a number
n=int(input("Enter a number : "))
sum=0
#same as reverse number logic just we do sum=sum*10+last digit for reversing and sum=sum+lastdigit for direct sum of digits
while(n!=0):
    last_digit=n%10
    sum=sum+last_digit
    n=n//10
print("sum of digits is : ", sum)