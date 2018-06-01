from mock import Mock,patch

import unittest
from os_simple import rt


class Test_Mock(unittest.TestCase):
	def test_rt(self):
		with patch("os.system") as os:
			print "here"
			rt()
			#print os.system.asser_called_with("ls -lrt")
			self.assertTrue(os.system.asser_called_with ,"ls -lrt")
			#self.assertFalse(os.system.asser_called_with ,"ls -lrt")  ## This will give an error
			print "here====="


if __name__ == '__main__':
	unittest.main()
		
