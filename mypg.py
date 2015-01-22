import string
import logging
import datetime
import os,subprocess 

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
#Difference between function decorator and class decorator
#If you want to keep state in the decorator you should use a class. 
#If you can write a function to implement your decorator you should prefer it. But not all decorators can easily be written as a function - for example when you want to store some internal state.
#I've seen people (including myself) go through ridiculous efforts to write decorators only with functions. I still have no idea why, the overhead of a class is usually totally negligible.
#http://stackoverflow.com/questions/4650333/difference-between-decorator-classes-and-decorator-functions
class counted(object):
    """ counts how often a function is called """
    def __init__(self, func):
        self.func = func
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self.func(*args, **kwargs)


@counted
def something():
    pass

something()
print something.counter #Magic/Trick is function can access class variables
something()
print something.counter #Magic/Trick is function can access class variables
print "=========================================="
#combining two lists into one

listone = [1,2,3]
listtwo = [4,5,6]

mergedlist = listone + listtwo # This will not remove duplicates
#[1, 2, 3, 4, 5, 6]

print "=========================================="
#Duplicating a list within itself
listone = [1,2,3]
listone = listone * 2 

print listone
#[1, 2, 3, 1, 2, 3]


print "=========================================="
#Python pass by value and pass by reference
def f(*t):
  print t
  t=3
  print t
t= 2
print t
2
f(t) #prints (2,)
print t #prints 2


#Ex:2
x = [ 2, 4, 4, 5, 5 ]
print x  # 2, 4, 4, 5, 5

def go( li ) :
  li = [ 5, 6, 7, 8 ]  # re-assigning what li POINTS TO, does not
  # change the value of the ORIGINAL variable x

go( x ) 
print x  # 2, 4, 4, 5, 5  [ STILL! ]

#Ex:3
def change(x):
    x[0] = 3

x = [1]
change(x)
print x #prints 3o

def rr(a):
    a=1
    return a


a=2
print rr(a) #prints 1
print a #prints 2


#Ex:4
#All parameters (arguments) in the Python language are passed by reference. It means if you change what a parameter refers to within a function, the change also reflects back in the calling function. For example:
#All parameters in python language are passed by assignments

#!/usr/bin/python

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist
#Here, we are maintaining reference of the passed object and appending values in the same object. So, this would produce the following result:

#Values inside the function:  [10, 20, 30, [1, 2, 3, 4]]
#Values outside the function:  [10, 20, 30, [1, 2, 3, 4]]


#There is one more example where argument is being passed by reference and the reference is being overwritten inside the called function.


# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist
#The parameter mylist is local to the function changeme. Changing mylist within the function does not affect mylist. The function accomplishes nothing and finally this would produce the following result:

#Values inside the function:  [1, 2, 3, 4]
#Values outside the function:  [10, 20, 30]

#Function Arguments:
#You can call a function by using the following types of formal arguments:
#
#Required arguments
#
#Keyword arguments
#
#Default arguments
#
#Variable-length arguments

print "=========================================="
#Inverting a dictionary using a dictionary comprehension
m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
m
#{'d': 4, 'a': 1, 'b': 2, 'c': 3}
{v: k for k, v in m.items()}
#{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

#Dictionry comprehension example

emails = {'Dick': 'bob@example.com', 'Jane': 'jane@example.com', 'Stou': 'stou@example.net'}
email_at_dotcom = dict( [name, '.com' in email] for name, email in emails.iteritems() )
# email_at_dotcom now is {'Dick': True, 'Jane': True, 'Stou': False}
print "=========================================="

#Sets and set operations
A = {1, 2, 3, 3}
print A
#set([1, 2, 3])
B = {3, 4, 5, 6, 7}
print B
#set([3, 4, 5, 6, 7])
print A | B
#set([1, 2, 3, 4, 5, 6, 7])
print A & B
#set([3])
print A - B
#set([1, 2])
print B - A
#set([4, 5, 6, 7])
print A ^ B
#set([1, 2, 4, 5, 6, 7])
print (A ^ B) == ((A - B) | (B - A))
#[1,2,3] True

