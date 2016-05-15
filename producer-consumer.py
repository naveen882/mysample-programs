from threading import Thread,Lock,Condition
import time
import random
from Queue import Queue

queue = []
#lock=Lock()
#Instead of Lock we use cindtion which can loack and also notify
condition = Condition()
max_len=10

class ProducerThread(Thread):
	def run(self):
		nums = range(5)
		global queue
		while True:
			num = random.choice(nums)
			print "num %s"%(num)
			#lock.acquire()
			condition.acquire()
			if len(queue) == max_len:
				print "Queue full ,producer waiting"
				condtition.wait()
				print "space in queue,consumer notified the producer"		
			queue.append(num)
			print "Produced num %s"%(num)
			condition.notify()
			condition.release()
			#lock.release()
			time.sleep(random.random())


class ConsumerThread(Thread):
	def run(self):
		global queue
		while True:
			#lock.acquire()
			condition.acquire()
			if not queue:
				print "Nothing in queue,but consumer will try to consume"
				condition.wait()
				print "Producer produced something into the queue"
			num = queue.pop(0)
			print "consumed num %s"%(num)
			condition.release()
			#lock.release()
			time.sleep(random.random())

pt = ProducerThread()
ct = ConsumerThread()
pt.start()
ct.start()
print "================Implementing the above by a queue================"

queue = Queue(10)
class ProducerQThread(Thread):
	def run(self):
		nums = range(5)
		global queue
		while True:
			num= random.choice(nums)
			queue.put(num)
			print "produced",num
			time.sleep(random.random())
			
class ConsumerQThread(Thread):
	def run(self):
		global queue
		while True:
			queue.get()
			queue.task_done()
			print "Consumed",num
			time.sleep(random.random())
			

pt1 = ProducerQThread()
ct1 = ConsumerQThread()
pt1.start()
ct1.start()
