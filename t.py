import string
import logging
import datetime
import os,subprocess

class Dynamo():
	def __init__(self,x):
		print "In Init def"
		self.x =x
	
	def __str__(self):
		print "In str function"
		return str(self.x) + "======"

	def __repr__(self):
		print "In repr function"
		return self.x + "======="

	def __getattr__(self,k):
		if k == "color":
			print "key is color"
		else:
			print "key is something else %s"%(k)

d = Dynamo(1)
d.color
d.color1
print d
print "%s"%(d.x)
print str(d)
print "====================="


class Rastan(object):
	def __init__(self,x):
		print "In Init def"
		self.x =x

	def __str__(self):
		print "In str function"
		return str(self.x) + "======"

	def __repr__(self):
		print "In repr function"
		return self.x + "======="

	def __getattribute__(self,k):
		if k == "color":
			print "key is color"
		else:
			print "key is something else %s"%(k)

d=Rastan(1)
d.color
d.color1
print "%s"%(d.x)
print "====================="
#class decorator
class counted(object):
	def __init__(self,func):
		self.func = func
		self.counter = 0

	def __call__(self,*args,**kwargs):
		self.counter += 1
		return self.func(*args,**kwargs)


@counted
def something():
	pass

something()
print something.counter
something()
print something.counter
print "====================="
listone = [1,2,3]
listtwo = [4,5,6]
print listone + listtwo

listone = (1,2,3)
listtwo = (4,5,6)
print listone + listtwo

listone = [1,2,3]
listtwo = (4,5,6)

try:
    print listone+listtwo
except Exception as e:
	print e

print "====================="
listone = [1,2,3]
listone = listone *2
print listone
print "====================="
#pass by value and pass by referenece To do
print "====================="
#dictionary comprehension
m={'a':1,'b':2,'c':3,'d':4}
print m
print {v:k for k,v in m.items()}

emails = {'Dick': 'bob@example.com', 'Jane': 'jane@example.com', 'Stou': 'stou@example.net'}
print dict( [name , ".com" in email] for name,email in emails.iteritems())
print "====================="
A = {1, 2, 3, 3}
B = {2,3, 4, 5, 6, 7}
print A|B #combines and removes duplicates and also sorts in asc order
print A&B #combines common elements and removes duplicates and also sorts in asc order
print "====================="
#dictionary to list
dictionary = {'a': 1, 'b': 2, 'c': 3}
print dictionary.items()
dict_as_list = [['a', 1], ['b', 2], ['c', 3]]
print dict(dict_as_list)
dict_as_list = [('a', 1), ('b', 2), ('c', 3)]
print dict(dict_as_list)
dict_as_list = (('a', 1), ('b', 2), ('c', 3))
print dict(dict_as_list)
print "====================="
f=open("/tmp/aa.txt","w")
f.write("Testing  and \n Testing again \n and \n again")
f.close()

f=open("/tmp/aa.txt")
for l in f.read():
	print l,
f.close()
f=open("/tmp/aa.txt")
print"1"
while True:
	for l in f.readline():
		print l,
	else:
		break
	f.close()
f=open("/tmp/aa.txt")
l=f.readline()
while l:
	print l,
	l=f.readline()
print"2"
f=open("/tmp/aa.txt")
for l in f.readlines():
	print l,
f.close()
print "===="
f=open('/tmp/aa.txt')
lines=f.readlines()
print lines[1]
print lines[2]
f.close()
os.system("touch /tmp/ab.txt")
f=open("/tmp/ab.txt","r+") # read  and write mode  and to use this file should be existing already
f.write("This is some text 123456789")
print f.seek(10) #read after tenth character
print f.read() #read after tenth character and print every thing
f.seek(10) #read after tenth character
print f.read(1) #read after tenth character and print one character only 
f.close()
print "====================="
a=(0,1,2,3,4)
print a[0]
print a[1]
print a[2]
print a[3]
print "====================="
b=((1,2,3,4),(1,2))
print b[0][0]
print b[0][1]
print b[0][2]
print b[0][3]
print b[1][0]
print b[1][1]
print "====================="
for i in range(len(b)):
	for j in range(len(b[i])):
		print b[i][j]
