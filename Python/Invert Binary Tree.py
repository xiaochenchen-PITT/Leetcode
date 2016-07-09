# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def invertTree(self, root):
		if not root or (not root.left and not root.right):
			return root

		self.invertTree(root.left)
		self.invertTree(root.right)

		node = root.left
		root.left = root.right
		root.right = node

		return root

