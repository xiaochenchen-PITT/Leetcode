# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def postorderTraversal(self, root):
		if not root:
			return []

		ret = []
		ret += self.postorderTraversal(root.left)
		ret += self.postorderTraversal(root.right)
		ret += [root.val]
		return ret

	def postorderTraversal_iterative(self, root):
		# compoare with preorderTraversal_iterative(),it is going from
		# the oppiste direction and thus :
		# first go to right node until None, and add node.val to the beginning of ret 
		if not root:
			return []

		ret = []
		stack = []
		while root or stack:
			while root:
				stack.append(root)
				ret.insert(0, root.val)
				root = root.right
			root = stack.pop()
			root = root.left
		return ret