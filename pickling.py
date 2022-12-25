import pickle , stud
numberOfStudent=int(input("Enter the no of students."))

with open("student.dat", mode="wb") as f:
    for i in range(numberOfStudent):
        name= input("Enter name: ")
        roll=int(input("Enter roll: "))
        address=input("Enter address: ")
        studentObject= stud.Student(name,roll,address)
        stu=pickle.dump(studentObject,f)
   
print("pickling done!")    