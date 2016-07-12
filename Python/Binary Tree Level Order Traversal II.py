# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def levelOrderBottom(self, root):
		if not root:
			return []

		currentLevel = [root]
		ret = [[root.val]]
		while currentLevel:
			nextLevel = []
			for node in currentLevel:
				if node.left:
					nextLevel.append(node.left)
				if node.right:
					nextLevel.append(node.right)
			if nextLevel:
				ret.append([node.val for node in nextLevel])
			currentLevel = nextLevel
		return ret[::-1]

root = TreeNode(3)
root.left =TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print Solution().levelOrderBottom(root)
