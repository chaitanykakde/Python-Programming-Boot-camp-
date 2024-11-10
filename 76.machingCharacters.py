str1 = 'abcdef'
str2 = 'defghia'

def match(str1,str2):
    m=False
    count=0
    l=[]
    for i in str1:
        for j in str2:
            if(i==j):
                m=True
        if m==True:
            count+=1        
            l.append(i)   
        m=False
    return count,l

count,l=match(str1,str2)
print("Number of Matching Characters:",count)
print("Maching Chaarcters:",l)             
            
        