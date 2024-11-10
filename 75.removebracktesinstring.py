#remove brackates function
def removeBrackets(str):
    new_str=""
    lent=len(str)-1
    i=0
    while i<lent:
        if(str[i]!=')' and str[i]!='('):
            new_str+=str[i]
        i+=1
    return new_str

str=input("Enter String:")
print("String withut Expression:",removeBrackets(str))



