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
functions = {1: 'key_1_pressed', 2: 'key_2_pressed', 3: 'key_3_pressed'}
functions.get(keycode, None)
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
S = {x^2 : x in {0 ... 9}}
V = (1, 2, 4, 8, ..., 2^12)
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
print p1 + p2 
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
#from __future__ import print_function #this line may not be imported in the middle of the program since it makes a call to the compiler
#map(lambda x:print("*"*x) ,range(1,11))

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
print any([True, True, True, False, True, True]) #Any one of the value in the list should be True
#True
#check all variables are inetgers or not
all([x for x in range(1,11) if isinstance(x,int)])
#True
print "================================================="
#unloading a python module is not supported .GTK
#from __future__ import print_function
import sys
#map(lambda x:print("*"*x) ,range(1,11))

#del sys.modules['__future__']
#print(sys.modules)
for i in range(1,11):
	try:
		print "*" * i #will cause an error,use print () here instead
	except:
		pass
print "================================================="
#Linked list
class Node:
	def __init__(self,content,nxt=None):
		self.content = content
		self.nxt = nxt
	
	def getcontents(self):
		return self.content

	def __str__(self):
		return str(self.content)

def print_list(node):
	while node:
		print node.getcontents()
		node=node.nxt

node1 = Node("car")
node2 = Node("bus")
node3 = Node("lorry")

node1.nxt=node2
node2.nxt=node3
#node3.nxt=node1 #circular linked list
print_list(node1)
print "================================================="
#different ways of writing if condition:
x=5
#bad
if x>0 and x<10:
	print "X is between 0 and 10"
#good way of writing the above is
if 0 < x<10:
	print "X is between 0 and 10"
#also works
if 10>x>0:
	print "X is between 0 and 10"
print "================================================="
#Python simple calculator
calculator = {
'plus': lambda x, y: x + y,
'minus': lambda x, y: x - y
}
print calculator['minus'](9,3)
#6
print "================================================="
#difference between staticmethod and class method

class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)

    @classmethod
    def class_foo(clss_something,x): #clss_somrthing can be any variable name
        print "executing class_foo(%s,%s)"%(clss_something,x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x    

a=A()
#Below is the usual way an object instance calls a method. The object instance, a, is implicitly passed as the first argument.

a.foo(1)
# executing foo(<__main__.A object at 0xb7dbef0c>,1)
#With classmethods, the class of the object instance is implicitly passed as the first argument instead of self.

a.class_foo(1)
# executing class_foo(<class '__main__.A'>,1)
#You can also call class_foo using the class. In fact, if you define something to be a classmethod, it is probably because you intend to call it from the class rather than from a class instance. A.foo(1) would have raised a TypeError, but A.class_foo(1) works just fine:

A.class_foo(1)
# executing class_foo(<class '__main__.A'>,1)
#One use people have found for class methods is to create inheritable alternative constructors.

#With staticmethods, neither self (the object instance) nor  cls (the class) is implicitly passed as the first argument. They behave like plain functions except that you can call them from an instance or the class:

a.static_foo(1)
# executing static_foo(1)

A.static_foo('hi')
# executing static_foo(hi)
#Staticmethods are used to group functions which have some logical connection with a class to the class.

#foo is just a function, but when you call a.foo you don't just get the function, you get a "curried" version of the function with the object instance a bound as the first argument to the function. foo expects 2 arguments, while a.foo only expects 1 argument.

#a is bound to foo. That is what is meant by the term "bound" below:

print(a.foo)
# <bound method A.foo of <__main__.A object at 0xb7d52f0c>>
#With a.class_foo, a is not bound to class_foo, rather the class A is bound to class_foo.

print(a.class_foo)
# <bound method type.class_foo of <class '__main__.A'>>
#Here, with a staticmethod, even though it is a method, a.static_foo just returns a good 'ole function with no arguments bound. static_foo expects 1 argument, and a.static_foo expects 1 argument too.

print(a.static_foo)
# <function static_foo at 0xb7d479cc>
print "=========="
print "================================================="
print "================================================="
print "================================================="
"""
In python Arguments are passed by assignment. The rationale behind this is twofold:

the parameter passed in is actually a reference to an object (but the reference is passed by value)
some data types are mutable, but others aren't
"""


"""
Some notes about java

Multiple inhertince is not directly supported in Java.You need to use interface for this in java.

When a class method has to be implemented in the child class then the parent class is an abstract class

"""


"""
Difference between compiled and interpreted language

Compiled language will raise an error if the last line of the code has an error at the compile time itself. And if there are no errors then only the  
program will be executed.

In intrepreted language if the 5th line of the program has an error then it will first execute the first four lines and when the interpreter sees the error in the 5th line then it raises the error. 


A Compiler and Interpreter both carry out the same purpose – convert a high level language (like C, Java) instructions into the binary form which is understandable by computer hardware. They are the software used to execute the high level programs and codes to perform various tasks. Specific compilers/interpreters are designed for different high level languages. However both compiler and interpreter have the same objective but they differ in the way they accomplish their task i.e. convert high level language into machine language. Through this article we will talk about the basic working of both and distinguish the basic difference between compiler and interpreter.

 
Compiler
A compiler is a piece of code that translates the high level language into machine language. When a user writes a code in a high level language such as Java and wants it to execute, a specific compiler which is designed for Java is used before it will be executed. The compiler scans the entire program first and then translates it into machine code which will be executed by the computer processor and the corresponding tasks will be performed.  


Interpreter
Interpreters are not much different than compilers. They also convert the high level language into machine readable binary equivalents. Each time when an interpreter gets a high level language code to be executed, it converts the code into an intermediate code before converting it into the machine code. Each part of the code is interpreted and then execute separately in a sequence and an error is found in a part of the code it will stop the interpretation of the code without translating the next set of the codes.  


The main differences between compiler and interpreter are listed below:
·         The interpreter takes one statement then translates it and executes it and then takes another statement. While the compiler translates the entire program in one go and then executes it.
·         Compiler generates the error report after the translation of the entire page while an interpreter will stop the translation after it gets the first error.
·         Compiler takes a larger amount of time in analyzing and processing the high level language code comparatively interpreter takes lesser time in the same process.
·         Besides the processing and analyzing time the overall execution time of a code is faster for compiler relative to the interpreter.
"""
