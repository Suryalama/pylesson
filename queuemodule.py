#Queue --> it is thread safe
#put()--> used to insert items in the queue


from threading import Thread
from queue import Queue

from time import sleep

class Producer:
    def __init__(self):
        self.q=Queue()
    def producer(self):
        for i in range(1,6):
            print("Item produced",i)
            self.q.put(i)
            sleep(1)
            
class Consumer:
    def __init__(self,prod):
        self.prod=prod
    def consume(self):
        for i in range(1,6):
            print("Item received", self.prod.q.get(i))
            
p=Producer()
c=Consumer(p)

t1=Thread(target=p.producer)
t2=Thread(target=c.consume)
t1.start()
t2.start()
