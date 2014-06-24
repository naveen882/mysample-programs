import string
import logging
import datetime

class Dynamo():
	def __init__(self,x):
		print "In Init def"
		self.x = x

	def __str__(self):
		print "In str function"
		return str(self.x)+ "======"

	def __repr__(self):
		print "In repr function"
		return self.x+ "===="

	def __getattr__(self,k):
		if k == "color":
			print "key is color"
		else:
			print "key is something else %s"%(k)

d=Dynamo(1)
d.color
d.color1
print "%s"%(d.x)
print str(d) ##//Thsi will print str function

print "==================================="


class Rastan(object):
	def __init__(self,x):
		print "In init def"
		self.x=x

	def __str__(self):
		print "In str func"
		return self.x + "====="

	def __repr__(self):
		print "In repr func"
		return self.x + "====="

	def __getattribute__(self,k):
		print "In get attribute"
		if k == "color":
			print "key is color"
		else:
			print "key is comething else %s  and %s"%(k,"============")

d=Rastan(1)
d.color
d.color1	
print "%s"%(d.x)

print "=========================================="

f=open("/tmp/aa.txt","w")
f.write("Testing  and \n Testing again \n and \n again")
f.close()

f=open("/tmp/aa.txt")
while True:
	for l in f.read(): #reads character by character
		print l,
	else:
		break
f.close()


f=open("/tmp/aa.txt")
while True:
	for l in f.readline(): #reads a sing line
		print l,
	else:
		break
f.close()


f=open("/tmp/aa.txt") # read entire file once and splits it line by line
while True:
	for l in f.readlines():
		print l,
	else:
		break
f.close()

print "====================="
f=open("/tmp/ab.txt","r+") # read  and write mode  and to use this file should be existing already
f.write("This is some text 123456789")
print f.seek(10) #read after tenth character
print f.read() #read after tenth character and print every thing
f.seek(10) #read after tenth character
print f.read(1) #read after tenth character and print one character only 
f.close()

print "======================================="

a=(1,2,3,4)
print a[0]
print a[1]
print a[2]
print a[3]

print "======================================="
b=((1,2,3,4),(1,2))
print b[0][0]
print b[0][1]
print b[0][2]
print b[0][3]
print b[1][0]
print b[1][1]

print "======================================="
for i in range(len(b)):
	for s in range(len(b[i])):
		print b[i][s]

print "======================================="
c={'a':1,'b':2}
print c['a']
print c['b']
print c.keys()
print c.values()
print c.pop('b',None) #returns 2
print c.get("b",c.update({'b':6}))
print c #prints {'a': 1, 'b': 6}
try :
	if c['a']:
		print c['a']
except:
	logging.debug("debug")
	logging.error("error")
	logging.exception("exception")

try :
	if c['c']:
		print c['c']
except:
	logging.debug("debug")
	logging.error("error")
	logging.exception("exception")
print "======================================="
def func(a,b=None):
	if b is None:
		print "b is None"
		print b is None ## this will print true
	else:
		print a,b

func(1)
func(1,2)
print "======================================="
def func1(a,*b): #* stands for a tuple
	print a
	if len(b) > 0 :
		print b
		for i in b:
			print i

func1(1,2,3,4,5,6)
func1(1)
print "======================================="
def func2(l,**c):
	print l
	if len(c) > 0:
		for i in c:
			print c[i]

c={'a':1,'b':2,'c':3}
func2(1,**c)
print "======================================="
aa=(1,2,3,(4,5),6)
print aa[0]
print aa[1]
print aa[2]
print aa[3][0]
print aa[3][1]
print aa[4]
print "======================================="
i=5
def fs(args=i):
	print args
	print i

i=6
fs()
fs(7)
print "======================================="
cc=[1,2,3,4]
dd=['1','2','3','4']
print "%s"%"====".join(dd) ##### To remember
print "====".join(dd) #This is similar to the above statement
for i in range(len(dd)):
	print i,dd[i]
