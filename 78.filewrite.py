file=open("file1",'w')
file.write("This is data")
print(file)
lines=["Hello","this is chaitany","from sambhajinagar"]
file.writelines(lines)
file.close()