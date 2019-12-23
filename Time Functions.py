
#date lib functions

print("Demoing date library functions")
print()

from datetime import date
from datetime import time
from datetime import datetime

today = date.today()
print("Today's date is: ", today)
print("Today's Date is: ", today.day, "Month is: ", today.month, "and year is: ", today.year)

timeNow = datetime.time(datetime.now())
print("Current time is: ", timeNow)

print(today.strftime("Current year is: %Y"))
