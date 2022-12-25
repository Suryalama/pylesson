import pickle, stud
with open("student.dat",mode="rb") as f:
    while True:
        try:   
            obj1=stud.pickle.load(f)
            obj1.disp() 
        except EOFError:
            print("Done")
            break # to get out from loop