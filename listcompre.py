
#list comprehension
# new_list= [i+1 for i in range(20)]
# print(new_list) 

# list comprehension with if statement
# new_list= [i for i in range(10) if i%2==0]
# print(new_list)
# list comprehension with nested if statemenet
# new_list= [i for i in range(10) if i%2==0 if i%3==0]
# print(new_list)
# list comprehension with if else statement
new_list= [i if i%2==0 else "invalid" for i in range(10)]
print(new_list)



 