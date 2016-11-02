class A(object):
	_dict = dict()

	def __new__(cls):
		if 'key' in A._dict:
			print "Exists"
			print A._dict
			#print str(cls) + "===="
			return A._dict['key']
		else:
			print A._dict
			print "NEW"
			return super(A,cls).__new__(cls)

	def __init__(self):
		print "INIT"
		A._dict['key'] = self
		print ""

a1=A() #print NEW INIT
a2=A() #print EXISTS INIT
a3=A() #print EXISTS INIT
	
"""
    Use __new__ when you need to control the creation of a new instance. Use __init__ when you need to control initialization of a new instance.

    __new__ is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class. In contrast, __init__ doesn't return anything; it's only responsible for initializing the instance after it's been created.

    In general, you shouldn't need to override __new__ unless you're subclassing an immutable type like str, int, unicode or tuple.
"""
