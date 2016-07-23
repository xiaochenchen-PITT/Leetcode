# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isSymmetric(self, root):
		if not root:
			return True

		return self.isSymmetric_helper(root.left, root.right)

	def isSymmetric_helper(self, left, right):
		if not left and not right:
			return True
		if not left or not right:
			return False
		if left.val != right.val:
			return False

		return self.isSymmetric_helper(left.left, right.right) and self.isSymmetric_helper(left.right, right.left)