print "====================="
c={'a':1,'b':2}
print c['a']
print c['b']
#key can also be added like this
c['c']=3
print c
print c.keys()
print c.values()
print c.pop('b',None)
print c
print c.get('b',c.update({'b':2}))
print c
print "====================="
try:
	if c['d']:
		print c['d']
except:
	logging.debug("debug")
	logging.debug("error")
	logging.debug("exception")
print "====================="
qq="12"
rr="13"
out = "<html>%(qq)s %(rr)s</html>"%locals()
print out
print "====================="
def func(a,b=None):
	if b is None:
		print "b is None"
		print b is None
	else:
		print a,b

func(1)
func(1,2)
print "====================="
def func1(a,*b):
	print a
	if len(b)>0:
		print b
		print type(b)
		for i in b:
			print i

func1(1)
func1(1,2,3,4,5)
print "====================="
def func2(l,**c):
	print l
	if len(c)>0:
		for i in c:
			print c[i]

func2(1)
func2(2,**({'a':3,'b':4}))
c={'a':1,'b':2,'c':3}
func2(1,**c)
print "====================="
aa=(1,2,3,(4,5),6)
print aa[0]
print aa[1]
print aa[2]
print aa[3][0]
print aa[3][1]
print aa[4]
print "====================="
i=5
def fs(args=i):
	print args
	print i

i=6
fs()
fs(7)
print "====================="
cc=[1,2,3,4]
dd=['1','2','3','4']
print "%s"%"====".join(dd)
print "".join(dd)

for i in range(len(dd)):
	print i ,dd[i]
a=11
b=22
c='ee'

print a,b,c
a,b,c=b,c,a
print a,b,c
print "====================="
add2 = lambda a,b:a+b;print "|||||";print "====="
print add2(1,2)
print add2(5,6)
def tr(add2):
	print add2(5,6)

#tr(add2)
print "====================="
ee=[1,2]
ff=[3,4]
c=[]
for i in zip(ee,ff):
	print i
	c.append(list(i)) 
print c
print [list(i) for i in zip(ee,ff)]
c= dict(c)
print c
c.update({'1':4})
print c
print "====================="
a=[1,2]
try:
	gg={a:2}
except:
	logging.exception("e")	
print "====================="
di=dict(a=1,b=2,c="22")
print di
print dir(di)
print di.items()
print di.has_key('a')
print di.keys()
print di.values()
it=di.iterkeys()
print dir(it)
print type(it)
print it.next()
print it.next()
print it.next()
it=di.itervalues()
print dir(it)
print type(it)
print it.next()
print it.next()
print it.next()
print "====================="
strings=['a','b','c','d','e']
for i,k  in enumerate(strings):
	print i,k
print "====================="
class test22:
	def hello(self,**args):
		print args['a']

jj={'a':1}
t=test22()
t.hello(**jj)
t.hello(**({'a':'b'}))
print "====================="
a=[6,6,1,1,2,3,3,3,4,5]
print set(a)
print list(set(a))
print type(list(set(a)))
print "====================="
a=[6,6,1,1,2,3,3,3,4,5]
print sorted(a)
print sorted(set(a),reverse=True)
print "====================="
def fun(*a,**kw):
	print a,kw

a=(1,2,3,'a')
b=dict(a=1,b=2,c=3)
fun(*a)
fun(**b)
fun(*a,**b)
print "====================="
opt = ["opt3", "opt2", "opt7", "opt6", "opt1", "opt10", "opt11"]
opt.sort()
print opt
print "====================="
list_of_tuples = [('key', 'value'), ('key2', 'value2')]
a_dict_2= dict(list_of_tuples)
print a_dict_2
a_dict_3 = a_dict_2
bb=1
aa=dict(a_dict_2=a_dict_3)
for val,key in enumerate(aa):
	print val
	print aa[key]
print a_dict_2 == a_dict_3
print a_dict_2.clear()
print str(a_dict_2) + "===="
print str(a_dict_3) + "===="
print "====================="
class mytest:
	p=1
	def __init__(self,a):
		self.a = a
		print str(self.p) + "===="
	def hello(self):
		print "in mytest hello"

