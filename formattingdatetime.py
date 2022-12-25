#Formatting Date and Time
#using strftime()
# for more format code visit python official site

from datetime import datetime
dt=datetime.today()

print(dt)
print()

newd1=dt.strftime("%B,%d,%Y")
print(newd1)
print()
newd2=dt.strftime("%d/%b/%Y")
print(newd2)
print()
newd1=dt.strftime("%d-%m-%Y")
print(newd1)
print()
newd1=dt.strftime("%H:%M:%S")
print(newd1)
print()

