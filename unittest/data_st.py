import json

def func1(**args):
    return {'a':1,'b':2}

def func2(*li):
    return [1,2,3,4,5]

def func3():
    a={'a':1,'id':2}
    j = json.dumps(a)
    return j
