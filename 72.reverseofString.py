str=input("Enter String:")
def reverse(str):
    newstr=''
    i=len(str)-1
    while(i>=0):
        newstr+=str[i]
        i-=1
    return newstr    



print("Reverse of String:",reverse(str))