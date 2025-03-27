def avg(*nums): #*nums create tuple of the given numbers
    sum=0
    for i in nums:
        sum=sum+i
    print(f"sum is {sum}")
    avg=sum/len(nums)
    print(avg)
avg(2,10)

def avg(*nums): #*nums create tuple of the given numbers
    sum=0
    for i in nums:
        sum=sum+i
    print(f"sum is {sum}")
    return sum/len(nums)
    
c= avg(2,10)
print(print.__doc__)
