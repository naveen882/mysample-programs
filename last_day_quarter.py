import datetime as dt
import calendar

month_quarter = [3,6,9,12]
d= dt.datetime.strptime('2017-12-11', "%Y-%m-%d").date()
if d.month in month_quarter:
    last_day = calendar.monthrange(d.year,d.month)[1]
    actual_date =  str(d.year)+"-"+str(d.month) +"-"+str(last_day)
    d1= dt.datetime.strptime(actual_date, "%Y-%m-%d").date()
    if d == d1:
        print "Matching"
    else:
        print "Select last day of the Quarter"
else:
    print "Select last day of the Quarter"
