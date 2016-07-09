# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def rob(self, root):
		if not root:
			return 0

		return self.rob_helper(root)[1]

	def rob_helper(self, root,stack):
		if not root:
			return [0, 0]

		left = self.rob_helper(root.left)
		right = self.rob_helper(root.right)
		return left[1] + right[1], max(left[0] + right[0] + root.val, left[1] + right[1])
