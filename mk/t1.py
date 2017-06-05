from mock import mock,patch,Mock
import unittest as ut
from test import foo
#http://www.voidspace.org.uk/python/mock/mock.html
#http://www.voidspace.org.uk/python/mock/examples.html

mck = mock.MagicMock()
print dir(mck)
class yy(ut.TestCase):
	def test_tt(self):
		print self.assertTrue(True)
		with patch('test.foo') as pt:
			p = pt()
			p.rt()
			print "===="
			print "===="
			p.rt()
			print p.rt.called
			print p.rt.call_count

	def test_rr(self):
		print "==================="
		m = Mock()
		#m.rr.return_value='foo1'
		print m.rr().return_value
		m1=Mock(return_value='abc')
		print m1.return_value
		print "==================="

	@patch.object(foo,'ty')
	def test_t1(self,i):
		print self.assertTrue(True)
		print "=================>"
		print dir(i)
		print i
		i()
		print i.assert_called
		print "=================>"

ut.main()

