
class Father:
    def __init__(self,r):
        self.money=r
        print("Father class constructor")
    def show(self):
        print(("Father class instance method"))  

        
class Son(Father):
    def __init__(self,r):
        super().__init__(r) # calling father class constructor
        self.money=r
        self.car="BMW"
        print("Child class constructor")
        
    def disp(self):
        print("Son class instance method calling father class  variable",self.money)
        
s=Son(2000)
print(s.money)
print(s.car)
s.disp()
s.show()


