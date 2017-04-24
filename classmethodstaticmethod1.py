#https://www.youtube.com/watch?v=rq8cL2XMM5M&t=632s

class Employee:
	amount = 0
	def __init__(self,name):
		print self.amount
		self.name = name
		print self.name

	@classmethod
	def set_amount(cls,amt): #Note here we do not have to pass class or object,as class is passed Explicitly
		cls.amount=amt

	@classmethod
	def s_amount(cls,amt): #Note here we do not have to pass class or object,as class is passed Explicitly
		cls.amount=amt
		return cls("Pluto") #This is another way of creating class object ,very important

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6: #checking if the day is saturday or sunday
			return False
		return True

e = Employee("Tom")
print e.amount
Employee.set_amount(1) #Note here we do not have to pass class or object,as class is passed Explicitly
print e.amount
e.set_amount(2) #Note here we do not have to pass class or object,as class is passed Explicitly
print e.amount
e1=Employee.s_amount(3)
print e1.amount
#static methods are mostly used when there is no connection either with class ,class objects aor instance objects,the function is somehow related to class but does have to do anything with the class but is a logical and reasonable behavior related to a class
import datetime

my_date = datetime.date(2017,4,25)
print Employee.is_workday(my_date)
print e.is_workday(my_date) #Static methods can also be called with instances but it makes no logical sense when reading the code

#In python monday= 0 and tuesday=1,...sunday=6



