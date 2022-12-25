#actually method overloading concept is not in python
#but we can achieve it see the following example 

class Myclass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
            return s
        else:
            s="provide atleast two numbers"
            return s
    
obj=Myclass()
print(obj.sum(10))