#sets are mutable
#fronzensets are immutable
print "=========================================="
#Dictionary to lists
dictionary = {'a': 1, 'b': 2, 'c': 3}
dict_as_list = dictionary.items()
#dict_as_list now contains [('a', 1), ('b', 2), ('c', 3)]

#Lists to Dicts
#You can reverse the process, turning a list of 2-element lists or tuples into a dict:
#'s
dict_as_list = [['a', 1], ['b', 2], ['c', 3]]
dictionary = dict(dict_as_list)
# dictionary now contains {'a': 1, 'b': 2, 'c': 3}
dict_as_list = [('a', 1), ('b', 2), ('c', 3)]
dictionary = dict(dict_as_list)
# dictionary now contains {'a': 1, 'b': 2, 'c': 3}
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

#Mixing while and for loop is probably a bad idea to read files since both are loops, using while only to ready files can be done by the following way

## Open the file with read only permit
f = open('/tmp/aa.txt')
## Read the first line 
line = f.readline()

#100.112.17.235# If the file is not empty keep reading line one at a time
## till the file is empty
while line:
	print line
	line = f.readline()
f.close()

print "====================="
os.system("touch /tmp/ab.txt")
f=open("/tmp/ab.txt","r+") # read  and write mode  and to use this file should be existing already
f.write("This is some text 123456789")
print f.seek(10) #read after tenth character
print f.read() #read after tenth character and print every thing
f.seek(10) #read after tenth character
print f.read(1) #read after tenth character and print one character only 
f.close()

#important reading speific lines

f=open('/tmp/aa.txt')
lines=f.readlines()
print lines[1]
print lines[2]
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
#Key value can also be added like the following
c['c'] = 3
print c
print c.keys() #returns keys list
print c.values() #returns values list
print c.pop('b',None) #returns 2
print c.get("b",c.update({'b':6}))
#print c.get("b",c['b']=6) #This raises an error saying assignment cannot be done here 
print c #prints {'a': 1, 'b': 6}
try :
	if c['d']:
		print c['d']
except:
	logging.debug("debug")
	logging.error("error")
	logging.exception("exception")

print "======================================="
qq="12"
rr="13"
out = "<html>%(qq)s%(rr)s</html>" % locals()
print out
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
		print b #This prints tuple
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
#####join takes liast as arguments
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
print "=======================================" ##From here
di=dict(a=1,b=2)
print di
print dir(di)
print di.items() # will represent key value in tuple format inside a list
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
#Array slicing
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
del a[2:4] #deletes items 2 and 3
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

def linear(a,b):
	def result(x):
		return a*x+b
	return result
aa= linear(5,6)
bb=aa(4)
print bb #prints 26
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
#class decorator without arguments
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


#class decorator with arguments
class decoratorWithArguments(object):

    def __init__(self, arg1, arg2, arg3):
        #If there are decorator arguments, the function
        #to be decorated is not passed to the constructor!
        print "Inside __init__()"
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        #If there are decorator arguments, __call__() is only called
        #once, as part of the decoration process! You can only give
        #it a single argument, which is the function object.
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


#Function decorator with arguments
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
d={}
print d['red'] if 'red' in d else 'None===========' 
d={'red':1}
#OR
d.get('red',"None===========")
print d['red'] if 'red' in d else 'None===========' 
d.get('red',"None===========")
#print help(d.get)
colors = ['red','red','red','red','green','blue','blue']
#Best way to count objects in a list
for i in colors:
	d[i]=d.get(i,0)+1
print d
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
#iterator
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
#Python polymorphism example and inheritence example
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
print x.__dict__
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

rt(ty=1) #you can call the function withc exact same function definition attributes.This is just for readability purpose.Changing the parameter will result in an error

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
	logging.exception("exception")
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: a() takes exactly 2 arguments (1 given)
print "======================================="
#oneliner to read a file
os.system("echo 'hello world' > ./ten_one_liners.py")
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
try:
    open("/tmp/s.txt")
    #pass
    #for i in range(10):
    #   break
except: #There can be more than one except
    print "Exception"
else:   #else part will be executed if no exceptions are raised
    print "In else"
finally: #finally will be executed irrespective of conditions
    print "In final"

try:
    pass
