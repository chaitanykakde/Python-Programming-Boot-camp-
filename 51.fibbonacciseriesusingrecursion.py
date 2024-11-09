n=int(input("Enter N term to print fibbonacci using recursiton:"))
def fibbonacchi(n):
    if n==0 or n==1:
        return 0
    if n==2:
        return 1
    else:
        return fibbonacchi(n-1)+fibbonacchi(n-2)

print(fibbonacchi(14))    


        