import datetime
import pytz

d=datetime.date(2017,4,25)
print d #prints 2017-04-25
#to get todays date
dt= datetime.date.today()
print dt
#to get current year
print dt.year
#to get the date only
print dt.day
#to get the week day in int
print dt.weekday() #Monday is 0 and sunday is 6
print dt.isoweekday() #Monday is 1 and sunday is 7

tdelta = datetime.timedelta(days=7)
print dt + tdelta  #what will be the date after 7 days,change the above days variable to get more date changes

print dt - tdelta  #what will be the date before 7 days,change the above days variable to get more date changes
#logic is 
#1. get date as result when add date and time delta
# date =date+timedelta
# timedelta =date+date
#ex: how many days till August 20 new year
a_dt =datetime.date(2017,8,20)
print  a_dt-dt #Result is datetime and output is 117 days, 0:00:0

print "======================DATETIME TIME================"
t=datetime.time(9,30,45,100000)
print t
print t.hour
#To get both date and time use datetime.datetime
dt=datetime.datetime(2016,4,25,9,30,45,100000)
print dt
print dt.date()
print dt.time()
print dt.year
tdelta = datetime.timedelta(days=7)
print dt+tdelta	
tdelta = datetime.timedelta(hours=12)
print dt+tdelta #adding hours to current dt 	
print "======================OTHER DATETIME OBJECTS================"
dt_today = datetime.datetime.today() #local timezon
dt_now = datetime.datetime.now() #here we can pass an option for timezone,if timezone is ignored local timezone will be taken as input by default
dt_utcnow = datetime.datetime.utcnow()#gives utc time

print dt_today
print "\n"
print dt_now
print "\n"
print dt_utcnow


dt=datetime.datetime(2016,4,25,9,30,45,tzinfo=pytz.UTC)
print dt #2016-04-25 09:30:45+00:00 #output is appended by +00:00
dt_now = datetime.datetime.now(tz=pytz.UTC)
print dt_now
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print dt_utcnow

dt_mtn=dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print  dt_mtn


for tz in pytz.all_timezones:
	#print tz #uncomment tis to see all timezones
	pass

#========CONVERTING DATIME FORMAT=================
dt=datetime.datetime(2016,4,25,9,30,45)
print dt
#format the above datetime using stringformatime = strftime
print (dt.strftime('%B %d, %Y'))
#convert string to datime object using strptime
dt_str = 'July 26, 2016'
#For the above now tell the datetime format to timezone library,i.e, which format this is in
dt=datetime.datetime.strptime(dt_str,'%B %d, %Y')
print dt

#strftime =>converts datetime to string
#strptime =>converts string to datetime
