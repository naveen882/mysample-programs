import string
import logging
import datetime
import os,subprocess 

class Dynamo():
	def __init__(self,x):
		print("In Init def\n")
		self.x = x

	def __str__(self):
		print("In str function")
		return str(self.x)+ "======"

	def __repr__(self):
		print("In repr function")
		return self.x+ "===="

	def __getattr__(self,k):
		if k == "color":
			print("key is color")
		else:
			print("key is something else %s"%(k))

d=Dynamo(1)
d.color
d.color1
print("%s"%(d.x))
print(str(d)) ##//Thsi will print(str function

print("===================================")
#A key difference between __getattr__ and __getattribute__ is that __getattr__ is only invoked if the attribute wasn't found the usual ways. It's good for implementing a fallback for missing attributes, and is probably the one of two you want.
print("===================================")


class Rastan(object):
	def __init__(self,x):
		print("In init def")
		self.x=x

        #getattribute is invoked before looking at the actual attributes on the object,
	def __getattribute__(self,k):
		print("In get attribute")
		if k == "color":
			print("key is color")
		else:
			print("key is comething else %s  and %s"%(k,"============"))

d=Rastan(1)
d.color
d.color1	
print("%s"%(d.x))

print("==========================================")
#Difference between function decorator and class decorator
#If you want to keep state in the decorator you should use a class decorator. 
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
print(something.counter) #Magic/Trick is function can access class variables
something()
print(something.counter) #Magic/Trick is function can access class variables
#### OR ######
#s=something
#print(s.counter
print("==========================================")
#combining two lists into one

listone = [1,2,3]
listtwo = [4,5,6]

mergedlist = listone + listtwo # This will not remove duplicates ,also this will result in a list [1,2,3,4,5,6]
listone.extend(listtwo) #To merge to list one
print(listone)
#[1, 2, 3, 4, 5, 6]
listone = (1,2,3)
listtwo = (4,5,6)

print(listone+listtwo) #also this will result in a tuple (1,2,3,4,5,6)
listone = [1,2,3]
listtwo = (4,5,6)

try:
    print(listone+listtwo)
except Exception as e: #Exception is a keyword
    print(e)

print(listone+list(listtwo))
print("==========================================")
#Duplicating a list within itself
listone = [1,2,3]
listone = listone * 2 

print(listone)
#[1, 2, 3, 1, 2, 3]

listone=[1,2,3]
print([listone]*2)
#[[1, 2, 3], [1, 2, 3]]


print("==========================================")
#Python pass by value and pass by reference
def f(*t):
  print(t)
  t=3
  print(t)
t= 2
print(t)
2
f(t) #prints (2,)
print(t) #prints 2


#Ex:2
x = [ 2, 4, 4, 5, 5 ]
print(x)  # 2, 4, 4, 5, 5

def go( li ) :
  li = [ 5, 6, 7, 8 ]  # re-assigning what li POINTS TO, does not
  # change the value of the ORIGINAL variable x

go( x ) 
print(x)  # 2, 4, 4, 5, 5  [ STILL! ]

#Ex:3
def change(x):
    x[0] = 3

x = [1]
change(x)
print(x) #prints 3o

def rr(a):
    a=1
    return a


a=2
print(rr(a)) #prints 1
print(a) #prints 2

a=1

def t():
	print(a) #prints 1

t()

a=1

def t():
	try:
		a=a+1 #this will raise an error,because a will be treated as a local variable and is unknow now
	except:
		pass

t()
#Ex:4
#All parameters (arguments) in the Python language are passed by reference. It means if you change what a parameter refers to within a function, the change also reflects back in the calling function. For example:
#All parameters in python language are passed by assignments


def tyhu(tt):
	tt+=10
	return tt

g=10
yy = tyhu(g)
print(g,yy)


#In this case the function is creating a copy of g as tt and also it is not mentioned as global variable

#!/usr/bin/python

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)
#Here, we are maintaining reference of the passed object and appending values in the same object. So, this would produce the following result:

#Values inside the function:  [10, 20, 30, [1, 2, 3, 4]]
#Values outside the function:  [10, 20, 30, [1, 2, 3, 4]]


#There is one more example where argument is being passed by reference and the reference is being overwritten inside the called function.


# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)
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
######################################Inference###########################
# from the above we see that a list passes can only be changed by list operations and not by assinging new list
#tuples cannot be changed
#integer cannot be changed

print("==========================================")
#Inverting a dictionary using a dictionary comprehension
m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(m)
#{'d': 4, 'a': 1, 'b': 2, 'c': 3}
print({v: k for k, v in m.items()})
#{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

#Dictionry comprehension example

emails = {'Dick': 'bob@example.com', 'Jane': 'jane@example.com', 'Stou': 'stou@example.net'}
email_at_dotcom = dict( [name, '.com' in email] for name, email in emails.items() )
# email_at_dotcom now is {'Dick': True, 'Jane': True, 'Stou': False}
print("==========================================")

#Sets and set operations
A = {1, 2, 3, 3}
print(A)
#set([1, 2, 3])
B = {2,3, 4, 5, 6, 7}
print(B)
#set([3, 4, 5, 6, 7])
print(A | B) #combines and removes duplicates and also sorts in asc order
#set([1, 2, 3, 4, 5, 6, 7])
print(A & B) #combines common elements and removes duplicates and also sorts in asc order
#set([2, 3])
print(A - B)
#set([1, 2])
print(B - A)
#set([4, 5, 6, 7])
print(A ^ B)
#set([1, 2, 4, 5, 6, 7])
print((A ^ B) == ((A - B) | (B - A)))
#[1,2,3] True

#sets are mutable
#fronzensets are immutable
print("==========================================")
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
dict_as_list = (('a', 1), ('b', 2), ('c', 3))
dictionary = dict(dict_as_list)
# dictionary now contains {'a': 1, 'b': 2, 'c': 3}
dict_as_list = (('a', 1), ('b', 2), ['c', 3])
dictionary = dict(dict_as_list)
# dictionary now contains {'a': 1, 'b': 2, 'c': 3}
print("==========================================")

f=open("/tmp/aa.txt","w")
f.write("Testing  and \n Testing again \n and \n again")
f.close()

f=open("/tmp/aa.txt")
while True:
	for l in f.read(): #reads full file at one stretch
		print(l,)
	else:
		break
f.close()


f=open("/tmp/aa.txt")
while True:
	for l in f.readline(): #reads a sing line
		print(l,)
	else:
		break
f.close()


f=open("/tmp/aa.txt") # read entire file once and splits it line by line
while True:
	for l in f.readlines():
		print(l,)
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
	print(line)
	line = f.readline()
f.close()

print("=====================")
os.system("touch /tmp/ab.txt")
f=open("/tmp/ab.txt","r+") # read  and write mode  and to use this file should be existing already
f.write("This is some text 123456789")
print(f.seek(10)) #read after tenth character
print(f.read()) #read after tenth character and print(every thing
f.seek(10) #read after tenth character
print(f.read(1)) #read after tenth character and print(one character only 
f.close()

#important reading speific lines

f=open('/tmp/aa.txt')
lines=f.readlines()
print(lines[1])
print(lines[2])
f.close()

print("=======================================")

a=(1,2,3,4)
print(a[0])
print(a[1])
print(a[2])
print(a[3])

print("=======================================")
b=((1,2,3,4),(1,2))
print(b[0][0])
print(b[0][1])
print(b[0][2])
print(b[0][3])
print(b[1][0])
print(b[1][1])

print("=======================================")
for i in range(len(b)):
	for s in range(len(b[i])):
		print(b[i][s])

print("=======================================")
c={'a':1,'b':2}
print(c['a'])
print(c['b'])
#Key value can also be added like the following
c['c'] = 3
print(c)
print(c.keys()) #returns keys list
print(c.values()) #returns values list
print(c.pop('b',None)) #returns 2
print(c.get("b",c.update({'b':6})))
#print(c.get("b",c['b']=6) #This raises an error saying assignment cannot be done here 
print(c) #prints {'a': 1, 'b': 6}
try :
	if c['d']:
		print(c['d'])
except:
	logging.debug("debug")
	logging.error("error")
	logging.exception("exception")

print("=======================================")
qq="12"
rr="13"
out = "<html>%(qq)s%(rr)s</html>" % locals()
print(out)
out = "<html>%(qq)s%(rr)s</html>" % globals()
print(out)
print("=======================================")
def func(a,b=None):
	if b is None:
		print("b is None")
		print(b is None) ## this will print(true
	else:
		print(a,b)

func(1)
func(1,2)
print("=======================================")
def func1(a,*b): #* stands for a tuple
	print(a)
	if len(b) > 0 :
		print(b) #This prints tuple
		print(type(b)) #This prints tuple
		for i in b:
			print(i)

func1(1,2,3,4,5,6) #watch the difference between the below line
func1(1,2,3,4,5,6,)
func1(1)
func1(1,) #this will not enter the if loop
print("=======================================")
def func2(l,**c):
	print(l)
	if len(c) > 0:
		for i in c:
			print(c[i])

c={'a':1,'b':2,'c':3}
func2(1,**c)
print("=======================================")
aa=(1,2,3,(4,5),6)
print(aa[0])
print(aa[1])
print(aa[2])
print(aa[3][0])
print(aa[3][1])
print(aa[4])
print("=======================================")
i=5
def fs(args=i):
	print(args)
	print(i)

i=6
fs()
fs(7)
print("=======================================")
cc=[1,2,3,4]
dd=['1','2','3','4']
print("%s"%"====".join(dd)) ##### To remember   
print("====".join(dd)) #This is similar to the above statement
#####join takes liast as arguments
for i in range(len(dd)):
	print(i,dd[i])
a=11
b=22
c="ee"

print(a,b,c)
a,b,c=c,a,b
print(a,b,c)
print("=======================================")
add2 = lambda a,b:a+b;print("=====");print("|||||||");print("iiiiiiiii")   ##To remember,first return statement and rest prints statement next
print(add2(3,4))
def tr(add2):
	print(add2(5,6))
print("=======================================")
ee=[1,2]
ff=[3,4]
gg=zip(ee,ff)
print(gg)
gg = dict(gg)
print(gg)
gg.update({'1':4})
print(gg[1])
print(gg['1'])     
print(gg)
print("=======================================")
a=[1,2]
try:
	gg={a:2}
	print(gg)
except:
	print(logging.exception("e")) #This prints unhashable type: 'list'
print("=======================================") ##From here
di=dict(a=1,b=2)
print(di)
print(dir(di))
print(di.items()) # will represent key value in tuple format inside a list
#print(di.has_key('a')) This works on python2.7
print(di.keys())
print(di.values())
#it =di.iterkeys() This works on python2.7
#print(it.next())
#print(it.next())
#it =di.itervalues()
#print(it.next())
#print(it.next())
print("=======================================")
strings=['a','b','c','d','e']
for i,k in enumerate(strings):
	print(i,k)