except:
    print "Exception"
finally: #finally will be executed irrespective of conditions
    print "In final"

#Python for else:
for i in range(1,11):
    print i
    break
else:
    print "In else1" #else will be executed only when there is no break
print "======================================="
#Python Access specifiers
#Python does not have mandatory access control like some other languages you may be used to. The philosophy of the language is "We are all consenting adults".
__private_access_specifier = 1 ## private has __
_protected_access_specifier = 2 ## protected has _
public_access_specifier = 3 ##with any underscore are public by default

#Ex:
class Cup:
	var = None #public variable by default
	_color = None    # protected variable
	__content = None # private variable

	def __init__(self, color):
		self._color = color

	def fill(self, beverage):
		self.__content = beverage

	def empty(self):
		self.__content = None

redCup = Cup("red")
redCup._Cup__content = "tea"

print "======================================="
#Important chnaging one character in a given string
string="yelloworld"
print string
string=list(string)
string[0]='h'
string1="".join(string)
print string1

string="yelloworld"
di={string:'123'}
print di
string=list(string)
string[0]='h'
string="".join(string)
print string
print di
#Note: Even though the string chnaged dictionary remain unchanged
#How to change a dictionary key 

di["helloworld"] = di.pop("yelloworld")
print di

#               OR

string="yelloworld"
di={string:'123'}
di["helloworld"]=di["yelloworld"]
print di
del di["yelloworld"]
print di

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

"""
class C(object):
    def m(self):
        print "m"


x=C()
x.m()
print dir(x)
print vars(x)
So the difference between vars(x) and dir(x) is that dir(x) does the extra work of looking in x's class (and it's bases) for attributes that are accessible from it, not just those attributes that are stored in x's own symbol table. In the above example, vars(x) returns an empty dictionary, because x has no instance variables. However, dir(x) returns
"""


"""
Difference between globals(), locals() and vars()
globals() always returns the dictionary of the module namespace
locals() always returns a dictionary of the current namespace
vars() returns either a dictionary of the current namespace (if called with no argument) or the dictionary of the argument.
def test():
    a = 1
    b = 2
    huh = locals()
    c = 3
    print(huh)
    huh['d'] = 4
    print(d)
test() #results in error where as 

class Test(object):
    a = 'one'
    b = 'two'
    huh = locals()
    c = 'three'
    huh['d'] = 'four'
    print huh
gives us:

{
  'a': 'one',
  'b': 'two',
  'c': 'three',
  'd': 'four',
  'huh': {...},
  '__module__': '__main__',
}
"""

"""
DeMorgans Laws

"not (A and B)" is the same as "(not A) or (not B)"

and also,

"not (A or B)" is the same as "(not A) and (not B)"

(not(x < 15 and y >= 3) has the same value as (x >= 15 or y < 3)
x = int(raw_input("Enter a value for x: "))
y = int(raw_input("Enter a value for y: "))
print (not(x < 15 and y >= 3))
print (x >= 15 or y < 3)
We have two values: T and F.
We can combine these values in three ways: NOT, AND, and OR.
NOT is the simplest:

NOT T = F
NOT F = T
http://www.annedawson.net/DeMorgansLaws.htm

"""


"""
What is __init__.py?
It is used to import a module in a directory, called package import.
 If we have a module, dir1/dir2/mod.py, we put __init__.py in each directories. So, we can import the mod like this:

import dir1.dir2.mod

The __init__.py is usually an empty py file. The hierarchy gives us a convenient way of organizing the files in a large system.
In the simplest case, __init__.py can just be an empty file, but it can also execute initialization code for the package or set the __all__ variable, described later.
"""

"""
Flake8 is a wrapper around these tools:

PyFlakes
pep8
Ned Batchelder's McCabe script
Flake8 runs all the tools by launching the single flake8 script. It displays the warnings in a per-file, merged output.

It also adds a few features:

files that contain this line are skipped:

# flake8: noqa
lines that contain a # noqa comment at the end will not issue warnings.

a Git and a Mercurial hook.
a McCabe complexity checker.
extendable through flake8.extension entry points.

QuickStart
pip install flake8

To run flake8 just invoke it against any directory or Python module:

$ flake8 coolproject
coolproject/mod.py:97:1: F401 'shutil' imported but unused
coolproject/mod.py:625:17: E225 missing whitespace around operato
coolproject/mod.py:729:1: F811 redefinition of function 'readlines' from line 723
coolproject/mod.py:1028:1: F841 local variable 'errors' is assigned to but never used
"""

