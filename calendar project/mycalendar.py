#p17095/creation of a table like calendar of the selected month


import datetime

year = int(input("enter the year you want:"))
month = int(input("enter the month you want:"))
FirstOfMonth=datetime.date(year , month,1)
print(FirstOfMonth.strftime("%A"))                                                                           #test line
days="S M T W T F S"
print(+month+year)
print(days)

month_data=[(1,31,"January"),(2,28,"February"),(3,31,"March"),(4,30,"April"),(5,31,"May"),(6,30,"June"),(7,31,"July"),(8,31,"August"),(9,30,"September"),(10, 31,"Ocotber"),(11,30,"November"),(12,31,"December")]
daysnum=((1,Sunday),(2,Monday),(3,Tuesday),(4,Wednesday),(5,Thursday),(6,Friday),(7,Saturday))
print(month_data)

if year%4==0 or (year%100==0 and year%400 !=0)
    month_data[1][1]=29

print(month_data)
