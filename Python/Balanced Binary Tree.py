# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isBalanced(self, root):
		if not root:
			return True

		depthLeft = self.findDepth(root.left)
		depthRight = self.findDepth(root.right)
		if abs(depthRight - depthLeft) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
			return True
		return False

	def findDepth(self, root):
		if not root:
			return 0

		return max(self.findDepth(root.left), self.findDepth(root.right)) + 1