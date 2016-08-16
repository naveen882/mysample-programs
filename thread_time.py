from threading import Thread
import time

def func1(a):
	print 'Working'
	print a
	print time.time()

def func2(a):
	print 'Working'
	print a
	print time.time()

if __name__ == '__main__':
    Thread(target = func1,args=(1,)).start()
    Thread(target = func2,args=(2,)).start()
