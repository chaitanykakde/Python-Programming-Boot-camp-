#Write a Python program to print the numbers from a given number n till 0 using recursion
n=int(input("Enter Number To print till 0 recursively:"))
def recur(n):
    if n==0:
        return
    else:
        print(n)
        n=n-1
        recur(n)
              
recur(n)    