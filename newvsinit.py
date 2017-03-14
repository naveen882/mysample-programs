#https://concentricsky.com/articles/detail/pythons-hidden-new

class NewedBaseCheck(object):
    def __new__(cls):
        print "In new"
        obj = super(NewedBaseCheck,cls).__new__(cls)
        obj._from_base_class = type(obj) == NewedBaseCheck
        return obj
    def __init__(self):
        print "In init"
        self.x = 5

newed = NewedBaseCheck()
print newed.x == 5
print newed._from_base_class is True
print "==============="
class StandardBaseCheck(object):
    def __init__(self):
        print type(self)
        print StandardBaseCheck
        self.x = 5
        self._from_base_class = type(self) == StandardBaseCheck

standard_base_check = StandardBaseCheck()
print standard_base_check.x == 5
print standard_base_check._from_base_class is True

class SubNewedBaseCheck(NewedBaseCheck):
    def __init__(self):
        self.x = 9

subnewed = SubNewedBaseCheck()
print subnewed.x == 9
print subnewed._from_base_class is False

class SubStandardBaseCheck(StandardBaseCheck):
    def __init__(self):
        self.x = 9

substandard_base_check = SubStandardBaseCheck()
print substandard_base_check.x == 9
print hasattr(substandard_base_check,"_from_base_class") is False


class NewedBaseCheck(object):
    def __new__(cls):
        obj = super(NewedBaseCheck,cls).__new__(cls)
        obj._from_base_class = type(obj) == NewedBaseCheck
        return obj

    def __init__(self, x):
        self.x = x

try:
    NewedBaseCheck(5)
except Exception as e:
    print "In exceptionnnnnn"
    print str(e)
    print True


class NewedBaseCheck(object):
    def __new__(cls, x):
        obj = super(NewedBaseCheck,cls).__new__(cls)
        obj._from_base_class = type(obj) == NewedBaseCheck
        return obj

    def __init__(self, x):
        print "In init"
        self.x = x

newed = NewedBaseCheck(5)
print newed.x == 5

print "=====================very important===================="
class NewedBaseCheck(object):
    def __new__(cls, *args, **kwargs):
        print "In new"
        obj = super(NewedBaseCheck,cls).__new__(cls)
        obj._from_base_class = type(obj) == NewedBaseCheck
        return obj

    def __init__(self, x,y=None):
        print "In init"
        self.x = x
        self.y=y

newed = NewedBaseCheck(5)
newed.x == 5

subnewed = NewedBaseCheck(5,6)
print subnewed.x == 5
print subnewed.y == 6


#If __new__ doesn't return an instance of the class it's bound to (e.g. GimmeFive), it skips the Constructor Step entirely:

class GimmeFive(object):
    def __new__(cls, *args, **kwargs):
        return 5

    def __init__(self,x):
        self.x = x

five = GimmeFive()
five == 5
print isinstance(five,int) is True
print hasattr(five, "x") is False

def instantiate(cls, *args, **kwargs):
    obj = cls.__new__(cls, *args, **kwargs)
    if isinstance(obj,cls):
        cls.__init__(obj, *args, **kwargs)
    return obj


print "============="
print instantiate(GimmeFive) == 5
newed = instantiate(NewedBaseCheck, 5)
print type(newed) == NewedBaseCheck
print newed.x == 5
print "============="
class A(object):
    def __new__(cls):
        print "In A new"
        return super(A,cls).__new__(B)
    def __init__(self):
        print "In A init"
        self.name = "A"
    def create(self):
        print "In A create"

class B(object):
    def __new__(cls):
        print "In B new"
        return super(B,cls).__new__(A)
    def __init__(self):
        print "In B init"
        self.name = "B"
    def create(self):
        print "In B create"

a = A()
a.create()
b=B()
b.create()
print type(a) == A
print type(b) == B
print hasattr(a,"name") == False
