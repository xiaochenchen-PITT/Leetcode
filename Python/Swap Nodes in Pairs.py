# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def swapPairs(self, head):
		if not head or not head.next:
			return head

		dummy = ListNode(0)
		dummy.next = head
		node = dummy
		while node and node.next and node.next.next:
			node1 = node.next
			node2 = node.next.next

			node1.next = node2.next
			node2.next = node1
			node.next = node2
			
			node = node1
		return dummy.next