"""
lambda functions:
Python supports the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, using a construct called "lambda".
>>> def f (x): return x**2
... 
>>> print f(8)
64
>>> 
>>> g = lambda x: x**2
>>> 
>>> print g(8)
64

As you can see, f() and g() do exactly the same and can be used in the same ways. Note that the lambda definition does not include a "return" statement -- it always contains an expression which is returned. Also note that you can put a lambda definition anywhere a function is expected, and you don't have to assign it to a variable at all. 


>>> def make_incrementor (n): return lambda x: x + n
>>> 
>>> f = make_incrementor(2)
>>> g = make_incrementor(6)
>>> 
>>> print f(42), g(42)
44 48
>>> 
>>> print make_incrementor(22)(33)
55

The above is equivalent to 

>>> def make_incrementor (n):
...     def x1(x):
...             return n+x
...     return x1

>>> foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
>>> 
print filter(lambda x: x % 3 == 0, foo)
#Construct a list from those elements of iterable for which function returns true. iterable may be either a sequence, a container which supports iteration, or an iterator. If iterable is a string or a tuple, the result also has that type; otherwise it is always a list.filter(function, iterable) is equivalent to [item for item in iterable if function(item)]

>>> print map(lambda x: x * 2 + 10, foo)
[14, 46, 28, 54, 44, 58, 26, 34, 64]
>>> 
>>> print reduce(lambda x, y: x + y, foo) #reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)
139
First we define a simple list of integer values, then we use the standard functions filter(), map() and reduce() to do various things with that list. All of the three functions expect two arguments: A function and a list. 

Of course, we could define a separate function somewhere else and then use that function's name as an argument to filter() etc., and in fact that's probably a good idea if we're going to use that function several times, or if the function is too complex for writing in a single line. However, if we need it only once and it's quite simple (i.e. it contains just one expression, like in the above examples), it's more convenient to use a lambda construct to generate a (temporary) anonymous function and pass it to filter() immediately. This creates very compact, yet readable code. 
"""


"""
A bit about Python's memory management
======================================
As you have seen before, a value will have only one copy in memory and all the variables having this value will refer to this memory location. For example when you have variables a, b, c having a value 10, it doesn't mean that there will be 3 copy of 10s in memory. There will be only one 10 and all the variables a, b, c will point to this value. Once a variable is updated, say you are doing a += 1 a new value 11 will be allocated in memory and a will be pointing to this.

Let's check this behaviour with Python Interpreter. Start the Python Shell and try the following for yourselves.

>>> a_list = [1] * 10
>>> a_list
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
>>> [id(value) for value in a_list]
[26089400, 26089400, 26089400, 26089400, 26089400, 26089400, 26089400, 26089400, 26089400, 26089400]
id() will return an objects memory address (object's identity). As you have noticed, when you create a list with same values, the values are not copied in memory. In fact, you are getting a list with references to the value 1; not a list with 10 copies of 1.

Now we will try to create custom objects and try to find their identities.

>>> class Foo:
...     pass
... 
>>> bar = Foo()
>>> baz = Foo()
>>> id(bar)
140730612513248
>>> id(baz)
140730612513320
>>> list_a = [1, 2, 3] # lists are mutable objects
>>> list_b = [1, 2, 3]
>>> id(list_a)
140116233272136
>>> id(list_b)
140116233272064
>>> [id(value) for value in list_a]
[24221624, 24221600, 24221576] # `int` is immutable
>>> [id(value) for value in list_b]
[24221624, 24221600, 24221576] # same as above
As you can see, the two instances have different identities. That means, there are two different copies of the same object in memory. This behaviour is different from what you have seen before. When you are creating objects they will have unique identities unless you are using Singleton Pattern. All immutable objects like str, int, float will have same identities when objects are created simultaneously.



"""


