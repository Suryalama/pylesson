# set doesnt accept duplicates
a=set()
print(type(a))
a= {10,20,30,40,'Geekyshows','Raj'}

print(a)
print(type(a))

for i in a:
    print(i)
    
# add()    

a.add('Python')

print(a)


# update()
# update can take list,tuples,

a.update([50,60,70,80,'Surya'])
print(a)

print()

# delete or discard()

a.remove('Surya') # if element is not exist it will throw errors

print(a)
print()
a.discard(30) # if element is not exist it will not throw errors
print(a,id(a))
print()

# copy
b= a.copy()
print(b, id(b))

# clear removes all elements at once from set

b. clear()
print(b)


# set classmethods

a={"Rahul","Raj","Sonam","Raani"}
b={"Sumit","Rahul","Raani","Python","Java"}

print("A : ",a)
print("B : ",b)

print()

ism= a.intersection(b)
print(ism)
print()
uni= a.union(b)
print(uni)

print()

diff=a.difference(b)
print(diff)
print()

subse=a.issubset(b)
print(subse)
print()

supeset=a.issuperset(b)
print(supeset)
print()




