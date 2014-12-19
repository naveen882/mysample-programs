"""
Metaclass
http://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example

A metaclass is defined as "the class of a class". Any class whose instances are themselves classes, is a metaclass. So, according to what we've seen above, this makes type a metaclass - in fact, the most commonly used metaclass in Python, since it's the default metaclass of all classes.

Since a metaclass is the class of a class, it is used to construct classes (just as a class is used to construct objects). But wait a second, don't we create classes with a standard class definition? Definitely, but what Python does under the hood is the following:

When it sees a class definition, Python executes it to collect the attributes (including methods) into a dictionary.
When the class definition is over, Python determines the metaclass of the class. Let's call it Meta
Eventually, Python executes Meta(name, bases, dct), where:
Meta is the metaclass, so this invocation is instantiating it.
name is the name of the newly created class
bases is a tuple of the class's base classes
dct maps attribute names to objects, listing all of the class's attributes
How do we determine the metaclass of a class? Simply stated [4], if either a class or one of its bases has a __metaclass__ attribute [5], it's taken as the metaclass. Otherwise, type is the metaclass.

So what happens when we define:

class MyKlass(object):
  foo = 2
Is this: MyKlass has no __metaclass__ attribute, so type is used instead, and the class creation is done as:

MyKlass = type(name, bases, dct)
Which is consistent to what we've seen in the beginning of the article. If, on the other hand, MyKlass does have a metaclass defined:

class MyKlass(object):
  __metaclass__ = MyMeta
  foo = 2
Then the class creation is done as:

MyKlass = MyMeta(name, bases, dct)
So MyMeta should be implemented appropriately to support such calling form and return the new class. It's actually similar to writing a normal class with a pre-defined constructor signature.

Metaclass's __new__ and __init__
To control the creation and initialization of the class in the metaclass, you can implement the metaclass's __new__ method and/or __init__ constructor [6]. Most real-life metaclasses will probably override just one of them. __new__ should be implemented when you want to control the creation of a new object (class in our case), and __init__ should be implemented when you want to control the initialization of the new object after it has been created.

So when the call to MyMeta is done above, what happens under the hood is this:

MyKlass = MyMeta.__new__(MyMeta, name, bases, dct)
MyMeta.__init__(MyKlass, name, bases, dct)
Here's a more concrete example that should demonstrate what's going on. Let's write down this definition for a metaclass:

class MyMeta(type):
    def __new__(meta, name, bases, dct):
        print '-----------------------------------'
        print "Allocating memory for class", name
        print meta
        print bases
        print dct
        return super(MyMeta, meta).__new__(meta, name, bases, dct)
    def __init__(cls, name, bases, dct):
        print '-----------------------------------'
        print "Initializing class", name
        print cls
        print bases
        print dct
        super(MyMeta, cls).__init__(name, bases, dct)
When Python executes the following class definition:

class MyKlass(object):
    __metaclass__ = MyMeta

    def foo(self, param):
        pass

    barattr = 2
What gets printed is this (reformatted for clarity):

-----------------------------------
Allocating memory for class MyKlass
<class '__main__.MyMeta'>
(<type 'object'>,)
{'barattr': 2, '__module__': '__main__',
 'foo': <function foo at 0x00B502F0>,
 '__metaclass__': <class '__main__.MyMeta'>}
-----------------------------------
Initializing class MyKlass
<class '__main__.MyKlass'>
(<type 'object'>,)
{'barattr': 2, '__module__': '__main__',
 'foo': <function foo at 0x00B502F0>,
 '__metaclass__': <class '__main__.MyMeta'>}
Study and understand this example and you'll grasp most of what one needs to know about writing metaclasses.

It's important to note here that these print-outs are actually done at class creation time, i.e. when the module containing the class is being imported for the first time. Keep this detail in mind for later.

Metaclass's __call__
Another metaclass method that's occasionally useful to override is __call__. The reason I'm discussing it separately from __new__ and __init__ is that unlike those two that get called at class creation time, __call__ is called when the already-created class is "called" to instantiate a new object. Here's some code to clarify this:

class MyMeta(type):
    def __call__(cls, *args, **kwds):
        print '__call__ of ', str(cls)
        print '__call__ *args=', str(args)
        return type.__call__(cls, *args, **kwds)

class MyKlass(object):
    __metaclass__ = MyMeta

    def __init__(self, a, b):
        print 'MyKlass object with a=%s, b=%s' % (a, b)

print 'gonna create foo now...'
foo = MyKlass(1, 2)
This prints:

gonna create foo now...
__call__ of  <class '__main__.MyKlass'>
__call__ *args= (1, 2)
MyKlass object with a=1, b=2
Here MyMeta.__call__ just notifies us of the arguments and delegates to type.__call__. But it can also interfere in the process, affecting the way objects of the class are created. In a way, this is not unlike overriding the __new__ method of the class itself, although there are some differences [7].

"""

class MyMeta(type):
    def __new__(meta, name, bases, dct):
        print '-----------------------------------'
        print "Allocating memory for class", name
        print meta #prints <class '__main__.MyMeta'>
        print bases #prints object
        print dct #prints __module__:foo
        print super(MyMeta, meta).__new__(meta, name, bases, dct)
        return super(MyMeta, meta).__new__(meta, name, bases, dct)
    def __init__(cls, name, bases, dct):
        print '-----------------------------------'
        print "Initializing class", name #Initializing class MyKlass
        print cls #prints <class '__main__.MyKlass'>
        print bases #prints (<type 'object'>,)
        print dct #prints {'__module__': '__main__', 'foo': <function foo at 0x7fe60c1f56e0>, '__metaclass__': <class '__main__.MyMeta'>}
        print super(MyMeta, cls)
        super(MyMeta, cls).__init__(name, bases, dct)

class MyKlass(object):
    __metaclass__ = MyMeta

    def foo(self, param):
        pass
