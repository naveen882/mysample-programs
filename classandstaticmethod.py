"""
Suppose we have a class called Math then nobody will want to create object of class Math and then invoke methods like ceil and floor and fabs on it.( >> Math.floor(3.14))

So we make them static.

One would use @classmethod when he/she would want to change the behaviour of the method based on which subclass is calling the method. remember we have a reference to the calling class in a class method.

While using static you would want the behaviour to remain unchanged across subclasses
http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner/31503491#31503491
Example:

"""
class Hero:

  @staticmethod
  def say_hello():
     print("Helllo...")

  @classmethod
  def say_class_hello(cls):
     if(cls.__name__=="HeroSon"):
        print("Hi Kido")
     elif(cls.__name__=="HeroDaughter"):
        print("Hi Princess")

class HeroSon(Hero):
  def say_son_hello(self):
     print("test  hello")



class HeroDaughter(Hero):
  def say_daughter_hello(self):
     print("test  hello daughter")


testson = HeroSon()

testson.say_class_hello()

testson.say_hello()

testdaughter = HeroDaughter()

testdaughter.say_class_hello()

testdaughter.say_hello()

print "============================================================================"
"""
static methods are best used when you want to call the class functions without creating the class object

"""
class  A(object):
    @staticmethod
    def r1():
            print "In r1"

print A.r1()
#In r1
a=A()
a.r1()
#In r1
class  A(object):
    def r1(self):
            print "In r1"

"""
print A.r1()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unbound method r1() must be called with A instance as first argument (got nothing instead)
"""

print "============================================================================"
class dynamo():

	@staticmethod
	def all_return_same():
		print "static method"

	@classmethod
	def all_return_different(cls):
		print cls
		if cls.__name__ == 'A':
			print "1"
		elif cls.__name__ == 'B':
			print "2"
		else:
			print "3"

class A(dynamo):
	pass
	
class B(dynamo):
	pass


d=dynamo()
d.all_return_same()
d.all_return_different()
dynamo().all_return_same()
dynamo().all_return_different()
print  "======"
a=A()
a.all_return_same()
a.all_return_different()
A.all_return_same()
A.all_return_different()
print  "======"
b=B()
b.all_return_same()
b.all_return_different()
B.all_return_same()
B.all_return_different()
print "============================================================================"
