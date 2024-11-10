L=[20,30,40,59,69,79,89]
# for item in L:
#     print(item)
# n=len(L)
# for i in range(n):
#     print(L[i]," ",end=" ")
# kay=int(input("Enter Search Element:"))
# f=False
# for i in L:
#     if(i==kay):
#         f=True
#         break
# if(f==True):
#     print("element is found")
# else:
#     print("element is not found")        

# l1=[1,2,3]
# l2=[4,5,6]
# l3=l1+l2
# print(l3)
# print(l1*10)

# l=[10,20,30,40]
# l.append(50)
# print(l)
# l2=l.copy()
# print(l2)
# print(l.index(40))
# l.reverse() 
# print(l)

# l=[]
# for i in range(5):
#     x=int(input())
#     l.append(x)
# print(l)
# l.clear()
# print(l)    

l=[1,11,2,3,44,4,4,5]
# print(l.count(4))

# l.extend([4,5,6])
# print(l)

# l.insert(0,25)
# print(l)

# print(l.pop())
# print(l.pop())
# print(l)

# l.remove(4)
# print(l)

# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)

# print(max(l))
# print(min(l))
# max=min=l[0]
# for i in l:
#     if(i>max):
#         max=i
#     if(i<min):
#         min=i
# print(max)
# print(min)            

# list comprehention
sqare_list=[x**2 for x in range(11)]
print(sqare_list
      )
even_square_list=[x**2 for x in range(20) if x%2==0]
print(even_square_list)