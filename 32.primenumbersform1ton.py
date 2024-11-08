n=int(input("Enter Limit upto you whnt generate prime numbers:"))
flag=0
j=2
for i in range(1,n+1):
    j=2
    while(j<i):
      if(i%j==0):
         flag=1
      j=j+1   
    if(flag==0):
       print(i)
    else:
       flag=0        

    
                
