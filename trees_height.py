class trees(object):
	def __init__(self,name,left=None,right=None):
		self.name = name
		self.left = None
		self.right = None

	@staticmethod
	def display(node,mode):
		count = 0
		while node:
			print node.name
			count += 1
			print "Depth is {count}".format(**locals())
			if mode == 'left':
				if node.left != None:
					node = node.left
				elif node.right != None:
					node = node.right
				else:
					break
			elif mode == 'right':
				if node.right != None:
					node = node.right
				elif node.left != None:
					node = node.left
				else:
					break
				
			



t1=trees('A')
t2=trees('B')
t3=trees('C')
t4=trees('D')
t5=trees('E')
t6=trees('F')
t7=trees('G')
t8=trees('H')
t9=trees('I')

t1.left = t2
t1.right = t3
t2.left= t4
t3.right = t5
t4.right = t6
t6.right = t7
t7.right = t8
t8.right = t9

trees.display(t1,'left')
print "====================================="
trees.display(t1,'right')
		
