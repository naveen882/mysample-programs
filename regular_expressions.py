import re

"""
 Use "r" at the start of the pattern string, it designates a python raw string. ##very very important
"""



pattern = re.compile('bar')
string = 'foobar'
print pattern.match(string) is None #prints True
string = 'barfoo'
print pattern.match(string) is None #prints False,since bar is matched at the beginning itself,so a match is found
print pattern.match(string, 3)

pattern = re.compile('bar')
print pattern.search('foobar') is None  #prints False
"""
search searches a string completly ,whereas compile match matches only the string that starts with the matching string
What are various methods of Regular Expressions?
re.match() re.search()
re.findall()
re.split()
re.sub()
re.compile()
Lets look at  all the examples for above
"""
print "=======================Match==============="
#1.re.match(pattern, string):
#This method finds match if it occurs at start of the string.For example, calling match() on the string 'AV Analytics AV' and looking for a pattern 'AV' will match. However, if we look for only Analytics, the pattern will not match. Let's perform it in python now.


result = re.match(r'AV', 'AV Analytics Vidhya AV')
print result
print result.group() #prints AV
# To print the matching string we'll use method group
print result.group(0) #prints AV
print result.start()
print result.end()

result = re.match(r'Analytics', 'AV Analytics Vidhya AV')
print result #prints None
print "=======================Search==============="
#2.re.search(pattern, string):
#It is similar to match() but it doesn't restrict us to find matches at the beginning of the string only. Unlike previous method, here searching for pattern 'Analytics' will return a match.
result = re.search(r'Analytics','AV Analytics Vidhya AV')
print result
print result.group(0)
#Here you can see that, search() method is able to find a pattern from any position of the string but it only returns the first occurrence of the search pattern.
print "=======================findall==============="
#3.re.findall (pattern, string):
#It helps to get a list of all matching patterns. It has no constraints of searching from start or end. If we will use method findall to search 'AV' in given string it will return both occurrence of AV. While searching a string, I would recommend you to use re.findall() always, it can work like re.search() and re.match() both.
result = re.findall(r'AV', 'AV Analytics Vidhya AV')
print result # Output: ['AV', 'AV']
print "=======================split==============="
#4.re.split(pattern, string, [maxsplit=0]):
#This methods helps to split string by the occurrences of given pattern.
result=re.split(r'y','Analytics')
print result # Output: ['Anal', 'tics']
#Above, we have split the string "Analytics" by "y". Method split() has another argument "maxsplit". It has default value of zero. In this case it does the maximum splits that can be done, but if we give value to maxsplit, it will split the string. Let's look at the example below:

result=re.split(r'i','Analytics Vidhya')
print result # Output: ['Analyt', 'cs V', 'dhya'] #It has performed all the splits that can be done by pattern "i".

result=re.split(r'i','Analytics Vidhya',maxsplit=1)
print result # Output: ['Analyt', 'cs Vidhya']
#Here, you can notice that we have fixed the maxsplit to 1. And the result is, it has only two values whereas first example has three values.
print "=======================sub==============="
#4.re.sub(pattern, repl, string):
#It helps to search a pattern and replace with a new sub string. If the pattern is not found, string is returned unchanged.
result=re.sub(r'India','the World','AV is largest Analytics community of India')
print result # Output: 'AV is largest Analytics community of the World'
print "=======================compile==============="
#5.re.compile(pattern, repl, string):

#We can combine a regular expression pattern into pattern objects, which can be used for pattern matching. It also helps to search a pattern again without rewriting it.
#using compile findall,search,match,sub,split can be done without rewriting again and again,very powerful
pattern=re.compile('AV')
print dir(pattern)
result=pattern.findall('AV Analytics Vidhya AV')
print result # ['AV', 'AV']
result2=pattern.findall('AV is largest analytics community of India')
print result2 # Output: ['AV']
print "=======================Matching examples==============="
#split all characters in the string including space
result = re.findall(r'.','AV is largest Analytics community of India')
print result #['A', 'V', ' ', 'i', 's', ' ', 'l', 'a', 'r', 'g', 'e', 's', 't', ' ', 'A', 'n', 'a', 'l', 'y', 't', 'i', 'c', 's', ' ', 'c', 'o', 'm', 'm', 'u', 'n', 'i', 't', 'y', ' ', 'o', 'f', ' ', 'I', 'n', 'd', 'i', 'a']
#split all characters in the string excluding space
result = re.findall(r'\w','AV is largest Analytics community of India1')
print result #['A', 'V', 'i', 's', 'l', 'a', 'r', 'g', 'e', 's', 't', 'A', 'n', 'a', 'l', 'y', 't', 'i', 'c', 's', 'c', 'o', 'm', 'm', 'u', 'n', 'i', 't', 'y', 'o', 'f', 'I', 'n', 'd', 'i', 'a','1']

#split the text by words including spaces
result = re.findall(r'\w*','AV is largest Analytics community of India1')
print result #['AV', '', 'is', '', 'largest', '', 'Analytics', '', 'community', '', 'of', '', 'India1', '']
#Again, it is returning space as a word because "*" returns zero or more matches of pattern to its left. Now to remove spaces we will go with "+".


#split the text by words excluding spaces
result = re.findall(r'\w+','AV is largest Analytics community of India1')
print result #['AV', 'is', 'largest', 'Analytics', 'community', 'of', 'India1']


#extract each word with ^
result=re.findall(r'^\w+','AV is largest Analytics community of India')
print result #['AV']
#extract each word with $
result=re.findall(r'\w+$','AV is largest Analytics community of India')
print result #['India']
result=re.findall(r'$\w+','AV is largest Analytics community of India')
print result #[]


