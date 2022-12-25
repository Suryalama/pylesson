#thread communication
#event class
#set(),wait(),clear(),is_set()

from threading import Thread,Event
from time import sleep

def light_switch():
    sleep(3)
    e.set() # set th flag true
    print("Green Light ON")
    sleep(5)
    print("Red Light is ON")
    e.clear() # sets flag false


def traffic():
    e.wait() # unblock the thread
    while e.is_set(): # checks the flag false or true
        print("You can Go...")
        sleep(.5)
    print("Program Done")
        
e=Event()

t1=Thread(target=light_switch)
t2=Thread(target=traffic)

t1.start()
t2.start()   
