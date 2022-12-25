#used for checking the obj has attribute(methods) 

class Duck:
    def walk(self):
        print("thapak thapak ")
        
class Horse:
    def walk(self):
        print("tabdak tabdak ")
class Cat:
    def talk(self):
        print("meow meow ")
        
def myfunction(obj):
    if hasattr(obj,'walk'): #checks the walk attribute in objj
        obj.walk()
    if hasattr(obj,'talk'): #checks the walk attribute in objj
        obj.talk()
    
d=Duck()
myfunction(d)
h=Horse()
myfunction(h)

c=Cat()
myfunction(c)