a=11
b=22
c="ee"

print a,b,c
a,b,c=c,a,b
print a,b,c
print "======================================="
add2 = lambda a,b:a+b;print "=====";print "|||||||";print "iiiiiiiii"   ##To remember
print add2(3,4)
def tr(add2):
	print add2(5,6)
print "======================================="
ee=[1,2]
ff=[3,4]
gg=zip(ee,ff)
print gg
gg = dict(gg)
print gg
gg.update({'1':4})
print gg[1]
print gg['1']     
print gg
print "======================================="
a=[1,2]
try:
	gg={a:2}
	print gg
except:
	print logging.exception("e") #This prints unhashable type: 'list'
print "======================================="
di=dict(a=1,b=2)
print di
print dir(di)
print di.items()
print di.has_key('a')
print di.keys()
print di.values()
it =di.iterkeys()
print it.next()
print it.next()
it =di.itervalues()
print it.next()
print it.next()
print "======================================="
strings=['a','b','c','d','e']
for i,k in enumerate(strings):
	print i,k
print "======================================="
class test22:
	def hello(self,**args):
		print args['a']

jj={'a': '1'}
t = test22()	
t.hello(**jj)
t.hello(**({'a':'b'}))
		
print "======================================="
a=[6,6,1,1,2,3,3,3,4,5]
print list(set(a))
print type(list(set(a)))
print "======================================="
a=[6,6,1,1,2,3,3,3,4,5]
print sorted(a)
print sorted(set(a),reverse=True)
print "======================================="
def fun(*a,**kw):
	print a,kw

a= [1,2,3,'a']
b=dict(a=1,b=2,c=3)
fun(*a)
fun(**b)
fun(*a,**b)
print "======================================="
opt = ["opt3", "opt2", "opt7", "opt6", "opt1", "opt10", "opt11"]
print sorted(opt)
print (opt.sort()) #This will sort the original list
print opt
print "======================================="

list_of_tuples = [('key', 'value'), ('key2', 'value2')]
a_dict_2 = dict(list_of_tuples)
print a_dict_2
a_dict_3 = a_dict_2
bb=1
aa=dict(a_dict_2 = a_dict_2)
print aa
for val ,key in enumerate(aa):
		for i in aa[key]:
			print "========"
			print aa[key]
			print aa[key][i]
print a_dict_2 ==a_dict_3	
print a_dict_2.clear()
print str(a_dict_2) + "====="
print "======================================="
class mytest:
	p = 1
	def __init__(self,a):
		self.a = a
		print str(self.p) + "======"		
	def hello(self):
		print "in mytest hello"

class myt(mytest):
	def __init__(self,b,obj):
		obj.p=2
		obj.__init__(4)
		print obj.p

	def hello(self):
		print "in myt hello"

mt = mytest(2)
m=myt(3,mt)
mt.hello()
m.hello()
print "======================================="
mystr1="hello world"
print mystr1[::-2]
print "======================================="
for x in range(1,11):
	print x
print "======================================="
str1="golf"
def reverse(str1):
	a=list(str1)
	for i in str1[::-1]:
		yield i

for i in reverse(str1):
		print i
print "======================================="
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print a
del a[2:4]
print a
del a[:]
del a[::]
print a
print "======================================="
knights={'a':1,'b':2}
for i,k in knights.iteritems():
	print type(i)
	print type(k)
	print i,k
for k in knights.iterkeys():
	print type(k)
	print k
for k in knights.itervalues():
	print type(k)
	print k
print "======================================="
def linear(a,b):
	def result(x):
		return a*x+b
	return result(1)

aa=linear(3,4)
print aa	
print "======================================="
if __name__ == "__main__":
	print __name__
import logging
print logging.__name__
print "======================================="
a = [66.25, 333, 333, 1, 1234.5]
print a.count(333)
print a.count(66.25)
print a.count('x')
print a.insert(2,-11)
print a.append(333)
print a.index(333)
print a
print a.reverse()
print a
print a.sort()
print a
print a.sort()

