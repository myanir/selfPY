#print the day of the weekend
import calendar
print ("enter date format dd/yy/yyyy:")
date = str(input())
year = int(date[-4:])
month = int(date[-7:-5])
day = int(date[0:2])
#print("year",year)
#print ("month",month)
#print (date)
#print ("day",day)
x=calendar.weekday(year, month, day)
print ("calendar day",calendar.day_name[x])