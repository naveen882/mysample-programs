"""
The asyncio module provides tools for building concurrent applications using coroutines. While the threading module implements concurrency through application threads and multiprocessing implements concurrency using system processes, asyncio uses a single-threaded, single-process approach in which parts of an application cooperate to switch tasks explicitly at optimal times. Most often this context switching occurs when the program would otherwise block waiting to read or write data, but asyncio also includes support for scheduling code to run at a specific future time, to enable one coroutine to wait for another to complete, for handling system signals, and for recognizing other events that may be reasons for an application to change what it is working on.
https://pymotw.com/3/asyncio
"""
"""
what is event loop?

Event loop "is a programming construct that waits for and dispatches events or messages in a program". Basically an event loop lets you go, "when A happens, do B". 

what is a coroutine?

An asynchronous function in Python is typically called a 'coroutine', which is just a function that uses the async keyword, or one that is decorated with @asyncio.coroutine. 
"""
import asyncio
import time
import functools
import socket 
import sys
import logging
import os
import signal

#@asyncio.coroutine decorator for version < 3.5
#async def coroutine(): python 3.5
async def coroutine():
	print ("In coroutine")

event_loop = asyncio.get_event_loop()
try:
	print("Entering event loop")
	event_loop.run_until_complete(coroutine())
finally:
	print("Closing event loop")
	#event_loop.close()


async def coroutine():
	print ("In coroutine")
	return 'result'

event_loop = asyncio.get_event_loop()
try:
	print("Entering event loop")
	return_value = event_loop.run_until_complete(coroutine())
	print("it returned: {!r}".format(return_value))
finally:
	print("Closing event loop")
	#event_loop.close()

async def outer():
	print("In outer")
	print("Waiting for result1")
	result1 = await phase1()
	print("Waiting for result2")
	result2 = await phase2(result1)
	return (result1,result2)


async def phase1():
	print ("In phase1")
	return "result1"

async def phase2(arg):
	print ("In phase2")
	return "result derived from {}".format(arg)


event_loop = asyncio.get_event_loop()
try:
	print("Entering event loop")
	return_value = event_loop.run_until_complete(outer())
	print("it returned: {!r}".format(return_value))
finally:
	print("Closing event loop")
	#event_loop.close()

print ("==============================")
"""
"yield from" keyword can now be only be used with "@asyncio.coroutine" not with async definition
"""
@asyncio.coroutine
def outer():
	print("In outer")
	print("Waiting for result1")
	result1 = yield from phase1()
	print("Waiting for result2")
	result2 = yield from phase2(result1)
	return (result1,result2)


@asyncio.coroutine
def phase1():
	print ("In phase1")
	return "result1"

@asyncio.coroutine
def phase2(arg):
	print ("In phase2")
	return "result derived from {}".format(arg)


event_loop = asyncio.get_event_loop()
try:
	print("Entering event loop")
	return_value = event_loop.run_until_complete(outer())
	print("it returned: {!r}".format(return_value))
finally:
	print("Closing event loop")
	#event_loop.close()

print("=================Scheduling a Callback 'Soon'==================")
def callback():
	print('Callback invoked')

def stopper(loop):
	print("Stopper invoked")
	loop.stop() #if this is not called,the program will look out for the stop method to be called somewhere until unless program will not exit

event_loop = asyncio.get_event_loop()
try:
	print('Registering callbacks')
	event_loop.call_soon(callback)
	event_loop.call_soon(stopper,event_loop)
	print('Entering event loop')
	event_loop.run_forever()
finally:	
	print('Closing event loop')
	#event_loop.close();
print("=================Scheduling a Callback with a Delay==================")
def callback(n):
	print('Callback {} invoked'.format(n))

def stopper(loop):
	print("Stopper invoked")
	loop.stop() #if this is not called,the program will look out for the stop method to be called somewhere until unless program will not exit

