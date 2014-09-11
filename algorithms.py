#!/usr/bin/python
import logging

#Anagrams
word = sorted('rac')
alternatives = ['car', 'girl', 'tofu', 'rca']

for alt in alternatives:
	if word == sorted(alt):
		print alt

#Bubble sort
a=[1,2,3,333,6,5,4,7,77,5566,94,2,34]
print a
for ii in range(len(a) -1):
   for j in range(len(a)-ii-1):
      if a[j]> a[j+1]:
         a[j],a[j+1]=a[j+1],a[j]

#swapping
a=1;b=2
a,b=b,a
print a,b

#fizzbuzz
for i in range(1,101):
   a=""
   if( (i%3 == 0) and (i%5 == 0)):
     print i,"FizzBuzz"
     a=i
   else:
      if( i % 3 == 0 ):
        print i,"Fizz"
        a=i
      if( i % 5 == 0):
        print i,"Buzz"
        a=i
   if(a == ""):
      print i,i
print "==============================================================="
#Default Argument Values are Only Evaluated Once
"""
The default value for a function argument is only evaluated once, when the function is defined. Python simply assigns this value to the correct variable name when the function is called.

Python doesn't check if that value (that location in memory) was changed. It just continues to assign that value to any caller that needs it. So, if the value is changed, the change will persist across function calls. Above, when we appended a value to the list represented by stuff, we actually changed the default value for all eternity. When we called function again looking for a default value, the modified default was given to us
"""
def func(a=[]):
	a.append(1)
	print a

func()
func()


#The solution: don't use mutable objects as function defaults. You might be able to get away with it if you don't modify them, but it's still not a good idea.

#A better way to write the above code would be:

#'s
def function(item, stuff = None):
    if stuff is None:
        stuff = []
    stuff.append(item)
    print stuff

function(1)
# prints '[1]'

function(2)
# prints '[2]', as expected
#None is immutable (and we're not trying to change it anyways), so we're safe from accidently changing value of the default.

#On the plus side, a clever programmer could probably turn this into a trick, in effect creating C-style 'static variables'.
print "==============================================================="
#'Switch Statements' using Dictionaries of Functions
keycode = 2
functions = {1: key_1_pressed, 2: key_2_pressed, 3: key_3_pressed}
functions.get(keycode, unknown_key_pressed)()
print "==============================================================="
#Passing 'self' Manually
class Class:
    def a_method(self):
        print 'Hey a method'

instance = Class()

instance.a_method()
# prints 'Hey a method', somewhat unsuprisingly.  You can also do:

Class.a_method(instance)
# prints 'Hey a method'

print "==============================================================="

#Modifying classes after creation

class Class:
   def method(self):
        print 'Hey a method'

instance = Class()
instance.method()
# prints 'Hey a method'

def new_method(self):
    print 'New method wins!'

Class.method = new_method
instance.method()
# prints 'New method wins!'
print "==============================================================="


#Lambda function
#Lambda Expressions (Anonymous Functions)

#As if the last section wasn't cool enough, let's try "lambda expressions", a concept borrowed from Lisp and other functional languages. Lambda expressions return functions as results. They build functions without assigning names to them. A normal function declaration assigns the functions value to the name of the function, but lambda expressions do not.

#Why would you want this dubious functionality? Because lambda expressions are nice to use in places that a function declaration wouldn't normally be allowed, and to write quick and dirty functions on the fly. Sometimes you want to build functions(callback handlers in gui's, object member data accessors, and so on), and using lambda expressions makes that a lot easier.

#So lambda lets you define and use a function inside an if statement body, or inside a list. However, lambda expressions are just that, expressions. It is difficult to write a complicated function because statements are not allowed.

#Python supports a concept called "list comprehensions". It can be used to construct lists in a very natural, easy way, like a mathematician is used to do.
"""
S = {x² : x in {0 ... 9}}
V = (1, 2, 4, 8, ..., 2¹²)
M = {x | x in S and x even}
"""
#>>> S = [x**2 for x in range(10)]
#>>> V = [2**i for i in range(13)]
#>>> M = [x for x in S if x % 2 == 0]
#>>> 
#>>> print S; print V; print M
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
#[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
#[0, 4, 16, 36, 64]

