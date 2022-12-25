
class Father:
    money=1000
     
    def show(self):
        print("Parent class instance method")
    @classmethod
    def showMoney(cls):
        print("Parent class method :",cls.money)
    @staticmethod   
    def stat():
        a=10
        print("Parent class stat method:",a)
        
        
class Son(Father):
    
    def disp(self):
        print("Child class instance method")
        
        
s=Son()
s.disp()   

s.show()
s.showMoney()   
s.stat() 