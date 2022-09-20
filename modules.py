# phyton modules 
import datetime
from datetime import timedelta, date

# my module
import fmath
from fmath import add, substract

print(datetime.date.today())
print(date.today())
print(datetime.timedelta(minutes=70))

fmath.add(1, 2)
add(1, 2)
fmath.substract(1, 2)
substract(1, 2)