class myt(mytest):
	def __init__(self,b,obj):
		obj.p=2
		obj.__init__(4)				
		print obj.p
	def hello(self):
		print "in myt hello"

mt=mytest(2)
m=myt(3,mt)
mt.hello()
m.hello()
print "====================="
mystr1="hello world"
print mystr1[::-2]
print mystr1[::-1]
print "====================="
for x in range(1,11):
	print x
print "====================="
str1="golf"
def reverse(str1):
	a=list(str1)
	for i in str1[::-1]:
		yield i

for i in reverse(str1):
	print i,
print "====================="
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print a
del a[2:4]
print a
del a[:]
print a
print "====================="
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
print "====================="
def linear(a,b):
	def result(x):
		return a*x+b
	return result(1)

aa=linear(3,4)
print aa
def linear(a,b):
	def result(x):
		return a*x+b
	return result

aa=linear(3,4)
print aa
bb=aa(5)
print bb
print "====================="
if __name__ == '__main__':
	print __name__
print logging.__name__
s="1"
print "====================="
a = [66.25, 333, 333, 1, 1234.5]
print a.count(333)
print a.count(66.25)
print a.count('x')
a.insert(2,-11)
print a
a.append(333)
print a.index(333)
print a
a.reverse()
print a
a.sort()
print a
print "====================="
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
print "====================="
class decoratorWithArguments(object):
	def __init__(self,a1,a2,a3,a4):
		print a1,a2,a3,a4

	def __call__(self,f):
		def rt(*args,**kwargs):
			f(*args,**kwargs)
			
		return rt

#@decoratorWithArguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print 'sayHello arguments:', a1, a2, a3, a4

def decoratorFunctionWithArguments(a1,a2):
	def rt(f):
		def t(*args):
			return f(*args)
		return t
	return rt		

@decoratorFunctionWithArguments(1,2)
def tt(a1,a2):
	print "Inside function"
	print a1,a2

tt(3,4)


def rt(f):
	def tt(*args,**kwargs):
		return f(*args,**kwargs)
	return tt

@rt
def t1():
	print "Inside t1"
	pass

t1()
print "====================="
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
print "====================="
a=[]
a=[1,2,3,333,6,'ab',5,4,7,'a',77,5566,94,2,34]
print a	
for ii in range(len(a)-1):
	for jj in range(len(a)-ii-1):
		if a[jj] > a[jj+1]:
			a[jj],a[jj+1]=a[jj+1],a[j]

print a 

a=[1,2,3,333,6,'ab',5,4,7,'a',77,5566,94,2,34]
print a
for ii in range(len(a)-1):
   for jj in range(len(a)-ii-1):
      if a[jj] > a[jj+ 1]:
         a[jj],a[jj+1]=a[jj+1],a[jj]

print a
print "====================="
word="acr"
word = sorted(word)
alternatives = ['car', 'girl', 'tofu', 'rca']
print [i for i in alternatives if sorted(i)==word  ]
print "====================="
a=['1','2','3']
a=map(int,a)
print a
print "====================="
def rt(a=[]):
	a.append(1)
	print a

rt()
rt()
rt()
rt()
print "====================="
d={}
print d['red'] if 'red' in d else "None======="
d={}
colors = ['red','red','red','red','green','blue','blue']
for i in colors:
	d[i] = d.get(i,0)+1
print d
print "====================="
def rs(a,b,c):
	print a,b,c

a=[1,2,3]
rs(*a)
T2=[(i,j) for i in range(3) for j in range(i) ]
print T2


arr=["harry","sally","tom"]
for i in range(len(arr)):
	print arr[i % len(arr)]*3
	print arr[(i+2) % len(arr)]*2
	print arr[(i+1) % len(arr)]*1

my_dict = {'carl':40, 'alan':2, 'bob':1, 'danny':3}
print dict([[v,k] for k,v in my_dict.items()])
print dict(my_dict.items())
print {v:k for k,v in my_dict.items()}
print "====================="
def fib():
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b

a= fib()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()

def fib(n):
	a,b=0,1
	while b<=n:
		yield a
		a,b=b,a+b

a=fib(5)
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print "====================="
def palindrome(word):
	return word == word[::-1]