event_loop = asyncio.get_event_loop()
try:
	print('Registering callbacks')
	event_loop.call_later(0.5,callback,1)
	event_loop.call_later(0.6,callback,2)
	event_loop.call_later(0.7,stopper,event_loop)
	event_loop.call_soon(callback,3)
	print('Entering event loop')
	event_loop.run_forever()
finally:	
	print('Closing event loop')
	#event_loop.close();
print("=================Scheduling a Callback for a Specific Time==================")
def callback(n,loop):
	print('Callback {} invoked at {}===='.format(n,loop.time()))

def stopper(loop):
	print("Stopper invoked at {}".format(loop.time()))
	loop.stop() #if this is not called,the program will look out for the stop method to be called somewhere until unless program will not exit

event_loop = asyncio.get_event_loop()
try:
	now =event_loop.time()
	print('clock time: {}===='.format(time.time()))
	print('loop time: {}'.format(now))
	print('Registering callbacks')
	event_loop.call_at(now + 0.2,callback,1,event_loop)
	#event_loop.call_later(0.2,callback,1,event_loop)
	event_loop.call_at(now + 0.1,callback,2,event_loop)
	#event_loop.call_later(0.1,callback,2,event_loop)
	event_loop.call_at(now + 0.3,stopper,event_loop)
	#event_loop.call_later(0.3,stopper,event_loop)
	event_loop.call_soon(callback,3,event_loop)
	print('Entering event loop')
	event_loop.run_forever()
finally:	
	print('Closing event loop')
	#event_loop.close();
	#The above code is not working and is posted @ http://stackoverflow.com/questions/38846962/asyncio-scheduling-callback-at-specific-time
print("=================Waiting for a Future==================")
def mark_done(future,result):
	print('Setting future result to {!r}'.format(result))
	future.set_result(result)
event_loop = asyncio.get_event_loop()
try:
	all_done = asyncio.Future()
	print('Scheduling mark_done')
	event_loop.call_soon(mark_done,all_done,'the result')
	print('Entering event loop')
	result = event_loop.run_until_complete(all_done)
	print('Returned result:{!r}'.format(result))
finally:
	print('Closing event loop')
	#event_loop.close();
print('Future result:{!r}'.format(all_done.result()))
print("=================Future Callbacks==================")
def callback(n,future):
	print('{}: future done: {}'.format(n,future.result()))
event_loop = asyncio.get_event_loop()
try:
	print('Registering callbacks on future')
	all_done = asyncio.Future()
	all_done.add_done_callback(functools.partial(callback,1))
	all_done.add_done_callback(functools.partial(callback,2))
	print('Setinng result of future')
	all_done.set_result('the result')

	print('Entering event loop')
	event_loop.run_until_complete(all_done)
finally:
	print('Closing event loop')
	#event_loop.close()
	#After future dataset has a result then also it can call functions
print("=================starting a task==================")
async def task_func():
	print("In task_func")
	return 'the result'

event_loop =asyncio.get_event_loop()
try:
	print('Creating task')
	task = event_loop.create_task(task_func())
	print('task: {!r}'.format(task))
	print('Entering event loop')
	return_value = event_loop.run_until_complete(task)
	print('task: {!r}'.format(task))
	print('return value: {!r}'.format(return_value))
finally:
	print('Closing event loop')
	#event_loop.close()
print('task result: {!r}'.format(task.result()))
print("=================cancelling a task==================")
async def task_func():
	print("In task_func")
	return 'the result'

event_loop =asyncio.get_event_loop()
try:
	print('Creating task')
	task = event_loop.create_task(task_func())
	print('Cancelling task')
	task.cancel()
	print('Entering event loop')
	return_value = event_loop.run_until_complete(task)
	print('task: {!r}'.format(task))
except asyncio.CancelledError:
	print('Caught error from cancelled task')
else:
	print('task result: {!r}'.format(task.result()))
finally:
	print('Closing event loop')
	#event_loop.close()
print("=================Notifying cancellation of a task after starting it==================")
async def task_func():
	print("In task_func, sleeping")
	try:
		await asyncio.sleep(1)
	except asyncio.CancelledError:
		print('task_func was cancelled')
		raise
	return 'the result'