print "======================================="
class Deco(object):
	def __init__(self):
		print "In Deco class init"
	def __call__(self,f):
		print "before"
		print dir(f)
		print f.__name__
		f()
		print "after"

@Deco()
def tt():
	print "in tt"

def Deco1():
	def all(F):
		print "before in func"
		print dir(F)
		F.__name__
		F()
		print "after in func"
	return all

@Deco1()
def gg():
	print "in gg"
print "======================================="
def shout(aa="yes"):
	print aa

scream=shout
scream()
scream(1)

print "======================================="
def makebold(fn):
    print "2"
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    print "1"
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

print hello()
print "======================================="
a=[1,2,3,333,6,'ab',5,4,7,'a',77,5566,94,2,34]
print a
for ii in range(len(a)-1):
	for jj in range(len(a)-ii-1):
		if a[jj] > a[jj+ 1]:
			a[jj],a[jj+1]=a[jj+1],a[jj]

print a
print "======================================="
word="acr"
word=sorted(word)
alternatives = ['car', 'girl', 'tofu', 'rca']	
for i in alternatives:
	if sorted(i) == word:
		print i
print "======================================="
a=['1','2','3']
a=map(int,a)
print a
b=['1','2','3']
print "======================================="
def rt(a=[]):
	a.append(1)
	print a

rt()
rt()
rt()
rt()
print "======================================="
def rs(a,b,c):
	print a,b,c

aa=[1,2,3]
rs(*aa)
print "======================================="
st='str'  'ing'             #  <-  This is ok
print st ##This prints string
print "======================================="
T2=[(i,j) for i in range(3) for j in range(i) ]
print T2

arr=["harry","sally","tom"]
for i in range(len(arr)):
	print arr[i %len(arr)] * 3 
	print arr[(i+2) % len(arr)] * 2
	print arr[(i+1) % len(arr)] * 1

mydict = {'carl':40, 'alan':2, 'bob':1, 'danny':3}

print dict(sorted(mydict.items(),key = lambda x:x[1]))  ## to remember
my_dict = {'carl':40, 'alan':2, 'bob':1, 'danny':3}
my_dict=dict(zip(my_dict.values(),my_dict.keys()))
print my_dict
my_dict = {'carl':40, 'alan':2, 'bob':1, 'danny':3}
my_dict = dict([(v,k) for k,v in my_dict.items()])
print my_dict

print "======================================="
def binary_search(a, x, lo=0, hi=None):
	if hi is None:
		hi = len(a)
	while lo < hi:
		print "lo %d"%(lo)
		print "hi %d"%(hi)
		mid = (lo+hi)//2
		print "mid %d"%(mid)
		midval = a[mid]
		print "midval %d"%(midval)
		if midval < x:
			lo = mid+1
			print "lo %d"%(lo)
		elif midval > x: 
			hi = mid
			print "hi %d"%(hi)
		else:
			return mid
	return -1
a=[1,2,3,4,5,6,7,8,9]
mid = binary_search(a,7) 
print mid
print "======================================="
def binary_saearch(a,x,lo=0,hi=None):
	if hi is None:
		hi = len(a)
	while (lo < hi):
		mid=(lo+hi)/2
		midval = a[mid]
		if midval < x:
			lo = mid+1
		elif midval > x:
			hi=mid
		else:
			return mid
	return -1

val = binary_search(a,8)
print "====="
print val
print "======================================="
#A dict cannot have list or dict as keys but it can have tuple since tuple cannot be chnages and is a read only datastructure
a=(1,2)
b={a:2}
print b
#{(1, 2): 2}
print b[(1,2)] # will give 2
print "======================================="
T2=[(i,j) for i in range(3) for j in range(i) ]

print "======================================="
class a:
	def __init__(self):
		self.l=None
		print self.l
		if self.l  :  #since self.l is None the print steatement is not printed
			print "exist" 
 

