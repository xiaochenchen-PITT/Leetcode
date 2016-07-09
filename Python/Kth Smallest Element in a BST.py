# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def kthSmallest(self, root, k):
		if not root:
			return -1

		stack = []
		i = 0
		while root or stack:
			if root:
				stack.append(root)
				root = root.left
			else:
				root = stack.pop()
				i += 1
				if i == k:
					return root.val
				root = root.right
				