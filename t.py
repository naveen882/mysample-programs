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
print "====================="
print "====================="
