#!/usr/bin/python
import string
import logging

class Dynamo:
   def __init__(self,x):
      print "In init def"
      self.x=x

   def __str__(self):
      print "In str func"
      return str(self.x) + "====="
      
   def __repr__(self):
      print "In repr func"
      return self.x + "====="
      
   def __getattr__(self,k):
      if k == "color":
         print "key is color"
      else:
         print "Some other key"
         print "%s",k

d=Dynamo(1)
d.color
d.color1
print "%s"%(d.x)
print str(d) ##This will print __str__ function
         
print "==================================================="            
   
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
      if k == "color":
         print "key is color"
      else:
         print "Some other key"
         print "%s",k

d=Rastan(1)
d.color
d.color1
print "%s"%(d.x)

f=open("/tmp/aa.txt","w")
f.write("Testing and testing\n again\n and \nagain")
f.close()
f=open("/tmp/aa.txt","r")
while True:
   for line in f.readlines(): #reads entire file at once and splits it by line
      print line
   else:
      break;
f.close()      

f=open("/tmp/aa.txt","r")
while True:
   for line in f.readline(): #read character by character
      print line
   else:
      break;
f.close()      

f=open("/tmp/aa.txt","r")
while True:
   for line in f.read(): #read character by character
      print line
   else:
      break;
f.close()      

a=(1,2,3,4)
print a[0]
print a[1]
print a[2]
print a[3]

b=((1,2,3,4),(1,2))
print b[0][0]
print b[0][1]
print b[0][2]
print b[0][3]
print b[1][0]
print b[1][1]
c={'a':1,'b':2}
print c['a']
print c['b']
try:
   if c['a']:
      print "hi"
except:      
   logging.debug("a1")
   logging.error("a1")
   logging.exception("a1")
      
try:
   if c['c']:
      print "hi"
except:      
   logging.debug("a1")
   logging.error("a1")
   logging.exception("a1")
      
def func(a,b=None):
   if b is None:
      print "b is none"
   else:
      print a,b

func("a","b")      
func("a")      

def func1(a,*b): #* stands for a tuple
   print a
   if len(b) > 0:
      print len(b)
      for i in range(len(b)):
         print i
   else:
      print "No b arguments"

func1(1,2,3,4,5)
func1(1)
   
def func2(d,**c): # ** stands for a dictionary
   if len(c)>0:
      print "func22222"
      print len(c)
      print c
      print "func222222222222"
   else:
      print "No c arguments"

u={'a':1,'b':2}      
func2(1,**u)


def func3(a,*d):
   if len(c) > 0:
      print "func2222222222222222222222222222222222222222222222222222222222222222223"
      print len(d)
      print d
      print a
      #for i in range(len(c)) and 'a' in c:
         #   print i,c[i]
         #   print c['a']
      print "func2222222222222222222222222222222222222222222222222222222222222222223"
   else:
      print "No c arguments"

u={'a':1,'b':2}
func3(1,'a','d','c')

aa=(1,2,3,(4,5),6)
print aa[0]
print aa[1]
print aa[2]
print aa[3]
print aa[3][0]
print aa[3][1]
print aa[4]

i=5
def fs(args=i):
   print args
   print i

i=6
fs()
fs(7)
print "========"
cc=[1,2,3,4]
dd=['1','2','3','4']
print "%s"%'=='.join(dd) ## very importtant to note

for i in range(len(dd)):
   print i,dd[i]


print dir(dd)
a=11
b=22
c="ee"
print a,b,c
a,b,c=c,a,b
print a,b,c
add2=lambda a,b:a+b;print "=========";print "|||||||||" #lambda are just like function pointers where add2 now can be passed as a parameter to someotehr function
print add2(3,4)

def ty(add2):
   print add2(5,4) ## will print 9

print "=============="
ty(add2)

