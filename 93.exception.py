try:
    x=0
    z="uuu"
    print(x)
    if x==0:
        raise Exception("Zero")
    if not type(z) is int:
        raise TypeError("Only integers are allowed")
except:
    print('exception Ocuuerd')
else:
    print("Exception is not occured")
finally:
    print("finnaly block")

