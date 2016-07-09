# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def oddEvenList(self, head):
		if not head:
			return 

		oddHead = ListNode(0)
		evenHead = ListNode(0)
		node = head
		i = 1
		while node and i < 3:
			if i == 1:
				oddHead.next = node
			else:
				evenHead.next = node
			node = node.next
			i += 1

		node = head
		i = 1
		oddNode = oddHead
		evenNode = evenHead
		while node:
			if i % 2 == 1:
				oddNode.next = node
				oddNode = oddNode.next
			else:
				evenNode.next = node
				evenNode = evenNode.next
			i += 1
			node = node.next

		oddNode.next = None
		evenNode.next = None
		oddNode.next = evenHead.next
		return oddHead.next