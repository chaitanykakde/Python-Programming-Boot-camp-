n=int(input("Enter Number for Reverse:"))
sum=0
while n!=0:
    rem=n%10
    sum=sum*10+rem
    n=n//10
print("Reverse:",sum)    
    