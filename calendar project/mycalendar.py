#p17095/creation of a table like calendar of the selected month

import datetime

year = int(input("enter the year you want:"))
month = int(input("enter the month you want:"))
FirstOfMonth=datetime.date(year , month,1)
print(FirstOfMonth.strftime("%A"))                                                                           #test line
days="S M T W T F S"
print(+month+year)
print(days)
