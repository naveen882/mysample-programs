import datetime as dt
import calendar

month_quarter = [3,6,9,12]
user_date = dt.datetime.strptime('2017-12-31', "%Y-%m-%d").date()
if user_date.month in month_quarter:
    last_day = calendar.monthrange(user_date.year,user_date.month)[1]
    actual_date =  dt.date(user_date.year,user_date.month, last_day)
    if user_date == actual_date:
        print "Matching"
    else:
        print "Select last day of the Quarter"
else:
    print "Select last day of the Quarter"

