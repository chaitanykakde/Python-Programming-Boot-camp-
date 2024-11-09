sum=lambda x,y:x+y
diff=lambda x,y:x-y
def small(a,b):
    if a<b:
        return a
    else:
        return b
print("Smaller:",small(sum(-2,5),diff(10,5)))