ee=[1,2]
ff=[3,4]
gg=zip(ee,ff)   
print gg
di=dict(a=1,b=2)
print di
print di.items()
print di.has_key('a')
print di.keys()
print di.values()
t= di.iterkeys()
print dir(t)
print t.next()
print t.next()

strings = ['a', 'b', 'c', 'd', 'e']
for index,string in enumerate(strings):
   print index,string

class test22:
   def hello(self,**args):
      print args['a']
jj={'a':1}
t= test22()
t.hello(**jj)

a=[6,6,1,1,2,3,3,3,4,5]
print set(a)
print dir(a)
a=[6,6,1,1,2,3,3,3,4,5]
print sorted(set(a))
print sorted(set(a),reverse=True)

def fun(*a,**kw):
   print a,kw

a=[1,2,3,'a']   
b=dict(a=1,b=2,c=3)
fun(*a)
fun(**b)
fun(*a,**b)

opt = ["opt3", "opt2", "opt7", "opt6", "opt1", "opt10", "opt11"]
print sorted(opt)
print (opt.sort()) #This will print None but will sort the original list
print opt

list_of_tuples = [('key', 'value'), ('key2', 'value2')]
a_dict_2 = dict(list_of_tuples)
print a_dict_2
a_dict_3 = a_dict_2
bb=1
aa=dict(a_dict_2=a_dict_2)
print aa
for val,key in enumerate(aa):
   for i in aa[key]:
         print "======"
         print aa[key][i]

print a_dict_3 == a_dict_2
print type(a_dict_2)
print a_dict_2.clear()
print str(a_dict_2) + "===="

class mytest:
   p=1
   def __init__(self,a):
      self.a=a
      print str(self.p) + "======"

class myt(mytest):
   def __init__(self,b,obj):
      obj.p  =2
      obj.__init__(4)
      print obj.p

mt = mytest(2)
m = myt(3,mt)
   
mystr1="hello world"   
mystr2=mystr1
mystr1=mystr1[:-2]
print mystr1
p=[x for x in range(1,11)]
print p

str1="golf"
def reverse(str1):
   a=list(str1)
   for i in str1[::-1]:
      yield i

for i in reverse(str1):
   print i

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print a
del a[2:4]
print a
del a[:] # or del a[::]
print a

#Looping techniques
knights={'a':1,'b':2}
for k, v in knights.iteritems():
   print k, v
for k in knights.iterkeys():
   print k
for v in knights.itervalues():
   print v

def linear(a,b):
   def result(x):
      return a*x + b
   return result(1)

aa= linear(3,4)
print aa

if __name__ == "__main__":
   print "__name__"
import random
print random.__name__

print __name__

a = [66.25, 333, 333, 1, 1234.5]
print a.count(333), a.count(66.25), a.count('x')
#2 1 0
a.insert(2, -11)
a.append(333)
print a
a.index(333)
print a
a.remove(333)
print "========="
print a
a.reverse()
print a
a.sort()
print a

class Deco(object):  #decorators to rememmber passing object
   def __init__(self):
      print "========"
      #if len(arg) > 0:
      #   print arg
   def __call__(self,g):
      print "In call"
      g()
      print "after call"

@Deco()
def tt():
   print "In tt"
            

def deco1():
   def all(F):
      print "in all"
      print F.__name__
      F()
      print "after all"
   return all      

@deco1()
def gg():
   print "In gg========="

def shout(aa="yes"):
   print aa

scream=shout
scream()
scream(1)

#Bubble sort
a=[1,2,3,333,6,'ab',5,4,7,'a',77,5566,94,2,34]
print a
for ii in range(len(a)-1):
   for j in range(len(a)-ii-1):
      if a[j]>a[j+1]:
         a[j],a[j+1]=a[j+1],a[j]
         
   print a   

#Anagrams
print "====================================================================================="
word="acr"
word = sorted(word)
alternatives = ['car', 'girl', 'tofu', 'rca']
for at in alternatives:
   if word == sorted(at):
      print at

