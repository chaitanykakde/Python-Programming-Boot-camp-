# message="Hello"
# # # for i in message:
# #     print(i)
# print(message[-1]) 
# print(message[3]) 
# print(message[0]) 

s1="hello"
# s2="world"
# s3=s1+s2
# # print(s3)
# # s1+=s2
# # print(s1*3)
# str="Chaitany "+str(123)
# print(str)

#length of str
print(len(s1))

#isalfanum
print(s1.isalnum())

#isAlfabets:

print(s1.isalpha())

#isdigit
s1='002'
print(s1.isdigit())

#islower()

s1='hello'
print(s1.islower())

#isuuper
s1="UUU"
print(s1.isupper())

#isspace
s1="  "
print(s1.isspace())

#capialize 
s1="hello world"
print(s1.capitalize())

s1=''
print(len(s1))

#lower
s1="HelLLo"
print(s1.lower())

#upper
print(s1.upper())

#strip -removes white spaces
s1="   he  llo  "
print(s1.strip())

s1="   hello  "
print(s1.lstrip())
print(s1.rstrip())

#id function in python returns memory address of object

a=10
print("Address of A:",id(a))
b=10
print("Addresss of b",id(b))
if(id(a)==id(b)):
    print("Addresses Are Same")
else:
    print("Difference in Addresses") 
       










    