"""
Difference between function decorator and class decorator
 14 down vote accepted
	

If you want to keep state in the decorator you should use a class else for a simple case use a class decorator.

For example, this does not work

def mydecorator(f):
    x = 0 
    def decorator():
        x += 1 # x is a nonlocal name and cant be modified
        return f(x)
    return decorator 

There are many workarounds for this but the simplest way is to use a class

class mydecorator(object):
    def __init__(self, f):
        self.f = f
        self.x = 0

    def __call__(self, *k, **kw):
        self.x += 1
        return f(self.x)


"""


"""
Monkey-patching

The origin of monkey-patch according to wiki is :
"The term monkey patch seems to have come from an earlier term, guerrilla patch, which referred to changing code sneakily at runtime. The word guerrilla, homophonous with gorilla, became monkey, possibly to make the patch sound less intimidating."

In Python, the term monkey patch only refers to dynamic modifications of a class or module at runtime, motivated by the intent to patch existing third-party code as a workaround to a bug or feature which does not act as you desire.

We have a module called m.py like this:

# m.py
class MyClass:
    def f(self):
        print "f()"

Then, if we run the monkey-patch testing like this:

>>> import m
>>> def monkey_f(self):
	print "monkey_f()"

	
>>> m.MyClass.f = monkey_f
>>> obj = m.MyClass()
>>> obj.f()
monkey_f()
>>> 

As we can see, we did make some changes in the behavior of f() in MyClass using the function we defined, monkey_f(), outside of the module m.

It is a risky thing to do, but sometimes we need this trick, such as testing.
"""


"""
>>> thing = ( x*2 for x in xrange(10) )
>>> 
>>> type(thing)
<type 'generator'>
>>> thing = [x*2 for x in xrange(10) ]
>>> type(thing) #list
>>> def t():
...     for i in range(10):
...             yield i
... 
>>> thing = (x for x in t())
>>> type(thing)
<type 'generator'>
>>> thing = [x for x in t()]
>>> type(thing)
<type 'list'>
>>> 

"""


"""
a=[]
b=list()
a==b #True

a=['hello']
b=list('hello')
a==b #False
a[0] #hello
b[0] #h
b[1] #e
b[2] #l
b[3] #l
b[4] #o
#Another trick for the same is :)

c="hello"
c[0] #h
c[1] #e
c[2] #l
c[3] #l
c[4] #o

a = 'hello'
a= a+ 'x'
a
#'hellox'



a=[1,2,3,4]
b=list(a)
b[0]
#1
b[1]
#2

"""


"""
#Map, filter and reduce
#Map
We have a built-in feature that does most of the work for us. The map(aFunction, aSequence) function applies a passed-in function to each item in an iterable object and returns a list containing all the function call results.
ex:
>>> items = [1, 2, 3, 4, 5]
>>> def sqr(x): return x ** 2

>>> list(map(sqr, items))
[1, 4, 9, 16, 25]

#Filter
#As the name suggests filter extracts each element in the sequence for which the function returns True. The reduce function is a little less obvious in its intent. This function reduces a list to a single value by combining elements via a supplied function. The map function is the simplest one among Python built-ins used for functional programming.

>>> list(range(-5,5))
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
>>>
>>> list( filter((lambda x: x < 0), range(-5,5)))
[-5, -4, -3, -2, -1]
>>> 


#Reduce
#The reduce is in the functools in Python 3.0. It is more complex. It accepts an iterator to process, but it's not an iterator itself. It returns a single result:

>>> 
>>> from functools import reduce
>>> reduce( (lambda x, y: x * y), [1, 2, 3, 4] )
24
>>> reduce( (lambda x, y: x / y), [1, 2, 3, 4] )
0.041666666666666664
>>> 
At each step, reduce passes the current product or division, along with the next item from the list, to the passed-in lambda function. By default, the first item in the sequence initialized the starting value.
"""


"""
#printing list in reverse order with python
>>> for length in range(10, 0,-1):
...     print length
... 
10
9
8
7
6
5
4
3
2
1
>>> for length in range(10, 0,-2):
...     print length
... 
10
8
6
4
2


"""


