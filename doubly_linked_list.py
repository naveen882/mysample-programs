class Node():
	def __init__(self,val):
		self.val = val
		self.next = None
		self.prev = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.next = n2
n2.prev = n1
n2.next=n3
n3.prev = n2
n3.next=n4

node = n1

while node:
	print "Actual val is"
	print node.val
	if node.prev:
		print "prev value is"
		print node.prev.val
	node = node.next
