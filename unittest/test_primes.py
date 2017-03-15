import unittest
from primes import is_prime
from data_st import func1,func2,func3
import json

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

    def test_is_four_non_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertFalse(is_prime(4),msg='4 is not a prime number')
    
    def test_is_zero_not_prime(self):
        """Is zero correctly determined not to be prime?"""
        self.assertFalse(is_prime(0))

    def test_negative_number(self):
        """Is a negative number correctly determined not to be prime?"""
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index))

    def test_negative_number1(self):
        """Is a negative number correctly determined not to be prime?"""
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-3))
        self.assertFalse(is_prime(-4))
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-6))
        self.assertFalse(is_prime(-7))
        self.assertFalse(is_prime(-8))
        self.assertFalse(is_prime(-9))

class TestDict(unittest.TestCase):
    def test_is_not_same_dict(self):
        d2={'a':1}
        self.assertNotEqual(func1(), d2)

    def test_is_same_dict(self):
        d2={'a':1,'b':2}
        self.assertEqual(func1(), d2)

    def test_contains_same_dict(self):
        print dir(self)
        d2={'a':1,'b':2}
        self.assertIn('a', func1()) #'key present in dict'

    def test_dict_keyerror_should_appear(self):
        my_dict = {'hey': 'world'}
        self.assertRaises(KeyError, lambda: my_dict['some_key']) #key not present in dict

class TestList(unittest.TestCase):
    def test_is_not_same_list(self):
        l2=[1,2,3,6]
        self.assertNotEqual(func2(), l2)

    def test_is_same_list(self):
        l2=[1,2,3,4,5]
        self.assertListEqual(func2(), l2)

    def test_contains_same_ele(self):
        l=3
        self.assertIn(l, func2()) #'element present in list'

    def test_dict_keyerror_should_appear(self):
        my_dict = {'hey': 'world'}
        self.assertRaises(KeyError, lambda: my_dict['some_key']) #key not present in dict

class Testjson(unittest.TestCase):
    def test_is_not_same_json(self):
        a={'a':1,'b':2}
        self.assertNotEqual(func3(), json.dumps(a))

    def test_is_same_json(self):
        a={'a':1,'id':2}
        self.assertEqual(func3(), json.dumps(a))

    def test_contains_same_ele(self):
        l='id'
        self.assertIn(l, func3()) #'element present in list'




if __name__ == '__main__':
    unittest.main()
    assert 1 ==2

"""
In the following code all the classes will be called automatically when run as python test_primes.py since unitest.main() is called

Now to run a specific test or one class test use the following #python % TestDict.test_contains_same_dict or python % TestDict

the various asserts available are print dir(self) and the result is 

['__call__', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_addSkip', '_baseAssertEqual', '_classSetupFailed', '_cleanups', '_deprecate', '_diffThreshold', '_formatMessage', '_getAssertEqualityFunc', '_resultForDoCleanups', '_testMethodDoc', '_testMethodName', '_truncateMessage', '_type_equality_funcs', 'addCleanup', 'addTypeEqualityFunc', 'assertAlmostEqual', 'assertAlmostEquals', 'assertDictContainsSubset', 'assertDictEqual', 'assertEqual', 'assertEquals', 'assertFalse', 'assertGreater', 'assertGreaterEqual', 'assertIn', 'assertIs', 'assertIsInstance', 'assertIsNone', 'assertIsNot', 'assertIsNotNone', 'assertItemsEqual', 'assertLess', 'assertLessEqual', 'assertListEqual', 'assertMultiLineEqual', 'assertNotAlmostEqual', 'assertNotAlmostEquals', 'assertNotEqual', 'assertNotEquals', 'assertNotIn', 'assertNotIsInstance', 'assertNotRegexpMatches', 'assertRaises', 'assertRaisesRegexp', 'assertRegexpMatches', 'assertSequenceEqual', 'assertSetEqual', 'assertTrue', 'assertTupleEqual', 'assert_', 'countTestCases', 'debug', 'defaultTestResult', 'doCleanups', 'fail', 'failIf', 'failIfAlmostEqual', 'failIfEqual', 'failUnless', 'failUnlessAlmostEqual', 'failUnlessEqual', 'failUnlessRaises', 'failureException', 'id', 'longMessage', 'maxDiff', 'run', 'setUp', 'setUpClass', 'shortDescription', 'skipTest', 'tearDown', 'tearDownClass', 'test_contains_same_dict', 'test_dict_keyerror_should_appear', 'test_is_not_same_dict', 'test_is_same_dict']

Also refer unit_test.py for various assert statements

"""
