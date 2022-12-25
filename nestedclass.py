class Army:
    def __init__(self):
        self.name="Surya"
        self.gn=self.Gun()
        
    def show(self):
        print("Name",self.name)
        
    class Gun:
        def __init__(self):
            self.name="AK47"   
            self.capacity='75 Rounds' 
            self.length=34.5
            
        def disp(self):
            print("Gun Name :",self.name)    
            print("Gun Capcity :",self.capacity)    
            print("Gun length :",self.length)    
            
a=Army()
print(a.name)
a.show()

# accessing inner class varible
print(a.gn.name)
# calling inner class method
a.gn.disp()