#Return two characters in each word
result=re.findall(r'\w\w','AV is largest Analytics community of India')
print result #['AV', 'is', 'la', 'rg', 'es', 'An', 'al', 'yt', 'ic', 'co', 'mm', 'un', 'it', 'of', 'In', 'di']
result=re.findall(r'\w\w','AV is largest Analytics community of i India') #In this a will be ignored as the words having more than two characters is considered
print result #['AV', 'is', 'la', 'rg', 'es', 'An', 'al', 'yt', 'ic', 'co', 'mm', 'un', 'it', 'of', 'In', 'di']
#Return the first two character of each word
result=re.findall(r'\b\w\w','AV is largest Analytics community of i India') #In this a will be ignored as the words having more than two characters is considered
print result #['AV', 'is', 'la', 'An', 'co', 'of', 'In']


#Return the domain type of given email-ids
result=re.findall('@\w+','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz') 
print result #['@gmail', '@test', '@analyticsvidhya', '@rest']
result=re.findall('@(\w+)','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz') 
print result #['@gmail', '@test', '@analyticsvidhya', '@rest']
result=re.findall('@\w+.\w+','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz') 
print result #['@gmail', '@test', '@analyticsvidhya', '@rest']
#Return the username of given email-ids
result=re.findall('\w+@','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz') 
print result
result=re.findall('(\w+)@','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz') 
print result
#Extract only domain name using "( )"
result=re.findall(r'@\w+.(\w+)','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print result #['com', 'in', 'com', 'biz']

#Return date from given string
result=re.findall(r'\d{2}-\d{2}-\d{4}','Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print result #['12-05-2007', '11-11-2011', '12-01-2009']
result=re.findall(r'\d{2}-(\d{2})-(\d{4})','Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print result #returns a tuple [('05', '2007'), ('11', '2011'), ('01', '2009')]
#getting only year
result=re.findall(r'\d{2}-\d{2}-(\d{4})','Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print result #['2007', '2011', '2009']

#Return all words of a string those starts with vowel
# Return words starts with alphabets (using [])
result=re.findall(r'[aeiouAEIOU]\w+','AV is largest Analytics community of India')
print result #['AV', 'is', 'argest', 'Analytics', 'ommunity', 'of', 'India']
#Above you can see that it has returned "argest" and "ommunity" from the mid of words. To drop these two, we need to use "\b" for word boundary.
result=re.findall(r'\b[aeiouAEIOU]\w+','AV is largest Analytics community of India')
print result #['AV', 'is', 'Analytics', 'of', 'India']
result=re.findall(r'\b[^aeiouAEIOU]\w+','AV is largest Analytics community of India')
print result #[' is', ' largest', ' Analytics', ' community', ' of', ' India']
#to get the words that does not start with a vowel will be
result=re.findall(r'\b[^aeiouAEIOU ]\w+','AV is largest Analytics community of India')
print result #['largest', 'community']

#Validate a phone number (phone number must be of 10 digits and starts with 8 or 9)
li=['9999999999','999999-999','99999x9999']
for val in li:
	result = re.match(r'[8-9]{1}\d{9}',val)
			#OR
	#result = re.match(r'[8-9]{1}[0-9]{9}',val)
	if result:
		print 'yes'
	else:
		print 'no'
#prints yes no no 

#Split a string with multiple delimiters
line = 'asdf fjdk;afed,fjek,asdf,foo 123;456, 789' # String has multiple delimiters (";",","," ")
result= re.split(r'[;,\s]', line)
print result  #['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo', '123', '456', '', '789']
#The above can also be done with re.sub() to replace these multiple delimiters with one as space " ".
line = 'asdf fjdk;afed,fjek,asdf,foo 123;456, 789' # String has multiple delimiters (";",","," ")
result= re.sub(r'[;,\s]',' ', line)
print result #asdf fjdk afed fjek asdf foo 123 456  789

st= """<tr align="center"><td>1</td> <td>Noah</td> <td>Emma</td></tr>
<tr align="center"><td>2</td> <td>Liam</td> <td>Olivia</td></tr>
<tr align="center"><td>3</td> <td>Mason</td> <td>Sophia</td></tr>
<tr align="center"><td>4</td> <td>Jacob</td> <td>Isabella</td></tr>
<tr align="center"><td>5</td> <td>William</td> <td>Ava</td></tr>
<tr align="center"><td>6</td> <td>Ethan</td> <td>Mia</td></tr>
<tr align="center"><td>7</td> <td HTML>Michael</td> <td>Emily</td></tr>"""

result = re.findall(r'<tr align="center"><td>\w+</td> <td>(\w+)</td> <td>(\w+)</td></tr>',st)
print result #[('Noah', 'Emma'), ('Liam', 'Olivia'), ('Mason', 'Sophia'), ('Jacob', 'Isabella'), ('William', 'Ava'), ('Ethan', 'Mia')]
#\s or use the acual space
result = re.findall(r'<td>\w+</td>\s<td>(\w+)</td>\s<td>(\w+)</td>',st)
print result #[('Noah', 'Emma'), ('Liam', 'Olivia'), ('Mason', 'Sophia'), ('Jacob', 'Isabella'), ('William', 'Ava'), ('Ethan', 'Mia')]

#ipaddress matching
st= "some text has a ip:192.1.23.255 and some text again with another ip:1.2.1.213"
result =re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',st)
print result #['192.1.23.255', '1.2.1.213']
result =re.findall(r'ip:(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})',st)
print result #['192.1.23.255', '1.2.1.213']

#You can read html file using library urllib2 (see below code).

#import urllib2
#response = urllib2.urlopen('https://www.yahoo.com')
#html = response.read()
