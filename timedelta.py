# creating object of timedelta class class

# object_name=timedelta(days=0,seconds=0,microseconds=0,milliseconds=0,minutes=0,hours=0,weeks=0)
# arguments are optional

# millisecond is converted to 60 seconds
# minute is converted to 60 seoconds
#an hour is converted to 3600 seconds
# a week is converted to 7 days

from datetime import timedelta,date

td=timedelta(days=10)# days after today
d= date.today() # current date
print(d+td) # ex: it will increase date not integer value

print(d-td) # ex : date before today

#----------------------------
#comparing two dates
#----------------------------

# using ==,<,>
# it will return True or False


d1=date(2019,8,12)
d2=date(2010,6,10)

print(d1==d2) #False
print(d1<d2) #False
print(d1>d2) #True
print(d1!=d2) #True

