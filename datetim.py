#time() returns time in seconds
#ctime() returns current date and time
#localtime() ->used to convert seconds into date and time

# from time import time,ctime,localtime

# epoch=time() #returns seconds from epoch
# print(epoch)
#
# et=ctime(epoch) #converts epoch seconds into date and time
#
# print(et)
#
# print(ctime()) # returns current date and time
#
# localtime=localtime()
# print(localtime) # returns time struct

# print(localtime.tm_year) #you can extract time, date day everything from time struct
# print(localtime.tm_mon)
# print(localtime.tm_mday)
# print(localtime.tm_hour,end=":")
# print(localtime.tm_min,end=":")
# print(localtime.tm_sec)


#datetime module
# dataetime object->A dateime object is a single object containing all the information of date and time object
from datetime import datetime


#year,month and day are compulsory argument for datetime method

dt1=datetime(year=2019,month=6,day=30)
dt2=datetime(year=2019,month=6,day=30,hour=15,minute=34)
dt3=datetime(2017,4,28)
dt4=datetime(2016,3,26,14,23)
print(dt1.year)
print(dt2.year)


# now()->returns current date and time
# ex -> datetime.now()
        # datetime.today()
        
ct=datetime.now()
print(ct)
print(ct.year)
print(ct.month)