print("=======================================")
class test22:
	def hello(self,**args):
		print(args['a'])

jj={'a': '1'}
t = test22()	
t.hello(**jj)
t.hello(**({'a':'b'}))
		
print("=======================================")
a=[6,6,1,1,2,3,3,3,4,5]
print(list(set(a)))
print(type(list(set(a))))
print("=======================================")
a=[6,6,1,1,2,3,3,3,4,5]
print(sorted(a))
print(sorted(set(a),reverse=True))
print("=======================================")
def fun(*a,**kw):
	print(a,kw)

a= [1,2,3,'a']
b=dict(a=1,b=2,c=3)
fun(*a)
fun(**b)
fun(*a,**b)
##very important below without * and ** while calling fun()
fun(a)
fun(b)
fun(a,b)
print("=======================================")
opt = ["opt3", "opt2", "opt7", "opt6", "opt1", "opt10", "opt11"]
print(sorted(opt))
print((opt.sort())) #This will sort the original list
print(opt)
print("=======================================")

list_of_tuples = [('key', 'value'), ('key2', 'value2')]
a_dict_2 = dict(list_of_tuples)
print(a_dict_2)
a_dict_3 = a_dict_2
bb=1
aa=dict(a_dict_2 = a_dict_2)
print(aa)
for val ,key in enumerate(aa):
		for i in aa[key]:
			print("========")
			print(aa[key])
			print(aa[key][i])
print(a_dict_2 ==a_dict_3)	
print(a_dict_2.clear()) #a_dict_3 is also cleared
print(str(a_dict_2) + "=====")
print(str(a_dict_3) + "=====")
print("=======================================")
class mytest:
	p = 1
	def __init__(self,a):
		self.a = a
		print(str(self.p) + "======")		
	def hello(self):
		print("in mytest hello")

class myt(mytest):
	def __init__(self,b,obj):
		obj.p=2
		obj.__init__(4)
		print(obj.p)

	def hello(self):
		print("in myt hello")

mt = mytest(2)
m=myt(3,mt)
mt.hello()
m.hello()
print("=======================================")
#Array slicing
mystr1="hello world"
print(mystr1[::-2])
print(mystr1[-1]) # prints d #This is Negative indexing in python ****************
print("=======================================")
for x in range(1,11):
	print(x)
print("=======================================")
str1="golf"
def reverse(str1):
	a=list(str1)
	for i in str1[::-1]:
		yield i

for i in reverse(str1):
		print(i)

print("=======================================")
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4] #deletes items 2 and 3
print(a)
del a[:]
del a[::]
print(a)
print("=======================================")
knights={'a':1,'b':2}
for i,k in knights.items():
	print(type(i))
	print(type(k))
	print(i,k)
for k in knights:
	print(type(k))
	print(k)
for k in knights.values():
	print(type(k))
	print(k)
print("=======================================")
def linear(a,b):
	def result(x):
		return a*x+b
	return result(1)

aa=linear(3,4)
print(aa)	

def linear(a,b):
	def result(x):
		return a*x+b
	return result
aa= linear(5,6)
bb=aa(4)
print(bb) #prints 26
print("=======================================")
if __name__ == "__main__":
	print(__name__)
import logging
print(logging.__name__)
class rtt(object):
    pass
print(rtt.__name__) #prints rtt as string
print("=======================================")
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333))
print(a.count(66.25))
print(a.count('x'))
print(a.insert(2,-11))
print(a.append(333))
print(a.index(333))
print(a)
print(a.reverse())
print(a)
print(a.sort())
print(a)
print(a.sort())

print("=======================================")
#class decorator without arguments
class decoratorWithoutArguments(object):

    def __init__(self, f):
        #If there are no decorator arguments, the function
        #to be decorated is passed to the constructor.
        #print("Inside __init__()"
        self.f = f

    def __call__(self, *args):
        #The __call__ method is not called until the
        #decorated function is called.
        print("Inside __call__()")
        self.f(*args)
        print("After self.f(*args)")

@decoratorWithoutArguments
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)

print("After decoration")

