# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def maxDepth(self, root):
		if not root:
			return 0

		if not root.left and not root.right:
			return 1

		return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.left = TreeNode(1)

print Solution().maxDepth(root)