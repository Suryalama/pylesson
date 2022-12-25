#method overriding is used to override the existing 
#behavior of parent class method 
#for method overriding there should be inheritance relation
# super()

class Add:
    def result(self,a,b):
        print("Addtion :",a+b)

class Multi(Add): # inheriting the parent class
    def result(self,a,b): # overriding the result method of parent
        super().result(a, b) #calling parent class method
        
        print("Multiplication :",a*b)
        
m=Multi()
m.result(10,20)

