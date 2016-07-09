# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
		if not root or not p or not q:
			return

		# node/leaf p/q to root path
		lcap = []
		lcaq = []
		self.getPath(root, p, lcap)
		self.getPath(root, q, lcaq)
		lcap = lcap[::-1]
		lcaq = lcaq[::-1]

		# # getPath2
		# self.getPath(root, p, [], lcap)
		# self.getPath(root, q, [], lcaq)
		# lcap = lcap[0][::-1]
		# lcaq = lcaq[0][::-1]

		# print [node.val for node in lcap]
		# print [node.val for node in lcaq]
		i = 0
		while i < len(lcap) and i < len(lcaq):
			if lcap[i] == lcaq[i]:
				i += 1
			else:
				return lcap[i - 1]
		return lcap[i - 1] if len(lcap) > len(lcaq) else lcaq[i - 1]

	def getPath(self, root, node, path):
		if not root:
			return False

		if root == node or self.getPath(root.left, node, path) or self.getPath(root.right, node, path):
			path.append(root)
			return True
		else:
			return False

	def getPath2(self, root, node, path, lca):
		if not root:
			return 

		if root == node:
			lca.append(path + [node])

		self.getPath2(root.left, node, path + [root], lca)
		self.getPath2(root.right, node, path + [root], lca)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print Solution().lowestCommonAncestor(root, root.left, root.right).val


