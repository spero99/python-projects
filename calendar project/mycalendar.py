#p17095/creation of a table like calendar of the selected month
import datetime

year = int(input("enter the year you want:"))
month = int(input("enter the month you want:"))
FirstOfMonth=datetime.date(year , month,1)
start=FirstOfMonth.strftime("%w")
days="S\tM\tT\tW\tT\tF\tS"
#print(+month+year)                                                              #testline
#print(days)                                                                     #testline
#print(start)                                                                    #testline
month_data=((31,"January"),(28,"February"),(31,"March"),(30,"April"),(31,"May"),(30,"June"),(31,"July"),(31,"August"),(30,"September"),( 31,"Ocotber"),(30,"November"),(31,"December"))
daysnum=((1,"Sunday"),(2,"Monday"),(3,"Tuesday"),(4,"Wednesday"),(5,"Thursday"),(6,"Friday"),(7,"Saturday"))


if year%4==0 or (year%100==0 and year%400 !=0):
    month_data[1][0]=29

#print(month_data)                                                               #testline
max_days=month_data[month-1][0]
calendar=[]


for i in range(1,max_days+1):
    calendar.append(i)
    i=i+1

print(calendar)
