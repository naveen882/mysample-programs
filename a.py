import string
import logging
import datetime
import os,subprocess

class Dynamo():
    def __init__(self,x):
        print "In init def"
        self.x =x
    def __str__(self):
        print "In str func"
        return str(self.x) +"====="
    def __repr__(self):
        print "In repr func"
        return str(self.x) +"====="
    def __getattr__(self,k):
        if k == "color":
            print "key is color"
        else:
            print "key is something else {},{}".format(k,"hello world")


d=Dynamo(1)
d.color
d.color1
print "%s"%(d.x)
print str(d)
        

class Rastan(object):
    def __init__(self,x):
        print "In init def"
        self.x =x
    def __str__(self):
        print "In str func"
        return str(self.x) +"====="
    def __repr__(self):
        print "In repr func"
        return str(self.x) +"====="
    def __getattribute__(self,k):
        if k == "color":
            print "key is color"
        else:
            print "key is something else {},{}".format(k,"hello world")
            return "hi"


d=Rastan(1)
d.color
d.color1
print "%s"%(d.x)
print str(d)

print "============="
class counted(object):
    def __init__(self,func):
        self.func=func
        self.counter=0
    def __call__(self,*args,**kwargs):
        self.counter+= 1
        return self.func(*args,**kwargs)

@counted
def something():
    print "In something"
    pass

something()
something()
print something.counter
print "============="
#combining two list into one

listone=[1,2,3]
listtwo=[4,5,6]

print listone+listtwo
listone=(1,2,3)
listtwo=(4,5,6)

print listone+listtwo
#duplicating a list in itself
a=[1,2,3]  #**************************************
print a*2
print [a]*2

def f(*t):
    print t
    t=3
    print t

t=2
f(t)
print t

x=[1,2,3,4,5]
print x

def go(li):
    li=[5,6,7,8]

go(x)
print x

def change(x):
    x[0]= 5


change(x)
print x

def yu(u):
    u+=10
    return u

g=10
yy=yu(10)
print g,yy

def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist

emails = {'Dick': 'bob@example.com', 'Jane': 'jane@example.com', 'Stou': 'stou@example.net'}
print dict([name,".com"in email]for name,email in emails.items())

dict_as_list = (('a', 1), ('b', 2), ['c', 3])
dictionary = dict(dict_as_list)
print dictionary
# dictionary now contains {'a': 1, 'b': 2, 'c': 3}

a=(1,2,3,4)
print a[0],a[1],a[2],a[3]

b=((1,2,3,4),(1,2))
print b[0][0]
print b[0][1]
print b[0][2]
print b[0][3]
print b[1][0]
print b[1][1]

for i in range(len(b)):
    for j in range(len(b[i])):
        print b[i][j]

c={'a':1,'b':2}
print c['a']
print c['b']
c['c']=2
print c
print c.pop('b',None)
print c
c.get('b',c.update({'b':2}))
print c

qq="12"
rr="13"

out = "<html>%(qq)sand%(rr)s</html>"%locals()
print out
out = "<html>%(qq)sand%(rr)s</html>"%globals()
print out

def func(a,b=None):
    if b is None:
        print "b is None"
        print b is None
    else:
        print a,b

func(1)
func(1,2)

def func1(a,*b):
    if len(b) == 0:
        print "b is None"
        print b is None
    else:
        print a,b

func1(1)
func1(1,*[2,3])
func1(1,(2,3))
func1(1,(2,3,))

def func2(**b):
    print b
    if len(b) > 0:
        for i in b:
            print "====="
            print b[i]
            b[i]=2



d=dict(a=1)
func2(**{'a':1})
func2(**dict(a=1))
print d
func2(**d)
print d

a,b,c=1,2,3
print a,b,c
c,b,a=a,c,b
print a,b,c

add2= lambda a,b:a+b;print "======";print "|||||||"
print add2.func_code
import dis
print add2(1,2)
print dis.dis(add2)

ee=[1,2]
ff=[3,4]
print [list(i) for i in zip(ee,ff)]
print dict(list(i) for i in zip(ee,ff))

di=dict(a=1,b=2)
print di
print dir(di)
print di.items().append([c,2])
print di.has_key('a')
print  di.keys()
print  di.values()
print di
it= di.iterkeys()
print it.next()
print it.next()

strings=['a','b','c','d','e']
for i,k in enumerate(strings):
    print i,k

class test22:
    def rt(self,**args):
        print args
        args['a']=2

a={'a':1}

t=test22()
t.rt(**a)
print a

a=[6,6,1,1,2,3,3,3,4,5]
print list(set(a))
print sorted(set(a),reverse=True)

def fun(*a,**kw): #**************************
    print a,kw

a=(1,2,3,4)
d={'a':1,'b':2}

fun(a)
fun(d)
fun(a,d)

