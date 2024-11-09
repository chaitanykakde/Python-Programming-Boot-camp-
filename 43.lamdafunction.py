sum=lambda x,y:x+y
print("Sum:",sum(5,3))

#___________________________

def fun(f,n):
    print(f(n))
twice=lambda x:x*2
thrice=lambda x:x*3

fun(twice,4)
fun(thrice,3)

#_____________________________

dee=lambda :sum(range(1,11))
print(dee())
