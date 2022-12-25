# The main applications areas of multi threading are 
# Multimedia graphics,Animations,Video Games Web Servers,applications servers

# import threading
#
# t = threading.current_thread().getName()
# print(t)

# creating thread

# creating thread without using class
#-------------------------------------

# from threading import Thread, current_thread # import thread module

# thread_object=Thread(target=fun_name,args=(arg1,arg2...))

# def disp(a):
#     print("Thread running",a) # passing args for disp()
#     # print("Default child thread name:",current_thread.getName())
# t=Thread(target=disp,args=(10,))
# t.start() # starting the thread using start()
#
# print("Default threadname: ",t.name)
# t.name="new thread"
# print("new child thread name :",t.name)


# NOTE : getName() and setName() method are deprecated instead use name porperty



# creating child thread of Thread class
#----------------------------------------

#from threading import Thread, current_thread

# class Mythread(Thread):
#     def run(self):
#         print("run method") # running by childthread
#         for i in range(5):
#             print("child thread")
#
# t=Mythread()
# t.start() # starts thread 
# #t.join() # it will wait until childthread is completed
# print()
# for i in range(5):
#     print("main thread") # running by main thread

#-----------------------------------------------

#ThreaChild class with constructor
#---------------------------------
#from threading import Thread

# class Mythread(Thread):
#     def __init__(self):
#         Thread.__init__(self)#calling constructor of thread class
#         print("constructor called")
#
#     def run(self):
#         pass
#
# t=Mythread()
# t.start()

#Note : you must call thread constructor if working with constructor


#creating thread without creating child class of Thread Class
#-------------------------------------------------------------

from threading import Thread

class Mythread:
    def disp(self,a,b):
        print(a,b)

#creating mythread class object
myt=Mythread() 

# creating thread object and passing myt.disp as target to run 
t=Thread(target=myt.disp(10, 20))
# starting thread
t.start()