fun(*a)
fun(**d)
fun(*a,**d)

opt = ["opt3", "opt2", "opt7", "opt6", "opt1", "opt10", "opt11"]
print sorted(opt)
opt.sort()
print opt

list_of_tuples = [('key', 'value'), ('key2', 'value2')]
print dict(list_of_tuples)

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
                print "12345"
                obj.__init__(4)
                print obj.p

        def hello(self):
                print "in myt hello"

mt = mytest(2)
m=myt(3,mt)
mt.hello()
m.hello()

mystr1="hello world"
print mystr1[::-2]
print mystr1[-1]

for x in xrange(1,11):
    print x

str1="golf"

def reverse(st):
    for i in st[::-1]:
        yield i

for i in reverse(str1):
    print i


def rt():
    for i in range(1,11):
        yield i


g=rt()
print g.next()
print g.next()
print dir(g)

a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]
print a
del a[2:4]
print a
a[:]
a[::]
print a

knights={'a':1,'b':2}
for i,k in knights.iteritems():
    print i,k
    print type(i),type(k)
for i in knights.iterkeys():
    print i
    print type(i)
for i in knights.itervalues():
    print i
    print type(i)


def linear(a,b):
    def rt(x):
        return a*x+b
    return rt

l =linear(3,4)
print l(1)
    
def linear(a,b):
    def rt(x):
        return a*x+b
    return rt(2)

print linear(3,4)

if __name__ == '__main__':
    print __name__

import logging
print logging.__name__

class rtt(object):
    pass

print rtt.__name__
r=rtt()
print type(r)

a = [66.25, 333, 333, 1, 1234.5]
print a.count(333)
print a.count(66.25)
print a.count('x')
print 'x' in a
print a.insert(2,-11)
print a
print a.append(333)
print a.index(333)
a.reverse()
print a
a.sort()
print a

a=[1,2,3,333,6,'ab',5,4,7,'a',77,5566,94,2,34]
print a
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]

print a

word ="acr"
word=sorted(word)
alternatives = ["car","girl","tofu","rca"]
for i in sorted(alternatives):
    if sorted(i) == word:
        print "{} is palindrome".format(i)

a=['1','2','3']
a=map(int,a)
print a

def rt(a=[]):
    a.append(1)
    print a

rt()
rt()
rt()

d={}

print d['red']  if 'red' in d else "Hi"
"OR"
print d.get("red","None")
print d.get("red",d.update({"red":"Hello"}))

print d.update({'1':2})

colors = ['red','red','red','red','green','blue','blue']
d={}
for i in colors:
    d[i] = d.get(i,0)+1 #***********************************
print d


def rs(a,b,c):
    print a,b,c

a=[1,2,3]
rs(*a)

st='hello'   'world'
print st

arr=["harry","sally","tom"] #***************Write down***********************
for i in range(len(arr)):
        print arr[i %len(arr)] * 3
        print arr[(i+2) % len(arr)] * 2
        print arr[(i+1) % len(arr)] * 1


mydict = {'carl':40, 'alan':2, 'bob':1, 'danny':3}
print dict((v,k) for k,v in mydict.items())
print {v:k for k,v in mydict.items()}
print {(v,k) for k,v in mydict.items()}

def fib(): #******************************************
    a,b=0,1
    while True:
        yield b
        a,b=b,a+b 

f=fib()
print next(f)
print next(f)
print next(f)
print next(f)
print next(f)
print next(f)
        
def fib(n): #****************************************
    a,b=0,1
    while b<n:
        yield a
        a,b=b,a+b 

f=fib(10)
print next(f)
print next(f)
print next(f)
print next(f)
print next(f)
print next(f)
        

class iterator(object):
    def __init__(self):
        self.x=0
    def next(self):
        self.x+=1
        if self.x>=3:
            print "Stop iteration"
        else:
            return self.x* self.x

i=iterator()
print next(i)
print i.next()
print next(i)
print i.next()
    
class Animal:
    def __init__(self,name):
        self.name = name
    def talk(self):
        raise NotImplementedError


class Dog(Animal):
    def talk(self):
        return "Woof Woof"

class Cat(Animal):
    def talk(self):
        return "Meow Meow"

animals=[Cat('Tom'),Cat('Mr. Mistoffelees'),Dog('Pluto')]
for animal in animals:
    print animal.name + " talks as " +animal.talk()

import datetime #********************
a = datetime.datetime.now()
b = datetime.datetime.now()

c=b-a
print c
print c.seconds,"2nd"
print c.microseconds,"1st"

colors = ["red","yellow","blue","green"]
for i in sorted(colors):
        print i
for i in sorted(colors,reverse=True): #This sorts the list in reverse alphabetical order
        print i
for i in reversed(colors): ##This sorts the list in reverse order
        print i

