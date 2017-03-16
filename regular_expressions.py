import re

pattern = re.compile('bar')
string = 'foobar'
print pattern.match(string) is None #prints True
print pattern.match(string, 3)

pattern = re.compile('bar')
print pattern.search('foobar') is None  #prints False