async def task_canceller(t):
	print('In task canceller')
	t.cancel()
	print('cancelled the task')

event_loop =asyncio.get_event_loop()
try:
	print('Creating task')
	task = event_loop.create_task(task_func())
	return_value = event_loop.run_until_complete(task_canceller(task))
finally:
	print('Closing event loop')
	#event_loop.close()
print("=================Creating Tasks from Coroutines==================")
async def wrapped():
	print('wrapped')
	return 'result'

async def inner(task):
	print('inner: starting')
	print('inner: waiting for {!r}'.format(task))
	result = await task
	print('inner: task returned {!r}'.format(result))

async def starter():
	print('starter: creating task')
	task = asyncio.ensure_future(wrapped())
	print('starter: waiting for inner')
	await inner(task)
	print('starter: inner returned')

event_loop =asyncio.get_event_loop()
try:
	print('Entering event loop')
	task = event_loop.run_until_complete(starter())
finally:
	print('Closing event loop')
	#event_loop.close()

print("=================Waiting for Multiple Coroutines==================")
async def phase(i):
	print('in phase {}'.format(i))
	await asyncio.sleep(0.1 * i)
	print('done with phase {}'.format(i))
	return 'phase {} result'.format(i)

async def main(num_phases):
	print('starting main')
	phases= [phase(i) for i in range(num_phases)]
	print('Waiting for phases to complete')
	completed,pending = await asyncio.wait(phases)
	results = [t.result() for t in completed]
	print('results:{!r}'.format(results))

event_loop = asyncio.get_event_loop()
try:
	event_loop.run_until_complete(main(3))
finally:
	print('Closing event loop')
	#event_loop.close()
print("=================Waiting for Multiple Coroutines =>cancelled & pending task==================")
async def phase(i):
	print('in phase {}'.format(i))
	try:
		await asyncio.sleep(0.1 * i)
	except asyncio.CancelledError:
		print('phase {} cancelled'.format(i))
		raise
	else:
		print('done with phase {}'.format(i))
		return 'phase {} result'.format(i)

async def main(num_phases):
	print('starting main')
	phases= [phase(i) for i in range(num_phases)]
	print('Waiting 0.1 for phases to complete')
	completed,pending = await asyncio.wait(phases,timeout=0.1)
	print('{} completed and {} pending'.format(len(completed),len(pending),))
	if pending:
		print('Cancelling tasks')
		for t in pending:
			t.cancel()
	print('exiting main')

event_loop = asyncio.get_event_loop()
try:
	event_loop.run_until_complete(main(3))
finally:
	print('Closing event loop')
	#event_loop.close()
print("=================Gathering Results from Coroutines==================")
async def phase1():
	print('in phase1')
	await asyncio.sleep(2)
	print('done with phase1')
	return 'phase1 result'

async def phase2():
	print('in phase2')
	await asyncio.sleep(1)
	print('done with phase2')
	return 'phase2 result'

async def main():
	print('starting main')
	print('Waiting for phases to complete')
	results = await asyncio.gather(phase1(),phase2(),)
	print('results: {!r}'.format(results))

event_loop = asyncio.get_event_loop()
try:
	event_loop.run_until_complete(main())
finally:
	print('Closing event loop')
	#event_loop.close()
print("=================Handling Background Operations as They Finish==================")
async def phase1(i):
	print('in phase1')
	await asyncio.sleep(0.5 - (0.1 * i))
	print('done with phase {}'.format(i))
	return 'phase {} result'.format(i)

async def main(num_phases):
	print('starting main')
	phases= [phase(i) for i in range(num_phases)]
	print('Waiting for phases to complete')
	results = []
	for next_to_complete in asyncio.as_completed(phases):
		answer = await next_to_complete
		print('received answer {!r}'.format(answer))
		results.append(answer)
	print('results: {!r}'.format(results))
	return results

event_loop = asyncio.get_event_loop()
try:
	event_loop.run_until_complete(main(3))
