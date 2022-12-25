
        
        
from threading import *
from time import sleep
class prouducer:
    def __init__(self):
        self.l=Lock()
        
        
    def produce(self):
        self.l.acquire()
        for i in range(1,8):
            print(i)
            sleep(1)
            
        self.l.release()
class consumer:
    def consume(self):
        for i in range(8):
            print("consume method",i)
p=prouducer()
c=consumer()

t1=Thread(target=p.produce)
t2=Thread(target=c.consume)

t1.start()
t2.start()