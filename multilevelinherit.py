class Father:
    def __init__(self):
        print("Father class constructor called")
        
    def showF(self):
        print("Father class instance method")
#inheriting father class      
class Son(Father):
    def __init__(self):
        super().__init__() #calling father class constructor
        print("Son class constructor called")
        
    def showS(self):
        print("Son class instance method")
                
#inheriting Son class      
class GrandSon(Son):
    def __init__(self):
        super().__init__() # calling son constructor
        print("Grandson class constructor called")
        
    def showG(self):
        print("Grandson class instance method")
#creating grandson object               
g=GrandSon()

g.showG()
g.showS()