finally:
	print('Closing event loop')
	#event_loop.close()
print("=================Synchronization Primitives - Locks==================")
def unlock(lock):
	print('Callback releasing lock')
	lock.release()

async def coro1(lock):
	print('Coro1 waiting for the lock')
	with await lock:
		print('corol lock acquired')
	print('Corol released lock')

async def coro2(lock):
	print('Coro2 waiting for the lock')
	await lock
	try:
		print('coro2 lock acquired')
	finally:
		print('Coro2 released lock')
		lock.release()

event_loop = asyncio.get_event_loop()
try:
	#create and acquired a shared lock
	lock = asyncio.Lock()
	print('Acquiring the lock before starting coroutines')
	event_loop.run_until_complete(lock.acquire())
	print('lock acquired: {}'.format(lock.locked()))
	#schedule a callback to unlock the lock
	event_loop.call_later(0.1,functools.partial(unlock,lock))
	#Run the coroutines that want to use the lock
	print('Entering event loop')
	event_loop.run_until_complete(asyncio.wait([coro1(lock),coro2(lock)]),)
	print('Exited event loop')
	print('lock status: {}'.format(lock.locked()))
finally:
	print('Closing event loop')
	#event_loop.close()
print("=================Synchronization Primitives - Events==================")
def set_event(event):
	print('setting event in callback')
	event.set()

async def coro1(lock):
	print('Coro1 waiting for event')
	await event.wait()
	print('Coro1 triggered')

async def coro2(lock):
	print('Coro2 waiting for event')
	await event.wait()
	print('Coro2 triggered')
event_loop = asyncio.get_event_loop()
try:
	#create and acquired a shared lock
	event = asyncio.Event()
	print('event state:{}'.format(event.is_set()))
	event_loop.call_later(0.1,functools.partial(set_event,event))
	print('Entering event loop')
	event_loop.run_until_complete(asyncio.wait([coro1(event),coro2(event)]),)
	print('Exited event loop')
	print('event status: {}'.format(lock.locked()))
finally:
	print('Closing event loop')
	#event_loop.close()
print("=================Synchronization Primitives - Conditions==================")
async def consumer(condition,n):
	with await condition:
		print('Consumer {} is awaiting'.format(n))
		await condition.wait()
		print('consumer {} triggered'.format(n))
	print('ending consumer {}'.format(n))

async def manipulate_condition(condition):
	print('starting manipulate condition')
	await asyncio.sleep(0.1)
	for i in range(1,3):
		with await condition:
			print('notifying {}'.format(i))
			condition.notify(n=i)
		await asyncio.sleep(0.1)
	with await condition:
		print('notifying remaining')
		condition.notify_all()
	print('ending manipulate condition')
	
event_loop = asyncio.get_event_loop()
try:
	#create and acquired a shared lock
	condition= asyncio.Condition()
	consumers = [ consumer(condition,i) for i in range(5)]
	event_loop.create_task(manipulate_condition(condition))
	print('Entering event loop')
	event_loop.run_until_complete(asyncio.wait(consumers),)
	print('Exited event loop')
finally:
	print('Closing event loop')
	#event_loop.close()
print("=================Synchronization Primitives - Conditions==================")
async def consumer(condition,n):
	with await condition:
		print('Consumer {} is awaiting'.format(n))
		await condition.wait()
		print('consumer {} triggered'.format(n))
	print('ending consumer {}'.format(n))

async def manipulate_condition(condition):
	print('starting manipulate condition')
	await asyncio.sleep(0.1)
	for i in range(1,3):
		with await condition:
			print('notifying {}'.format(i))
			condition.notify(n=i)
		await asyncio.sleep(0.1)
	with await condition:
		print('notifying remaining')
		condition.notify_all()
	print('ending manipulate condition')
	
event_loop = asyncio.get_event_loop()
try:
	#create and acquired a shared lock
	condition= asyncio.Condition()
	consumers = [ consumer(condition,i) for i in range(5)]
	event_loop.create_task(manipulate_condition(condition))
	print('Entering event loop')
	event_loop.run_until_complete(asyncio.wait(consumers),)
	print('Exited event loop')
