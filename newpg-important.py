"""
Id:          $Id: $
Copyright:   2018 J.P. Morgan Chase & Co. Incorporated.  All rights reserved.
Type:        util
Sensitive:   RCMOTech
Platform:    Windows 32bit
Description: server commands module for fdw reports created by created by naveen.x.kumars
"""

import lib.compatibility
lib.compatibility.assertPlatform()
from atom.api import Value, Atom, Str, Int,Bool, observe




#def ApplyFilter(f):
#    def rt(self,data):
#        print f.__name__
#        return f(self,data)
#    return rt

from functools import update_wrapper, partial

class ApplyFilter():
        def __init__(self,f):
            #update_wrapper(self, f)
            print "In init"
            self.f = f 

        def __get__(self, obj, objtype):
            """Support instance methods."""
            return partial(self.__call__, obj)

        def __call__(self,obj,args):
            #return self.__wrapped__(*args, **kwargs)
            print "Calling function"
            print args
            print "===="
            return self.f(obj, args)

##Apply_Adjustments = ApplyAdjustments

class Test(object):
    #a=1
    #def __init__(self):
    #    self.a = 1

    @ApplyAdjustments
    def myfunc(self,data):
        print "===="
        print "In my func and args in  {0}  ".format(data)
        print self.a

a=[1,2,3,4]
b={'a':1}
t=Test()
t.myfunc("Args 12345")


class ApplyFilter(object):
    def __init__(self, func):
        #update_wrapper(self, func)
        self.func = func

    def __get__(self, obj, objtype):
        """Support instance methods."""
        return partial(self.__call__, obj)

    def __call__(self, obj, args):
        print('Logic here')
        return self.func(obj, args)

#my_decorator = MyDecorator

class MyClass(object):
     @ApplyFilter
     def my_method(self,a):
         print "In mymrthod {0}".format(a)
         pass

mt = MyClass()
mt.my_method("Got the arguments passed")



class ApplyFilter(object):
        def __init__(self,func):
            print "In init"
            self.func = func 
        def __call__(self,args):
            print "In call"
            #args['summary']['effect_of_double_default_treatment_on_rwa'] = 456
            #args['memoranda']['risk_weighted_assets_associated_with_non_material_portfolios_not_included_above'] = 789
            #args['exp_to_wholesale']['weighted_average_lgd_before_consideration_of_eligible_guarantees_and_credit_derivatives'] = 123
            #args['exp_to_wholesale']['expected_credit_loss'] = 101112
            self.func(args)


#The descriptor is how Python's property type is implemented. A descriptor simply implements __get__, __set__, etc. and is then added to another class in its definition (as you did above with the Temperature class). For example:

temp=Temperature()
temp.celsius #calls celsius.__get__


class Celsius(object):
    def __init__(self):
        pass
    
    def __get__(self, obj, objclass):
        return self.__call__(obj)
    
    def __set__(self, instance, value):
        self.value = float(value)
    
    def __call__(self,obj):
        return obj.tt(123)
   


class Temperature(object):
    celsius = Celsius()
    def tt(self,a):
        return "In tt {0}".format(a)
    

def __get__():
    print "get Main"

temp=Temperature()
print temp.celsius

class T(object):
    pass
    #def __call__(self):
    #    return "Hi"

t = T()
print t()

