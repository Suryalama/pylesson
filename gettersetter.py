# to access variable of data
#also called accessor method


class Mobile(object):
    def __init__(self):
        self.model="Redmi X"
        
    def get_model(self):
        return self.model
    
    def set_model(self):
        self.model="Redmi 1"
        
redmi=Mobile()
m=redmi.get_model()
print(m)
# after setting model
redmi.set_model()

m=redmi.get_model()
print(m)