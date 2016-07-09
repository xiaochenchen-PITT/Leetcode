# Definition for binary tree with next pointer.
class TreeLinkNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

class Solution(object):
	def connect(self, root):
		if not root:
			return 

		currentLevel = [root]
		nextLevel = []
		while currentLevel:
			currentLevel.append(None)
			for i in xrange(len(currentLevel)):
				if currentLevel[i] and i < len(currentLevel) - 1:
					currentLevel[i].next = currentLevel[i + 1]
					if currentLevel[i].left:
						nextLevel.append(currentLevel[i].left)
					if currentLevel[i].right:
						nextLevel.append(currentLevel[i].right)
			currentLevel = nextLevel
			nextLevel = []
		# return root # do not return anything 