#returning some other object instead os the correct object hack
class k(object):
    def __init__(self):
        print "In k"



class t(object):
    def __new__(cls):
        print "In new"
        print cls.__name__
        if cls.__name__ == 'y':
            class rt(t):
                def __init__(self):
                    print "In rt"
                def new1(self):
                    print "In new1"
            
            r =rt()
            return  r
        else:
            print "In else"
            return super(t,cls).__new__(cls)
    def __init__(self):
        print "In t init"

class y(t):
    def __new__(cls):
        print "In new11"
        return super(y,cls).__new__(cls)
    def __init__(self):
        print "In y init"
    def r(self):
        print "In r"

obj1=y()
obj1.new1()
