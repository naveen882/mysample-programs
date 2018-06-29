class A(object):
    def __init__(self):
        self.a =True
        
    def rt(self):
        return self.a
    
    def show(self):
        a = self.rt()                  
        return a

a=A()
print "===="
a.show()


class test_A(TestCase):

    def test_A(self):
        print "In A======"
        a=A()
        self.assertFalse(a.show())
        
unittest.main()
#https://docs.python.org/3.3/library/unittest.mock-examples.html