print palindrome("tat")
print palindrome("t")
print palindrome("tat1")
print "====================="
#iterator
print "====================="
#python polymorphism and inheritenc exmaple
class Animal:
	def __init__(self,name):
		self.name = name
	def talk():
		raise NotImplementedError("Subclass must implement base class")

class Dog(Animal):
	def talk(self):
		return "woof woof"

class Cat(Animal):
	def talk(self):
		return "meow meow"


animals=[Cat("Missy"),Dog("Pluto"),Cat("Tom")]
for animal in animals:
	print animal.name + "speak as "+ animal.talk()
print "====================="
class a:
	pass
x=a()
print x.__dict__
print "====================="
art = ["a","b","c","d","e"]
for i in reversed(art):
	print i

colors = ["red","yellow","blue","green"]
for i in sorted(colors,reverse=True):
	print i
for i in reversed(colors):
	print i
a={'b':1}
del a['b']
print a
a,b,c,d=colors
print a,b,c,d
print "====================="
os.system('echo "hello world" > ./ten_one_liner.py')
print open('./ten_one_liner.py').readlines()
print open('./ten_one_liner.py').read()
print open('./ten_one_liner.py').readline()
x=1
print eval('x+1')
print eval('x')
print "====================="
os.system("touch /tmp/s.txt && echo 'hi' > /tmp/s.txt")
try:
	open("/tmp/s.txt").close()
except:
	print "exception"
else:
	print "no exception"
finally:
	print "In final"	
print "====================="
for i in range(1,11):
	print i
	break
else:
	print "In else1"
print "====================="
__p1= 1 #privare
_p2=2 #protected
p3=3 #public
print "====================="
string="yelloworld"
di={string:'123'}
print di
string ="yelloworld"
string=list(string)
string[0]='h'
string="".join(string)
print string
print di
di['helloworld']=di.pop('yelloworld')
print di
#OR
string="yelloworld"
di={string:'123'}
di['helloworld'] = di['yelloworld']
print di
print "====================="
f =open("/tmp/aa.txt")
while True:
	for l in f.readline():
		print l,
	else:
		break
f.close()
print "====================="
def fib1():
	a,b=0,1
	while b<5:
		yield a
		a,b=b,a+b

f=fib1()
print type(f)
print f.next()
print next(f)
print f.next()
print next(f)
print "====================="
from timeit import timeit

print timeit("a={'a':1,'b':2}")
print timeit("a=dict(a=1,b=2)")

class B():
	"Doc of class B"
	pass

print B.__dict__ 
print B.__doc__ 
print B.__dict__ ['__doc__']
class C(object):
    def m(self):
        print "m"


x=C()
x.m()
print dir(x)
print vars(x)
print "====================="
#not(A or B) == (not A) and (not B)
#not(A and B) == (not A) or (not B)
print "====================="
def make_incrementor(n): return lambda x:x+n
f=make_incrementor(2)
g=make_incrementor(4)

print f(42)
print g(48)
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
foo1 = [2, 9, 22, 12]
print filter(lambda x:x%3==0,foo)
print map(lambda x: x*2+10,foo)
print reduce(lambda x,y: x+y,foo1)

a_list = [1] * 10
print [id(i) for i in a_list]
print "====================="
#monkey patching
class rt:
	def rr(self):
		print "In rr"

def ww(self):
	print "In ww"

rt.rr = ww
r=rt()
r.rr()
print "====================="
thing = (i*2 for i in xrange(1,11))
print type(thing)
print thing
print next(thing)
print thing.next()
print thing.next()
print thing.next()
print thing.next()

print "====================="
a=[[1,2,3,4]]
b=list(a)
print b
print "====================="
#printing list in reverse order
for l in range(10,0,-1):
	print l
for l in range(10,0,-2):
	print l
print "====================="
def func(t):
	for i in t:
		yield i

a=[1,2,3,4,5]
g=func(a)
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()
	
print "====================="
import copy
a=[1,2,3]
b=[4,5,6]
c=[a,b]
d=c
print d
d[0][1]='a'
print d
print c
print id(c)==id(d)
print id(d[0])==id(c[0])

