# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def inorderTraversal(self, root):
		if not root:
			return []

		ret = []
		ret += self.inorderTraversal(root.left)
		ret += [root.val]
		ret += self.inorderTraversal(root.right)
		return ret
		
	def inorderTraversal_iterative(self, root):
		if not root:
			return []

		ret = []
		stack = []
		while root or stack:
			while root:
				stack.append(root)
				root = root.left
			root = stack.pop()
			ret.append(root.val)
			root = root.right
		return ret