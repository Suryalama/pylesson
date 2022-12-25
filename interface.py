#actually python has no interface concept
# if you declares only abstract methods inside the abstract class
#no single concrete method but if you create concrete method also 
#do not show error but it will be abstract class instead


from abc import  ABC, abstractmethod
from numpy import disp

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    @abstractmethod
    def show(self):
        pass

class Child(Father):
    
    def disp(self):
        print("disp method from child overriding father disp")
    def show(self):
        print("show method overriding father show method")
        
c= Child()
c.disp()
c.show()

