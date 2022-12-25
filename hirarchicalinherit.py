class Father:
    def __init__(self):
        print("Father class constructor")
        
    def showF(self):
        print("Father class method")
class Son(Father):
    def __init__(self):
        super().__init__() # calling father class constructor
        print("Son class constructor")
        
    def showS(self):
        print("Son class method")
        
class Daughter(Father):
    def __init__(self):
        super().__init__() #calling father class constructor
        print("Daughter class constructor")
        
    def showD(self):
        print("Daughter class method")
        
s=Son()
d=Daughter()
d.showF()
d.showD()
s.showF()
s.showS()
