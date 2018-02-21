#p17095/creation of a table like calendar of the selected month
import datetime

year = int(input("enter the year you want:"))
month = int(input("enter the month you want(1-12):"))

FirstOfMonth=datetime.date(year , month,1)
start=int(FirstOfMonth.strftime("%w"))
days="S\t M\t T\t W\t T\t F\t S"
month_data=[[31,"January"],[28,"February"],[31,"March"],[30,"April"],[31,"May"],[30,"June"],[31,"July"],[31,"August"],[30,"September"],[ 31,"Ocotber"],[30,"November"],[31,"December"]]
daysnum=((1,"Sunday"),(2,"Monday"),(3,"Tuesday"),(4,"Wednesday"),(5,"Thursday"),(6,"Friday"),(7,"Saturday"))

if year%4==0 or (year%100==0 and year%400 !=0):
    month_data[1][0]=29

print(month_data[1][0])
max_days=month_data[month-1][0]
print(max_days)
calendar=[]
month_name=month_data[month-1][1]
count=0

for j in range(start):
    calendar.append(" ")
    calendar.append('\t')
    count=count+1
print("count:"+str(count))
for i in range(1,max_days+1):
    calendar.append(str(i))
    calendar.append('\t')
    i=i+1

week1=calendar[0:14]
week2=calendar[14:28]
week3=calendar[28:42]
week4=calendar[42:56]
week5=calendar[56:70]


print(month_name+" "+str(year))
print(days)
print(" ".join(week1))
print(" ".join(week2))
print(" ".join(week3))
print(" ".join(week4))
print(" ".join(week5))
