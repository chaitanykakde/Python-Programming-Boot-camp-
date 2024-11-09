import math
a=int(input("enter numner one:"))
b=int(input("Enter Number Two:"))
sum=a+b
print("Sqrt:",math.sqrt(sum))
#__________________________________

radius=int(input("Enter the radius of  circle:"))
area=math.pi*radius**2
circumference=2*math.pi*radius
print("Area:",area)
print("circumference:",circumference)

#___________________________________________

angle=int(input("Enter the angle in degrees:"))
radius=math.radians(angle)
print(math.sin(radius))
print(math.cos(radius))
print(math.tan(radius))

#____________________________________________________