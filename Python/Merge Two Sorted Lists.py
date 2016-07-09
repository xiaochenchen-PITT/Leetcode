# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		if not l1 and not l2:
			return l1

		if not l1 or not l2:
			return l1 if l1 else l2

		dummy = ListNode(0)
		node = dummy
		while l1 and l2:
			if l1.val < l2.val:
				node.next = l1
				l1 = l1.next
			else:
				node.next = l2
				l2 = l2.next
			node = node.next
		if l1:
			node.next = l1
		else:
			node.next = l2
		return dummy.next