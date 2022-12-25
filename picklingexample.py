# pickling-> converts class obj to byte obj
# also known as serialization
# has dump(obj,filename) method to pickle 
# import pickle module 
#-----------------------------------------
# unpickling -> converts byte obj to class obj
# also known as de-serializaton 
# has load(file) method to unpickle
#-----------------------------------------

import pickle 
class Student:
    def __init__(self,name,roll ,address):
        self.name= name
        self.roll= roll
        self.address= address
    def disp(self):
        print(f'Name: {self.name} Roll: {self.roll} Address: {self.address}') 


# with open("student.dat", mode="wb") as f:
#     stu1= Student("Surya",101, "Tokyo")
#     stu2= Student("Sonam",102, "KTM")
#     stu3= Student("Sunita",103, "UK")
#
#     pickle.dump(stu1,f)
#     pickle.dump(stu2,f)
#     pickle.dump(stu3,f)
#     print("Pickling done!")
#
#
# with open("student.dat",mode="rb") as f:
#     obj1=pickle.load(f)
#     obj2=pickle.load(f)
#     obj3=pickle.load(f)
#     print("Unpickling done!")
#
#     obj1.disp() 
#     obj2.disp() 
#     obj3.disp() 
#

# user input




    
    
    
    
    
    
    
    
    
        