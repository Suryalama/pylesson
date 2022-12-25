a=[10,20,30,40,50]
b=[1,2,3,4,5]

# def incre(n):
#     return n+2

# # result =list(map(incre,a))
# result= list(map(lambda n :n+2,a))
# print(type(result))
# for i in result :
#     print(i)

result = list(map(lambda n,m:n+m,a,b))
for i in result:
    print(i)
    