a,b,c,d=colors #*******************************
print a,b,c,d


try: #******************
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

##Python Access specifiers
#Python does not have mandatory access control like some other languages you may be used to. The philosophy of the language is "We are all consenting adults".
__private_access_specifier = 1 ## private has __
_protected_access_specifier = 2 ## protected has _
public_access_specifier = 3 ##with any underscore are public by default

string="yelloworld" #********************
print string[0]
string=list(string)#********************
string[0]='h'
print "".join(string)#********************

di={"yelloworld":"hello world"}
di['helloworld']=di.pop("yelloworld")
print di

#del di["yelloworld"] #******

f=open("/tmp/a.txt","w")
f.write("helloworld\nhi")
f.close()
f=open("/tmp/a.txt","r")
print type(f.read())
f.close()
f=open("/tmp/a.txt","r")
for l in f.xreadlines():
    print type(l)
f.close()


#pickle.dump(x,f) #fshould be open for writing
#pickle.load(f)

def makeincrementor(n):return lambda x:x+n
f=makeincrementor(2)
g=makeincrementor(4)
print f(32)
print g(44)

#print map(lambda x: x * 2 + 10, foo)#:1515
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]  #*******************************
print filter(lambda x:x%3==0,foo) #[18, 9, 24, 12, 27]
print map(lambda x:x*2+10,foo)# [14, 46, 28, 54, 44, 58, 26, 34, 64]
print reduce(lambda x,y:x+y,foo)#139
print sum(foo) #139
#id() will return objects memory address
#objects have different memory address but their values will have the same values and no duplicates in memory always

#class decorator
class mydeco(object):
    def __init__(self,f):
        self.f=f
        self.x=0
    def __call__(self,*k,**kw):
        self.x+=1
        return self.f()

@mydeco
def rt():
    print "In rt"

rt()
rt()
print rt.x
#monkey patching ************************************
class myclass(object):
    def f(self):
        print "In f"

def monkey(self):
    print "In monkey patch"

myclass.f=monkey

m=myclass()
m.f()

thing=(x for x in range(10))
print type(thing)
for x in thing:
    print x

a=[]
b=list()
print a==b

a=[1,2,3,4] #verys trange
b=list(a)
print b
a=(1,2,3,4,)
print list(a)

#printing list in reverse order
for i in range(10,0,-1):
    print i
for i in reversed(range(11)):
    print i

a=[1]

for i in a:
    print i
else:
    print "HI"

#To do shallowcopy and deep copy

d={"a":1,"b":2,"c":3}
print zip(*d.iteritems())
print zip(d.iteritems())

def yy(*t):
    print t

yy(*d.iteritems())

a, b, c = [1, 2, 3]
print a,b,c

a=[1,2,3,4,5]
b=[6,7,8,9]
print dict(zip(a,b))

#calculator = {
#{
#'plus':lambda x,y:x+y,
#'minus':lambda x,y:x-y
#}
#print calculator['plus'](2,3)

with open("/tmp/a.txt") as f:
    print f.readlines()

def f(x): #******************************************
    return {
    'foo':1,
    'bar':2
    }.get(x,None)

print f('foo')
print f('bar')
print f('hi')

p=lambda k: {'foo':1,'bar':2}.get(k,None) #*************************************
print p('foo')
print p('bar')
print p('hi')

BaseClass = type('BaseClass',(object,),{}) #********************************************

@classmethod
def Check1(self,mystr):
    return mystr == "ham"

@classmethod
def Check2(self,mystr):
    return mystr == "sandwich"

@classmethod
def Check3(self,mystr):
    return mystr == "wich"

C1= type("C1",(BaseClass,),{'x':1,"Check":Check1})
C2= type("C2",(BaseClass,),{'x':2,"Check":Check2})
C3= type("C3",(BaseClass,),{'x':3,"Check":Check3})

c1=C1()
print c1.Check("ham")
print c1.x
c2=C2()
print c2.Check("sandwich")
print c2.x
c3=C3()
print c3.Check("ham")
print c3.x
def myfactory(rt):
    for cls in BaseClass.__subclasses__():#*****************************************
        if cls.Check(rt):
            print cls.__name__
            return cls()

print myfactory("ham")
print myfactory("sandwich")
print myfactory("wich")

#super is mostly for calling baseclass functions   super(tty,self).__init__() #*********************************


from collections import defaultdict
ice_cream = defaultdict(lambda: 'Vanilla') #*****************
ice_cream['Sarah'] = 'Chunky Monkey'
ice_cream['Abdul'] = 'Butter Pecan'
print ice_cream['Sarah']
#Chunky Monkey
print ice_cream['Joe']
#Vanilla


def tt():
        def rt():
                print "inside"
        #rt #only writing rt insted of rt() will not call the rt function unlike the decorator
        return rt

tt()


#to do prime number
