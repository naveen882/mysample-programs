#!/usr/bin/python3

#this runs on py3

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        try:
            return Singleton._instances[cls]
        except KeyError:
            obj = cls.__new__(cls, *args, **kwargs)
            cls.__init__(obj, *args, **kwargs)
            ret = Singleton._instances[cls] = obj
            return ret


class D(metaclass=Singleton):
    def __init__(self) -> None:
        self.x = 1

    def increment_thing(self) -> None:
        self.x += 1

    def get_thing(self) -> int:
        return self.x

d = D()    
print(d)    
#<__main__.D object at 0x7f20f8118588>
d1 = D()    
print(d1)
#<__main__.D object at 0x7f20f8118588>
print(d1 is d)
True
