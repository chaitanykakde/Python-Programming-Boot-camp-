file=open("Aura",'r')
words=file.read()
print(len(words))
ch=input("enter Char to count:")
count=0
for i in words:
    if i==ch:
        count+=1
print("Counts of char %c:%d"%(ch,count))        