#using shallow copy
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
print c
print "shallowcopy"
d=copy.copy(c)
print d
print id(c)==id(d)
print id(d[0])==id(c[0])
d[0][1]='a'
print d
print c
#deep copy
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
print c
print "deepcopy"
d=copy.deepcopy(c)
print d
print id(c)==id(d)
print id(d[0])==id(c[0])
d[0][1]='a'
print d
print c
print "====================="
c={'a':1}
d=copy.copy(c)
print c,d
d.update({'b':2})
c.update({'c':3})
print c,d
print "deepcopy"
c={'a':1}
d=copy.deepcopy(c)
print "========"
print c,d
d.update({'a':2})
print c,d
c.update({'c':3})
print c,d
print "====================="
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print a[-1]
print a[-3]
print "====================="
x, y = 50, 25
small = x if  x<y else y
print small

b = 1==1
print b
name = "I am %s" % ["John","Doe"][b]
print name
n=0
print n<0 and 'n is negative' or 'n is positive'

abc = 'mystring',
print abc
print type(abc)
print "====================="
def foo(a,b,c):
	print a,b,c

mydict={'a':1,'b':2,'c':3}
mylist=[1,2,3]
foo(*mydict)
foo(**mydict)
foo(*mylist)
print "====================="
#enums

class enums:
	a,b,c,d = range(4)

print enums.a
print enums.b
print enums.c
print enums.d
os.system("echo '{\"key\":\"value\"}' | python -m json.tool")
calculator = {
	'+' : lambda x,y:x+y,
	'-' :  lambda x,y:x-y
	}
print calculator['+'](1,2)
print calculator['-'](2,1)
print "====================="
#context managers

with open("/tmp/aa.txt") as f:
	print f.read()
print "====================="
def f(x):
	return {
		'foo':1,
		'gg':2
	}.get(x,3)

print f('cc')
print f('gg')
print "====================="
p= lambda k : {'a':1,'b':2}.get(k,"default")
print p('a')
print p('aa')
print "====================="
#getting common elements form the list
a = [1,2,3,4]
b = [2,3,4,5]
c = [3,4,5,6]

print set(a) & set(b) & set(c)
print "====================="
#class method
class MyClass:
	@classmethod
	def tt(self):
		print "In tt"

MyClass.tt()
m=MyClass()
m.tt()
print "====================="
def yu(**kwargs):
   for i,k in kwargs.items():
      print i,k

yu(x=13,y=7,z=12)
print "====================="
class deco3(object):
   def __init__(self,u):
      self.u = u
   def __call__(self):
      print "====3"
      print self.u.f.g.__name__
      self.u.f.g()
      print "===="


class deco2(object):
   def __init__(self,f):
      self.f = f
   def __call__(self):
      print "====2"
      print self.f.g.__name__
      print "===="

class deco1(object):
   def __init__(self,g):
      self.g = g
   def __call__(self):
      print "====1"
      print self.g.__name__
      print "===="

@deco3
@deco2
@deco1
def tr():
   print "In tr"

tr()

print "====================="
def deco3(u):
   def ss():
      print "1"
      u()
   return ss

def deco2(y):
   def yy():
      print "2"
      print y.__name__
      y()
   return yy

def deco1(f):
   def tt():
      print "3"
      print f.__name__
      f()
   return tt

@deco3
@deco2
@deco1
def tr():
   print "In tr"

tr()
print "====================="
a=[1,2,3,333,6,5,4,7,77,5566,94,2,34,'a',66,'b']
print a
for i in range(len(a)-1):
	for j in range(len(a)-i-1):
		if a[j] > a[j+1]:
			a[j],a[j+1]=a[j+1],a[j]
print a
print "====================="
for i in range(1,101):
	if(i%3==0 and i%5==0):
		print i,"fizzbuzz"
	elif(i%3==0):
		print i,"fizz"
	elif(i%5==0):
		print i,"buzz"
	
print "====================="
T2 = ['13', '17', '18', '21', 32]
print map(int,T2)
print "====================="
class B(object):
	def __init__(self):
		print "In base class"
class childA(B):
	def __init__(self):
		B.__init__(self)
class childB(B):
	def __init__(self):
		super(childB,self).__init__()

print childA(),childB()
	
print "====================="
