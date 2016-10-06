class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        print "In property x"
        return self._x

    @x.setter
    def x(self, value):
        print "In setter x"
        self._x = value

    @x.getter
    def x(self):
        print "In getter x"
        return self._x

    @x.deleter
    def x(self):
        print "In deletter x"
        del self._x


c=C()
c.x = 1
print c.x