finally:
	print('Closing event loop')
	#event_loop.close()
print("=================Synchronization Primitives - Queue==================")
async def consumer(n,q):
	print('consumer {}:starting'.format(n))
	while True:
		print('Consumer {}:Waiting for Item'.format(n))
		item =await q.get()
		print('Conssumer {}: has item{}'.format(n,item))
		if item is None:
			q.task_done()
			break
		else:
			await asyncio.sleep(0.01*item)
			q.task_done()
	print('consumer {}:ending'.format(n))

async def producer(q,num_workers):
	print('producer: starting')
	#Add some numbers to the queue to simulate jobs
	for i in range(num_workers * 3):
		await q.put(i)	
		print('producer: added task {} to the queue'.format(i))
	#Add none entries on ther queue
	#to signal the consumers to exit
	print('producer:asssing stop signals to the queue')
	for i in range(num_workers):
		await q.put(None)
	print('producer:waiting for queue to empty')
	await q.join()
	print('producer ending')

event_loop = asyncio.get_event_loop()
try:
	num_consumers = 2
	#create the queue with a fixed size so the producer will block until the consumers pull some items out
	q= asyncio.Queue(maxsize=num_consumers)
	#scheduled the consumer tasks
	consumers = [ event_loop.create_task(consumer(i,q)) for i in range(num_consumers)]
	prod = event_loop.create_task(producer(q,num_consumers))
	#wait for all of the coroutines to finish
	print('Entering event loop')
	event_loop.run_until_complete(asyncio.wait(consumers +[prod]),)
	print('Exited event loop')
finally:
	print('Closing event loop')
	#event_loop.close()
print("=================Interacting with Domain Name Services==================")
targets = [('pymotw.com', 'https'), ('doughellmann.com', 'https'), ('python.org', 'https'),]
event_loop = asyncio.get_event_loop()
try:
	for target in targets:
		info = event_loop.run_until_complete(event_loop.getaddrinfo(*target,proto=socket.IPPROTO_TCP,))
	for host in info:
		print(host)
		print('{:20}: {}'.format(target[0],host[4][0]))
finally:
	print('Closing event loop')
	#event_loop.close()
print("=================Name Lookup by Address==================")
targets = [ ('66.33.211.242', 443), ('104.130.43.121', 443), ]

event_loop = asyncio.get_event_loop()
try:
	for target in targets:
		info = event_loop.run_until_complete(event_loop.getnameinfo(target))
		#print(info)
		print('{:15}: {} {}'.format(target[0],*info))
finally:
	print('Closing event loop')
	#event_loop.close()
print("=================Receiving signals==================")
def signal_handler(name):
		print('signal_handler({!r})'.format(name))


event_loop = asyncio.get_event_loop()
try:
	event_loop.add_signal_handler(signal.SIGHUP,functools.partial(signal_handler,'SIGHUP'),)
	event_loop.add_signal_handler(signal.SIGUSR1,functools.partial(signal_handler,'SIGUSR1'),)
	event_loop.add_signal_handler(signal.SIGINT,functools.partial(signal_handler,'SIGINT'),)
finally:
	print('Closing event loop')
	#event_loop.close()
print("=================Sending signals==================")
async def send_signals():
	pid = os.getpid()
	print('starting sending signals for {}'.format(pid))
	await asyncio.sleep(5)

	for name in ['SIGHUP','SIGHUP','SIGUSR1','SIGINT']:
		print('sending {}'.format(name))
		os.kill(pid,getattr(signal,name))
		#yield control to allow the signal handler to run,
		#since the signal does not interrupt the program flow otherwise
		print('Yielding control')
		await asyncio.sleep(0.01)
	return

event_loop = asyncio.get_event_loop()
try:
	event_loop.run_until_complete(send_signals())	
finally:
	print('Closing event loop')
	event_loop.close()
