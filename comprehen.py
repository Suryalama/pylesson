# list comprehension


# syntax: [expression for item in iterable_object if_ state]
lst= [0,1,2,3, 4,5,6]
# new_lis=[]
# for i in lst:
#     new_lis.append(i+1)
# print(new_lis)
#
# print()
#
# # with list comprehension
#
# lst2= [0,1,2,3, 4,5,6]
#
# new_lst2=[i+1 for i in lst2]
# print(new_lst2)

print()

lst1=[]
# for i in range(20):
#     if (i%2==0):
#         lst1.append(i)
# print(lst1)

# lst1=[ i for i in range(20) if i%2==0 if i<=10 ]

# print(lst1)


# list comprehension with if else statement

# for i in range(20):
#     if (i%2==0):
#         lst1.append(i)
#     else:
#         lst1.append('Invalid')  


lst1=[i if i%2==0 else 'invalid' for i in range(10)]

print(lst1)

print()
# nested list comprehension

a=[[24,30,36],[28,35,42]]

for i in range(6,8):
    for j in range(4,7):
        pass

lst2=[[ i*j for j in range(4,7) if i*j<=40 ]  for i in range(6,8) ]
print(lst2)
print()
# set comprehension

set1=set()
set1={ i*2 for i in range(10)}
print(set1)
print((type(set1)))

# dict comprehension

# without comprehension

dict1={}
for n in range(10):
    if (n%2==0):
        if(n%3==0):
            dict1[n]=n*2


print(dict1)
print()
# with comprehension

dict2={n:n*2 for n in range(10) if n%2==0 if n%3==0}
print(dict2)
print(type(dict2))
print()

# with else

dict1={}
for n in range(10):
    if (n%2==0):
        dict1[n]=n
    else:
        dict1[n]='Invalid'

print(dict1)

print()

dict2={n:(n if n%2==0 else 'Invalid') for n in range(10)}
print(dict2)
print(type(dict2))
print()

# list of tuple into dict

ls=[(101,'Rahul'),(102,'Surya')]
dict3 ={k:v for k,v in ls}

print(dict3)
print(type(dict3))
print()






