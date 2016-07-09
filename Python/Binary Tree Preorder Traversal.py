#Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def preorderTraversal(self, root):
		if not root:
			return []

		ret = []
		ret += [root.val]
		ret += self.preorderTraversal(root.left)
		ret += self.preorderTraversal(root.right)
		return ret

	def preorderTraversal_iterative(self, root):
		if not root:
			return []

		ret = []
		stack = []
		while root or stack:
			while root:
				stack.append(root)
				ret.append(root.val)
				root = root.left
			root = stack.pop()
			root = root.right
		return ret