class Mobile:
    fp="Yes"
        #class variable
    @classmethod
    def is_fp(cls):   # class method
        print(cls.fp)   #accessing class variable
    @classmethod   
    def show_model(cls,r):
        cls.ram=r
        print("the ram :",cls.ram)
    
Mobile.is_fp()   # calling class function
Mobile.show_model("4GB")

    
    