#converting list to integer
T2 = ['13', '17', '18', '21', '32']
T3 = [map(int, x) for x in T2]

#palindrome
def ispalindrome(word):
    return word == word[::-1]

#http://www.careercup.com/page?pid=algorithm-interview-questions
#http://blog.agafonov.net.ua/post/2010/12/31/Top-15-Tricky-Algorithm-Interview-Questions.aspx

#Data structures in python are
#list
#stack
#queue

x = 2; y = 3; print x * y # 6
# but ...
x = 'A'; y = 3; print x * y # AAA


def fib():
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b

f=fib()
for i in range(5):
	f.next()
##########OR###########################
# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while b < 200:
	print b,
	a, b = b, a+b
##########OR###########################
# Defining Functions
def fib(n):    # write Fibonacci series up to n
	"""Print a Fibonacci series up to n."""
	a, b = 0, 1
	while b < n:
		print b,
		a, b = b, a+b
 
# Now call the function we just defined:
fib(2000)

''.join([`i` for i in range(101)])
#'0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100'


def f():
    yield

def g():
    return

print 'f()=', f() #f()= <generator object f at 0x7f705eb3c820>
print 'g()=', g() #g()= None

#Python opertor overloading
#Why is it required
class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

#Now when we try to add two points that we create as follows.


p1 = Point(2,3)
p2 = Point(-1,2)
try:
	p1 + p2
except:
	import logging 
	logging.debug("eeeeeeeeee")
#Traceback (most recent call last):
#...
#TypeError: unsupported operand type(s) for +: 'Point' and 'Point'

######Whoa! That's a lot of complains. TypeError was raised since Python didn't know how to add two Point objects together. However, the good news is that we can teach this to Python through operator overloading. But first, let's get a notion about special functions.


class Point:
    # previous definitions...
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)

#Now let's try that addition again.


p1 = Point(2,3)
p2 = Point(-1,2)
print type(p1),type(p2)
print(p1 + p2)
#(1,5)
#similarly operator overloading an be done for substraction,mulitplication,devision etc
#http://www.programiz.com/python-programming/operator-overloading


#print "*" with recursion

i=0

def t():
    global i
    i += 1
    if i < 11:
        print "*" * i
        t()

t()
## Another way of doing the same is

for i in range(1,11):
	print "*" * i

## Another way of doing the same is
#lambda functions only accespts expression and not statement
#y=a+b is an expression
#print "*"* i is a statement
from __future__ import print_function
map(lambda x:print("*"*x) ,range(1,11))

print "================================================="
## using super and its advantages

class Base(object):
    def __init__(self):
        print "Base created"

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()

print ChildA(),ChildB()

#super() lets you avoid referring to the base class explicitly, which can be nice. But the main advantage comes with multiple inheritance, where all sorts of fun stuff can happen. See the standard docs on super if you haven't already.

#Note that the syntax changed in Python 3.0: you can just say super().__init__() instead of super(ChildB, self).__init__() which IMO is quite a bit nicer.

print "================================================="

#all and any, in a nutshell, allow you to do the equivalent of and and or respectively but on an entire list.* So, in the most basic case, here's how they work:

print all([True, True, True, False, True, True])  #All values in the list should be True
#False
print any([True, True, True, False, True, True]) #Any one of the value in the list should be Trur
#True
#check all variables are inetgers or not
all([x for x in range(1,11) if isinstance(x,int)])
#True
print "================================================="
#unloading a python module is not supported .GTK
from __future__ import print_function
import sys
map(lambda x:print("*"*x) ,range(1,11))

del sys.modules['__future__']
print(sys.modules)
for i in range(1,11):
	try:
		print "*" * i #will cause an error,use print () here instead
	except:
		pass
print "================================================="
"""
In python Arguments are passed by assignment. The rationale behind this is twofold:

the parameter passed in is actually a reference to an object (but the reference is passed by value)
some data types are mutable, but others aren't
"""
