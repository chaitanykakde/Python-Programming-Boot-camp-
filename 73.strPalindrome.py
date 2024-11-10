str=input("Enter String:")
def reverse(str):
    newstr=''
    i=len(str)-1
    while(i>=0):
        newstr+=str[i]
        i-=1
    return newstr    


rev=reverse(str)
print("Reverse of String:",rev)
if(rev==str):
    print("String is Palindrome")
else:
    print("String is not Palindrome")
        
