#!/usr/bin/python

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

def func(a=[]):
	a.append(1)
	print a

func()
func()


#Lambda function
#Lambda Expressions (Anonymous Functions)

#As if the last section wasn't cool enough, let's try "lambda expressions", a concept borrowed from Lisp and other functional languages. Lambda expressions return functions as results. They build functions without assigning names to them. A normal function declaration assigns the functions value to the name of the function, but lambda expressions do not.

#Why would you want this dubious functionality? Because lambda expressions are nice to use in places that a function declaration wouldn't normally be allowed, and to write quick and dirty functions on the fly. Sometimes you want to build functions(callback handlers in gui's, object member data accessors, and so on), and using lambda expressions makes that a lot easier.

#So lambda lets you define and use a function inside an if statement body, or inside a list. However, lambda expressions are just that, expressions. It is difficult to write a complicated function because statements are not allowed.

#Python supports a concept called "list comprehensions". It can be used to construct lists in a very natural, easy way, like a mathematician is used to do.
#S = {x² : x in {0 ... 9}}
#V = (1, 2, 4, 8, ..., 2¹²)
#M = {x | x in S and x even}

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
T3 = [map(int, x) for x in T1]

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
