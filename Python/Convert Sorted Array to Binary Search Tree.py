# Definition for a binary tree node.
#class TreeNode(object):
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None

class Solution(object):
	# def sortedArrayToBST(self, nums):
	#   if not nums:
	#       return 

	#   # BFS builds the tree
	#   root = TreeNode(0)
	#   i = 1
	#   current = [root]
	#   next = []
	#   while i < len(nums):
	#       for node in current:
	#           if i < len(nums):
	#               node.left = TreeNode(0)
	#               next.append(node.left)
	#               i += 1      
	#           if i < len(nums):
	#               node.right = TreeNode(0)
	#               next.append(node.right)
	#               i += 1      
	#           current = next  

	#   # place the number in order
	#   nums = nums[::-1]
	#   self.inOrder(root, nums)
	#   return root 

	# def inOrder(self, root, nums):
	#   if not root:
	#       return

	#   self.inOrder(root.left,nums)
	#   root.val = nums.pop()
	#   self.inOrder(root.right,nums)

	def sortedArrayToBST(self, nums):
		if not nums:
			return

		return self.buildTree(nums, 0, len(nums) - 1)

	def buildTree(self, nums, start, end):
		if start > end:
			return

		root = TreeNode(nums[start + (end - start) / 2])
		root.left = self.buildTree(nums, start, (start + (end - start) / 2 - 1))
		root.right = self.buildTree(nums, (start + (end - start) / 2 + 1), end)
		return root
		

		
