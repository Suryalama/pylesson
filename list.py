
# creating list
a=[10,30,-50,21.7,"Geekyshows"]

# creating empty list
# a=[]

# print(a,id(a))
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
#
# #modifying list
# print("After modification")
# a[1]=40
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a,id(a))

# Accssing using loop
#
# for i in a:
#     print(i)

# Accessing list using while loop

# i=0
# l=len(a)
# while i<l:
#     print(a[i])
#     i+=1
#


# append()
# print("before append")
# for el in a:
#     print(el)
#
#
# a.append(100)
# print()
# print("Afer appending ")     
#
# for ele in a:
#     print(ele)

# user input
# b=[]
#
# n=int(input("Enter number of elements : "))
#
# for i in range(n):
#
#     b.append(int(input("Enter element: ")))
#
#
# print("List : ")
# for element in b:
#     print(element)

# insert()

# print(" before insert ")
# print(a)
# a.insert(2, 300)
# print(" After insert 300")
# print(a)

# pop()

# print("before pop")
# print(a)
# a.pop(2)
# print(" after pop")
# print(a)

# remove()

# print("before remove",a)
# a.remove(-50)
# print("after remove :",a)


# index()
# i=a.index(21.7)
# print(i)

# reverse()
# a.reverse()
# for re in a:
#     print(re)


# extend()
# b=[21,32,65]
#
# a.extend(b)
#
# print(a)

# count(),sort(),clear(),slicing,

# list concatenation
# b=[10,30,54,65]
# c=[21,54,85,79]
#
# result=b+c
#
# print(result)

# repetion
#
# a=[12,11,14]
# c=a*2
#
# print(c)

# copy()
# b=a.copy()
# print(b)


# clone()

# b=a[:]
# print(b)


# nested list
#
# a=[10,20,33,[50,63]]
# b=[40,90,80]
# # a=[10,20,30,b]
#
# n= len(a)
#
# for i in range(n):
#     if type(a[i]) is list:
#         if len(a[i])>1:
#             m=len(a[i])
#             for j in range(m):
#                 print(i,j, a[i][j])
#
#     else:
#         print(i,a[i])            




# filter()
#
# a=[10,20,50,56,76,65]
#
#
# def high_marks(n):
#     if n>=60:
#         return True
#
# # result=filter(high_marks,a)
# # print(result)
# # print(type(result))
# # result=list(filter(high_marks,a))
# #using lambda
#
# result=list(filter(lambda n:(n>=60),a))
#
# print(result)
# print(type(result))
# for i in result:
#     print(i)      
#



# map()

a=[10,20,30,40,50]
b=[1,2,3,4,5]

def inc(n):
    return n+2

# map
result=map(inc,a)

# making map as list
result=list(map(inc,a))

# using lambda
result=list(map(lambda n:n+2,a))

# lambda with two variables
result=list(map(lambda n,m: n+m,a,b))


print(result)
print(type(result))

for i in result:
    print(i)

print("*********************")


# reduce()

from functools import reduce

result= reduce(lambda n,m:n+m,a)
print(result)
print(type(result))

# yield


# def show(a,b):
#     yield a
#     yield b
#
#
# result=show(1,5)
# # converting into list
# lst=list(result)
#
# print(lst)
# print(type(lst))


def show (a,b):
    while a<=b:
        yield a
        a+=1
        
result= show(1,5)
print(next(result))

print("********")

lst=list(result)

for i in lst:
    print(i)
    
# next()





