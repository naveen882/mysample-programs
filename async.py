"""
The asyncio module provides tools for building concurrent applications using coroutines. While the threading module implements concurrency through application threads and multiprocessing implements concurrency using system processes, asyncio uses a single-threaded, single-process approach in which parts of an application cooperate to switch tasks explicitly at optimal times. Most often this context switching occurs when the program would otherwise block waiting to read or write data, but asyncio also includes support for scheduling code to run at a specific future time, to enable one coroutine to wait for another to complete, for handling system signals, and for recognizing other events that may be reasons for an application to change what it is working on.
https://pymotw.com/3/asyncio
"""
import asyncio
import time
import functools

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
	event_loop.close()
