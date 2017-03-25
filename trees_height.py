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
			node_tmp = node
			if mode == 'left':
				if node.left != None and node.right != None:
					node = node_tmp
				elif node.left != None:
					node = node.left
				elif node.right != None:
					node = node.right
				else:
					break
			elif mode == 'right':
				visited_right = 0
				if node.right != None:
					node_tmp = node
					node = node.left
					if node.right == None:
						node = node_tmp
					else:
						continue
					visited_right = 1
					node = node.right
				elif node.left != None:
					visited_right = 2
					node = node.left
				else:
					break
				
			
def inorderTraversal(root):
	return (inorderTraversal(root.left) + [root.name] + inorderTraversal(root.right)) if root else []
a=0
def inorderTraversal(root):
	global a
	res = []
	if root:
		a+=1
		res = inorderTraversal(root.left) 
		print root.name
		print a
		res.append(root.name)
		#res = res + inorderTraversal(root.right)
	return res




t1=trees('A')
t2=trees('B')
t3=trees('C')
t4=trees('D')
t5=trees('E')
t6=trees('F')
t7=trees('G')
t8=trees('H')
t9=trees('I')
t10=trees('J')

t1.left = t2
t1.right = t3
t2.left= t4
t3.right = t5
t4.right = t6
t4.left = t10
t6.right = t7
t7.right = t8
t8.right = t9

#trees.display(t1,'left')
print inorderTraversal(t1)
print "====================================="
#trees.display(t1,'right')
		
