
# date object = contains information about year,month,day
#creating date object

# object_name=date(year,month,day)

# today()=> today() of date class returns only date
# dt=date.today()

from datetime import date

d1=date(year=2019,month=11,day=23)
print(d1.year)
print(d1.month)
print(d1.day)

# today()=>returns only date(year)
# ---------

cd= date.today()
print(cd)
print(cd.year)