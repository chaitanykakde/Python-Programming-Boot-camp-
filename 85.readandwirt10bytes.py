with open("Aura",'rb')as file1:
    with open("Num",'wb') as file2:
        txt=file1.read(10)
        file2.write(txt)