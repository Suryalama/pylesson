# Generators are functions that return as sequence of values.
#We use yield statement to return the value from function.
a=[12,14,14,41,43]

def disp(b):
    yield b

result =disp(a)
print(result)
print(type(result))
for i in result:
    print(i)


