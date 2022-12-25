from threading import *

class Flight:
    def __init__(self,available_seat):
        self.available_seat=available_seat
        self.l=BoundedSemaphore(2)
        
        
    def reserve(self,need_seat):
        #locking thread
        self.l.acquire()
        print("Available seats: ",self.available_seat)
        if(self.available_seat>=need_seat):
            name=current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.available_seat-=need_seat
            
            
        else:
            print("Sorry!! All seats are alloted")
            #releasing thread 
        self.l.release()   
        self.l.release()   
        self.l.release()   
f=Flight(2)

t1=Thread(target=f.reserve,args=(1,),name="Rahul")            
t2=Thread(target=f.reserve,args=(1,),name="Sonam")   
t3=Thread(target=f.reserve,args=(1,),name="Raj")   

t1.start()        
t2.start()
t3.start()

# NOTE: here both threads t1,t2 are acting on same reserve function at same time  
#so it result unexpected results this is called race condition
  
            