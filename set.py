# # a=set() #empty set

# a={10,20,30,40,"Surya"}
# print(a)
# a.add(70) # to add single element use add()
# b={"lama","moktan"}
# a.update(b) # to add multiple elements use update() 
# print("adding set new element: ",a)
# a.remove("Surya") # throws error if element does not exist
# a.discard("lama")
# print(a)

# for i in a:
#     print(i)

s=set()
n=int(input("Enter number of elements : "))

for el in range(n):
    el= int(input("Enter elements : "))
    s.add(el)
# print(s)
t=s.copy()
print("Elemets in t :",t)

# intersecton(),issubset(),issuperset(),difference()