"""
Difference between an iterator and generator is that consider the following example,
"""
def func(t):
	for i in t:
		yield i

li=[1,2,3,4,5]
gn = func(li)
print gn.next() #after printing 1, 1 is discarded from memory
print gn.next() #after printing 2, 2 is discarded from memory
print gn.next() #after printing 3, 3 is discarded from memory
"""
From above,Thats why generator are more efficient,where as in iterator after returning 1 ,1 is still retained in memory , we may have to use del() explicitly to remove it from memory,but also some times the object have circular references and therefore may need to delete all the objects associated with it which is more complicated and errorsum. So generator is ususally preferred over an iterator most of the times
"""



"""
>>> a=[]
>>> for i in a:
...     print "inside"
... else:
...     print "in else"
... 
in else
"""


"""
>>> li = [0] * 3
>>> li
[0, 0, 0]
>>> li = [[0] * 3] * 3
>>> li
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> li[0][0]=5
>>> li
[[5, 0, 0], [5, 0, 0], [5, 0, 0]]
>>> li[0][1]=6
>>> li
[[5, 6, 0], [5, 6, 0], [5, 6, 0]]
>>> li[0][2]=7
>>> li
[[5, 6, 7], [5, 6, 7], [5, 6, 7]]
>>> 

"""


"""
#Shallow copy and deep copy
Shallow copies duplicate as little as possible. A shallow copy of a collection is a copy of the collection structure, not the elements. With a shallow copy, two collections now share the individual elements.

Deep copies duplicate everything. A deep copy of a collection is two collections with all of the elements in the original collection duplicated.
In short, it depends on what points to what. In a shallow copy, object B points to object A's location in memory. In deep copy, all things in object A's memory location get copied to object B's memory location.

For example:
"""
import copy
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
print "======Normal copy============="
print c

#Using normal assignment operatings to copy:
d=c
print d
d[0][1]="a"
print c #"a"is found in both c and d
print d #"a"is found in both c and d
print id(c) == id(d)  #True ,both have same ids
print id(c[0]) == id(d[0]) #True ,Elements are also same

#using a shallow copy
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
print "======Shallow copy============="
print c
d = copy.copy(c)
print id(c) == id(d)  #False ,both have different ids
print id(c[0]) == id(d[0]) #True ,Elements are also same
d[0][1]="a"
print c #"a"is found in both c and d
print d #"a"is found in both c and d

#using a shallow copy
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
print "======Deep copy============="
print c
d = copy.deepcopy(c)
print id(c) == id(d)  #False ,both have different ids
print id(c[0]) == id(d[0]) #False ,Elements are also same
d[0][1]="a"
print c #"a"is found in d only
print d #"a"is found in d only

print "======shallow dict copy============="
c={'a':1}
d=copy.copy(c)
d.update({'b':2})
print c,d
c.update({'c':3})
print c,d
print "======deep dict copy============="
c={'a':1}
d=copy.deepcopy(c)
d.update({'a':2})
print c,d
c.update({'c':3})
print c,d
print "=========================================="
d={"a":1,"b":2,"c":3}
print zip(*d.iteritems()) #To separate keys and values, 
#[('a', 'c', 'b'), (1, 3, 2)]
print zip(d.iteritems()) #if "* is omitted the output is as follows"
#[(('a', 1),), (('c', 3),), (('b', 2),)]

a, b, c = 1, 2, 3
print a, b, c
#(1, 2, 3)
a, b, c = [1, 2, 3]
print a, b, c
#(1, 2, 3)
a, (b, c), d = [1, (2, 3), 4]
print a
#1
print b
#2
print c
#3
print d
#4

#Negative indexing

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print a[-1]
#10
print a[-3]
#8

#List slices with step (a[start:end:step])

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print a[::2]
#[0, 2, 4, 6, 8, 10]
print a[::3]
#[0, 3, 6, 9]
print a[2:8:2]
#[2, 4, 6]


a = [1, 2, 3, 4, 5, 6]

# Using iterators
group_adjacent = lambda a, k: zip(*([iter(a)] * k))
print group_adjacent(a, 3)
#[(1, 2, 3), (4, 5, 6)]
print group_adjacent(a, 2)
#[(1, 2), (3, 4), (5, 6)]
print group_adjacent(a, 1)
#[(1,), (2,), (3,), (4,), (5,), (6,)]


