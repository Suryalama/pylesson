class Father:
    def __init__(self):
        self.money=1000
        print("Father class constructor")
        
    def show(self):
        print("Father class method")
  

class Son(Father):
    # def __init__(self):
    #     print("Child class constructor")
    def disp(self):
        print("Father class constructor :",self.money)
        
        
s=Son()
s.show()
print(s.money)
s.disp()