a=(10,20,30,(40,50))
b=((10,20,30),(60,70,80))
n=len(a)
for i in range(n):
    if type(a[i]) is tuple:
        if len(a[i])>1:
            m=len(a[i])
            for j in range(m):
                print(i,j,a[i][j])
    else:
        print(i,a[i])


print('*********')
for r in b :
    for m in r:
        print(m)

print('****************')

n=len(b)
i=0;
while i<n:
    j=0;
    while j<len(b[i]):
        print(i,j,b[i][j])
        j+=1
    i+=1
print('**********')