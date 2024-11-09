def cube(x):

    def square(x):
        s=x*x
        print(s)
        return s
    c= square(x)*x
    return c  
     
n=int(input("Enter Any Value"))
print(cube(n))         