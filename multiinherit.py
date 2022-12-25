class Father:
    def __init__(self):
        super().__init__()
        print("Father class constructor")
    def showf(self):
        print("Father class method")
        
class Mother:
    def __init__(self):
        super().__init__()
        print("Mother class constructor")
    def showM(self):
        
        print("Mother class method")
        
        
class Son(Mother,Father):
    def __init__(self):
        super().__init__() #calling parent class constructor
        print("son class constructor")
    def showS(self):
        print("Son class method")
        
        
s=Son()
s.showS()
s.showM()
s.showf()