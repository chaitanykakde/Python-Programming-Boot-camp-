#calculate area of triangle using Heron's Formula 
#area=sqrt(S*(S-a)*(S-b)*(S-c))
a=float(input("Enter the first side of triangle"))
b=float(input("Enter the second side of triangle"))
c=float(input('Enter the third side of of triangle'))

s=(a+b+c)/2
print("S=",s)
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area :",area)