#[on_true] if [expression] else [on_false]
x, y = 50, 25
small = x if x < y else y
print small

print "=========="
#Boolean as indexes
b = 1==1
name = "I am %s" % ["John","Doe"][b]
print name

print "=========="
#In python false is treated as 0 and True is treated as 1
a=1
print (a==1) + (a>0) + (a==2)
#2
print "=========="
a = ['two', 'three', 'four']
for i, word in enumerate(a, 2):
  print i, word

#2 two
#3 three
#4 four

print "====List comprehension if else======"
a=1
b=2
print [ a if a== 1 else  b]
print "=========="
n=1
if n < 0:
    result = 'n is negative'
else:
    result = 'n is positive'
#Or in short this can be written as ,
result = n < 0 and 'n is negative' or 'n is positive'
print result
print "=========="
a=[1,2,3,4,5]
b=[6,7,8,9]
print dict(zip(a,b))
#{1: 6, 2: 7, 3: 8, 4: 9}
print "=========="
abc = 'mystring',
print abc
# ('mystring,) #abc is a tuple now ust because of the leading comma

print "=========="
def foo(a, b, c):
    print a, b, c

mydict = {'a':1, 'b':2, 'c':3}
mylist = [10, 20, 30]

foo(*mydict)
#a, b, c
foo(**mydict)
#1, 2, 3
foo(*mylist)
#10 20 30
print "=========="
#Python enums
class PlayerRanking:
  Bolt, Green, Johnson, Mom = range(4)

print PlayerRanking.Mom
#3
print "=========="
#Inline if statement
print "Hello" if True else "World"
#Hello
print "=========="
#List comprehension
numbers = [1,2,3,4,5,6]
even = [number for number in numbers if number%2 == 0]
print "=========="
#This is more of a fun one than a useful technique. In python True and False are basically just global variables. Thus:
print False == True
#False
False = True
if False:
    print "Hello"
else:
    print "World"
#Hello
print "=========="
os.system("echo '{\"key\":\"value\"}' | python -m json.tool")
print "=========="
#Python simple calculator and writing lamda functions inside dictionary
calculator = {
'plus': lambda x, y: x + y,
'minus': lambda x, y: x - y
}
print calculator['minus'](9,3)
#6
print "=========="
#Context Managers!
with open("ten_one_liners.py") as f:
   print(f.readlines())

#It will automatically close the file on exit, this can be used for creating resources which are automatically cleaned up after exiting scope.

print "=========="
#Implementing a switch-case statement:
def f(x):    
    return {
        'foo': 1,
        'bar': 2,        
    }.get(x, 3) #.get is like the default,very important

print f('gg')
print f('foo')
print "=========="
#Default value
text = ''
option = text or 'empty'
print option
#'empty'
print "=========="
#Ternary Expressions

y = 1
x = 10 if (y == 1) else 20
print x
#10
y = 2
x = 10 if (y == 1) else 20
print x
#20
print "=========="
p = lambda k : {"a":1,"b":2}.get(k,"Default")
p("a")
#1
p("b")
#2
p("bb")
#'Default'
print "=========="
#creating a class on the fly using type
#using type to create classes
#type takes three arguments 
#1.Name of the new class
#2.parent class in tuple format if any
#3. class functions in dict format as shown

def t(self,a):
	print a


class A(object):
	def __init__(self):
		print "In A"

B= type("B",(A,),{"t1":t})
b=B()
b.t1(11)
C= type("C",(object,),{"t2":t})
c=C()
c.t2(12)
#print "=========="
#As to why the dict.update function is used beacuse u can update more than one variable at the same time. As oppose to a['aa'] where only one value can be updated at one time
#print "=========="
#Get common elements from 3 lists
a = [1,2,3,4]
b = [2,3,4,5]
c = [3,4,5,6]
print set(a) & set(b) & set(c)
#{3, 4}
# or 
out = [x for x in a if x in b and x in c] # Depending on the length of the lists, a very expensive solution
print out

