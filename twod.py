from numpy import *
from termios import CRPRNT
from django.contrib.admin.utils import flatten

a= array([ [10,30,40,20],
          [23,65,45,98]
            ])

# print(a[0][0])
# print(a[1][3])
# print(a[0][3])
# print(a[1][2])
# print(a[1][1])

#access 2D array using for loop


# n= len(a)
#
# for i in range(n):
#     for j in range(len(a[i])):
#         print(a[i][j])
#     print()    


# access 2D array using while loop

# n= len(a)
# i=0
# while i<n:
#     j=0
#     while j<len(a[i]):
#         print(a[i][j])
#         j+=1
#     i+=1
#     print()
#

#creating 2D using zeros()

# a= zeros((3,2),dtype=float)
# n= len(a)
#
# for i in range(n):
#     for j in range(len(a[i])):
#         print(a[i][j])
#     print()    



 #creating 2D using ones()

# a= ones((3,2),dtype=float)
# n= len(a)
#
# for i in range(n):
#     for j in range(len(a[i])):
#         print(a[i][j])
#     print()    

# reshape()

# 1D to 2D
a= array([1,2,3,4,5,6])
b= reshape(a,(2,3))
#
# print(a)
# print(b)
#
# # 2D to and 
# f= reshape(b,(6))
# print(f) 
#

#flatten()

# 2D to 1D
# f= b.flatten()
# print(f)


# input from user

m= int(input("Enter no of rows : "))
n= int(input("Enter no of columns : "))

ar=zeros((m,n),dtype=int)
l= len(ar)

print(ar)





    
    
    
    
    
    
    
    
    
    
    