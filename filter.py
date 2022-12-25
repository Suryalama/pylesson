a=[10,40,20,30,5,9,35,45]
def high_marks(n):
    if n>=30:
        return True

result=list(filter(high_marks,a))

print(result)
print(type(result))
for i in result:
    print(i)


