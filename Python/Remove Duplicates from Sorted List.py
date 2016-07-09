# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def deleteDuplicates(self, head):
		if not head:
			return 

		currentNode = head
		nextNode = currentNode
		while currentNode:
			while nextNode and nextNode.val == currentNode.val:
				nextNode = nextNode.next
			currentNode.next = nextNode
			currentNode = currentNode.next
		return head
		