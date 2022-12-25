# class Mobile:
#     @staticmethod
#     def show_model(m,p):
#         model=m
#         price=p
#         print(model,price)
#
# Mobile.show_model("Redmi",2500)

class Student:
    def __init__(self,n,r):
        self.name=n
        self.roll=r
    
    def disp(self):
        print(("Student Name :",self.name))
        print(("Student roll :",self.roll))
        
        
class User:
    @staticmethod
    def show(s):
        # accessing student obj
        print(s.name)
        print(s.roll)
    
        
# creating instance of student       
stu = Student("Surya",102)
# passing stu object to class user     
User.show(stu)
 


        