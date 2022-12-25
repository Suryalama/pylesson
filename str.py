from numpy.core.defchararray import endswith

# String creation

s="Surya"
st='Surya'
str="""
I am
Surya
Lama"""

print(str)
print()
#find length of string

sl= len(str)
print(sl)

# loop through string
print()
for s in st:
    print(s)

print()
# while loop

i=0
while i<len(st):
    print(st[i])
    i+=1


#repetition of string

print("&"*7)
    
    
#slicing in string

print(st[3:5]*5)

#comparing string

str1="Geekyshows"
str2="Geekyshows"

result= str1==str2
print(result)
    
# formatting string  
  
print("{}".format(10))    
print("{} {}".format(10,20))    
    
#Integer

# print("{num:d}".format(num=15))
# print("{num:5d}".format(num=15))
# print("{num:05d}".format(num=15))
# print("{num:+5d}".format(num=15))
# print("{num:<5d}".format(num=15))
# print("{num:*<5d}".format(num=15))
# print("{num:*>5d}".format(num=15))
# print("{num:^5d}".format(num=15))
# print("{num:*^5d}".format(num=15))
    
    
# upper(),lower(),swapcase(),title()

name="Geekyshows"
# print(name.upper())  
# print(name.lower())  
# print(name.swapcase())  
# print(name.title())  
  
print()
# isupper(),islower(),istitle()
  
# print(name.isupper())
# print(name.islower())
# print(name.istitle())
#

 
 # isdigit(),isalpha(),isalnum(),isspace()
 #lstrip,rstrip,strip()
    
# Integer
num=15.23

# print(f"{num}")
# print(f"{num:5d}")
# print(f"{num:05d}")
# print(f"{num:+5d}")
# print(f"{num:<5d}")
# print(f"{num:*<5d}")
# print(f"{num:^5d}")
# print(f"{num:*^5d}")
    

# print(f"{num}")
# print(f"{num:f}")
# print(f"{num:5f}")
# print(f"{num:.20f}")
# print(f"{num:+5.2f}")
# print(f"{num:<5.2f}")
# print(f"{num:*<5.2f}")
# print(f"{num:*>5.2f}")
# print(f"{num:^5.2f}")
# print(f"{num:*^5.2f}")

# replace()
# nam="Surya Lama"
# print(nam.replace("S", "D"))

#split
st="Surya-Lama"

print(st.split("-"))

#join

name=("Surya","Lama","is","best")
print(" ".join(name))

# startswith,endswith


















