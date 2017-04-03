class trees(object):
    def __init__(self,name,left=None,right=None):
        self.name = name
        self.left = None
        self.right = None

    @staticmethod
    def inorderTraversal(root):
        """
        In an inorder traversal, we recursively do an inorder traversal on the left subtree, visit the root node, and finally do a recursive inorder traversal of the right subtree.
        Left root and right
        """
        if root:
            print "====1"
            print root.name
            print "====2"
            trees.inorderTraversal(root.left) 
            print "====3"
            print root.name
            print "====4"
            trees.inorderTraversal(root.right)
            print "====5"

    @staticmethod
    def preorder(root):
        """
        In a preorder traversal, we visit the root node first, then recursively do a preorder traversal of the left subtree, followed by a recursive preorder traversal of the right subtree.
        root left  right
        """
        if root:
            print root.name
            trees.preorder(root.left)
            trees.preorder(root.right)

    @staticmethod
    def postorder(root):
        """
        In a postorder traversal, we recursively do a postorder traversal of the left subtree and the right subtree followed by a visit to the root node.
        Right Left root

        """
        if root:
            trees.postorder(root.left)
            trees.postorder(root.right)
            print root.name

    @staticmethod
    def height(root):
        if root is None:
            return 0
        else:
            #return max(trees.height(root.left), trees.height(root.right)) + 1
            l = trees.height(root.left)
            #r = trees.height(root.right)
            print int(l)+1
            #return max(l, r) + 1

#def inorderTraversal(root):
#	return (inorderTraversal(root.left) + [root.name] + inorderTraversal(root.right)) if root else []

#def inorderTraversal(root):
#	global a
#	res = []
#	if root:
#            res = inorderTraversal(root.left) 
#            print root.name
#            inorderTraversal(root.right)
#            #res = res + inorderTraversal(root.right)
#	return res

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
t2.right = t5
t4.right = t6
t4.left = t10
t6.right = t7
t7.right = t8
t8.right = t9

print "========Inordertraversal============"
trees.inorderTraversal(t1)
print "========Preordertraversal============"
trees.preorder(t1)
print "========Postordertraversal============"
trees.postorder(t1)
print "===========Height of ther tree=========================="
print trees.height(t1)
