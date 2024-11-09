def facto(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i

    return fact

print("Factorial:",facto(5))    