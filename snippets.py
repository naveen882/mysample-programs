
#From Python 3.1 it is possible to omit eld names, in which case Python
#will in ect put them in for us, using numbers starting from 0. For example:
print "{} {} {}".format("Python", "can", "count")
#'Python can count'

number = 999
hero = "Buffy"
print "Element {number} is a {hero}".format(**locals())
#'Element 999 is a Buffy':


#spilitting methods for python
slayers = "Buffy\nFaith"
print slayers.splitlines()
#['Buffy', 'Faith']

def count_unique_word(filename):
	import string
	words = {} # create an empty dictionary
	strip = string.whitespace + string.punctuation + string.digits + "\"'"
	#for filename in f:
	with open(filename) as file:
		for line in file:
			for word in line.lower().split():
				word = word.strip(strip)
				if len(word) > 2:
					words[word] = words.get(word,0) +1
	for word in sorted(words):
		print("'{0}' occurs {1} times.".format(word, words[word]))

count_unique_word("/tmp/a.txt")

slayers = "Buffy and Faith"
slayers.swapcase()
#'bUFFY AND fAITH'


t= 1,5,7 #defines a tuple
print type(t)
x, y,a,b = (1, 2, 3, 4)
print x,y,a,b
#Below works in python 3
#x, *y = (1, 2, 3, 4)
#print x,*y

from enum import Enum
class Animal():
    DOG, CAT = range(2)

print Animal.DOG,Animal.CAT

words = 'Buffy is awesome and a vampire slayer'.split()
e = [[w.upper(), w.lower(), len(w)] for w in words]
for i in e:
	print(i)

#['BUFFY', 'buffy', 5]
#['IS', 'is', 2]
#['AWESOME', 'awesome', 7]
#['AND', 'and', 3]
#['A', 'a', 1]
#['VAMPIRE', 'vampire', 7]
#['SLAYER', 'slayer', 6]


x=(n for n in [1,2,3,4,5] if n % 2 ==0)
print type(x) #generator object
for i in x:
	print type(i)

def draw_point(x, y):
	print x,y

point_foo = (3, 4)
point_bar = {'y': 3, 'x': 2}

draw_point(*point_foo)
draw_point(**point_bar)

#Incrementing dictionary values
sum1={'a':2}
value = 'a';
sum1[value] = sum1.get(value, 0) + 1 ##important
print sum1


for i in range(5):
    if i == 4:
        break
else:
    print("i was never 4")

#The "else" block will be normally executed at the end of the for loop, unless the break is called.


a = [(2, "b"), (1, "a"), (2, "a"), (3, "c")]
print sorted(a)
#[(1, 'a'), (2, 'a'), (2, 'b'), (3, 'c')]

l=[(1,2),(3,4)]
[a+b for a,b in l ] 
[3,7]
