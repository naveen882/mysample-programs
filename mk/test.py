#

from mock import MagicMock,Mock

class ProductionClass:
	def method(self):
		print "In methid"
		self.something(1, 2,3)
	def something(self, a, b,c):
		print "In something"
		pass
	def thing(self, a, b,c):
		print "In something"
		pass
	def closer(self,something):
		something.close()
	def rt(self,a):
		print a

real = ProductionClass()
real.something = MagicMock()
real.method()
real.something.assert_called_once_with(1, 2,3) #This is to ensure that previously the method was called using the same values
# OR IN this both can be used
real.something.assert_called_with(1, 2,3) #This is to ensure that previously the method was called using the same values
real.thing=MagicMock()
real.thing(4,5,6)
real.thing.assert_called_with(4,5,6)
real.thing.assert_called_once_with(4,5,6)
mock=Mock()
real.closer(mock)
mock.close.assert_called_with()
#We don't have to do any work to provide the 'close' method on our mock. Accessing close creates it. So, if 'close' hasn't already been called then accessing it in the test will create it, but assert_called_with() will raise a failure exception.

#assert_that_called_once_with
#assert_called_once
#assert_called
#assert_once_called

#assert_called
#Assert that the mock was called at least once.
m = Mock()
m.method(real.rt(1))
m.method.assert_called()

#assert_called_once
#Assert that the mock was called exactly once.
m.method.assert_called_once()
m.method.assert_once_called()
m.method(real.rt(1))
#m.method.assert_called_once()
