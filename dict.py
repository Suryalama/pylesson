
# elements are with key value pair in dict
# createing empty dict
# dict_name={}
# print(type(dict_name))
stu = {101:"Rahul", 102:"Raj", 103:"Sonam"}
fees = {'Rahul':1000, 'Raj':3000, 'Sonam':4000}

# accessing dict
print(stu)
print(type(stu))

print(stu[101])
print(stu[102])
print(stu[103])

print()

print(fees)
print(fees['Rahul'])

print()

# modifying dict

print("Before modification ")
print(stu, id(stu))

stu[101] = 'Python'
print("After modification ")
print(stu, id(stu))
print()

# adding new item 
# while adding new item if the key name is same it override the value 
stu[104] = 'Surya'
print(stu, id(stu))
print()

# Deletion

# for single item
# del stu[102] 

# to delete all item
# del stu

# testing key

if 101 in stu:
    print("True")

print(101 in stu)

print(105 not in stu)

# clear() to clear all elements from dict

# stu.clear()

# copy()
# syntax; dict.copy()

new_stu = stu.copy()
print(stu, id(stu))
print(new_stu, id(new_stu))
print()

# fromkeys() to create new dict with specified keys

# syntax: dict.fromkeys(keys,value)

key = (105, 106, 107)
# v='Geekyshows','Surya','Lama'
v = 'Geekyshows'

d = dict.fromkeys(key, v)
print(d)
print()

# get() this method returns value of specified key
# if key is not found it will return none

print(stu.get(103))

# items()

it = stu.items()
print(it)
print(type(it))
print()

lst = list(it)
print(lst)
print(type(lst))
print()

# print(lst[0])
# print(lst[0][0])
# print(lst[0][1])
#

# for r in lst:
#     for c in r:
#         print(c)

# keys()

all_keys = stu.keys()
# converting into list
lst = list(all_keys)

print(all_keys)
print(lst)

print()

# values() return all values of keys present in dict

all_values = stu.values()

# converting into list

values_list = list(all_values)

print(all_values)
print(type(all_values))
print()
print(values_list)
print(type(values_list))

for i in all_values:
    print(i)
print()

# update()
print("before updating :", stu, id(stu))
stu.update({101:"Surya"})
print("After updating :", stu, id(stu))

print()

# pop()

# stu.pop(102)
# print(stu)

# popitem this will remove last inserted item in dict

remove_item = stu.popitem()

print(remove_item)

# setdefault() if the key is present returns its value  otherwise inserts item

# returned_value=stu.setdefault(101, "Java")
returned_value = stu.setdefault(109, "Java")

print(returned_value)

print()

# accessing dict using for loop

for k in stu:
    print(k, '=', stu[k])  # printing values using keys

print()

# nested dictionary

# a={
#     1:{},
#     2:{},
#     3:{}
#
#     }

a = { 'course':'Python',
   'fees':15000,
   1:{'course':'Javascript', 'fees':20000}
         
    }

print(a['course'])
print(a['fees'])
print(a[1])
print(a[1]['course'])
print(a[1]['fees'])

print()
# modifying nested dict
a['course'] = 'Machine Learning'
a[1]['fees'] = 200000

print(a)

# deleting 

# del a[1]['course']
# del a

# adding new items

a['Duration'] = '6 months'
a[1]['Teacher'] = 'Geekyshows'

print(a)
print()

# accessing nested dict using for loop

for i in a:
    if type(a[i])is dict:
        for k in a[i]:
            print(k, '=', a[i][k])
            
    else:
        print(i, '=', a[i])

