#invalide date findings
print("Enter month, day, year")
month=int(input())
day=int(input())
year=int(input())

if(month<1 or month>31) :
    print("Date is invalid")
elif(day<1 or day>31) :
    print("Date is invalid")
elif(month==2 and day> (29 if ((year%4==0 and year%100 !=0) or (year%400==0)) else (28))):
    print("Date is invalid")
elif(month in [4,6,9,11] and day>30) :
    print("Date is invalid")
else :
    print("date is valid")