# Definition for a  binary tree node
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class BSTIterator(object):
	def __init__(self, root):
		self.nodes = []
		self.__inOrder__(root, self.nodes)
		self.nodes = self.nodes[::-1]

	def __inOrder__(self, root, nodes):
		if not root:
			return

		self.__inOrder__(root.left, self.nodes)
		self.nodes.append(root.val)
		self.__inOrder__(root.right, self.nodes)


	def hasNext(self):
		if self.nodes:
			return True
		return False
		

	def next(self):
		return self.nodes.pop()

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())