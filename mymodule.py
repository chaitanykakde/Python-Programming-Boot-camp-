def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return (n*fact(n-1))
def fibo(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return (fibo(n-1)+fibo(n-2))
     