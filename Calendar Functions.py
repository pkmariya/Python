
# Calendar Functions

print("Calendar functions in Python")
print()

import calendar

print("Plain Text Calendar")
c = calendar.TextCalendar(calendar.SUNDAY)
st = c.formatmonth(2019, 12, 0, 0)
print(st)

print("HTML Calendar")
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2019, 12)
print(st)

print("Month Names: ")
for name in calendar.month_name:
    print(name)

print()

print("Day Names: ")
for day in calendar.day_name:
    print(day)

print("1st Mondays in the year 2020")
print("Team meetings will be on: ")
for m in range(1, 13):
    cal = calendar.monthcalendar(2020, m)
    weekone  = cal[0]
    weektwo = cal[1]

    if weekone[calendar.MONDAY] != 0:
        meetday = weekone[calendar.MONDAY]
    else:
        meetday = weektwo[calendar.MONDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))

