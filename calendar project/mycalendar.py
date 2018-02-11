#p17095/creation of a table like calendar of the selected month

import calendar
c=calendar.TextCalendar(calendar.MONDAY)
year = int(input("enter the year you want:"))
month = int(input("enter the month you want:"))
str=c.formatmonth(year,month)
print(str)
