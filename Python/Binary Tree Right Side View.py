# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def rightSideView(self, root):
		if not root:
			return []

		ret = []
		currentLevel = [root]
		while currentLevel:
			nextLevel = []
			for i in range(len(currentLevel)):
				if currentLevel[i].left:
					nextLevel.append(currentLevel[i].left)
				if currentLevel[i].right:
					nextLevel.append(currentLevel[i].right)
				if i == len(currentLevel) - 1:
					ret.append(currentLevel[i].val)
			currentLevel = nextLevel
		return ret