print "======================================="
def fib():
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b

a = fib()	
print a.next()
print next(a)
print next(a)
print next(a)
print next(a)
print next(a)
print "=========="
def fibn(n):
	a,b=0,1
	while b<n:
		yield a
		a,b=b,a+b
i = fibn(20)	
print next(i)
print next(i)
print next(i)
print next(i)
print next(i)
print next(i)
print next(i)
print "======================================="
def palindrome(word):
	return word == word[::-1]

print palindrome("tat")
print palindrome("t")
print palindrome("ti")
print "======================================="
def binary_search(a,x,lo=0,hi=None):
	if hi is None:
		hi=len(a)
	while lo < hi:
		mid=(lo+hi)/2
		midval = a[mid]
		if midval < x:
			lo = mid + 1
		elif midval > x:
			hi = mid
		else:
			return midval,mid
	return -1

a=[1,1,1,1,2,3,4,5,56,76]
answer,pos =binary_search(a,5)
print answer,pos
print "======================================="
class seq:
	x= 0 
	def __iter__(self):
		return self
	def next(self):
		self.x += 1
		if self.x >= 3:
			raise StopIteration
		return self.x * self.x

s=seq()
type(s)
print s.next()
print s.next()
#print s.next() ## this will call StopIteration
print "======================================="
#Python polymorphism example
class Animal:
	def __init__(self, name):    # Constructor of the class
		self.name = name
	def talk(self):              # Abstract method, defined by convention only
		raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
	def talk(self):
		return 'Meow!'

class Dog(Animal):
	def talk(self):
		return 'Woof! Woof!'

animals = [Cat('Missy'),
           Cat('Mr. Mistoffelees'),
           Dog('Lassie')]

for animal in animals:
	print animal.name + ': ' + animal.talk()

print "======================================="
class a:
	pass

x=a()
x.a =1
x.__dict__
print "======================================="
# class can also be created with metaclasses read about this..
print "======================================="
art = ["a","b","c","d","e"]
a = datetime.datetime.now()
for i in reversed(art):
	print i
b = datetime.datetime.now()
c=b-a
print c.seconds,"1st"
print c.microseconds,"1st"
a = datetime.datetime.now()
for i in art[::-1]:
	print i
b = datetime.datetime.now()
c=b-a
print c.seconds,"2nd"
print c.microseconds,"2nd"

print "======================================="
colors = ["red","yellow","blue","green"] 
for i in sorted(colors):
	print i
for i in sorted(colors,reverse=True): #This sorts the list in reverse alphabetical order
	print i
for i in reversed(colors): ##This sorts the list in reverse order
	print i



a={'b':1}
del a['b']
print a ##If u delete a value by its key it will delete the key also

def rt(ty):
	print ty

rt(ty=1) #you can call the function withc exact same function definition attributes.This is just for readability purpose.Chaning the parameter will result in an error

a,b,c,d=colors #unpacking an array into different variable
print a,b,c,d
print "======================================="
try:
    a={'b':1}
    for i in a:
        del a[i] #RuntimeError: dictionary changed size during iteration
except:
    logging.exception("Error while iterating dictionary")
print "======================================="
#overloading is not supported in python
def at(r):
  print r
  print "Inm 1"

def at(r,t):
  print "Inm 2"
  print r,t

try:
	at(1)
except:
	logging.exception(e)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: a() takes exactly 2 arguments (1 given)
print "======================================="
#oneliner to read a file
print open("ten_one_liners.py").readlines()

print "======================================="
#Difference between is and "=="
#is will return True if two variables point to the same object, == if the objects referred to by the variables are equal.
print "======================================="
#using eval

#The eval function lets a python program run python code within itself.