a=['1','2','3']
print a
a=map(int,a)
print a


def rt(a=[]):
   a.append(1)
   print a

rt()   
rt()   

def rs(a,b,c):
   print a,b,c

aa=[1,2,3]
rs(*aa)

st='str' 'ing'             #  <-  This is ok
print st ##This prints string

a="sumthing"
print sorted(a,reverse=True)
print a[::-1]

import re
m_="sumthing@sumthing.com"
tt=re.findall(r"\w+@\w+\.(?:com|in)",m_)
print tt
line = "He is a German called Mayer."
if re.search(r"G[aert]r[mk]an",line):
   print "string found"

line = "He is a Grrkan called Mayer."
if re.search(r"G[aert]r[mk]an",line):
   print "string found"
line = "He is a Gyrkan called Mayer."
if re.search(r"G[aert]r[mk]an",line):
   print "string found"
line = "67He is a Gerkan called Mayer."
if re.search(r"^[0-9]\w+ G[aert]r[mk]an",line):
   print "string found123"
line = "He is a Gerkan called Mayer.45"
if re.search(r"\d+$",line):
   print "string found"



d="30-12-2001"   
aa=re.match(r"\b\d{1,2}[-/:]\d{1,2}[-/:]\d{4}\b",d)
aa.group()

ip="1.1.1.112 and other ip is 112.113.112.112"
aa=re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",ip)
#aa.group()

line="This line has smiley :) ;-) ;)"
re.findall(r":\)|[:;]-\)|;\)",line)
#[':)', ';-)', ';)']

m_="valid@emailid.com"
re.findall(r"\w[^\s]+@\w[^\s]+\.(?:com|in)",m_)
m_1="valid@emailid.in"
re.findall(r"\w[^\s]+@\w[^\s]+\.(?:com|in)",m_1)
m_2="val id@email id.in"
re.findall(r"\w[^\s]+@\w[^\s]+\.(?:com|in)",m_2)


line='12He is a German called Mayer'
uu=re.compile(r"^\d+\w+ .*")
re.findall(uu,line)
#['12He is a German called Mayer']
uu=re.compile(r"(^\d+\w+) .*")
re.findall(uu,line)
#['12He']
line="He is a German called Mayer12345 dfdfd"
re.findall(uu,line)
aa="192.168.254.35,henry,thesecond,0"
aa1="192.168.254.35,henry,0"
#The below regular expression would satisfy bot aa and aa1
re.findall(r"(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b),((?:\w+,\w+|\w+)),(\d+)",aa)


T2=[(i,j) for i in range(3) for j in range(i) ]
#first,second,*rest = (1,2,3,4,5,6,7,8) #this is supported in python 3 onwards

#Note xrange will return an iterator
arr=["harry","sally","tom"]
for i in range(len(arr)):
	print arr[i % len(arr)] * 3
	print arr[(i+1) % len(arr)] * 2
	print arr[(i+2) % len(arr)] * 1

#Output:
#harry #harry #harry #sally #sally #tom

#sally #sally #sally #tom #tom #harry

#tom #tom #tom #harry #harry #sally
#Sorting a dictionaty by keys
mydict = {'carl':40, 'alan':2, 'bob':1, 'danny':3}
dict(sorted( mydict.items(), key = lambda(x): x[1] ))

#dictionary - swapping key to values 
my_dict = {'carl':40, 'alan':2, 'bob':1, 'danny':3}
dict(zip(my_dict.values(),my_dict.keys()))

#Adding a two dimensional array
a=[1,2]
b=[3,4]
a+b  #=>   [1, 2, 3, 4]
summed = [sum(pair) for pair in zip(a, b)] #[4, 6]


#Adding a three dimesional array
A=[[[1,2,3]]]
B=[[[3,4,5]]]
C=[[[4,5,6]]]
print [[map(sum, zip(A[0][0], B[0][0], C[0][0]))]]  ##=>   [[[8, 11, 14]]]

