# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	# given only access to that node. 
	# swap value
	def deleteNode(self, node):
		if not node.next:
			return

		node.val = node.next.val
		node.next = node.next.next
		return