#eval example (interactive shell):
x = 1
eval('x + 1')
#2
eval('x')
#1
print "======================================="
"""
The str() function is meant to return representations of values which are fairly human-readable
repr() is meant to generate representations which can be read by the interpreter (or will force a SyntaxError if there is no equivalent syntax).


Old style classes and new style classes

Up to Python 2.1, old-style classes were the only flavour available to the user. The concept of (old-style) class is unrelated to the concept of type: if x is an instance of an old-style class, then x.__class__ designates the class of x, but type(x) is always <type 'instance'>. This reflects the fact that all old-style instances, independently of their class, are implemented with a single built-in type, called instance.

New-style classes were introduced in Python 2.2 to unify classes and types. A new-style class neither more nor less than a user-defined type. If x is an instance of a new-style class, then type(x) is the same as x.__class__. 
 
Reading files:
==============
Using simple  loop is the best way to go about it as it still avoid a function call
In some versions of python readline() really does just read a single line while the for loop reads large chunks and splits them up into lines so it may be faster. I think that more recent versions of Python use buffering also for readline() so the performance difference will be miniscule (for is probably still microscopically faster because it avoids a method call). However choosing one over the other for performance reasons is probably premature optimisation.

Edit to add: I just checked back through some Python release notes. Python 2.5 said:

It's now illegal to mix iterating over a file with for line in file and calling the file object's read()/readline()/readlines() methods.
* read(size) >> size is an optional numeric argument and this func returns a quantity of data equal to size. If size if omitted, then it reads the entire file and returns it

* readline() >> reads a single line from file with newline at the end

* readlines() >> returns a list containing all the lines in the file

* xreadlines() >> Returns a generator to loop over every single line in the file
r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it's omitted.

Python Pickling:
================

Rather than have users be constantly writing and debugging code to save complicated data types, Python provides a standard module called pickle. This is an amazing module that can take almost any Python object (even some forms of Python code!), and convert it to a string representation; this process is called pickling. Reconstructing the object from the string representation is called unpickling. Between pickling and unpickling, the string representing the object may have been stored in a file or data, or sent over a network connection to some distant machine.

If you have an object x, and a file object f that's been opened for writing, the simplest way to pickle the object takes only one line of code:

pickle.dump(x, f)

To unpickle the object again, if f is a file object which has been opened for reading:

x = pickle.load(f)

Decorators:
===========
A decorator is just a callable that takes a function as an argument and returns a replacement function. We'll start simply and work our way up to useful decorators.

Python 2.4 provided support to wrap a function in a decorator by pre-pending the function definition with a decorator name and the @ symbol. In the code samples above we decorated our function by replacing the variable containing the function with a wrapped version.

What is logn:
=============
Logarithmic running time (O(log n)) essentially means that the running time grows in proportion to the logarithm of the input size - as an example, if 10 items takes at most some amount of time x, and 100 items takes at most, say, 2x, and 10,000 items takes at most 4x, then it's looking like an O(log n) time complexity.

Explain how pyhton program is interpreted:
==========================================
Python program runs directly from the source code. Each type Python programs are executed code is required. Python converts source code written by the programmer into intermediate language which is again translated it into the native language / machine language that is executed. So Python is an Interpreted language.         
.pyc files are byte compiled versions of the original .py file. When a .py file is executed by python, it first checks to see if there is a .pyc file with the same name and that the original .py file hasn't been modified since the .pyc file was created. It both of these are true then it executes the .pyc file because it can save the step of byte compiling the .py file thus making the execution time faster. So the .pyc file really is executable just like you discovered.
The `*.pyc` files are usually only created when you import a module, not
when a module is run directly.

Generators:
==========
A generator function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function (even if it also contains a return statement). There's nothing else we need to do to create one. 
So whenever next() is called on a generator, the generator is responsible for passing back a value to whomever called next(). It does so by calling yield along with the value to be passed back (e.g. yield 7). The easiest way to remember what yield does is to think of it as return 
When a generator function calls yield, the "state" of the generator function is frozen; the values of all variables are saved and the next line of code to be executed is recorded until next() is called again. Once it is, the generator function simply resumes where it left off. If next() is never called again, the state recorded during the yield call is (eventually) discarded. 

-
 In general, a generator is a special routine that can be used to control the iteration behaviour of a loop. A generator is similar to a function returning an array. A generator has parameters, it can be called and it generates a sequence of numbers. But unlike functions, which return a whole array, a generator yields one value at a time. This requires less memory. (Wikipedia)

Generators in Python:

    Are defined with the def keyword
    Use the yield keyword
    May use several yield keywords
    Return an iterator


Iterators:
==========
 In Python programming language, an iterator is an object which implements the iterator protocol. The iterator protocol consists of two methods. The __iter__() method that returns self, which must return the iterator object and the next() method, which returns the next element from a sequence.

Python has several built-in objects, which implement the iterator protocol. For example lists, tuples, strings, dictionaries or files. 
 Iterators have several advantages:

    Cleaner code
    Iterators can work with infinite sequences
    Iterators save resources
By saving system resources we mean, that when working with iterators, we can get the next element in a sequence without keeping the entire dataset in memory. 

Difference between an iterator and a generator:
===============================================
iterator is a more general concept: any object whose class has a next method (__next__ in Python 3) and an __iter__ method that does return self.

Every generator is an iterator, but not vice versa. A generator is built by calling a function that has one or more yield expressions (yield statements, in Python 2.5 and earlier), and is an object that meets the previous paragraph's definition of an iterator.

You may want to use a custom iterator, rather than a generator, when you need a class with somewhat complex state-maintaining behavior, or want to expose other methods besides next (and __iter__ and __init__). Most often, a generator (sometimes, for sufficiently simple needs, a generator expression) is sufficient, and it's simpler to code because state maintenance (within reasonable limits) is basically "done for you" by the frame getting suspended and resumed.

All Generators are iterators, but not all iterators are generators.


New style classes:
The core change is to unify types and classes, and the nice side-effect of this is that it allows you to inherit from built-in types.
                                               ======================================================================================                        

Basic data types in python are:
===============================
Python also provides some built-in data types, in particular, dict, list, set (which along with frozenset, replaces the deprecated sets module), and tuple. The str class can be used to handle binary data and 8-bit text, and the unicode class to handle Unicode text.


To generate pyc files
======================
>>> import py_compile
>>> py_compile.compile('abc.py')
python -m compileall .


Python is strongly, dynamically typed.

    Strong typing means that the type of a value doesn't suddenly change. A string containing only digits doesn't magically become a number, as may happen in Perl. Every change of type requires an explicit conversion.
    Dynamic typing means that runtime objects (values) have a type, as opposed to static typing where variables have a type.

How does set work in python
===============================
A set in python is a hash itself. So implementing difference for it is not as hard as you imagine. Looking from a higher level how does one implement set difference? Iterate over one of the collections and add to the result all elements that are not present in the other sequence.

"""




