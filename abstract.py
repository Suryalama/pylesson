# PVM can't create object of an abstract class class:
# it is not necessary to declare all the methods abstract in abstract class
# abstract class can have abstract method and concrete method
#if one method is abstract in class that class must be abstract
#abstract method of an abstract class must be defined in child class
#to create abstract class you must inherit ABC class


from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    
    def show(self):
        print("Concrete Method")
        
        
class Child(Father):
    
    def disp(self):
        print("Child class")
        print("Defining abstract method")
        
c=Child()
c.disp()
c.show()