print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("After first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("After second sayHello() call")


#class decorator with arguments
class decoratorWithArguments(object):

    def __init__(self, arg1, arg2, arg3):
        #If there are decorator arguments, the function
        #to be decorated is not passed to the constructor!
        print("Inside __init__()")
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3

    def __call__(self, f):
        #If there are decorator arguments, __call__() is only called
        #once, as part of the decoration process! You can only give
        #it a single argument, which is the function object.
        print("Inside __call__()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", self.arg1, self.arg2, self.arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f

@decoratorWithArguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)


#Function decorator with arguments
def decoratorFunctionWithArguments(arg1, arg2, arg3):
    def wrap(f):
        print("Inside wrap()")
        def wrapped_f(*args):
            print("Inside wrapped_f()")
            print("Decorator arguments:", arg1, arg2, arg3)
            f(*args)
            print("After f(*args)")
        return wrapped_f
    return wrap

@decoratorFunctionWithArguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
    print('sayHello arguments:', a1, a2, a3, a4)

print("After decoration")

print("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("after second sayHello() call")
print("=======================================")
def shout(aa="yes"):
	print(aa)

scream=shout
scream()
scream(1)

print("=======================================")
def makebold(fn):
    print("2")
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    print("1")
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

print(hello())
print("=======================================")
"""This works on python2.7, string and integer cannot be compared on python 3
a=[1,2,3,333,6,'ab',5,4,7,'a',77,5566,94,2,34]
print(a)
for ii in range(len(a)-1):
	for jj in range(len(a)-ii-1):
		if a[jj] > a[jj+ 1]:
			a[jj],a[jj+1]=a[jj+1],a[jj]

print(a)
"""
print("=======================================")
word="acr"
word=sorted(word)
alternatives = ['car', 'girl', 'tofu', 'rca']	
for i in alternatives:
	if sorted(i) == word:
		print(i)
print("=======================================")
a=['1','2','3']
a=map(int,a)
print(a)
b=['1','2','3']
print("=======================================")
def rt(a=[]):
	a.append(1)
	print(a)

rt()
rt()
rt()
rt()
print("=======================================")
d={}
print(d['red'] if 'red' in d else 'None===========' )
d={'red':1}
#OR
d.get('red',"None===========")
print(d['red'] if 'red' in d else 'None===========' )
d.get('red',"None===========")
#print(help(d.get)
colors = ['red','red','red','red','green','blue','blue']
#Best way to count objects in a list
for i in colors:
	d[i]=d.get(i,0)+1
print(d)
print("=======================================")
def rs(a,b,c):
	print(a,b,c)

aa=[1,2,3]
rs(*aa)
print("=======================================")
st='str'  'ing'             #  <-  This is ok
print(st) ##This prints string
print("=======================================")
T2=[(i,j) for i in range(3) for j in range(i) ]
print(T2)

arr=["harry","sally","tom"]
for i in range(len(arr)):
	print(arr[i %len(arr)] * 3 )
	print(arr[(i+2) % len(arr)] * 2)
	print(arr[(i+1) % len(arr)] * 1)

mydict = {'carl':40, 'alan':2, 'bob':1, 'danny':3}

print(dict(sorted(mydict.items(),key = lambda x:x[1])))  ## to remember
my_dict = {'carl':40, 'alan':2, 'bob':1, 'danny':3}
my_dict=dict(zip(my_dict.values(),my_dict.keys()))
print(my_dict)
my_dict = {'carl':40, 'alan':2, 'bob':1, 'danny':3}
my_dict = dict([(v,k) for k,v in my_dict.items()])
print(my_dict)
my_dict = {'carl':40, 'alan':2, 'bob':1, 'danny':3}
mydict= {v:k for k,v in mydict.items()}
print(my_dict)  #dictionary comprehension
print({(v,k) for k,v in mydict.items()}) #use : for dictionary else it would be a set
#set([(1, 'bob'), (40, 'carl'), (2, 'alan'), (3, 'danny')])
print("=======================================")
def binary_search(a, x, lo=0, hi=None):
	if hi is None:
		hi = len(a)
	while lo < hi:
		print("lo %d"%(lo))
		print("hi %d"%(hi))
		mid = (lo+hi)//2
		print("mid %d"%(mid))
		midval = a[mid]
		print("midval %d"%(midval))
		if midval < x:
			lo = mid+1
			print("lo %d"%(lo))
		elif midval > x: 
			hi = mid
			print("hi %d"%(hi))
		else:
			return mid
	return -1
a=[1,2,3,4,5,6,7,8,9]
mid = binary_search(a,7) 
print(mid)
print("=======================================")
#A dict cannot have list or dict as keys but it can have tuple since tuple cannot be chnages and is a read only datastructure
a=(1,2)
b={a:2}
print(b)
#{(1, 2): 2}
print(b[(1,2)]) # will give 2
print("=======================================")
class a:
	def __init__(self):
		self.l=None
		print(self.l)
		if self.l  :  #since self.l is None the print(steatement is not printed
			print("exist" )
 

print("=======================================")
def fib():
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b

a = fib()	
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print("==========")
def fibn(n):
	a,b=0,1
	while b<n:
		yield a
		a,b=b,a+b
i = fibn(20)	
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print("=======================================")
def palindrome(word):
	return word == word[::-1]

print(palindrome("tat"))
print(palindrome("t"))
print(palindrome("ti"))
print("=======================================")
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
print(s.next())
print(s.next())
#print(s.next() ## this will call StopIteration
print("=======================================")
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
	print(animal.name + ': ' + animal.talk())

print("=======================================")
class a:
	pass

x=a()
x.a =1
print(x.__dict__)
print("=======================================")
# class can also be created with metaclasses read about this..
print("=======================================")
art = ["a","b","c","d","e"]
a = datetime.datetime.now()
for i in reversed(art):
	print(i)
b = datetime.datetime.now()
c=b-a
print(c.seconds,"1st")
print(c.microseconds,"1st")
a = datetime.datetime.now()
for i in art[::-1]:
	print(i)
b = datetime.datetime.now()
c=b-a
print(c.seconds,"2nd")
print(c.microseconds,"2nd")

print("=======================================")
colors = ["red","yellow","blue","green"] 
for i in sorted(colors):
	print(i)
for i in sorted(colors,reverse=True): #This sorts the list in reverse alphabetical order
	print(i)
for i in reversed(colors): ##This sorts the list in reverse order
	print(i)



a={'b':1}
del a['b']
print(a) ##If u delete a value by its key it will delete the key also

def rt(ty):
	print(ty)

rt(ty=1) #you can call the function withc exact same function definition attributes.This is just for readability purpose.Changing the parameter will result in an error

a,b,c,d=colors #unpacking an array into different variable
print(a,b,c,d)
print("=======================================")
try:
    a={'b':1}
    for i in a:
        del a[i] #RuntimeError: dictionary changed size during iteration
except:
    logging.exception("Error while iterating dictionary")
print("=======================================")
#overloading is not supported in python
def at(r):
  print(r)
  print("Inm 1")

def at(r,t):
  print("Inm 2")
  print(r,t)

try:
	at(1)
except:
	logging.exception("exception")
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: a() takes exactly 2 arguments (1 given)
print("=======================================")
#oneliner to read a file
os.system("echo 'hello world' > ./ten_one_liners.py")
print(open("ten_one_liners.py").readlines())

print("=======================================")
#Difference between is and "=="
#is will return True if two variables point to the same object, == if the objects referred to by the variables are equal.
print("=======================================")
#using eval

#The eval function lets a python program run python code within itself.

#eval example (interactive shell):
x = 1
eval('x + 1')
#2
eval('x')
#1
print("=======================================")
try:
    open("/tmp/s.txt")
    #pass
    #for i in range(10):
    #   break
except: #There can be more than one except
    print("Exception")
else:   #else part will be executed if no exceptions are raised
    print("In else")
finally: #finally will be executed irrespective of conditions
    print("In final")

try:
    pass
except:
    print("Exception")
finally: #finally will be executed irrespective of conditions
    print("In final")

#Python for else:
for i in range(1,11):
    print(i)
    break
else:
    print("In else1") #else will be executed only when there is no break
print("=======================================")
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

print("=======================================")
#Important chnaging one character in a given string
string="yelloworld"
print(string)
string=list(string)
string[0]='h'
string1="".join(string)
print(string1)

string="yelloworld"
di={string:'123'}
print(di)
string=list(string)
string[0]='h'
string="".join(string)
print(string)
print(di)
#Note: Even though the string chnaged dictionary remain unchanged
#How to change a dictionary key 

di["helloworld"] = di.pop("yelloworld")
print(di)

#               OR

string="yelloworld"
di={string:'123'}
di["helloworld"]=di["yelloworld"]
print(di)
del di["yelloworld"]
print(di)

print("=======================================")
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
Why isn't RAM as fast as registers/cache memory?
Registers and cache are on the cpu chip itself, or tied to it very closely. Normal RAM is accessed through an address bus, and it often subject to a level of indirection by memory mapping
The hierarchy is:

    Internal registers. ( ~ 1 clock cycle. So if it's a 3GHz CPU, that's 0.3ns)
    Cache ( a few clock cycles. So usually the order of 1-5ns)
    RAM (This depends entirely on how fast the RAM is, but can be in the order of few hundred ns.
    Secondary storage. (Even if it's an SSD, this still ranges to the ms order).
"""
"""
what is the difference between div and span
There are lots of block elements (linebreaks before and after) defined in HTML, and lots of inline tags (no linebreaks)
***important: https://stackoverflow.com/questions/183532/what-is-the-difference-between-html-tags-div-and-span *****
    div is a block element
    span is an inline element.
<div> this is a div </div>
<div> this is a div </div>
<div> this is a div </div>

Output:
this is a div
this is a div
this is a div
<span> this is a span </span>
<span> this is a span </span>
<span> this is a span </span>
Output: this is a span this is a span this is a span
This means that to use them semantically, divs should be used to wrap sections of a document, while spans should be used to wrap small portions of text, images, etc.

*****For example: As in html 4******

<div>This a large main division, with <span>a small bit</span> of spanned text!</div>

Note that it is illegal to place a block level element within an inline element, so:

<div>Some <span>text that <div>I want</div> to mark</span> up</div>

...is illegal.
"""

"""
Object:

This is the basic unit of object oriented programming. That is both data and function that operate on data are bundled as a unit called as object.
Class:

When you define a class, you define a blueprint(for an object. This doesn't actually define any data, but it does define what the class name means, that is, what an object of the class will consist of and what operations can be performed on such an object.
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
        print("m"


x=C()
x.m()
print(dir(x))
print(vars(x))
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
    print(huh)
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
print((not(x < 15 and y >= 3))
print((x >= 15 or y < 3)
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
>>> print(f(8))
64
>>> 
>>> g = lambda x: x**2
>>> 
>>> print(g(8))
64

As you can see, f() and g() do exactly the same and can be used in the same ways. Note that the lambda definition does not include a "return" statement -- it always contains an expression which is returned. Also note that you can put a lambda definition anywhere a function is expected, and you don't have to assign it to a variable at all. 


>>> def make_incrementor (n): return lambda x: x + n
>>> 
>>> f = make_incrementor(2)
>>> g = make_incrementor(6)
>>> 
>>> print(f(42), g(42))
44 48
>>> 
>>> print(make_incrementor(22)(33)
55

The above is equivalent to 

>>> def make_incrementor (n):
...     def x1(x):
...             return n+x
...     return x1

>>> foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
>>> 
print(filter(lambda x: x % 3 == 0, foo) #[18, 9, 24, 12, 27]
#Construct a list from those elements of iterable for which function returns true. iterable may be either a sequence, a container which supports iteration, or an iterator. If iterable is a string or a tuple, the result also has that type; otherwise it is always a list.filter(function, iterable) is equivalent to [item for item in iterable if function(item)]

>>> print(map(lambda x: x * 2 + 10, foo)
[14, 46, 28, 54, 44, 58, 26, 34, 64]
>>> 
>>> print(reduce(lambda x, y: x + y, foo) #reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)
139
The above reduce is equal to 
print(sum(foo)#139
First we define a simple list of integer values, then we use the standard functions filter(), map() and reduce() to do various things with that list. All of the three functions expect two arguments: A function and a list. 

Of course, we could define a separate function somewhere else and then use that function's name as an argument to filter() etc., and in fact that's probably a good idea if we're going to use that function several times, or if the function is too complex for writing in a single line. However, if we need it only once and it's quite simple (i.e. it contains just one expression, like in the above examples), it's more convenient to use a lambda construct to generate a (temporary) anonymous function and pass it to filter() immediately. This creates very compact, yet readable code. 
Note:Cannot use assignment in lamda functions i.e, ex:lambda x:x=1
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
        print("f()")

Then, if we run the monkey-patch testing like this:

>>> import m
>>> def monkey_f(self):
	print("monkey_f()")

	
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
...     print(length
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
...     print(length
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
print(next(gn)) #after printing 1, 1 is discarded from memory
print(next(gn)) #after printing 2, 2 is discarded from memory
print(next(gn)) #after printing 3, 3 is discarded from memory
"""
From above,Thats why generator are more efficient,where as in iterator after returning 1 ,1 is still retained in memory , we may have to use del() explicitly to remove it from memory,but also some times the object have circular references and therefore may need to delete all the objects associated with it which is more complicated and errorsum. So generator is ususally preferred over an iterator most of the times
"""



"""
>>> a=[]
>>> for i in a:
...     print("inside")
... else:
...     print("in else")
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
print("======Normal copy=============")
print(c)

#Using normal assignment operatings to copy:
d=c
print(d)
d[0][1]="a"
print(c) #"a"is found in both c and d
print(d) #"a"is found in both c and d
print(id(c) == id(d))  #True ,both have same ids
print(id(c[0]) == id(d[0])) #True ,Elements are also same

#using a shallow copy
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
print("======Shallow copy=============")
print(c)
d = copy.copy(c)
print(id(c) == id(d))  #False ,both have different ids
print(id(c[0]) == id(d[0])) #True ,Elements are also same
d[0][1]="a"
print(c) #"a"is found in both c and d
print(d) #"a"is found in both c and d

#using a shallow copy
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
print("======Deep copy=============")
print(c)
d = copy.deepcopy(c)
print(id(c) == id(d))  #False ,both have different ids
print(id(c[0]) == id(d[0])) #False ,Elements are also same
d[0][1]="a"
print(c) #"a"is found in d only
print(d) #"a"is found in d only

print("======shallow dict copy=============")
c={'a':1}
d=copy.copy(c)
d.update({'b':2})
print(c,d)
c.update({'c':3})
print(c,d)
print("======deep dict copy=============")
c={'a':1}
d=copy.deepcopy(c)
d.update({'a':2})
print(c,d)
c.update({'c':3})
print(c,d)
print("==========================================")
d={"a":1,"b":2,"c":3}
print(zip(*d.items())) #To separate keys and values, 
#[('a', 'c', 'b'), (1, 3, 2)]
print(zip(d.items())) #if "* is omitted the output is as follows"
#[(('a', 1),), (('c', 3),), (('b', 2),)]

a, b, c = 1, 2, 3
print(a, b, c)
#(1, 2, 3)
a, b, c = [1, 2, 3]
print(a, b, c)
#(1, 2, 3)
a, (b, c), d = [1, (2, 3), 4]
print(a)
#1
print(b)
#2
print(c)
#3
print(d)
#4

#Negative indexing

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[-1])
#10
print(a[-3])
#8

#List slices with step (a[start:end:step])

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[::2])
#[0, 2, 4, 6, 8, 10]
print(a[::3])
#[0, 3, 6, 9]
print(a[2:8:2])
#[2, 4, 6]


a = [1, 2, 3, 4, 5, 6]

# Using iterators
group_adjacent = lambda a, k: zip(*([iter(a)] * k))
print(group_adjacent(a, 3))
#[(1, 2, 3), (4, 5, 6)]
print(group_adjacent(a, 2))
#[(1, 2), (3, 4), (5, 6)]
print(group_adjacent(a, 1))
#[(1,), (2,), (3,), (4,), (5,), (6,)]


#[on_true] if [expression] else [on_false]
x, y = 50, 25
small = x if x < y else y
print(small)

print("==========")
#Boolean as indexes
b = 1==1
name = "I am %s" % ["John","Doe"][b]
print(name)

print("==========")
#In python false is treated as 0 and True is treated as 1
a=1
print((a==1) + (a>0) + (a==2))
#2
print("==========")
a = ['two', 'three', 'four']
for i, word in enumerate(a, 2):
  print(i, word)

#2 two
#3 three
#4 four

print("====List comprehension if else======")
a=1
b=2
print([ a if a== 1 else  b])
print("==========")
n=1
if n < 0:
    result = 'n is negative'
else:
    result = 'n is positive'
#Or in short this can be written as ,
result = n < 0 and 'n is negative' or 'n is positive'
print(result)
print("==========")
a=[1,2,3,4,5]
b=[6,7,8,9]
print(dict(zip(a,b)))
#{1: 6, 2: 7, 3: 8, 4: 9}
print("==========")
abc = 'mystring',
print(abc)
# ('mystring,) #abc is a tuple now ust because of the leading comma

print("==========")
def foo(a, b, c):
    print(a, b, c)

mydict = {'a':1, 'b':2, 'c':3}
mylist = [10, 20, 30]

foo(*mydict)
#a, b, c
foo(**mydict)
#1, 2, 3
foo(*mylist)
#10 20 30
print("==========")
#Python enums
class PlayerRanking:
  Bolt, Green, Johnson, Mom = range(4)

print(PlayerRanking.Mom)
#3
print("==========")
#Inline if statement
print("Hello" if True else "World")
#Hello
print("==========")
#List comprehension
numbers = [1,2,3,4,5,6]
even = [number for number in numbers if number%2 == 0]
print("==========")
#This is more of a fun one than a useful technique. In python True and False are basically just global variables. Thus:
print(False == True)
#False
"""
The following cannot be done in python 3

False = True
if False:
    print("Hello")
else:
    print("World")
#Hello
"""
print("==========")
os.system("echo '{\"key\":\"value\"}' | python -m json.tool")
print("==========")
#Python simple calculator and writing lamda functions inside dictionary
calculator = {
'plus': lambda x, y: x + y,
'minus': lambda x, y: x - y
}
print(calculator['minus'](9,3))
#6
print("==========")
#Context Managers!
with open("ten_one_liners.py") as f:
   print(f.readlines())

#It will automatically close the file on exit, this can be used for creating resources which are automatically cleaned up after exiting scope.

print("==========")
#Implementing a switch-case statement:
def f(x):    
    return {
        'foo': 1,
        'bar': 2,        
    }.get(x, 3) #.get is like the default,##very important

print(f('gg'))
print(f('foo'))
print("==========")
#Default value
text = ''
option = text or 'empty'
print(option)
#'empty'
print("==========")
#Ternary Expressions

y = 1
x = 10 if (y == 1) else 20
print(x)
#10
y = 2
x = 10 if (y == 1) else 20
print(x)
#20
print("==========")
p = lambda k : {"a":1,"b":2}.get(k,"Default")
p("a")
#1
p("b")
#2
p("bb")
#'Default'
print("==========")
#creating a class on the fly using type
#using type to create classes
#type takes three arguments 
#1.Name of the new class
#2.parent class in tuple format if any
#3. class functions in dict format as shown

def t(self,a):
	print(a)


class A(object):
	def __init__(self):
		print("In A")

B= type("B",(A,),{"t1":t})
b=B()
b.t1(11)
C= type("C",(object,),{"t2":t})
c=C()
c.t2(12)
#print("=========="
#As to why the dict.update function is used beacuse u can update more than one variable at the same time. As oppose to a['aa'] where only one value can be updated at one time
#print("=========="
#Get common elements from 3 lists
a = [1,2,3,4]
b = [2,3,4,5]
c = [3,4,5,6]
print(set(a) & set(b) & set(c))
#{3, 4}
# or 
out = [x for x in a if x in b and x in c] # Depending on the length of the lists, a very expensive solution
print(out)

print("=================================================")
if "" : print("A",)
if[[]]:print("B",)
if None: print("C",)
if ():print("D",)
if " ":print("E",)
if 9%9:print("F",)

print("The above print(B E")

print("=================================================")
def myfunc():
	"""The purpose of myfunc is to prepare scambled eggs with spam"""
	eggs=2
	spam = 'spam' * 10
	breakfast = "eggs" * eggs + spam


print(myfunc.__doc__)

print("==============================")
import timeit
#s =timeit.timeit()
s = {s for s in range(10000)} #This is set comprehension
x = [x for x in range(10000)] 
d=[{i:i} for i in x]
print(s)
print(type(s))
print(timeit.timeit('print(x[9999])', setup='from __main__ import x',number=1))
print(timeit.timeit('print(d[9999])', setup='from __main__ import d',number=1))
print(tuple(i for i in (1, 2, 3)))

for i in [(1,2,3)]:
	print(i)

dct= {'spam' : 'eggs',1:2,(1,2):(3,4)}
print(dir(dct))

print(dct['spam'])
print("==============================")
#What are containers in python


#Containers are any object that holds an arbitrary number of other objects. Generally, containers provide a way to access the contained objects and to iterate over them.

#Examples of containers include tuple, list, set, dict; these are the built-in containers. More container types are available in the collections module
# A Container is a class that implements the __contains__ method.

print("==============================")
#Singleton class: is a design pattern in which only one instance of the object may be created.One of something.Ex: One phonebook
class MySingleTon(object):
	_instance = None
	def __new__(self):
		if not self._instance:
			self._instance = super(MySingleTon,self).__new__(self)
			self.y= 10
		return self._instance

x=MySingleTon()
print(x.y)
x.y=20
z=MySingleTon()
print(z.y)
#The above can be done using a decorator also
print("==============================")
#classdecorator: lets you call a class function without creating the object of the class

class MyClass:
	@classmethod
	def printHam(self):
		print("HAM")

MyClass.printHam()
print("==============================")
#Factory: is a design pattern in which you let a function determine which class to create

BaseClass = type("BaseClass",(object,),{})
C1 = type("C1",(BaseClass,),{"x":1})
C2 = type("C2",(BaseClass,),{"x":30})

def MyFactory(myBool=None):
	return C1() if myBool else C2()

m = MyFactory(True)
v = MyFactory()
print(m.x,v.x)
#Factory allows stuff to be created on the fly and not have programmer  harcode everything
#In this example if there are 100 subclasses if loop will be nested over and over again which is very confusing and difficlut to maintain so we can refactor the above solution like the following:
print("==============================")
BaseClass = type("BaseClass",(object,),{})

@classmethod
def Check1(self,myStr):
	return myStr == "ham"

@classmethod
def Check2(self,myStr):
	return myStr == "sandwich"

@classmethod
def Check3(self,myStr):
	return myStr == "wich"


C1 = type("C1",(BaseClass,),{"x":1,"Check":Check1})
C2 = type("C2",(BaseClass,),{"x":30,"Check":Check2})
C3 = type("C2",(BaseClass,),{"x":30,"Check":Check3})

#Important:::::::::::::::::::::::::::::::::::::::::::::::
def MyFactory(myStr):
	for cls in BaseClass.__subclasses__():
		if cls.Check(myStr):
			return cls()

m = MyFactory("ham")
v = MyFactory("sandwich")
print(m.x,v.x)
print("==============================")
"""
Abstract base class:cannot be instantiated
                    It can only be inherited from,
					May also be called as virtual class


"""
print("==============================")
def yu(**kwargs):
	for i,k in kwargs.items():
		print(i,k)

yu(x=13,y=7)

def yut(*args):
	for i in args:
		print(i)

try:
	#Important:::::::::::::::::::::::::::::::::::::::::::::::
	##This will cause an error as 14 is passed after the keyword arguments
	#yut(x=13,y=7,14) #This will cause an error as 14 is passed after the keyword arguments
	pass
except:
	print("In  exception")
print("==============================")
def outside():
	x=10
	def inr():
		print(x)
	return inr

o = outside()
o() #prints 10, because when inr is created it initializes all the local variables available with outside() fucntion
print("==============================")
def ph(self):
	print("In ph")

C1 = type("C1",(BaseClass,),{"x":1,"Check":Check1,"ph1":ph})
c = C1()
print(c.x) #=>equivalent to self.x
c.ph1() #=>equivalent to obj.ph1
print("==============================")
print("1".__class__)
print("1".__class__.__class__)
print("==============================")
"""
class tty(object): #object is a must else super will not be called
	def __init__(self):
		self.health =10
		return self.health

class bs(tty):
	def __init__(self):
		super(tty,self).__init__()

iu= bs()
print(dir(iu)
print(iu.health
"""
print("===================================")
"""
Tuples:a mechanism for grouping and organizing data to make it easier to use ex:(a_born,1981)

Tuples are used for grouping data

"""
print("===================================")
"""
Important default dict
"""
from collections import defaultdict

#counting
s = 'mississippi'
d = defaultdict(int)
for k in s:
	d[k] += 1

print(d)
#defaultdict(<type 'int'>, {'i': 4, 'p': 2, 's': 4, 'm': 1})
print(d.items())
#[('i', 4), ('p', 2), ('s', 4), ('m', 1)]


s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
	d[k].append(v)

print(d)
#defaultdict(<type 'list'>, {'blue': [2, 4], 'red': [1], 'yellow': [1, 3]})
print(d.items())
#[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]


somedict = {}
try:
	print(somedict[3]) # KeyError
except  Exception as e:
	print(e)
	
someddict = defaultdict(int)
print(someddict[3])


ice_cream = defaultdict(lambda: 'Vanilla')
ice_cream['Sarah'] = 'Chunky Monkey'
ice_cream['Abdul'] = 'Butter Pecan'
print(ice_cream['Sarah'])
#Chunky Monkey
print(ice_cream['Joe'])
#Vanilla
print("=========================================")
"""
Important: While chaining decorators only the top __Call__ is executed
Also in function decorators deco3 has access to deco2 inner function and deco2 has control over deco1 
"""
class deco3(object):
	def __init__(self,u):
		self.u = u
	def __call__(self):
		print("====3")
		print(self.u.f.g.__name__)
		self.u.f.g()
		print("====")


class deco2(object):
	def __init__(self,f):
		self.f = f
	def __call__(self):
		print("====2")
		print(self.f.g.__name__)
		print("====")

class deco1(object):
	def __init__(self,g):
		self.g = g
	def __call__(self):
		print("====1")
		print(self.g.__name__)
		print("====")

@deco3
@deco2
@deco1
def tr():
	print("In tr")

tr()
print("==========================================================")
def deco3(u):
	def ss():
		print("1")
		u()
	return ss 

def deco2(y):
	def yy():
		print("2")
		print(y.__name__)
		y()
	return yy 

def deco1(f):
	def tt():
		print("3")
		print(f.__name__)
		f()
	return tt
	
@deco3	
@deco2
@deco1
def tr():
	print("In tr")

tr()
print("==========================================================")
#In a function decorator there should always be a return type and ususally the inner it is the inner function like "return rt" and "return rt()" will not work but if it is not a generator then calling only "rt" will not work it should be like "rt()" properly as in the below example
print("==========================================================")
def tt():
	def rt():	
		print("inside")
	#rt #only writing rt insted of rt() will not call the rt function unlike the decorator
	rt()

tt()
print("==========================================================")
a=[1]
b=['1']
print(a+b)
#[1, '1']
a=[1]
b=[2]
print(a+b)
#[1, 2]
a=(1)
b=(2)
print(a+b)
#3
a=(1,2)
b=(3,4)
print(a+b)
#(1, 2, 3, 4)
s="Hello worl. example again"
s.replace("worl","world")
#'Hello world. example again'
print(s)
#'Hello worl. example again'
s=s.replace("worl","world")
print(s)
#'Hello world. example again'
a=(1,)
print(type(a))
#<type 'tuple'>
b=(2,)
print(a+b)
#(1, 2)
a=((1))
print(type(a))
#<type 'int'>
b=((2))
print(a+b)
#3
a=(((1)))
b=(((2)))
print(a+b)
#3
print("==========================================================")
x = [1, 2, 3]
x.append([4, 5])
print((x))

#gives you: [1, 2, 3, [4, 5]]

x = [1, 2, 3]
x.extend([4, 5])
print((x))

#gives you: [1, 2, 3, 4, 5]
print("==========================================================")
s="a","b",[1,2,3,4],5
print(type(s)) #prints tuple
s=1,2,
print(type(s)) #prints tuple
s={1:'a'}
print(s)
print("==========================================================")
a="abc"
b="def"
print([i+j for i in a for j  in b]) #print(all combinations from both the list
#['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
print("==========================================================")
a=['']
for i in a:
	print(i) #prints ''
	print("inside")  #prints inside

print('' is None) #prints False
print('' == None) #prints False
print("==========================================================")
print([1,2,3,4][1])
#2
print("==========================================================")
def t():
   a=0
   while True:
      a+=1
      if a%2==0:
         yield a
         if a ==10:
            break

for i in t():
   print(i)
#this example is to show that next(i) or i.next() is not mandatory.The advantage with the above is you dont have to take care of the stopiteration condition
#It is only mandatory when as below example,Here if you do not know the number of elements you need to take care of StopIteration condition

i=t()
next(i)
next(i)
next(i)
next(i)
next(i)
try:
	next(i)
except Exception as e:
	print("In exception",e)
print("==========================================================")
class aa:
   a=11
   @classmethod
   def t(classname):
      return classname.a
   @staticmethod
   def foo():
      return aa.a

print(aa.t())
print(aa.foo())
print("==========================================================")
print(list(enumerate(["a", "b", "c"])))
#[(0, "a"), (1, "b"), (2, "c")]
for i, c in enumerate(["a", "b", "c"]):
    print(i, c)

#0 a
#1 b
#2 c
print("==========================================================")
#convert string to variable
a=['a','b','c','d']
for i in a:
    exec("%s = %d" % (i,2))
    print(i)

#a
#b
#c
#d
print(a,b,c,d)
#2 2 2 2

print("==========================================================")
"""
xrange is not a generator but it evaluates lazily and acts like a generator.  
explain what "evaluates lazily" means?
"evaluates lazily" means that each i is evaluated on demand rather than on initialization.
http://stackoverflow.com/questions/94935/what-is-the-difference-between-range-and-xrange-functions-in-python-2-x
"""
print("==========================================================")
x=[1,2,3]
y=[4,5,6]
zipped = zip(x,y)
print(zipped)
[(1, 4), (2, 5), (3, 6)]
x2,y2 = zip(*zipped)
#[(1, 2, 3), (4, 5, 6)]
print(x == list(x2) and y == list(y2))
print("==========================================================")
sentinel = object()

def foo(self, value=sentinel):
	if value is not sentinel:
		print("you passed something else")

sentinel = []
sentinel = {}

foo(1)
""" 
http://stackoverflow.com/questions/13287887/using-none-as-parameter-to-keyword-argument
"""
print("==========================================================")
print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
if None:
    print("insideeee")
else:
    print("in elseeeee")


if {}:
    print("In iffffff")
else:
    print("in elseeeee")
print("==========================================================")
#Python lstrip() and rstrip()
a = '        hello world!    '
print(a)
#' \t hello world!\t '
print(a.lstrip(' '))
print(repr(a.lstrip(' ')))
#'\t hello world!\t '
print(a.lstrip())
#'hello world!\t '
print(a.rstrip(' '))
#' \t hello world!\t'
print(a.rstrip())
#' \t hello world!'
print(a.strip())
#hello world!
print("==========================================================")
"""
Context managers are the statment which uses with ex:
with open('a.txt') as f:  #This line will make sure that the file will be closed after the operation and even if there is an exception the outer exception will catch it and close the file before inner exception takes place
	//do something
"""
print("==========================================================")
a = set()

#Use add to append single values

a.add(1)
a.add(2)

#Use update to append iterable values

a.update([3,4])

#Check your collection

print(a)
#Out[*n*]: {1, 2, 3, 4}
print(a.add.__doc__)
#'Add an element to a set.\n\nThis has no effect if the element is already present.'
print("==========================================================")
#Named tuple
#What is namedtuple ?

#As the name suggests, namedtuple is a tuple with name. In standard tuple, we access the elements using the index, whereas namedtuple allows user to define name for elements. This is very handy especially processing csv (comma separated value) files and working with complex and large dataset, where the code becomes messy with the use of indices (not so pythonic).
a=(1,'tom',2)
b=[1,'tom',2]
print("%s serial number name is %s and leaves at house # %s "%a) #Note that the actual datatype %d or %s can be used here
print("%d serial number name is %s and leaves at house # %d "%a) #Note that the actual datatype or %s can be used here
#We cannot use list to do the same
#print("%d serial number name is %s and leaves at house # %d "%b #This gives an error , 
#Instead of accessing a tuple by indexes 
from collections import namedtuple
Emp = namedtuple('Emp', 'id batch empno')
t1= Emp(1,2,3)
print(t1.id)
print(t1.batch)
print(t1.empno)
print("==========================================================")
def rt(a,l=[]):
	l.append(a)
	return l

print(rt(10)) # [10]
print(rt(20,[])) # [20]
print(rt(30)) # [10, 30]
print(rt(40,["a","b","c"])) # [10, 30]
print("==========================================================")
#Best way to count the number of words in a file
print("==========================================================")
l=[1,2,3,None,{},(),[]]
print(len(l))
#7
print("==========================================================")
import collections

l=[1,2,3,4,5,6,1,2]
print(collections.Counter(l))
#Counter({1: 2, 2: 2, 3: 1, 4: 1, 5: 1, 6: 1})
print("==========================================================")
def count(a,*l):
	print(a,l)

a=[1,2,3,4,5]
count(*l) #This is variable list argument
#1 (2, 3, 4, 5, 6, 1, 2)
print("==========================================================")
#Python parallel vs concurrent programming
print("==========================================================")
#To count the number of words in a file
print("++++++++++++++++++++++++++++++++++")
os.system("echo 'this is a test file used for testing and  this file file is only for testing' > /tmp/a.txt")
with open('/tmp/a.txt') as f:
	di.update({ w : (di[w]+1 if w in di else 1)  for l in f for w in l.split(' ')})
print(di)
print("++++++++++++++++++++++++++++++++++")
#print(di	
#In python we cant refer to the current object i.e, dictionary in this case
	
#No you cant, 99% of the python is about runtime. It will define the objects in runtime, and until the end of your operations python doesn't create the di

from collections import Counter
counter = Counter()
with open('test_readme.txt') as f:
	for line in f:
		counter += Counter(line.split())
print(counter)
print(dict(counter))
print("==========================================================")
"""map(function, iterable, ...)
Return an iterator that applies function to every item of iterable, yielding the results. If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is exhausted.
"""
"""
The below works only on a python interpreter
import sys
sys.ps1
'>>> '
print(sys.ps2
'... '
print(sys.ps3
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'ps3'
sys.ps1= '+++'
#console.changes to '+++'
"""
"""
***
def Execute at Runtime
***
"""
print("==========================================================")
#The following shows the number of cpu present on the system
import multiprocessing as m
print(m.cpu_count())
print("==========================================================")
#******* VERY IMPORTANT READ REFER GIL.txt
print("==========================================================")
#https://kovshenin.com/2010/pickle-vs-json-which-is-faster/
#JSON is faster as per the above link
print("==========================================================")
class Candidate(object):
   def __init__(self, name):
      self.name = name

obj = Candidate('Python')
print(obj.__dict__)
obj.__dict__['email'] = 'in@python.org'
print(obj.__dict__)
print("==========================================================")
output = 1<< 10 #Left shift operator
print(output) #output is 1024

#os.tempnam(dir, prefix) .Creates a  temporary file in the given directory with the file prefixed with the prefix name.see example below
#os.tempnam('/tmp/tutorialsdir','tuts1')

#/tmp/tutorialsdir/tuts1IbAco8

print("==========================================================")
#num = int(input("Enter a number: "))
num = 407

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")
print("==========================================================")
print(r"\nwoow")
"""
the text exactly like this: r"\nwoow"
When prefixed with the letter 'r' or 'R' a string literal becomes a raw string and the escape sequences such as \n are not converted.
"""

print("\x48\x49!")
"""
HI!
description:
\\x is an escape sequence that means the following 2 digits are a hexadicmal number encoding a character.
"""

print("hello" 'world')
#helloworld
class Person:
	def __init__(self, id):
		self.id = id
p =Person(1)
print(p.__dict__)
#{'id': 1}
p.__dict__['age']=2
print(p.__dict__)
#{'age': 2, 'id': 1}
"""
What does the code below do?

sys.path.append('/root/mods')

    Adds a new directory to seach for python modules that are imported - correct
rocesses are searched for after they are launched

description:
The list sys.path contains, in order, all the directories to be searched when trying to load a module

"""

"""
Question #45: What gets printed?

confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1.0] = 4

sum = 0
for k in confusion:
    sum += confusion[k]

print(sum

    6 - correct

description:
Note from python docs: "if two numbers compare equal (such as 1 and 1.0) then they can be used interchangeably to index the same dictionary entry. (Note however, that since computers store floating-point numbers as approximations it is usually unwise to use them as dictionary keys.)"
"""


"""
Question #50: What gets printed?

names = ['Amir', 'Barry', 'Chales', 'Dao']
print(names[-1][-1]

    o - correct

description:
-1 refers to the last position in a list or the last character in a string. In this case, we are referencing the last character in the last string in the list.
"""
"""
Question #61: What gets printed in the below?
"""
def print_header(str):
    print("+++%s+++" % str)


print_header.category = 1
print_header.text = "some info"

print_header("%d %s" %(print_header.category, print_header.text))

#    +++1 some info+++ - correct

#description:
#As of python 2.1 you could assign arbitrary typed information to functions.


"""
class NumFactory:
    def __init__(self, n):
        self.val = n
    def timesTwo(self):
        self.val *= 2
    def plusTwo(self):
        self.val += 2

f = NumFactory(2)
for m in dir(f):
    mthd = getattr(f,m)
    if callable(mthd):
        mthd()

print(f.val

    An exception is thrown - correct

description:
An exception will be thrown when trying to call the __init__ method of the object without any parameters: TypeError: __init__() takes exactly 2 arguments (1 given)
"""


"""
Question #75: What gets printed?

kvps = { '1' : 1, '2' : 2 }
theCopy = kvps.copy()

kvps['1'] = 5

sum = kvps['1'] + theCopy['1']
print(sum

    1
    2
    6 - correct
    10
    An exception is thrown

description:
The copy method of the dictionary will make a new (shallow) copy of the dictionary so a change to the original in this case does not change the copy.
Question #76: What gets printed

aList = [1,2]
bList = [3,4]

kvps = { '1' : aList, '2' : bList }
theCopy = kvps.copy()

kvps['1'][0] = 5

sum = kvps['1'][0] + theCopy['1'][0]
print(sum

    10 - correct
    An exception is thrown

description:
The copy method provides a shallow copy therefore the list being held as the value inside the dictionary is the same list in the copy as the original.
Question #77: What gets printed?

import copy

aList = [1,2]
bList = [3,4]

kvps = { '1' : aList, '2' : bList }
theCopy = copy.deepcopy(kvps)

kvps['1'][0] = 5

sum = kvps['1'][0] + theCopy['1'][0]
print(sum

    6 - correct

description:
A deep copy will copy all the keys and values inside a dictionary. Therefore the list inside the dictionary are different in the first and second dictionaries of this example.
Question #78: What gets printed?

kvps = { '1' : 1, '2' : 2 }
theCopy = dict(kvps)

kvps['1'] = 5

sum = kvps['1'] + theCopy['1']
print(sum

    6 - correct

description:
Creating a new dictionary object initialized from the first does a 'shallow copy'
"""
print("==========================================================")
print([2,3,4]*3)
#[2, 3, 4, 2, 3, 4, 2, 3, 4]
print("==========================================================")
def rt(a,b,c=set()):
	print(a,b,c)
	if len(c)>0:
		print("hi")

rt(1,2,(1,3))
rt(1,2)
print("==========================================================")
"""
>>> x=1,
>>> x
(1,)
>>> type(x)
<type 'tuple'>
>>> x=1
>>> x
1
>>> type(x)
<type 'int'>
"""
print("==========================================================")
"""
>>> 1
1
>>> _+2
3
"""

print("==========================================================")
"""
>>> Jan = Mar = May = range(1, 32)
>>> Jan
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
>>> Mar
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
>>> May
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
"""
print("==========================================================")
def bool_to_str(value):
	"""value should be a bool"""
	if value: #This is just to avoid None condition
		print("12345")
		print(value)
		return ['No', 'Yes'][value]

print(bool_to_str(True)) #Prints Yes
print(bool_to_str(False)) #Prints No
print(bool_to_str(None)) #Prints None
#False is 0 and True is 1
print("==========================================================")
"""
The assert statement exists in almost every programming language. When you do...

assert condition
************************##very important******************
... you're telling the program to test that condition, and trigger an error if the condition is false.
******************************************

In Python, it's roughly equivalent to this:

if not condition:
    raise AssertionError()

Try it in the Python shell:

>>> assert True
>>> assert False
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError

"""
print("==========================================================")
"""
How is memory managed in python?
- Memory management in Python involves a private heap containing all Python objects and data structures. Interpreter takes care of Python heap and that the programmer has no access to it.
- The allocation of heap space for Python objects is done by Python memory manager. The core API of Python provides some tools for the programmer to code reliable and more robust program.
- Python also has a build-in garbage collector which recycles all the unused memory. When an object is no longer referenced by the program, the heap space it occupies can be freed. The garbage collector determines objects which are no longer referenced by the sprogram frees the occupied memory and make it available to the heap space.
- The gc module defines functions to enable /disable garbage collector:
gc.enable() -Enables automatic garbage collection.
gc.disable() - Disables automatic garbage collection.
"""
print("==========================================================")
"""
********##very important************
Difference between _, __ and __xx__ in Python

One underline in the beginning

Python doesn't have real private methods in classes and modules, so one underline in the beginning of a method or attribute means you shouldn't access this method, because it's not part of the API. It's very common when using properties:

Two underlines in the beginning


This one causes a lot of confusion. It should not be used to mark a method as private, the goal here is to avoid your method to be overridden by a subclass. Let's see an example:


class A(object):
    def __method(self):
        print("I'm a method in A")



	def method(self):
		self.__method()



a = A()
a.method()



The output here is


$ python example.py 
I'm a method in A



Fine, as we expected. Now let's subclass A and customize __method


class B(A):
    def __method(self):
        print("I'm a method in B")



b = B()
b.method()



and now the output is...


$ python example.py
I'm a method in A



as you can see, A.method() didn't call B.__method() as we could expect. Actually this is the correct behavior for __. So when you create a method starting with __ you're saying that you don't want anybody to override it, it will be accessible just from inside the own class.


How python does it? Simple, it just renames the method. Take a look:


a = A()
a._A__method()  # never use this!! please! #********************************



$ python example.py
I'm a method in A



If you try to access a.__method() it won't work either, as I said, __method is just accessible inside the class itself.


Two underlines in the beginning and in the end


When you see a method like __this__, the rule is simple: don't call it. Why? Because it means it's a method python calls, not you. Take a look:


>>> name = "igor"
>>> name.len()
4
>>> len(name)
4



>>> number = 10
>>> number.add(20)
30
>>> number + 20
30



There is always an operator or native function that calls these magic methods. The idea here is to give you the ability to override operators in your own classes. Sometimes it's just a hook python calls in specific situations. __init__(), for example, is called when the object is created so you can initialize it. __new__() is called to build the instance, and so on...


Here's an example:


class CrazyNumber(object):



def __init__(self, n):
    self.n = n

def __add__(self, other):
    return self.n - other

def __sub__(self, other):
    return self.n + other

def __str__(self):
    return str(self.n)



num = CrazyNumber(10)
print(num           # 10
print(num + 5       # 5
print(num - 20      # 30



Another example:


class Room(object):



def __init__(self):
    self.people = []

def add(self, person):
    self.people.append(person)

def __len__(self):
    return len(self.people)



room = Room()
room.add("Igor")
print(len(room)     # 1



The documentation covers all these special methods.


Conclusion


Use _one_underline to mark you methods as not part of the API. Use __two_underlines__ when you're creating objects to look like native python objects or you wan't to customize behavior in specific situations. And don't use __just_to_underlines, unless you really know what you're doing!
"""


print("==========================================================")
"""
FYI
In python 3 functions can be defined as >>> def foo((x1, y1: expression), (x2: expression, y2: expression)=(None, None)):

"""

print("==========================================================")

"""
In python 3 only functions can be defined as below ,but it is not mandatory but it is done because the user can call functions with proper type praameters http://stackoverflow.com/questions/39698290/python-3-x-what-is-annotation
 def g() -> str :
    ...
    return 'hello world'
-> is an annotation[https://www.python.org/dev/peps/pep-3107/], attached to the function return value. Annotations are optional, but you can use the syntax to attach arbitrary objects to a function. You can attach more annotations by using name : annotation on the parameters too.

In the sample you gave, it is being used to create a type hint. Type hinting is a new Python 3 extension. It is not mandatory, but using type hints can make development in an IDE like PyCharm easier, as well as enable static typechecking by tools like mypy.

See the typing module[https://docs.python.org/3/library/typing.html] for a set of objects to help create type hints, and the PEP 484 Type Hints proposal.

"""
print("==========================================================")
"""
what is lazy loading

Lazy loading is a design pattern commonly used in computer programming to defer initialization of an
object until the point at which it is needed.Lazy loading is a design pattern commonly used in
computer programming to defer initialization of an object until the point at which it is needed

"""
print("==========================================================")

"""
what is @property decorator

One simple use case will be to set a read only instance attribute , as you know leading a variable
name with one underscore _x in python usually mean it's private (internal use) but sometimes we want
to be able to read the instance attribute and not to write it so we can use property for this:

class C(object):
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

c = C(1)
print(c.x)
#1
c.x = 2
AttributeError        Traceback (most recent call last)
AttributeError: can't set attribute
"""
print("==========================================================")
"""
python 3 only

first, second, *tail, last = [1, 2, 3, 4, 5]
print(first)
# Out: 1
print(second)
# Out: 2
print(tail)
# Out: [3, 4]
print(last)
# Out: 5
first, second, *tail, last = [1, 2, 3, 4]
print(tail)
# Out: [3]

first, second, *tail, last = [1, 2, 3]
print(tail)
# Out: []
print(last)
# Out: 3
begin, *tail = "Hello"
print(begin)
# Out: 'H'
print(tail)
# Out: ['e', 'l', 'l', 'o']
*head, *tail = [1, 2]
# Out: SyntaxError: two starred expressions in assignment
{*range(4), 4, *(5, 6, 7)}
# Out: {0, 1, 2, 3, 4, 5, 6, 7}
iterable = [1, 2, 3, 4, 5]
print(iterable)
# Out: [1, 2, 3, 4, 5]
print(*iterable)
# Out: 1 2 3 4 5
tail = {'y': 2, 'z': 3}
{'x': 1, **tail}
 # Out: {'x': 1, 'y': 2, 'z': 3}
 dict1 = {'x': 1, 'y': 1}
 dict2 = {'y': 2, 'z': 3}
 {**dict1, **dict2}
 # Out: {'x': 1, 'y': 2, 'z': 3}

"""
print("==========================================================")
"""
Python 2
>>> True, False = False, True
>>> True
False
>>> False
True

Python 3
>>> True, False = False, True
  File "<stdin>", line 1
  SyntaxError: can't assign to keyword


  Python 2.x2.7

  print("Hello World")
  print()                        # print(a newline
  print("No newline",)           # add trailing comma to remove newline 
  print(>>sys.stderr, "Error")   # print(to stderr
  print("hello")                # print("hello", since ("hello") == "hello"
  print()                       # print(an empty tuple "()"
  print(1, 2, 3)                 # print(space-separated arguments: "1 2 3"
  print(1, 2, 3)                # print(tuple "(1, 2, 3)"

  In Python 3, print() is a function, with keyword arguments for common uses:
      Python 3.x3.0

      print("Hello World")              # SyntaxError
      print("Hello World")
      print()                          # print(a newline (must use parentheses)
      print("No newline", end="")      # end specifies what to append (defaults to newline)
      print("Error", file=sys.stderr)  # file specifies the output buffer
      print("Comma", "separated", "output", sep=",")  # sep specifies the separator
      print("A", "B", "C", sep="")     # null string for sep: prints as ABC
      print("Flush this", flush=True)  # flush the output buffer, added in Python 3.3
      print(1, 2, 3)                   # print(space-separated arguments: "1 2 3"
      print((1, 2, 3))                 # print(tuple "(1, 2, 3)"


      Leaked variables in list comprehension
      Python 2.x2.3

      x = 'hello world!'
      vowels = [x for x in 'AEIOU'] 

      print((vowels)
      # Out: ['A', 'E', 'I', 'O', 'U']
      print(x)
      # Out: 'U'   

      Python 3.x3.0

      x = 'hello world!'
      vowels = [x for x in 'AEIOU']

      print((vowels)
      # Out: ['A', 'E', 'I', 'O', 'U']
      print(x)
      # Out: 'hello world!'




"""
print("==========================================================")
#finding out which version of python
import sys
py2 = sys.version_info < (3,)
py3 =not py2
print(py3)
#False
print(py2)
#True
print("==========================================================")
"""
#veryvery important
Differnce between class and instance attributes , class variable vs instance variables

>>> class A: foo = []
>>> a, b = A(), A()
>>> a.foo.append(5)
>>> b.foo
[5]
>>> class A:
...  def __init__(self): self.foo = []
>>> a, b = A(), A()
>>> a.foo.append(5)
>>> b.foo    
[]

"""
print("==========================================================")
"""
json dumps takes an object and produces a string:

    >>> a = {'foo': 3}
    >>> json.dumps(a)
    '{"foo": 3}

    load would take a file-like object, read the data from that object, and use that string to
    create an object:
"""

"""
## veryvery important
log n typically is indicated when the problem is iteratvely made smaller
"""
print("==========================================================")
"""
if you want to use {} while using format.This is the way to do it

"""

print("{{Hello}} {}".format('world')) #{Hello} world
"""
This is the way to print(the variables
"""
auth_url="www.yahoo.com"
search_url="google.com"
print("auth url is {auth_url} and search url is {search_url}".format(**locals()))##use ** to "unpack" a dictionary and * to unpack a dictionary
"""
Important:

use ** to "unpack" a dictionary  and * to unpack a dictionary
"""
print("==========================================================")
"""
Accessing dictionary by index
"""
#This works on python2.7
#a={'a':1,'b':33,'c':44,'d':66,'e':5}
#b={'aa':1,'bb':33,'cc':44,'dd':66,'ee':5}
#for i in range(len(a)):
	#print(b.keys()[i])
	#print(b.values()[i])
print("==========================================================")
u=str('unicode')
s=str('string')
print(u,s)
print(u+s)
print("==========================================================")
import json
d={'a':1,'b':2}
#to import the dictionary to json use
print(json.dumps(d))
t=json.dumps(d)
#to retreieve the javascript data structure to python use
print(json.loads(t))
d=json.loads(t)
print(d)
print("==========================================================")
search_url = "www.example.com"

def custom_search_url(search_url):
	print("search url {search_url}".format(**locals()))
	print("search url {search_url}".format(**globals()))

custom_search_url("www.otherexample.com")
print("search url {search_url}".format(**locals()))
print("search url {search_url}".format(**globals()))
print("==========================================================")
print('%s and {0}'%('hellow').format('world'))
#'hellow and {0}'
'%s and {0}'%('hello {0}').format('world')
#'hello world and {0}'
print('%s and {0}'.format('world')%('hello'))
#'hello and world'
print("==========================================================")
"""
vars([object])

Without an argument, act like locals().
You can just use the vars builtin function which looks up __dict__ for you:
vars(t).keys()
"""
print("==========================================================")
#UTF-8 is an extension of ASCII
print("==========================================================")
ee=[1,2]
ff=[3,4]
print([list(i) for i in zip(ee,ff)])
print(dict(list(i) for i in zip(ee,ff)))

#Find duplicates in O(n) time and O(1) extra space
arr=[1, 2, 3, 1, 3, 6, 6]
print(arr)
a = datetime.datetime.now()
for i in range(len(arr)):
    if (arr[abs(arr[i])] >= 0):
        arr[abs(arr[i])] = -arr[abs(arr[i])];
    else:
        print(" %d "%(abs(arr[i])));
b = datetime.datetime.now()
c=b-a
print(c)

print("==========================================================")
#list to string

li= [1, 2, 3, 4, 5, 6]
print(map(str,li)) #['1', '2', '3', '4', '5', '6']
print("".join(str(e) for e in li))
#123456
print("==========================================================")
#Tower of hanoi can be solved always in i.e,2powern-1 moves'
#Example if we have three disks then it would take 2^3-1 moves i,e 7 moves
#For more example watch tower_of_hanoi.gif in the same directory 
print("==========================================================")
#printing 3*3 matrix

for i in range(1,10):
    print(i,)
    if i % 3 ==0:
        print()

print("==========================================================")
#It's just a variable name, and it's conventional in python to use _ for throwaway variables. It just indicates that the loop variable isn't actually used. ##very important
#In python interpreter, _ is the last value printed in the console and not the declared one.
#To hold the result of the last executed statement in an interactive interpreter session

print("==========================================================")
#In try finally continue and break cannot be used together
print("==========================================================")
#PYTHONPATH sets the search path for importing python modules.
print("==========================================================")
"""
How to quickly copy a list without linking them together:
>>> A = [1,2,3,4,5]
>>> B = A
>>> C = A[:] #####very important , so this will not require copy library,it is the alternative of deep copy
>>> A[0] = 8
>>> A
[8, 2, 3, 4, 5]
>>> B
[8, 2, 3, 4, 5]
>>> C
[1, 2, 3, 4, 5]
"""
print("==========================================================")
"""
#dictionary counting 
>>> D['cat'] = D.get('cat', 0) + 1 ##very important
"""
print("==========================================================")
"""
"==" compares the object by value and "is" compares the object by their memory address ##very important
>>> a=10
>>> b=10
>>> id(a)
38412416
>>> id(b)
38412416
>>> a=500
>>> b=500
>>> id(a)
38430232
>>> id(b)
38430184
>>> a==b
True
"""
print("==========================================================")
"""
Builtin types can be over written
>>> str="123"
>>> str("123")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
"""
print("==========================================================")
#unpacking
a,b=(1,2)
print(a,b)
a,b=[1,2]
print(a,b)
print("==========================================================")
"""
Ternary operator in Python
Although python does not have an inbuilt ternary operator like  ? :  but python supports its simulation as follow:

>>> 'true' if True else 'false'
'true'
>>> 'true' if False else 'false'
'false'
"""
print("==========================================================")
"""
Execute the Python code contained in script, which must be a filesystem path (absolute or relative) referring to either a Python file, a directory containing a __main__.py file, or a zipfile containing a __main__.py file.
$ echo "print('hello world'" > __main__.py
$ zip runme.zip __main__.py
 adding: __main__.py (stored 0%)
$ python runme.zip
hello world
"""
print("==========================================================")
"""
python uses 'j' instead of i for imaginary numbers
>>> x = 3j + 6
print(x.imag)
3.0
"""
print("==========================================================")
def work():
    print("Hello ",work.w)
 
work.w ="World"
work()
#prints Hello  World
print("==========================================================")
"""
To read data as it is from csv file  ##very important

import csv

f=open("TopicEmails.csv")
c=csv.reader(open("TopicEmails.csv", "rb"), delimiter=',')
for l in c:
   ....
"""
print("==========================================================")
#Only try and finally can be used ,this is majorly for cleaningup code in cse of exception,like file open can be closed with  finally block
try:
   a= int("1")
finally:
    print(a)
    print("Done")
print("==========================================================")
"""
what is a descriptor ?
A descriptor is any object that implements at least one of methods named __get__(),__set()__ and __delete__()

A data desciptor implements both __get__() and __set__().Implementing only __get__() makes you a non data descriptor
"""
print("==========================================================")
"""
class AA(object):
	def __init__(self,name):
		self.name =name
		return self.name

class BB(AA):
	super().__init__("Tom") #this is same as the below line but this is in python3 and super definition has to be chnaged for python 2.7 and this is preferred for reading conventions and where there are more inheritence
	AA.__init__(self,"Pluto") 
"""
print("==========================================================")
class AA(object):
	def __init__(self,name):
		self.name = name

a=AA("Tom")
print(a) #This does not make any sense so consider the below
class BB(object):
	def __init__(self,name):
		self.name = name

	def __repr__(self): #mostlt to be used for debugging puprose
		return "AA({})".format(self.name)

b=BB("Tom")
print(b) #This is much better than above AA
print(repr(b)) #another way of calling __repr__()

class CC(object):
	def __init__(self,name):
		self.name = name

	def __repr__(self):
		return "AA({})".format(self.name)

	def __str__(self):
		return "{} - is the correct name".format(self.name) #making it more meanigful and str overwrites repr in this case
c=CC("Tom")
print(c) #This is much better than above AA
print(repr(c))
print(str(c)) #another way of calling __str__()

print("==========================================================")
print(1+2)
print(int.__add__(1,2))
print(str.__add__('a','b'))
print( len('test'))
print('test'.__len__())
#__len__() mostly overwritten in the case when they want to know the length of first name and last name together as it will suit the documents length or not


"""
class Emp(object):
	def __init__(self,pay):
		self.pay=pay

e1=Emp(5000)
e2=Emp(6000)
#print(e1+e2 #This will raise an error as it doesnot know how to add objects,so we define __add__() as below
"""
class Emp(object):
	def __init__(self,pay):
		self.pay=pay

	def __add__(self,other):
		return self.pay+other.pay

e1=Emp(5000)
e2=Emp(6000)
print(e1+e2)
print("==========================================================")
"""

class  G():
	def t(self):
		return  NotImplemented #the purpose of returning an object (NotImplemented) in this case is that the other methods knows how to fallback on the other object seeing it knows how to handle the operation or  else in the end eventually if does not know how to handle it will throw an error
"""
print("==========================================================")
"""
class TT(object):
	def __init__(self):
		self.name="Tom"

	def showname(self):
		return self.name

t=TT()
print(t #This will print(some info like <__main__.TT object at 0x7f3a69375250> but see the below example
"""

class TT(object):
	def __init__(self):
		self.name="Tom"

	def showname(self):
		return self.name

	__str__ = showname    ##very very important

t=TT()
print() #This will print(as Tom
print("==========================================================")
class YY(object):
	def __init__(self):
		self.first_name="Tom"
		self.last_name=" Pluto"

	@property
	def fullname(self):
		return self.first_name+ " " +self.last_name

	@fullname.setter
	def fullname(self,s):
		s=s.split(" ")
		self.first_name=s[0]
		self.first_name=s[1]

	@fullname.deleter
	def fullname(self):
		print("In deleter")
		self.first_name=None
		self.first_name=None

#In the above by using property decorator we can just call the fullname instead of  fullname()
y=YY()
print(y.fullname)

#But to set a different name on the same object we use the setter decorator which will  set  the new name and then call full name in this case
y.fullname = "Tom  Missie"
#so to cleanup code we can  use a deleter  as @fullname.deleter as above
del y.fullname
#print(y.fullname #So this will raise as exception in this case

print("==========================================================")
#Reading from one file and writing to another
with open("/tmp/aa.txt") as rf: #rd is for binary read and wb is for writing to a binary file,this is  for reading from a  image binary file and write to another
	with  open("/tmp/yy.txt","w") as wf:
		for l in rf:
			wf.write(l)
print("==========================================================")
print( os.path.basename("/tmp/aa.txt")) #will print(aa.txt
print( os.path.dirname("/tmp/aa.txt")) #will print( /tmp
print( os.path.split("/tmp/aa.txt")) #will print(('/tmp', 'aa.txt')
print("==========================================================")
#LEGB  => Local,Enclosing,Global,Builtin
x='Global'
def outer():
	x='In outer'   #Enclosing
	def inner():
		#nonlocal x #python 3,this will overwrite Enclosing variable,this is also widely used than global variable
		x= 'inner' #Local
		print(x)
	inner()
	print(x)

outer()
print("==========================================================")
"""
All the known errors are caught to be first as the general exception at the last "except Exception as e" or if we use this first other exception code will never be executed
try:
except FileNotFound as fnf:
	print(fnf)
except  FloatingPointError as fpe:
	print(fpe)
except ArithmeticError as ae:
	print(ae)
except Exception as e:
	print(e)
"""
print("==========================================================")
#set is a collection of unique elements ##very very important
a=[1,2,2,3,4,5,5]
my_set=set()
for i in a:
	my_set.add(i)
print(my_set)
#The above can also be doen in the following way using set comprehension
#set comprehension
my_set={i for i in a}
print(my_set)
print("==========================================================")
#generator #comprehension style ##very very important
a=[1,2,3,4,5]
gen = (i**i for i in a)
print(type(gen))
print(gen)
print(next(gen),next(gen),next(gen),next(gen),next(gen))
print("==========================================================")
#How to sort objects ##very very important
class Employee(object):
	def __init__(self,name,age,salary):
		self.name = name
		self.age = age
		self.salary = salary
	def __repr__(self):
		return "name {0.name} ,age{0.age},salary is {0.salary}".format(self)
	def __str__(self):
		return "name {0.name} ,age{0.age},salary is {0.salary}".format(self)


e1=Employee("Carl",37,70000)
e2=Employee("Sarah",29,80000)
e3=Employee("John",43,90000)

employee=[e1,e2,e3]
print(e1) #This will cal __str__
print(repr(e1)) #This will cal __repr__
#print(sorted(employee)) #This will not sort the objects with name . this used to work in python2.7
#To sort the objects with name we have to use the "key" in sorted function as follows

def e_sort(e):
	return e.name
print(sorted(employee,key=e_sort))#this will sort the employee with name ,in the e_sort function if you change e.name to e.age ,then the sorting will happen based on the age
#The above can done using lambda also,like the following
print(sorted(employee,key=lambda e:e.name))
#OR
from operator  import attrgetter
print(sorted(employee,key=attrgetter('name')))
print("==========================================================")
"""
yield can be used with dictionary,list...
ex:

def rt():
	for i in xrange(100000):
		yield {'id':1,'val':2}
"""
print("==========================================================")
#comparing first and last element in a list,this better works on a even number of elements in the list
##very very important
a=[1,2,3,3,2,1]
if len(a)%2 ==0:
	for i in range(len(a)):
		if i <= (len(a)/2)-1:
			if a[i] == a[-i-1]: #first element is compared like a[0] == a[-0-1] ,second elemen like a[1] == a[-1-1] and so on.........
				print("Same")
			else:
				print("Not Same")

print("==========================================================")
"""
In python 3
/  => 5/2 =>2.5
// is known as floor division => 5//2 will give the integer part of this i.e,2
% is used to mainly know whether the number is divisible or not
"""

print("==========================================================")
"""
Serialization is the process of converting an object into a stream of bytes in order to store the object 
or 
transmit it to memory, a database, or a file. Its main purpose is to save the state of an object in 
order to be able to recreate it when needed. The reverse process is called deserialization.
"""
"""
Creating class object depending on condition
x = (classA if y == 1 else classB)(param1, param2)
"""
"""
Splitting a  string with back slash in a new line may cause whit space. so using the double quotes is the best way of splitting a string into different line
multiStr= ("select * from multi_row "
"where row_id < 5 "
"order by age") 
print(multiStr)

#select * from multi_row where row_id < 5 order by age
"""
"""
testList = [1,2,3]
x, y, z = testList

print(x, y, z)

# 1 2 3
"""

"""
print(the file path of imported modules.
import threading 
import socket

print(threading)
print(socket)

#1- <module 'threading' from '/usr/lib/python2.7/threading.py'>
#2- <module 'socket' from '/usr/lib/python2.7/socket.py'>
"""

"""
Unpack function arguments using splat operator.
def test(x, y, z):
	print(x, y, z)

testDict = {'x': 1, 'y': 2, 'z': 3} 
testList = [10, 20, 30]

test(*testDict)
test(**testDict)
test(*testList)

#1-> x y z
#2-> 1 2 3
#3-> 10 20 30
"""

"""
Check the memory usage of an object.
import sys
x=1
print(sys.getsizeof(x))

#-> 24
"""

"""
Use __slots__ to reduce memory overheads.
Have you ever observed your Python application consuming a lot of resources especially memory? Here is one trick which uses <__slots__> class variable to reduce memory overhead to some extent.
import sys
class FileSystem(object):

	def __init__(self, files, folders, devices):
		self.files = files
		self.folders = folders
		self.devices = devices

print(sys.getsizeof( FileSystem ))

class FileSystem1(object):

	__slots__ = ['files', 'folders', 'devices']
	
	def __init__(self, files, folders, devices):
		self.files = files
		self.folders = folders
		self.devices = devices

print(sys.getsizeof( FileSystem1 ))

#In Python 3.5
#1-> 1016
#2-> 888
Clearly, you can see from the results that there are savings in memory usage. But you should use __slots__ when the memory overhead of a class is unnecessarily large. Do it only after profiling the application. Otherwise, you'll make the code difficult to change and with no real benefit.
"""

"""
 In line search for multiple prefixes in a string.
 print("http://www.google.com".startswith(("http://", "https://")))
print("http://www.google.co.uk".endswith((".com", ".co.uk")))

#1-> True
#2-> True
"""

"""
********##very important************
raw_input list and string
>>> print((raw_input().split())
['1,2,3,4']
1,2,3,4
>>> print((raw_input().split())
['1', '2', '3', '4']
1 2 3 4
"""

"""
********##very important************
>>> a=['1','2','3','4','5']
>>> ', '.join(map(lambda x: "'" + x + "'", a))
"'1', '2', '3', '4', '5'"
"""
class ExampleClass(object):
	def __call__(self, *args, **kwargs):
		print("Hell yeah!")

	def rt(self):
		print("In rt")

# Create an instance of ExampleClass
inst = ExampleClass()

# Call the object as a function!
inst()
#print(inst.rt() #AttributeError: 'ExampleClass' object has no attribute 'rt'

'''
set important examples
# Program to perform different set operations
# as we do in  mathematics
 
# sets are define
A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};
 
# union
print("Union :", A | B)
 
# intersection
print("Intersection :", A & B)
 
# difference
print("Difference :", A - B)
 
# symmetric difference
print("Symmetric difference :", A ^ B)

Output:

('Union :', set([0, 1, 2, 3, 4, 5, 6, 8]))
('Intersection :', set([2, 4]))
('Difference :', set([8, 0, 6]))
('Symmetric difference :', set([0, 1, 3, 5, 6, 8]))

'''
"""
Quick sort algorith very very easy .*******important*******
https://www.youtube.com/watch?v=kFeXwkgnQ9U
#preferred algorithm for sorting. Doesnt matter even if there are duplicates
"""
def quick_sort(sequence):
	length = len(sequence)
	if length <= 1 :
		return sequence
	else:
		pivot= sequence.pop() #get the last item of the list as pivot

	items_greater = []
	items_lower = []

	for item in sequence:
		if item>pivot:
			items_greater.append(item)
		else:
			items_lower.append(item)

	return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([0,9,3,8,2,7,5]))#Time complexity n logn and worst is n*n


print("=== Important ****==========")
#sharing attributes between objects
class Employee():
	total = 0
	def __init__(self,name):
		self.name = name
		Employee.total += 1

	def print_total(self):
		print(self.total)

e=Employee('1')
e1=Employee('2')
e.print_total()
e1.print_total()
print("===========")
#multiple assignments important
d= {}
b= d[1] = '123'
print(b)
#'123'
print(d)
#{1: '123'}
print("===========")
#Important
#return vs yield
#once the return keywords returns the lines after return is ignored
#but after the call of the yield statment the lines after the yield statement continues
def rt():
	'''   doctsting    '''

	for i in range(10):
		yield i
	print("Printing i after yielding")

for i in rt():
	print(i)
print("===========")
#Important
#when anyvariable assigned to slots only those can be used and new instance variables cannot be assigned that is the reason slots are used
class FileSystem1(object):

	__slots__ = ['files', 'folders', 'devices']
	
	def __init__(self, files, folders, devices):
		self.files = files
		self.folders = folders
		self.devices = devices

f=FileSystem1(1,2,3)
print(f.files)
try:
	f.newvariable = 10
except Exception as e:
	print(e)
print("===========")
#property descriptor
class Foo(object):
	def __init__(self, value):
		self._name = value	

	@property
	def name(self):
		print("returning name")
		return self._name

	@name.setter
	def name(self, value):
		print("setting name")
		self._name = value

o = Foo(value='test')
print(o.name) #prints "returning name" test
o.name='123' #prints setting name
print(o.name)#prints "returning name"123 
print("===========")

class Foo(object):
	def __init__(self):
		self.__a = 1 #__a becomes a private variable and is not accessible from the object so we have to write a getter method

	def get(self):
		return self.__a

o = Foo()
#print(o.__a)# gives an error important
print(o.get())

print("===========")
class Foo(object):
	at = 1

	def access_var(cls):
		print(id(cls))
		print(cls.at)

o = Foo()
print(id(Foo))
print(id(o))
print(o.access_var())

print("===========")
#Important: In the below class since __baz is a private variable , even thought child class overrides the value the old value is retained and there are two copies of __baz
class Foo(object):
    def __init__(self):
        self.__baz = 42
    def foo(self):
        print(self.__baz)
    
class Bar(Foo):
    def __init__(self):
        super(Bar, self).__init__()
        self.__baz = 21
    def bar(self):
        print(self.__baz)

x = Bar()
x.foo()
#42
print(x.bar())
#21
print(x.__dict__)
#{'_Bar__baz': 21, '_Foo__baz': 42}
#==============================================
"""
Coroutines : Are methods which waits until at the yield until the next input is available

def grep(pattern):
    print('Looking for ', pattern)
    try:
        while True:
            line = (yield)
            if pattern in line:
            print(line)
    except GeneratorExit:
        print('Going away. GoodBye')

This is the simple example of a coroutine. It is initialized by specifying a pattern it will look for(this is of course optional; not all coroutines will take an initial parameter)/ It will then wait until a value is submitted to it and then using the if statement it will decide if the pattern is present in the value. If it is then it will print the line out. If the close() method is called on this coroutine the GeneratorExitexception will be called.

The difference between genrators and coroutines are
Generrators are data producers
Coroutines are data consumers
A generator produces a series of values using yield

"""
"""
********Important***********
O(1) < O(logn) < O(n) < O(nlogn) holds true.
https://stackoverflow.com/questions/56506410/why-is-on-better-than-o-nlogn
"""