"""
Object:

This is the basic unit of object oriented programming. That is both data and function that operate on data are bundled as a unit called as object.
Class:

When you define a class, you define a blueprint for an object. This doesn't actually define any data, but it does define what the class name means, that is, what an object of the class will consist of and what operations can be performed on such an object.
Abstraction:

Data abstraction refers to, providing only essential information to the outside word and hiding their background details ie. to represent the needed information in program without presenting the details.

For example, a database system hides certain details of how data is stored and created and maintained. Similar way, C++ classes provides different methods to the outside world without giving internal detail about those methods and data.
Encapsulation:

Encapsulation is placing the data and the functions that work on that data in the same place. While working with procedural languages, it is not always clear which functions work on which variables but object-oriented programming provides you framework to place the data and the relevant functions together in the same object.
Inheritance:

Encapsulation is process of the data and function binding together in one single entity such as an object
Encapsulation: bundling code and data together in an object. Some people use this as a synonym for information hiding. See this for a distinction that I like

Inheritence :One of the most useful aspects of object-oriented programming is code reusability. As the name suggests Inheritance is the process of forming a new class from an existing class that is from the existing class called as base class, new class is formed called as derived class.

This is a very important concept of object oriented programming since this feature helps to reduce the code size.
Polymorphism:

The ability to use an operator or function in different ways in other words giving different meaning or functions to the operators or functions is called polymorphism. Poly refers many. That is a single function or an operator functioning in many ways different upon the usage is called polymorphism.
Overloading:

The concept of overloading is also a branch of polymorphism. When the exiting operator or function is made to operate on new data type it is said to be overloaded.

"""

