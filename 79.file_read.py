file=open("file1",'r')
str=file.read(10)
print(str)
print(list(file))
for line in file:
    print(line)
file.close()