a=(10,)

a=(10,20,30,40,"Geekyshows")

b=(12,13,46,79)

# for loop without index
for i in a:
    print(i)
print()
n=len(a)

# for loop with index
 
for i in range(n):
    print(a[i])
    
print()

# concatenation    

c=a+b

print(c)    

print()
# slicing 


print(a[0:])
print(a[:3])
print(a[-3:])
print(a[-5:-3])

print()

# userinput for tuple

# take input in list and convert into tuple
#
# a=[]
# n= int(input("Ener number of elements : " ))
#
# for i in range(n):
#     a.append(int(input("Enter a element: ")))
#
# print(type(a))
# a= tuple(a)
#
# print(type(a))
# print("Tuples :")
# for ele in a:
#     print(ele)


# repetition in tuples
# a=(10,20,2,0)
# print(a*2)
# print()
# # alasing in tuple
# b= a
#
# print(b)


# copying using slice

# a=(10,20,30,40,50)
# b=a[0:5]
#
# print(id(b),b)
# print(id(a),a)


# nested tuple

a=(10,20,30,40,(50,60))
b=(50,60)
a=(10,20,30,b)

# a=((10,20,30),(40,50,60))

# print(a)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[3][0])
# print(a[3][1])

n= len(a)
for i in range(n):
    if type(a[i]) is tuple:
        if len(a[i])>1:
            m=len(a[i])
            for j in range(m):
                print(i,j, a[i][j])
    else:
        print(i, a[i])           
                















