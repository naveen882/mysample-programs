from mock import mock,patch,Mock
import unittest as ut

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

ut.main()