"""
class decorator without arguments
class decoratorWithoutArguments(object):

    def __init__(self, f):
        #If there are no decorator arguments, the function
        #to be decorated is passed to the constructor.
        #print "Inside __init__()"
        self.f = f

    def __call__(self, *args):
        #The __call__ method is not called until the
        #decorated function is called.
        print "Inside __call__()"
        self.f(*args)
        print "After self.f(*args)"

@decoratorWithoutArguments
def sayHello(a1, a2, a3, a4):
    print 'sayHello arguments:', a1, a2, a3, a4

print "After decoration"

print "Preparing to call sayHello()"
sayHello("say", "hello", "argument", "list")
print "After first sayHello() call"
sayHello("a", "different", "set of", "arguments")
print "After second sayHello() call"


class decorator with arguments
class decoratorWithArguments(object):

    def __init__(self, arg1, arg2, arg3):
        #If there are decorator arguments, the function
        #to be decorated is not passed to the constructor!
        print "Inside __init__()"
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        print "Inside __call__()"
        def wrapped_f(*args):
            print "Inside wrapped_f()"
            print "Decorator arguments:", self.arg1, self.arg2, self.arg3
            f(*args)
            print "After f(*args)"
        return wrapped_f

@decoratorWithArguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print 'sayHello arguments:', a1, a2, a3, a4


Function decorator with arguments
def decoratorFunctionWithArguments(arg1, arg2, arg3):
    def wrap(f):
        print "Inside wrap()"
        def wrapped_f(*args):
            print "Inside wrapped_f()"
            print "Decorator arguments:", arg1, arg2, arg3
            f(*args)
            print "After f(*args)"
        return wrapped_f
    return wrap

@decoratorFunctionWithArguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print 'sayHello arguments:', a1, a2, a3, a4

print "After decoration"

print "Preparing to call sayHello()"
sayHello("say", "hello", "argument", "list")
print "after first sayHello() call"
sayHello("a", "different", "set of", "arguments")
print "after second sayHello() call"
"""

"""
Method resolution operrator

Python uses timsort to sort lists

Why python doesnt support overloading
You generally don't need to overload functions in Python. Python is dynamically typed, and supports optional arguments to functions.

def myfunction(first, second, third = None):
    if third is None:
        #just use first and second
    else:
        #use all three

myfunction(1, 2) # third will be None, so enter the 'if' clause
myfunction(3, 4, 5) # third isn't None, it's 5, so enter the 'else' clause


Tuples are heterogeneous data structures (i.e., their entries have different meanings), while lists are homogeneous sequences. Tuples have structure, lists have order.
Tuples are immutable lists are mutable

$(document).ready(function() {
 // executes when HTML-Document is loaded and DOM is ready
 alert("document is ready");
});


$(window).load(function() {
 // executes when complete page is fully loaded, including all frames, objects and images
 alert("window is loaded");
});


Difference between dict and {}
=======================================
>>> from timeit import timeit
>>> timeit("a = {'a': 1, 'b': 2}")
0.424...
>>> timeit("a = dict(a = 1, b = 2)")
0.889...

python __dict__
>>> class B(object):
...     "Documentation of B class"
...     pass
...
>>> B.__doc__
'Documentation of B class'
>>> B.__dict__
<dictproxy object at 0x00B83590>
>>> B.__dict__['__doc__']
'Documentation of B class'
"""
