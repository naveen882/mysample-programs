import asyncio
import os

def callback(n):
	print('Callback {} invoked'.format(n))
	i=0
	os.system("> /tmp/aa")
	while i < 100000:
		print(i)
		i += 1

def stopper(loop):
    print("Stopper invoked")
    loop.stop() #if this is not called,the program will look out for the stop method to be called somewhere until unless program will not exit

event_loop = asyncio.get_event_loop()
try:
    print('Registering callbacks')
    #event_loop.call_later(10,callback,1)
    #event_loop.call_later(10,callback,2)
    #event_loop.call_later(11,stopper,event_loop)
    #now =event_loop.time()
    #event_loop.call_at(now + 300,callback,3)
    #event_loop.call_at(now+301,stopper,event_loop)
    #event_loop.async(now+301,stopper,event_loop)
    asyncio.async(callback(1))
    print("======")
    print("======")
    print("======")
    print("======")
    print("======")
    print("======")
    print('Entering event loop')
    event_loop.run_forever()
finally:
    print('Closing event loop')
    event_loop.close();
